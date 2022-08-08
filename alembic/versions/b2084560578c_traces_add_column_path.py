"""traces: Add column path

Revision ID: b2084560578c
Revises: 62fc5d33f3a7
Create Date: 2022-08-08 19:51:05.968794

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b2084560578c'
down_revision = '62fc5d33f3a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('path', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'path')
