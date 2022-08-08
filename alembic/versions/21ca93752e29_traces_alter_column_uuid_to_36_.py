"""traces: Alter column uuid to 36 characters string

Revision ID: 21ca93752e29
Revises: d39383d16c59
Create Date: 2022-08-08 16:23:15.610760

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '21ca93752e29'
down_revision = 'd39383d16c59'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name='traces',
        column_name='uuid',
        type_=sa.String(36),
    )


def downgrade() -> None:
    op.alter_column(
        table_name='traces',
        column_name='uuid',
        type_=sa.String(32),
    )
