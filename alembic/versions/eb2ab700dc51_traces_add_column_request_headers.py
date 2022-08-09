"""traces: Add column request_headers

Revision ID: eb2ab700dc51
Revises: 370fd871fecb
Create Date: 2022-08-08 19:29:27.926423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb2ab700dc51'
down_revision = '370fd871fecb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('request_headers', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'request_headers')
