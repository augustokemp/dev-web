from app.db.base_class import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return v

    email = Column(String, nullable=False, index=False)
    full_name = Column(String, nullable=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    addresses = relationship("Address", secondary="user_address", back_populates="users")
    user_tools = relationship("UserTool", backref="user", lazy="joined")
    