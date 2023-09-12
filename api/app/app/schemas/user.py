from datetime import datetime
from typing import List, Optional

from app.schemas.address import Address
from app.schemas.user_tool import UserTool
from pydantic import BaseModel, EmailStr

from app.schemas.address import AddressCreate
from app.schemas.user_tool import UserToolCreateFull

# Shared properties


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    is_active: bool = False
    is_admin: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str
    

class UserCreateFull(UserCreate):
    addresses: List[AddressCreate]
    user_tools: List[UserToolCreateFull]

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    id: int
    addresses: List[Address]
    user_tools: List[UserTool]

    class Config:
        arbitrary_types_allowed = True
