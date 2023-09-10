from datetime import datetime

from pydantic import BaseModel


# Shared properties
class ToolBase(BaseModel):
    name: str
    path: str
    icon: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class ToolUpdate(ToolBase):
    pass

class ToolCreate(ToolBase):
    pass


class ToolInDBBase(ToolBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Tool(ToolBase):
    id: int
