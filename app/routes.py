"""Маршруты FastAPI.

APIRouter и DI для AsyncSession.
"""

from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from app.schemas import ReviewCreate, ReviewRead, Sentiment
from app.services import create_review as svc_create_review, list_reviews as svc_list_reviews

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
async def create_review_endpoint(
    payload: ReviewCreate,
    db: AsyncSession = Depends(get_async_session),
) -> ReviewRead:
    """Создать отзыв.

    Args:
        payload (ReviewCreate): тело запроса.
        db (AsyncSession): DI-сессия.

    Returns:
        ReviewRead: созданный отзыв.
    """
    obj = await svc_create_review(text=payload.text, db=db)
    return ReviewRead.model_validate(obj)


@router.get("", response_model=list[ReviewRead])
async def list_reviews_endpoint(
    sentiment: Annotated[Sentiment, Query(description="Фильтр по тональности")],
    db: AsyncSession = Depends(get_async_session),
) -> list[ReviewRead]:
    """Список отзывов по заданной тональности.

    Args:
        sentiment (Sentiment): фильтр.
        db (AsyncSession): DI-сессия.

    Returns:
        list[ReviewRead]: коллекция отзывов.
    """
    items = await svc_list_reviews(sentiment=sentiment.value, db=db)
    return [ReviewRead.model_validate(o) for o in items]
