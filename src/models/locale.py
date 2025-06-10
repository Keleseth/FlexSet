from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.annotations import int_pk
from src.models.base import BaseModel, TimeStampMixin

if TYPE_CHECKING:
    from src.models.word import Word
    from src.models.set import Set


class Locale(BaseModel, TimeStampMixin):
    """
    Table with available language sets.

    Поля:
        id: int Primary key
        code: Short language code (e.g. 'en', 'ru')
        name: Full language name (e.g. 'English', 'Russian')
    """

    id: Mapped[int_pk]
    code: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    words: Mapped[list['Word']] = relationship(
        'Word',
        back_populates='locale',
    )
    set_target: Mapped[list['Set']] = relationship(
        'Set',
        back_populates='target_locale',
        foreign_keys='Set.target_locale_id'
    )
    set_source: Mapped[list['Set']] = relationship(
        'Set',
        back_populates='source_locale',
        foreign_keys='Set.source_locale_id'
    )
