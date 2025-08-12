"""Репозиторий Review.

Инкапсулирует CRUD-доступ к таблице reviews.
"""

from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Review


class ReviewRepository:
    """Репозиторий для работы с таблицей reviews."""

    def __init__(self, db: AsyncSession) -> None:
        """Сохранить ссылку на сессию.

            Args:
                session (AsyncSession): активная сессия.
        """
        self._db = db

    async def create(self, *, text: str, sentiment: str) -> Review:
        """Создать и сохранить отзыв.

        Args:
            text (str): текст отзыва.
            sentiment (str): 'positive' | 'negative' | 'neutral'.

        Returns:
            Review: сохранённый ORM-объект.
        """
        obj = Review(text=text, sentiment=sentiment)
        self._db.add(obj)
        await self._db.flush()
        await self._db.commit()
        await self._db.refresh(obj)
        return obj

    async def list_by_sentiment(self, *, sentiment: str) -> Sequence[Review]:
        """Вернуть отзывы по тональности.

        Args:
            sentiment (str): фильтр по тональности.

        Returns:
            Sequence[Review]: список ORM-объектов.
        """
        stmt = (
            select(Review)
            .where(Review.sentiment == sentiment)
            .order_by(Review.created_at.desc())
        )
        res = await self._db.execute(stmt)
        return list(res.scalars().all())
