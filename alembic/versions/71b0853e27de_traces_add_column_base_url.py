"""traces: Add column base_url

Revision ID: 71b0853e27de
Revises: d5fc8114e5e5
Create Date: 2022-08-08 17:20:48.785320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71b0853e27de'
down_revision = 'd5fc8114e5e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('base_url', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'base_url')
