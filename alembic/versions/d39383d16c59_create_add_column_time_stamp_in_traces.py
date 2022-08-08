"""Create add column time_stamp in traces

Revision ID: d39383d16c59
Revises: 883377985264
Create Date: 2022-08-08 15:37:01.462942

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd39383d16c59'
down_revision = '883377985264'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('time_stamp', sa.DateTime, ))


def downgrade() -> None:
    op.drop_column('traces', 'time_stamp')
