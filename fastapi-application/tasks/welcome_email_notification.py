import logging

from core import broker
from mailing.send_welcome_email import (
    send_welcome_email as send,
)


log = logging.getLogger(__name__)


@broker.task
async def send_welcome_email(user_id: int) -> None:
    log.info("Sending welcome email to user %s", user_id)
    await send(user_id=user_id)
