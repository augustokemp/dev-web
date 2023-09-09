
from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)
    __name__: str

    created_at = Column(TIMESTAMP, server_default=func.now(), index=True)

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
        index=True
    )

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
