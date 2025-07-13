import logging
from typing import Annotated

from faststream import Depends, Path
from faststream.nats import NatsRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User
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
