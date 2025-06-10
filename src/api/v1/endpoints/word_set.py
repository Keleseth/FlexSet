from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.word_set import handle_add_word_to_set
from src.database.db_dependencies import get_async_session
from src.schemas.word_set import WordSetCreateSchema, WordSetBaseSchema

router = APIRouter()


@router.post(
    '/',
    # response_model=WordSetBaseSchema,
    status_code=status.HTTP_201_CREATED
)
async def add_word_to_set(
    obj_in: WordSetCreateSchema,
    session: AsyncSession = Depends(get_async_session)
)-> None:
    # TODO добавить валидацию в crud функцию. Существование связи и тд.
    await handle_add_word_to_set(
        obj_in=obj_in,
        session=session,
    )
