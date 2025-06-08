from typing import Generic, TypeVar, Type

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.constants import DEFAULT_AUTO_COMMIT


ModelType = TypeVar('ModelType')
CreateSchemaType = TypeVar('CreateSchemaType')
UpdateSchemaType = TypeVar('UpdateSchemaType')


class BaseMutableCRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Универсальный базовый класс для CRUD операций.
    """

    def __init__(self, model: Type[ModelType] = None):
        """
        Инициализирует CRUD-класс с указанной моделью.

        Параметры:
            model: SQLAlchemy-модель (класс), связанный с таблицей в БД.
        """
        self.model = model

    async def create(
        self,
        session: AsyncSession,
        obj_in: CreateSchemaType,
        auto_commit: bool = DEFAULT_AUTO_COMMIT,
    ) -> ModelType:
        obj_data = obj_in.model_dump()
        print(f' --------------------------------- model = {self.model}, obj_data = {obj_data}')
        db_obj = self.model(**obj_data)
        try:
            if auto_commit:
                session.add(db_obj)
                await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        return db_obj

    async def object_exists(
        self,
        session: AsyncSession,
        **filters
    ):
        stmt = select(self.model).filter_by(**filters).limit(1)
        obj = await session.scalar(stmt)
        if obj is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.model.__name__} not found'
            )

    async def object_not_exists(
        self,
        session: AsyncSession,
        **filters
    ):
        stmt = select(self.model).filter_by(**filters).limit(1)
        obj = await session.scalar(stmt)
        if obj:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'{self.model.__name__} already exists'
            )
        return None