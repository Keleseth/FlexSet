from typing import Annotated

from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column


int_pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
]
