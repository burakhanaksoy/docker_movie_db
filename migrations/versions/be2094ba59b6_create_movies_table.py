"""create movies table

Revision ID: be2094ba59b6
Revises: 
Create Date: 2021-05-09 20:33:15.805636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be2094ba59b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    account = op.create_table(
        'movies',
        sa.Column('mov_title', sa.String(200), primary_key=True),
        sa.Column('mov_time', sa.Integer(), nullable=False, default=0)
    )


def downgrade():
    op.drop_table('movies')
