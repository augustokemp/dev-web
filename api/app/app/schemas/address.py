from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class AddressBase(BaseModel):
    street: str
    street_number: str
    neighborhood: str
    city: str
    uf: str


# Properties to receive via API on creation
class AddressCreate(AddressBase):
    pass


# Properties to receive via API on update
class AddressUpdate(AddressBase):
    street: Optional[str]
    street_number: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    uf: Optional[str]


class AddressInDBBase(AddressBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True