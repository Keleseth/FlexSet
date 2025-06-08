from pydantic import BaseModel, ConfigDict, Field

from src.schemas.locale import LocaleReadSchema


class SetBaseSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)


class SetReadSchema(SetBaseSchema):

    name: str


class SetCreateSchema(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=64,
        description='Set name',
        examples=['Top 100 nouns', 'Tourist word set'],
    )
    description: str | None = Field(
        min_length=2,
        max_length=256,
        description='Set description',
    )
    source_locale_id: int
    target_locale_id: int


class SetUpdateSchema(SetBaseSchema):
    pass
