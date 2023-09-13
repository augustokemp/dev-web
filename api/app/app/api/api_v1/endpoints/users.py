from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retorna lista de users
    """

    user_tool = crud.user_tool.get(db=db, user_id=current_user.id)

    if not user_tool or not user_tool.allow_read:
        raise HTTPException(403, "Usuário não autorizado")

    return crud.user.get_multi(db=db)


@router.get("/me/", response_model=schemas.User)
def read_user_me(
    # db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retorna current user.
    """

    return current_user


@router.get("/{id}/", response_model=schemas.User)
def read_user(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retorna usuário específico
    """

    return crud.user.get(db=db, id=id)


@router.put("/{id}/", response_model=schemas.User)
def update_user(
    id: int,
    payload: schemas.UserUpdateFieldsToReceive,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Atualiza user, addresses e tools
    """

    # Verifica se current_user tem permissão para criar users
    user_tool = crud.user_tool.get(db=db, user_id=current_user.id, tool_id=1)
    if not user_tool or not user_tool.allow_update:
        raise HTTPException(403, "Usuário não autorizado")

    addresses_ids = []

    # Verifica se já existe user com o mesmo e-maiç
    db_user = crud.user.get(db=db, id=id)
    if not db_user:
        raise HTTPException(404, "Usuário não encontrado")

    # Cria addresses não existentes
    crud.user_address.remove_multi(db=db, user_id=id)
    for address in payload.addresses:
        db_address = crud.address.get(db=db, **jsonable_encoder(address))

        if not db_address:
            db_address = crud.address.create(db=db, obj_in=address)

        addresses_ids.append(db_address.id)

    # Cria User
    user_in = schemas.UserUpdate(**jsonable_encoder(payload))
    db_user = crud.user.update(db=db, db_obj=db_user, obj_in=user_in)

    # Cria vínculo de address com user
    for address_id in addresses_ids:
        crud.user_address.create(db=db, obj_in=models.UserAddress(
            user_id=id,
            address_id=address_id
        ))

    # Cria user_tools
    crud.user_tool.remove_multi(db=db, user_id=id)
    for user_tool in payload.user_tools:
        user_tool_in = models.UserTool(
            **jsonable_encoder(user_tool))
        user_tool_in.user_id = db_user.id

        crud.user_tool.create(db=db, obj_in=user_tool_in)

    # Retorna user criado
    db.refresh(db_user)
    return db_user


@router.post("/", response_model=schemas.User)
def create_user(
    payload: schemas.UserCreateFieldsToReceive,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Cria e retorna user.
    Cria endereços não existentes.
    Cria vínculo de endereço com user.
    Cria/Atualiza user_tools
    """

    # Verifica se current_user tem permissão para criar users
    user_tool = crud.user_tool.get(db=db, user_id=current_user.id, tool_id=1)
    if not user_tool or not user_tool.allow_create:
        raise HTTPException(403, "Usuário não autorizado")

    addresses_ids = []

    # Verifica se já existe user com o mesmo e-maiç
    db_user = crud.user.get(db=db, email=payload.email)
    if db_user:
        raise HTTPException(409, "Já existe um usuário com este e-mail")

    # Cria addresses não existentes
    for address in payload.addresses:
        db_address = crud.address.get(db=db, **jsonable_encoder(address))

        if not db_address:
            db_address = crud.address.create(db=db, obj_in=address)

        addresses_ids.append(db_address.id)

    # Cria User
    user_in = schemas.UserCreate(**jsonable_encoder(payload))
    db_user = crud.user.create(db=db, obj_in=user_in)

    # Cria vínculo de address com user
    for address_id in addresses_ids:
        crud.user_address.create(db=db, obj_in=models.UserAddress(
            user_id=db_user.id,
            address_id=address_id
        ))

    # Cria user_tools
    for user_tool in payload.user_tools:
        user_tool_in = models.UserTool(
            **jsonable_encoder(user_tool))
        user_tool_in.user_id = db_user.id

        crud.user_tool.create(db=db, obj_in=user_tool_in)

    # Retorna user criado
    db.refresh(db_user)
    return db_user


@router.delete("/{id}/", response_model=int)
def delete_user(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Remove usuário, tools e user_addresses
    """

    user_tool = crud.user_tool.get(db=db, user_id=current_user.id, tool_id=1)
    if not user_tool or not user_tool.allow_delete:
        raise HTTPException(403, "Usuário não autorizado")

    db_user = crud.user.get(db=db, id=id)
    if not db_user:
        raise HTTPException(404, "Usuário não encontrado")

    crud.user_tool.remove_multi(
        db=db, user_id=db_user.id
    )

    crud.user_address.remove_multi(
        db=db, user_id=db_user.id
    )

    db.refresh(db_user)
    crud.user.remove(db=db, id=id)
    return db_user.id
