"""add created_at col to users table

Revision ID: 43f1b0af9635
Revises: 6f17b7a3c495
Create Date: 2025-08-30 22:49:43.526117

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "43f1b0af9635"
down_revision: Union[str, None] = "6f17b7a3c495"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "created_at")
