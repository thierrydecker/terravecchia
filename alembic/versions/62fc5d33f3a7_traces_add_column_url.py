"""traces: Add column url

Revision ID: 62fc5d33f3a7
Revises: eb2ab700dc51
Create Date: 2022-08-08 19:46:06.059117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62fc5d33f3a7'
down_revision = 'eb2ab700dc51'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('url', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'url')
