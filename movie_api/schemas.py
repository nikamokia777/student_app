from pydantic import BaseModel, Field
from typing import Optional


class MovieCreate(BaseModel):
    title: str
    genre: str
    year: int = Field(gt=1900, le = 2026)
    rating: float = Field( gt = 0, le = 10)
    description: Optional[str] = None

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = Field(default=None, gt=1900, le=2026)
    rating: Optional[float]  = Field(default=None, ge=0, le=10)
    description: Optional[str] = None

class MovieResponse(BaseModel):
    id: int
    title: str
    genre: str
    year: int
    rating: float
    description: Optional[str] = None

    class Config:
        from_attributes = True