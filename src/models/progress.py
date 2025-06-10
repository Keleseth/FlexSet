from datetime import datetime
from enum import IntEnum
from uuid import UUID

from sqlalchemy import ForeignKey, Enum as SQLAEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseModel, TimeStampMixin

from src.core.annotations import int_pk


class LearningStage(IntEnum):
    NEW = 0
    FIRST_STAGE = 1
    SECOND_STAGE = 2
    THIRD_STAGE = 3
    FOURTH_STAGE = 4
    LEARNED = 5


class UserWordProgress(BaseModel, TimeStampMixin):

    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'), nullable=False)
    word_id: Mapped[int_pk] = mapped_column(ForeignKey('word.id'), nullable=False)
    stage: Mapped[LearningStage] = mapped_column(
        SQLAEnum(LearningStage, native_enum=False),
        default=LearningStage.NEW
    )
    attempts: Mapped[int] = mapped_column(default=0)
    last_reviewed: Mapped[datetime] = mapped_column(nullable=True)
    next_review: Mapped[datetime] = mapped_column(nullable=True)