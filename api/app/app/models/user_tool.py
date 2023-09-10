from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class UserTool(Base):

    __tablename__ = "user_tool"

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return v

    user_id = Column(ForeignKey("user.id"), index=True)
    tool_id = Column(ForeignKey("tool.id"), index=True)
    allow_create = Column(Boolean, default=False)
    allow_read = Column(Boolean, default=False)
    allow_update = Column(Boolean, default=False)
    allow_delete = Column(Boolean, default=False)
    
    tool = relationship("Tool", backref="user_tool")