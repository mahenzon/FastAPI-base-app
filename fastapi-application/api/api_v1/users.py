from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    BackgroundTasks,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.utils.send_welcome_email import send_welcome_email
from core.models import db_helper
from core.schemas.user import (
    UserRead,
    UserCreate,
)
from crud import users as users_crud

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
    # session: AsyncSession = Depends(db_helper.session_getter),
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await users_crud.get_all_users(session=session)
    return users


@router.post("", response_model=UserRead)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
    background_tasks: BackgroundTasks,
):
    user = await users_crud.create_user(
        session=session,
        user_create=user_create,
    )
    background_tasks.add_task(send_welcome_email, user_id=user.id)
    return user
