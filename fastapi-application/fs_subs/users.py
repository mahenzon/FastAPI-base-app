import asyncio
import logging
from typing import Annotated

from faststream import Depends, Path
from faststream.nats import NatsRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import count

from core.models import db_helper, User, Address
from core.schemas.user import UserStatsRequest, UserStatsResponse
from crud import users
from mailing.send_welcome_email import (
    send_welcome_email as send_welcome,
)

router = NatsRouter()

log = logging.getLogger(__name__)


@router.subscriber("users.{user_id}.created")
async def send_welcome_email(
    user_id: Annotated[int, Path()],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    msg: str,
) -> None:
    """
    Handles user registration:
    - Sends a welcome email to the user;
    - Write logs.
    """
    log.info(
        "Send welcome email to user #%d, also msg = %r",
        user_id,
        msg,
    )
    user: User = await users.get_user(
        session=session,
        user_id=user_id,
    )
    await send_welcome(user=user)


@router.subscriber("users.{user_id}.stats")
async def reply_user_stats(
    user_id: Annotated[int, Path()],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    msg: UserStatsRequest,
) -> UserStatsResponse:

    log.info(
        "User stats request for user #%d, msg = %r",
        user_id,
        msg,
    )
    user_addresses_count_stmt = select(
        count(Address.id),
    ).where(
        Address.user_id == msg.user_id,
    )
    addresses_count = await session.scalar(user_addresses_count_stmt)
    await asyncio.sleep(0)
    # попробуйте 1 и посмотрите, что будет
    # await asyncio.sleep(1)
    return UserStatsResponse(
        user_id=user_id,
        stat_type="addresses",
        addresses=addresses_count,
    )
