from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import BaseMutableCRUD
from src.models.set import Set
from src.models.word import Word
from src.schemas.set import SetCreateSchema, SetUpdateSchema


class SetCRUD(BaseMutableCRUD[Set, SetCreateSchema, SetUpdateSchema]):

    async def get_set_words(
        self,
        session: AsyncSession,
        set_id: int
    ):
        stmt = select(Set).filter_by(id=set_id)
        result = await session.execute(stmt)
        set_obj = result.scalar_one_or_none()
        return set_obj.words


set_crud = SetCRUD(Set)