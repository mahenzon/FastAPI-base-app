"""add is_active flag to users

Revision ID: 4129c713b4d0
Revises: b6a07962907c
Create Date: 2025-10-04 18:45:29.518613

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4129c713b4d0"
down_revision: Union[str, None] = "b6a07962907c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "is_active")
