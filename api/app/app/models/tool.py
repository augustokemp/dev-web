from app.db.base_class import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Tool(Base):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return v

    name = Column(String, nullable=False, index=False)
    path = Column(String, nullable=False, index=False)
    icon = Column(String, nullable=False, index=False)
