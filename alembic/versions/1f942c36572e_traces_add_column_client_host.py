"""traces: Add column client_host

Revision ID: 1f942c36572e
Revises: 71b0853e27de
Create Date: 2022-08-08 17:28:22.111193

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1f942c36572e'
down_revision = '71b0853e27de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('client_host', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'client_host')
