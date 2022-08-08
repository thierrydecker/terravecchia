"""traces: Alter column status_code to Integer

Revision ID: d5fc8114e5e5
Revises: f86238c8c1a7
Create Date: 2022-08-08 16:52:41.125285

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd5fc8114e5e5'
down_revision = 'f86238c8c1a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('traces', 'status_code')
    op.add_column('traces', sa.Column('status_code', sa.Integer, ))


def downgrade() -> None:
    op.drop_column('traces', 'status_code')
    op.add_column('traces', sa.Column('status_code', sa.String, ))
