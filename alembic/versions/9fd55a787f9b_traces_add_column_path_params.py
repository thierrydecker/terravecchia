"""traces: Add column path_params

Revision ID: 9fd55a787f9b
Revises: 0c2b64e961bb
Create Date: 2022-08-08 18:58:42.363867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fd55a787f9b'
down_revision = '0c2b64e961bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('path_params', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'path_params')
