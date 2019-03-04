"""Initial Migration

Revision ID: c706a891882f
Revises: 299fb49c2830
Create Date: 2019-03-04 16:31:43.425622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c706a891882f'
down_revision = '299fb49c2830'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('username', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_comments_username'), 'comments', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_username'), table_name='comments')
    op.drop_column('comments', 'username')
    # ### end Alembic commands ###