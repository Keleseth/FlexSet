from fastapi import APIRouter

from src.api.v1.endpoints import (
    home_router,
    set_router,
    word_set_router
)

main_router = APIRouter()
main_router.include_router(
    home_router,
    prefix=''
)
main_router.include_router(
    set_router,
    prefix='/sets',
    tags=['Set']
)
main_router.include_router(
    word_set_router,
    prefix='/word-set',
    tags=['Word-Set']
)
