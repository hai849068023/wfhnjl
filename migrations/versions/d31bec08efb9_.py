"""empty message

Revision ID: d31bec08efb9
Revises: 
Create Date: 2019-05-24 10:33:34.438808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd31bec08efb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('introduction', sa.String(length=50), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('image_1', sa.String(length=200), nullable=True),
    sa.Column('image_2', sa.String(length=200), nullable=True),
    sa.Column('image_3', sa.String(length=200), nullable=True),
    sa.Column('vedio', sa.String(length=200), nullable=True),
    sa.Column('introduction', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('line_price', sa.Float(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('classification')
    # ### end Alembic commands ###