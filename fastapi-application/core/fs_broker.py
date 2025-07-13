__all__ = (
    "broker",
    "user_registered",
)

from faststream.nats import NatsBroker

from core.config import settings

broker = NatsBroker(
    settings.faststream.nats_url,
)

user_registered = broker.publisher(
    "users.{user_id}.created",
)
