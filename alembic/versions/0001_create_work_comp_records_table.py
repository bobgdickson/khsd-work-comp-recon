"""create work_comp_records table

Revision ID: 0001_create_work_comp_records_table
Revises: 
Create Date: 2023-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_create_work_comp_records_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'work_comp_records',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('field1', sa.String(), nullable=True),
        sa.Column('field2', sa.String(), nullable=True),
    )

def downgrade():
    op.drop_table('work_comp_records')