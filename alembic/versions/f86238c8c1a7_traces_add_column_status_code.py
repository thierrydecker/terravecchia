"""traces: Add column status_code

Revision ID: f86238c8c1a7
Revises: 21ca93752e29
Create Date: 2022-08-08 16:48:52.414017

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f86238c8c1a7'
down_revision = '21ca93752e29'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('status_code', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'status_code')
