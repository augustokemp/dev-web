from typing import Any, List

from app import crud, schemas
from app.api import deps
from app.db.session import Session
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/", response_model=List[schemas.Tool])
def read_tools(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reads tools
    """

    tools = crud.tool.get_multi(db=db)
    return tools
