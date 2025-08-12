"""Инициализация SQLAlchemy (async) и провайдер сессии.

- create_async_engine + sessionmaker для AsyncSession (SQLAlchemy 2.0).
- declarative_base для моделей.
- get_async_session для DI в FastAPI.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.config import settings

class Base(DeclarativeBase):
    """Базовый класс для моделей SQLAlchemy.

    Используется для декларативного определения ORM-моделей.
    """
    pass


engine = create_async_engine(settings.database_url_async, echo=False)
async_session_maker = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncSession:
    """Создаёт и отдаёт асинхронную сессию БД.

    Возвращает:
        AsyncSession: контекстно управляемая сессия.
    """
    async with async_session_maker() as session:
        yield session
