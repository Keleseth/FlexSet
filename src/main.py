from fastapi import FastAPI

from src.config import settings
from src.api.v1.router import main_router

app = FastAPI(
    title=settings.app_title,
    description=settings.description,
    version='1.0.0'
)

app.router.include_router(main_router)
