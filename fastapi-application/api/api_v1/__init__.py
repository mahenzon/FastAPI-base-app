from fastapi import APIRouter

from core.config import settings

from .users import router as users_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)
