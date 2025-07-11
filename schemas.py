from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ParsonsProblemBase(BaseModel):
    name: str
    description: str
    solution_code: str
    difficulty: Optional[int] = None
    language: str

class ParsonsProblemCreate(ParsonsProblemBase):
    pass

class ParsonsProblemOut(ParsonsProblemBase):
    id: UUID

    class Config:
        from_attributes = True