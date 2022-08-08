"""Alter users column uuid

Revision ID: dcb93ae60d87
Revises: 49a27ab5a374
Create Date: 2022-08-03 18:09:10.667269

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dcb93ae60d87'
down_revision = '49a27ab5a374'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name='users',
        column_name='uuid',
        type_=sa.String(36),
    )


def downgrade() -> None:
    op.alter_column(
        table_name='users',
        column_name='uuid',
        type_=sa.String(32),
    )
