import logging

from faststream import FastStream

from core.config import settings
from core.fs_broker import broker
from fs_subs.users import router as users_router

app = FastStream(
    broker,
)

broker.include_router(users_router)


@app.after_startup
async def configure_logging() -> None:
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.logging.log_format,
        datefmt=settings.logging.date_format,
    )
