"""empty message

Revision ID: 62f0048e7277
Revises: 105e9cbcf7a6
Create Date: 2023-02-26 19:22:50.738211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62f0048e7277'
down_revision = '105e9cbcf7a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
