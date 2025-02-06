__all__ = ("broker",)

from taskiq_aio_pika import AioPikaBroker

from core.config import settings

broker = AioPikaBroker(
    # url="amqp://guest:guest@localhost:5672//",
    url=settings.taskiq.url,
)
