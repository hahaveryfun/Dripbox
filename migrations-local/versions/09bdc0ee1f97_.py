"""empty message

Revision ID: 09bdc0ee1f97
Revises: 5c5a58c76437
Create Date: 2020-11-15 17:24:26.370709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09bdc0ee1f97'
down_revision = '5c5a58c76437'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('public', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'public')
    # ### end Alembic commands ###
