"""remove unused user props

Revision ID: 6f17b7a3c495
Revises: ed30a8f17cf4
Create Date: 2025-02-02 19:21:10.949604

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6f17b7a3c495"
down_revision: Union[str, None] = "ed30a8f17cf4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint("uq_users_foo_bar", "users", type_="unique")
    op.drop_column("users", "foo")
    op.drop_column("users", "bar")


def downgrade() -> None:
    op.add_column(
        "users",
        sa.Column("bar", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "users",
        sa.Column("foo", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_unique_constraint("uq_users_foo_bar", "users", ["foo", "bar"])
