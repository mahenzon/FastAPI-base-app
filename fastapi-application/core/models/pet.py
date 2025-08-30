import uuid

from sqlalchemy import UUID, func
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins.created_at import CreatedAtMixin


class Pet(CreatedAtMixin, Base):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        server_default=func.uuid_generate_v7(),
        primary_key=True,
    )
    name: Mapped[str]
