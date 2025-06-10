from pydantic import BaseModel


class WordCreateSchema(BaseModel):
    pass


class WordReadSchema(BaseModel):

    id: int
    text: str
