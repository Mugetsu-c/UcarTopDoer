"""Инициализация SQLAlchemy (async) и провайдер сессии.

- create_async_engine + sessionmaker для AsyncSession (SQLAlchemy 2.0).
- declarative_base для моделей.
- get_async_session для DI в FastAPI.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.config import settings

class Base(DeclarativeBase):
    """Базовый класс ORM-моделей."""

engine = create_async_engine(
    settings.database_url_async,
    echo=settings.debug,
    pool_pre_ping=True,
)

AsyncSessionMaker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

async def get_async_session() -> AsyncSession:
    """Провайдер сессии БД для DI.

    Yields:
        AsyncSession: отдельная сессия на HTTP-запрос (AsyncSession per task).
    """
    async with async_session_maker() as session:
        yield session
