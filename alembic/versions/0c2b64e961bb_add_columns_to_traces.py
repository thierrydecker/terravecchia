"""Add column method to traces

Revision ID: 0c2b64e961bb
Revises: c2c482bd0cb0
Create Date: 2022-08-08 18:41:31.348911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c2b64e961bb'
down_revision = 'c2c482bd0cb0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('method', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'method')
