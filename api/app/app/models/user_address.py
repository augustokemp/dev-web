from app.db.base_class import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class UserAddress(Base):
    __tablename__ = "user_address"

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return v

    user_id = Column(ForeignKey("user.id"), nullable=False, index=True)
    user = relationship("User", backref="user_address")
    address_id = Column(ForeignKey("address.id"), nullable=False, index=True)
    address = relationship("Address", backref="user_address")
