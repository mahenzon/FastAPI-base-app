import logging
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from taskiq import TaskiqDepends

from core.models import db_helper, User
from crud import users
from core import broker
from mailing.send_welcome_email import (
    send_welcome_email as send_welcome,
)


log = logging.getLogger(__name__)


@broker.task
async def send_welcome_email(
    user_id: int,
    session: Annotated[
        AsyncSession,
        TaskiqDepends(db_helper.session_getter),
    ],
) -> None:
    user: User = await users.get_user(
        session=session,
        user_id=user_id,
    )
    log.info("Sending welcome email to user %s", user_id)
    await send_welcome(user=user)
