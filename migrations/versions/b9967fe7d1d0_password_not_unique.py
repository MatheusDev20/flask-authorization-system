"""password_not_unique

Revision ID: b9967fe7d1d0
Revises: 0cfe08f3200c
Create Date: 2022-04-14 05:17:08.327877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9967fe7d1d0'
down_revision = '0cfe08f3200c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_password_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_password_key', 'user', ['password'])
    # ### end Alembic commands ###