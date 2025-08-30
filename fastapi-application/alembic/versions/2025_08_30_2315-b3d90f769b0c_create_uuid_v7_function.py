"""create uuid v7 function

Revision ID: b3d90f769b0c
Revises: 43f1b0af9635
Create Date: 2025-08-30 23:15:57.831527

"""

from pathlib import Path
from typing import Sequence, Union

from alembic import op, context


# revision identifiers, used by Alembic.
revision: str = "b3d90f769b0c"
down_revision: Union[str, None] = "43f1b0af9635"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


uuid_v7_functions = (
    Path(
        context.config.get_section_option(
            "extra",
            "functions.dir",
        )
    )
    / "uuid_v7"
)


def upgrade() -> None:
    op.execute(
        (uuid_v7_functions / "upgrade.sql").read_text(),
    )


def downgrade() -> None:
    op.execute(
        (uuid_v7_functions / "downgrade.sql").read_text(),
    )
