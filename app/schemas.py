"""Pydantic-схемы запроса/ответа.

Pydantic v2 + from_attributes для ORM.
"""

from enum import Enum
from datetime import datetime
from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, StringConstraints, Field


class Sentiment(str, Enum):
    """Допустимые значения тональности."""
    positive = "positive"
    negative = "negative"
    neutral = "neutral"


TextStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class ReviewCreate(BaseModel):
    """Тело POST /reviews.

    Attributes:
        text (str): текст отзыва.
    """
    text: TextStr = Field(description="Текст отзыва")


class ReviewRead(BaseModel):
    """Ответ с данными отзыва (ORM -> API)."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    text: str
    sentiment: Sentiment
    created_at: datetime
