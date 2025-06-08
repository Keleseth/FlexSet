from src.crud.base import BaseMutableCRUD

from src.models.set import Set
from src.schemas.set import SetCreateSchema, SetUpdateSchema


class SetCRUD(BaseMutableCRUD[Set, SetCreateSchema, SetUpdateSchema]):
    pass


set_crud = SetCRUD(Set)