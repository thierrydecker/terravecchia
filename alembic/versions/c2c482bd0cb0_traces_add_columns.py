"""traces: Add columns

Revision ID: c2c482bd0cb0
Revises: 9606246d159e
Create Date: 2022-08-08 17:52:37.212931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2c482bd0cb0'
down_revision = '9606246d159e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('cookies', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'cookies')

