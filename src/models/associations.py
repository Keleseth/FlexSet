from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseModel


class WordSet(BaseModel):

    word_id: Mapped[int] = mapped_column(ForeignKey('word.id'), primary_key=True)
    set_id: Mapped[int] = mapped_column(ForeignKey('set.id'), primary_key=True)


class UserSet(BaseModel):
    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    set_id: Mapped[int] = mapped_column(ForeignKey('set.id', ondelete='CASCADE'), primary_key=True)
