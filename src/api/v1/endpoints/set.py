from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.set import set_crud
from src.schemas.set import SetCreateSchema, SetReadSchema
from src.database.db_dependencies import get_async_session


router = APIRouter()

@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=SetReadSchema
)
async def create_wordset(
    obj_in: SetCreateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    print(f"⏵⏵⏵ CRUD model is: {set_crud.model.__name__}")
    created_set = await set_crud.create(
        obj_in=obj_in,
        session=session,
    )
    return created_set
