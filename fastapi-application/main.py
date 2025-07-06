import logging

import uvicorn

from core.config import settings

from api import router as api_router
from views import router as views_router
from create_fastapi_app import create_app

logging.basicConfig(
    level=settings.logging.log_level_value,
    format=settings.logging.log_format,
)

main_app = create_app(
    create_custom_static_urls=True,
)

main_app.include_router(
    api_router,
)
main_app.include_router(
    views_router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
