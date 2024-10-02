"""tagvenue_model_v1

Revision ID: 9cab7d9d6c34
Revises: 
Create Date: 2024-09-20 16:05:44.401427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# revision identifiers, used by Alembic.
revision: str = '9cab7d9d6c34'
down_revision: Union[str, None] = None
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
