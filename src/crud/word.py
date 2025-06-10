from src.crud.base import BaseMutableCRUD

from src.models.word import Word
from src.schemas.word import WordCreateSchema, WordReadSchema


class WordCRUD(BaseMutableCRUD[Word, WordCreateSchema, WordReadSchema]):
    pass


word_crud = WordCRUD(Word)