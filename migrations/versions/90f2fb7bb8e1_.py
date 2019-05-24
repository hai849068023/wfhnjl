"""empty message

Revision ID: 90f2fb7bb8e1
Revises: 7e25b6900e38
Create Date: 2019-05-24 10:51:11.392263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '90f2fb7bb8e1'
down_revision = '7e25b6900e38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('id_pay', sa.Integer(), nullable=False),
    sa.Column('pay_time', sa.DateTime(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('products', sa.Column('banner', sa.String(length=200), nullable=True))
    op.alter_column('products', 'price',
               existing_type=mysql.FLOAT(),
               nullable=False)
    op.create_foreign_key(None, 'products', 'classification', ['cid'], ['cid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.alter_column('products', 'price',
               existing_type=mysql.FLOAT(),
               nullable=True)
    op.drop_column('products', 'banner')
    op.drop_table('orders')
    # ### end Alembic commands ###
