"""empty message

Revision ID: 05580833a689
Revises: fed5988a16d9
Create Date: 2020-12-18 00:56:29.682904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05580833a689'
down_revision = 'fed5988a16d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
