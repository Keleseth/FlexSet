from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, relationship

from src.models.base import TimeStampMixin, BaseModel


if TYPE_CHECKING:
    from src.models.set import Set


class User(BaseModel, TimeStampMixin, SQLAlchemyBaseUserTableUUID):   # type: ignore[misc]
    """
    User Table from fastapi_users.

    Additional fields:
        created_at: Datetime when user was created
        updated_at: Datetime when user was updated
    """

    sets: Mapped['Set'] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
        lazy='selectin'
    )
    sets_taken: Mapped[list['Set']] = relationship(
        secondary='userset',
        back_populates='taken_by_users',
        lazy='selectin'
    )
