"""add_delivered_column

Revision ID: b11010a9d8c8
Revises: fb38bb11b19c
Create Date: 2024-10-01 12:48:20.293969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = 'b11010a9d8c8'
down_revision: Union[str, None] = 'fb38bb11b19c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'tagvenue',
        sa.Column('delivered', sa.Boolean, nullable=False, default=False, server_default=text('FALSE'))
    )


def downgrade() -> None:
    op.drop_column('tagvenue', 'delivered')
