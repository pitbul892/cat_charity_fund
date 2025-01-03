"""add created_date default

Revision ID: 5d9125bb4d80
Revises: 9e5a21ff857f
Create Date: 2024-12-04 23:01:29.388986

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '5d9125bb4d80'
down_revision = '9e5a21ff857f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.alter_column('create_date',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.alter_column('create_date',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###
