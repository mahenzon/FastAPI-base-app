from typing import TYPE_CHECKING

from sqlalchemy import true
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.created_at import CreatedAtMixin

if TYPE_CHECKING:
    from core.models import Address


class User(IntIdPkMixin, CreatedAtMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)

    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default=true(),
    )

    addresses: Mapped[list["Address"]] = relationship(
        back_populates="user",
    )

    @property
    def email(self) -> str:
        return f"{self.username}@domain.com"
