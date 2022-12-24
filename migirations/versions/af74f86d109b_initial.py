"""initial

Revision ID: af74f86d109b
Revises: 
Create Date: 2022-12-24 20:40:37.477014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af74f86d109b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_addresses', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_payments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_payments', type_='foreignkey')
    op.drop_constraint(None, 'user_addresses', type_='foreignkey')
    # ### end Alembic commands ###