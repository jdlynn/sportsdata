"""empty message

Revision ID: 20d40ecf8839
Revises: e089c12816bc
Create Date: 2019-07-10 18:38:48.261638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d40ecf8839'
down_revision = 'e089c12816bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_stock_name', table_name='stock')
    op.create_index(op.f('ix_stock_name'), 'stock', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stock_name'), table_name='stock')
    op.create_index('ix_stock_name', 'stock', ['name'], unique=1)
    # ### end Alembic commands ###
