"""migr

Revision ID: c6dd155e6a17
Revises: 
Create Date: 2023-05-08 17:07:50.850491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6dd155e6a17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('themes',
    sa.Column('id', sa.Integer(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647), nullable=False),
    sa.Column('theme', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647), nullable=False),
    sa.Column('group_name', sa.String(length=255), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('theme_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['theme_id'], ['themes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('theme_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['theme_id'], ['themes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('question')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('groups')
    op.drop_table('users')
    op.drop_table('themes')
    # ### end Alembic commands ###