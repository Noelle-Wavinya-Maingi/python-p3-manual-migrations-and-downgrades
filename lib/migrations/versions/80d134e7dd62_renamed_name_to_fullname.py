"""Renamed name to fullname

Revision ID: 80d134e7dd62
Revises: 791279dd0760
Create Date: 2023-08-31 15:51:23.946505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80d134e7dd62'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='fullname')


def downgrade() -> None:
    op.alter_column('students', 'fullname', new_column_name='name')