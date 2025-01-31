"""Initial migration

Revision ID: 500599ef8e36
Revises: 
Create Date: 2024-09-22 23:07:17.680359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '500599ef8e36'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('department_id')
    )
    op.create_table('patients',
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('_age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('patient_id')
    )
    op.create_table('specialists',
    sa.Column('doc_id', sa.Integer(), nullable=False),
    sa.Column('_name', sa.String(), nullable=False),
    sa.Column('_specialty', sa.String(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.department_id'], ),
    sa.PrimaryKeyConstraint('doc_id')
    )
    op.create_table('appointments',
    sa.Column('appointment_id', sa.Integer(), nullable=False),
    sa.Column('patient_name', sa.String(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('specialist_name', sa.String(), nullable=False),
    sa.Column('specialist_id', sa.Integer(), nullable=True),
    sa.Column('appointment_time', sa.DateTime(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.department_id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.patient_id'], ),
    sa.ForeignKeyConstraint(['specialist_id'], ['specialists.doc_id'], ),
    sa.PrimaryKeyConstraint('appointment_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    op.drop_table('specialists')
    op.drop_table('patients')
    op.drop_table('departments')
    # ### end Alembic commands ###
