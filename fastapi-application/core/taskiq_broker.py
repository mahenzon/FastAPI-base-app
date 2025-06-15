__all__ = ("broker",)
import logging

from taskiq import TaskiqEvents, TaskiqState
from taskiq_aio_pika import AioPikaBroker

from core.config import settings

broker = AioPikaBroker(
    # url="amqp://guest:guest@localhost:5672//",
    url=settings.taskiq.url,
)


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState) -> None:
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.taskiq.log_format,
        datefmt=settings.logging.log_date_format,
    )
