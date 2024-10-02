"""create_tagvenue

Revision ID: fb38bb11b19c
Revises: 9cab7d9d6c34
Create Date: 2024-09-30 13:26:21.657625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# revision identifiers, used by Alembic.
revision: str = 'fb38bb11b19c'
down_revision: Union[str, None] = '9cab7d9d6c34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tagvenue',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('url', sa.String(length=255), nullable=False),
        sa.Column('price', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()),
    )


def downgrade() -> None:
    pass

