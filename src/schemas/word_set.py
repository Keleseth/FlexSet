from pydantic import BaseModel


class WordSetBaseSchema(BaseModel):

    word_id: int
    set_id: int


class WordSetCreateSchema(WordSetBaseSchema):
    pass


class WordSetReadSchema(WordSetBaseSchema):
    pass