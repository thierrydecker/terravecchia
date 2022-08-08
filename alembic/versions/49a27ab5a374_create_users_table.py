"""Create users table

Revision ID: 49a27ab5a374
Revises: 
Create Date: 2022-08-03 17:46:27.471329

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '49a27ab5a374'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('users', )

    op.add_column('users', sa.Column('uuid', sa.String(32), ))
    op.add_column('users', sa.Column('id', sa.String(50), ))
    op.add_column('users', sa.Column('first_name', sa.String(100), ))
    op.add_column('users', sa.Column('last_name', sa.String(100), ))

    op.create_primary_key(
        constraint_name='pk_users',
        table_name='users',
        columns=['uuid'],
    )

    op.create_unique_constraint(
        constraint_name='uc_users_id',
        table_name='users',
        columns=['id']
    )


def downgrade() -> None:
    op.drop_table(
        'users',
    )
