"""empty message

Revision ID: 9d148d9e510b
Revises: a6e8ed230a04
Create Date: 2020-06-03 12:38:15.160329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d148d9e510b'
down_revision = 'a6e8ed230a04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_casecigar_case_date'), 'casecigar', ['case_date'], unique=False)
    op.create_index(op.f('ix_casecigar_case_id'), 'casecigar', ['case_id'], unique=False)
    op.create_index(op.f('ix_casecigar_cigar_codebehind'), 'casecigar', ['cigar_codebehind'], unique=False)
    op.create_index(op.f('ix_casecigar_cigar_codefront'), 'casecigar', ['cigar_codefront'], unique=False)
    op.create_index(op.f('ix_casecigar_store_name'), 'casecigar', ['store_name'], unique=False)
    op.create_index(op.f('ix_hidepicture_audit_id'), 'hidepicture', ['audit_id'], unique=False)
    op.create_index(op.f('ix_hidepicture_store_id'), 'hidepicture', ['store_id'], unique=False)
    op.create_index(op.f('ix_personinfo_name'), 'personinfo', ['name'], unique=False)
    op.create_index(op.f('ix_purchase_store_id'), 'purchase', ['store_id'], unique=False)
    op.create_index(op.f('ix_store_department_id'), 'store', ['department_id'], unique=False)
    op.create_index(op.f('ix_store_person_id'), 'store', ['person_id'], unique=False)
    op.create_index(op.f('ix_store_store_name'), 'store', ['store_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_store_store_name'), table_name='store')
    op.drop_index(op.f('ix_store_person_id'), table_name='store')
    op.drop_index(op.f('ix_store_department_id'), table_name='store')
    op.drop_index(op.f('ix_purchase_store_id'), table_name='purchase')
    op.drop_index(op.f('ix_personinfo_name'), table_name='personinfo')
    op.drop_index(op.f('ix_hidepicture_store_id'), table_name='hidepicture')
    op.drop_index(op.f('ix_hidepicture_audit_id'), table_name='hidepicture')
    op.drop_index(op.f('ix_casecigar_store_name'), table_name='casecigar')
    op.drop_index(op.f('ix_casecigar_cigar_codefront'), table_name='casecigar')
    op.drop_index(op.f('ix_casecigar_cigar_codebehind'), table_name='casecigar')
    op.drop_index(op.f('ix_casecigar_case_id'), table_name='casecigar')
    op.drop_index(op.f('ix_casecigar_case_date'), table_name='casecigar')
    # ### end Alembic commands ###
