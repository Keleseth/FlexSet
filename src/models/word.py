from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Enum as SqlEnum
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.core.annotations import int_pk
from src.models.base import BaseModel, TimeStampMixin
if TYPE_CHECKING:
    from src.models.locale import Locale
    from src.models.associations import Set


class LanguageEnum(str, Enum):
    en = 'en'
    ru = 'ru'
    de = 'de'
    fr = 'fr'


class Word(BaseModel):
    """
    Represents a single word in the platform's vocabulary.

    All words across all supported languages are stored in this table.

    Fields:
        id: Primary key
        text: The word itself
        language: Foreign key to Locale (indicates the language of the word)
        is_verified: Whether the word has been verified
    """
    #TODO добавить поля транскрипции, звучания и тд.

    id: Mapped[int_pk]
    text: Mapped[str] = mapped_column(nullable=False)
    language: Mapped[int] = mapped_column(ForeignKey('locale.id'))
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)

    locale: Mapped['Locale'] = relationship(
        'Locale',
        back_populates='words',
        lazy='selectin'
    )
    sets: Mapped[list['Set']] = relationship(
        secondary='wordset',
        back_populates='words',
    )

    outgoing_translations = relationship(
        'Translation',
        back_populates='source_word',
        foreign_keys='[Translation.source_word_id]'
    )

    incoming_translations = relationship(
        'Translation',
        back_populates='translated_word',
        foreign_keys='[Translation.translated_word_id]'
    )

    def __repr__(self):
        return self.text


class Translation(BaseModel, TimeStampMixin):
    """
    Таблица словарного запаса платформы.
    Слова всех языков платформы в одной таблице

    Поля:
    id - int
    text - str, само слово
    language - Enum поле с выбором языкового кода
    is_verified - верифицированность слова.
    """
    id: Mapped[int_pk]
    source_word_id: Mapped[int] = mapped_column(ForeignKey("word.id", ondelete="CASCADE"), nullable=False)
    translated_word_id: Mapped[int] = mapped_column(ForeignKey("word.id", ondelete="CASCADE"), nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    created_by: Mapped[int | None] = mapped_column(nullable=True)

    source_word: Mapped[Word] = relationship(
        back_populates="outgoing_translations",
        foreign_keys=[source_word_id]
    )
    translated_word: Mapped[Word] = relationship(
        back_populates="incoming_translations",
        foreign_keys=[translated_word_id]
    )
