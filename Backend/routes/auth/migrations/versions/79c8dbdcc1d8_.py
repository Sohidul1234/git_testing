"""empty message

Revision ID: 79c8dbdcc1d8
Revises: 59550c3a98d9
Create Date: 2023-08-06 23:09:36.752985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79c8dbdcc1d8'
down_revision = '59550c3a98d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Student_Course',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('achieved_score', sa.Integer(), nullable=False),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    op.create_table('WeeklyModules',
    sa.Column('weeklymodule_id', sa.Integer(), nullable=False),
    sa.Column('week_no', sa.Integer(), nullable=False),
    sa.Column('module_name', sa.String(length=50), nullable=False),
    sa.Column('module_description', sa.String(length=500), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('weeklymodule_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('WeeklyModules')
    op.drop_table('Student_Course')
    # ### end Alembic commands ###
