"""Точка входа приложения FastAPI.

Создаёт приложение и подключает роутер.
"""

from fastapi import FastAPI
from core.config import settings
from app.routes import router as reviews_router

app = FastAPI(title=settings.app_name, debug=settings.debug)
app.include_router(reviews_router)
