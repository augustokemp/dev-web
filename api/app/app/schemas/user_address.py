from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserAddressBase(BaseModel):
    user_id: int
    address_id: int


# Properties to receive via API on creation
class UserAddressCreate(UserAddressBase):
    pass


# Properties to receive via API on update
class UserAddressUpdate(UserAddressBase):
    pass
