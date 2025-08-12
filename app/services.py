"""Бизнес-логика."""

from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories import ReviewRepository


_POSITIVE_KEYS = ("хорош", "люблю")
_NEGATIVE_KEYS = ("плохо", "ненавижу")


def detect_sentiment(text: str) -> str:
    """Примитивный детектор тональности.

    Args:
        text (str): исходный текст.

    Returns:
        str: 'positive' | 'negative' | 'neutral'.
    """
    t = text.lower()
    if any(k in t for k in _POSITIVE_KEYS):
        return "positive"
    if any(k in t for k in _NEGATIVE_KEYS):
        return "negative"
    return "neutral"


async def create_review(*, text: str, db: AsyncSession):
    """Создать отзыв через репозиторий с детекцией тональности.

    Args:
        text (str): текст отзыва.
        db (AsyncSession): сессия БД.

    Returns:
        app.models.Review: созданный объект.
    """
    repo = ReviewRepository(db)
    sentiment = detect_sentiment(text)
    return await repo.create(text=text, sentiment=sentiment)


async def list_reviews(*, sentiment: str, db: AsyncSession):
    """Вернуть список отзывов по тональности.

    Args:
        sentiment (str): 'positive' | 'negative' | 'neutral'.
        db (AsyncSession): сессия БД.

    Returns:
        list[app.models.Review]: список объектов.
    """
    repo = ReviewRepository(db)
    return await repo.list_by_sentiment(sentiment=sentiment)
