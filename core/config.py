"""Конфиг приложения.

Минимальный статический конфиг, подходит для локального запуска.
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Глобальные настройки приложения.

    Attributes:
        app_name: Название сервиса.
        database_url_async: DSN для async SQLAlchemy.
        database_url_sync: DSN для sync-инструментов (миграции).
        debug: Режим отладки.
    """

    app_name: str = Field(default="UCAR<>TOPDOER Sentiment")
    database_url_async: str = Field(default="sqlite+aiosqlite:///./reviews.db")
    database_url_sync: str = Field(default="sqlite:///./reviews.db")
    debug: bool = Field(default=True)


settings = Settings()
