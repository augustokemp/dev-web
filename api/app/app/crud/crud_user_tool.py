
from app.crud.base import CRUDBase
from app.models import UserTool
from app.schemas import UserToolCreate, UserToolUpdate
from sqlalchemy.orm import Session


class CRUDUserTool(CRUDBase[UserTool, UserToolCreate, UserToolUpdate]):
    pass


user_tool = CRUDUserTool(UserTool)
