from datetime import datetime
from typing import List, Optional

from app.schemas.tool import Tool
from pydantic import BaseModel


# Shared properties
class UserToolBase(BaseModel):
    user_id: int
    tool_id: int
    allow_create: Optional[bool] = False
    allow_read: Optional[bool] = False
    allow_update: Optional[bool] = False
    allow_delete: Optional[bool] = False

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

# Properties to receive via API on update


class UserToolUpdate(UserToolBase):
    pass

class UserToolCreate(UserToolBase):
    pass


class UserToolCreateFull(UserToolBase):
    user_id: Optional[int]

class UserToolInDBBase(UserToolBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserTool(UserToolBase):
    id: int
    tool: Tool
