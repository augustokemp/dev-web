
from app.crud.base import CRUDBase
from app.models import Address
from app.schemas import AddressCreate, AddressUpdate
from sqlalchemy.orm import Session


class CRUDAddress(CRUDBase[Address, AddressCreate, AddressUpdate]):
    pass


address = CRUDAddress(Address)
