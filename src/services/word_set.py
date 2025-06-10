from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.set import set_crud
from src.crud.word import word_crud
from src.crud.word_set import word_set_crud
from src.schemas.word_set import WordSetCreateSchema


async def handle_add_word_to_set(
    session: AsyncSession,
    obj_in: WordSetCreateSchema,
):
    """
    Verify that the given set and word exist,
    and that there is no existing connection between them.

    Args:
        session: Async SQLAlchemy session.
        obj_in: Input schema containing set_id and word_id.
    """
    filters = obj_in.model_dump()
    await set_crud.object_exists(
        session=session,
        id=filters['set_id']
    )
    await word_crud.object_exists(
        session=session,
        id=filters['word_id']
    )
    await word_set_crud.object_not_exists(
        session=session,
        set_id=filters['set_id'],
        word_id=filters['word_id']
    )
    return await word_set_crud.create(
        obj_in=obj_in,
        session=session
    )
