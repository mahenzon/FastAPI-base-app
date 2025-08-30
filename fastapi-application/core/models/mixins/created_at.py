from datetime import datetime, timezone

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


def get_current_dt() -> datetime:
    dt = datetime.now(tz=timezone.utc)
    return dt.replace(microsecond=0, tzinfo=None)


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=get_current_dt,
        server_default=func.now(),
    )
