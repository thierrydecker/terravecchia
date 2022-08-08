"""traces: Add column client_port

Revision ID: 9606246d159e
Revises: 1f942c36572e
Create Date: 2022-08-08 17:29:55.752075

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9606246d159e'
down_revision = '1f942c36572e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('traces', sa.Column('client_port', sa.String, ))


def downgrade() -> None:
    op.drop_column('traces', 'client_port')
