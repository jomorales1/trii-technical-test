from pydantic import BaseModel
from typing import Literal

class RickAndMortyParams(BaseModel):
    page: int | None = None
    name: str | None = None
    status: Literal["alive", "dead", "unknown"] | None = None
    gender: Literal["female", "male", "genderless", "unknown"] | None = None
    generate_zip: bool = False

class RickAndMortyFilters(BaseModel):
    name: str | None = None
    status: Literal["alive", "dead", "unknown"] | None = None
    gender: Literal["female", "male", "genderless", "unknown"] | None = None