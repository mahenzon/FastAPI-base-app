from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.created_at import CreatedAtMixin


class User(IntIdPkMixin, CreatedAtMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)

    @property
    def email(self) -> str:
        return f"{self.username}@domain.com"
