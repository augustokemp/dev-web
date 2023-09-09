from app.db.base_class import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Address(Base):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return v

    street = Column(String, nullable=False, index=False)
    street_number = Column(String, nullable=True, index=False)
    neighborhood = Column(String, nullable=True, index=False)
    city = Column(String, nullable=True, index=False)
    uf = Column(String, nullable=True, index=False)