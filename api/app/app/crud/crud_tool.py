
from app.crud.base import CRUDBase
from app.models import Tool
from app.schemas import ToolCreate, ToolUpdate
from sqlalchemy.orm import Session


class CRUDTool(CRUDBase[Tool, ToolCreate, ToolUpdate]):
    pass


tool = CRUDTool(Tool)
