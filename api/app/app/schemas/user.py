from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, EmailStr
from app import models


# Shared properties
class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    is_active: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


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

    class Config:
        arbitrary_types_allowed = True
