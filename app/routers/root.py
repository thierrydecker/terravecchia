from fastapi import APIRouter

from ..config.urls import app_prefix

router = APIRouter(
    prefix=f'{app_prefix}',
    tags=["Root endpoint endpoints"],
)


@router.get("/")
async def get_root():
    return {'message': 'Welcome big API'}
