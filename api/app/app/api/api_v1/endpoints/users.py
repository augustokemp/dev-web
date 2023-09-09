from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/me/", response_model=schemas.User)
def read_user_me(
    # db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """

    return current_user
