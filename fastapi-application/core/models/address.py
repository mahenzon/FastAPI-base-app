from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.created_at import CreatedAtMixin

if TYPE_CHECKING:
    from core.models import User


class Address(IntIdPkMixin, CreatedAtMixin, Base):
    __tablename__ = "addresses"

    street: Mapped[str] = mapped_column(
        String(200),
    )
    city: Mapped[str] = mapped_column(
        String(100),
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    user: Mapped["User"] = relationship(
        back_populates="addresses",
    )
