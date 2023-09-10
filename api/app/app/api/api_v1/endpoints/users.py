from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Body, Depends, HTTPException
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
