from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from datetime import datetime
from db_connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    is_super_user = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"