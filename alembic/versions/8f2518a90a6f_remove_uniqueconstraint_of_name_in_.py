"""remove uniqueconstraint of name in productmodel

Revision ID: 8f2518a90a6f
Revises: 
Create Date: 2025-05-24 10:48:43.339935

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '8f2518a90a6f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        'product_model_name_key',
        'product_model',
        type_='unique'
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
