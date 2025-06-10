from pydantic import BaseModel, ConfigDict


class LocaleReadSchema(BaseModel):

    id: int
    code: str

    model_config = ConfigDict(from_attributes=True)
