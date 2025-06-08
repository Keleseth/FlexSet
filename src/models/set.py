from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.annotations import int_pk
from src.models.base import BaseModel, TimeStampMixin

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.word import Word
    from src.models.locale import Locale


class Set(BaseModel, TimeStampMixin):

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    is_standard: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[UUID | None] = mapped_column(
        ForeignKey('user.id'), nullable=True
    )
    source_locale_id: Mapped[int] = mapped_column(
        ForeignKey('locale.id'), nullable=False
    )
    target_locale_id: Mapped[int] = mapped_column(
        ForeignKey('locale.id'), nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates='sets',
        lazy='selectin'
    )
    source_locale: Mapped['Locale'] = relationship(
        foreign_keys=[source_locale_id],
        lazy='selectin'
    )
    target_locale: Mapped['Locale'] = relationship(
        foreign_keys=[target_locale_id],
        lazy='selectin'
    )
    words: Mapped[list["Word"]] = relationship(
        secondary='wordset',
        back_populates='sets',
        lazy='selectin'
    )
    taken_by_users: Mapped[list['User']] = relationship(
        secondary='userset',
        back_populates='sets_taken',
        lazy='selectin'
    )