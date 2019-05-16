"""Removed location field

Peek Plugin Database Migration Script

Revision ID: 87f770b6a183
Revises: 53e411bea4ab
Create Date: 2019-05-17 09:33:15.251151

"""

# revision identifiers, used by Alembic.
revision = '87f770b6a183'
down_revision = '53e411bea4ab'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('BranchDetail', 'location', schema='pl_branch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('BranchDetail', sa.Column('location', sa.INTEGER(), autoincrement=False, nullable=False), schema='pl_branch')
    # ### end Alembic commands ###