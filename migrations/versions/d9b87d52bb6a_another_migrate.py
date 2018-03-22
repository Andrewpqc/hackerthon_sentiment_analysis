"""another migrate

Revision ID: d9b87d52bb6a
Revises: 466355067556
Create Date: 2017-10-22 00:49:27.722535

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd9b87d52bb6a'
down_revision = '466355067556'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('allcomment',
                  sa.Column('nagcount', sa.Integer(), nullable=True))
    op.add_column('allcomment',
                  sa.Column('poscount', sa.Integer(), nullable=True))
    op.add_column('allcomment', sa.Column('result', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('allcomment', 'result')
    op.drop_column('allcomment', 'poscount')
    op.drop_column('allcomment', 'nagcount')
    # ### end Alembic commands ###
