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


@router.post("/", response_model=schemas.User)
def create_user(
    payload: schemas.UserCreateFull,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Cria e retorna user.
    Cria endereços não existentes.
    Cria vínculo de endereço com user.
    Cria/Atualiza user_tools
    """

    db.expire_on_commit = False

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

    # Cria/Atualiza user_tools
    for user_tool in payload.user_tools:

        db_user_tool = crud.user_tool.get(
            db=db, user_id=db_user.id, tool_id=user_tool.tool_id)

        if not db_user_tool:
            user_tool_in = models.UserTool(
                **jsonable_encoder(user_tool))
            user_tool_in.user_id = db_user.id

            db_user_tool = crud.user_tool.create(db=db, obj_in=user_tool_in)

        else:
            user_tool_in = schemas.UserToolUpdate(
                **jsonable_encoder(user_tool))
            user_tool_in.user_id = db_user.id

            db_user_tool = crud.user_tool.update(
                db=db, db_obj=db_user_tool, obj_in=user_tool_in
            )
    # Retorna user criado
    db.refresh(db_user)
    return db_user
