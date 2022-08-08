"""Create traces table

Revision ID: 883377985264
Revises: dcb93ae60d87
Create Date: 2022-08-08 15:31:35.008181

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '883377985264'
down_revision = 'dcb93ae60d87'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('traces', )

    op.add_column('traces', sa.Column('uuid', sa.String(32), ))

    op.create_primary_key(
        constraint_name='pk_traces',
        table_name='traces',
        columns=['uuid'],
    )


def downgrade() -> None:
    op.drop_table(
        'traces',
    )
