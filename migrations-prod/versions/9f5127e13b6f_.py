"""empty message

Revision ID: 9f5127e13b6f
Revises: 
Create Date: 2020-07-04 14:23:37.007770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f5127e13b6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('file_uuid', sa.Text(), nullable=False),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.Column('file_extension', sa.Text(), nullable=True),
    sa.Column('date_uploaded', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('file_digest', sa.Text(), nullable=True),
    sa.Column('source_identifier', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('file_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    # ### end Alembic commands ###
