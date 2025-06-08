from src.crud.base import BaseMutableCRUD

from src.models.associations import WordSet
from src.schemas.set import SetCreateSchema, SetUpdateSchema


class WordSetCRUD(BaseMutableCRUD[WordSet, SetCreateSchema, SetUpdateSchema]):
    pass


word_set_crud = WordSetCRUD(WordSet)