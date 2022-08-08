"""traces: Add column query_params

Revision ID: 370fd871fecb
Revises: 9fd55a787f9b
Create Date: 2022-08-08 19:03:07.067179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '370fd871fecb'
down_revision = '9fd55a787f9b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('query_params', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'query_params')
