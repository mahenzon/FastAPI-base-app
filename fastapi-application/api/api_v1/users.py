import logging
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from faststream.nats import NatsMessage
from sqlalchemy.ext.asyncio import AsyncSession

from core.fs_broker import user_registered, broker
from core.models import db_helper
from core.schemas.user import (
    UserRead,
    UserCreate,
    UserStatsRequest,
    UserStatsResponse,
)
from crud import users as users_crud

log = logging.getLogger(__name__)
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
):
    user = await users_crud.create_user(
        session=session,
        user_create=user_create,
    )
    log.info("Created user %s", user.id)
    await user_registered.publish(
        subject=f"users.{user.id}.created",
        message=None,
    )
    # await send_welcome_email.kiq(user_id=user.id)
    return user


@router.get("/{user_id}/stats")
async def get_user_stats(
    user_id: int,
) -> UserStatsResponse:
    msg = UserStatsRequest(
        user_id=user_id,
        stat_type="addresses",
    )
    subject = f"users.{user_id}.stats"
    try:
        response: NatsMessage = await broker.request(
            message=msg.model_dump(mode="json"),
            subject=subject,
            timeout=1,
        )
    except TimeoutError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Request timed out",
        )

    user_stats = UserStatsResponse.model_validate_json(
        response.body,
    )
    return user_stats
