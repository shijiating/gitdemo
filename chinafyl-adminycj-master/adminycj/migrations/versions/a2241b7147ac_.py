"""empty message

Revision ID: a2241b7147ac
Revises: d89ad2f83575
Create Date: 2020-06-03 21:22:41.259562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2241b7147ac'
down_revision = 'd89ad2f83575'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_predictrule_id'), 'predictrule', ['id'], unique=False)
    op.create_index(op.f('ix_purchase_id'), 'purchase', ['id'], unique=False)
    op.create_index(op.f('ix_role_id'), 'role', ['id'], unique=False)
    op.create_index(op.f('ix_role_author_id'), 'role_author', ['id'], unique=False)
    op.create_index(op.f('ix_ruledata_id'), 'ruledata', ['id'], unique=False)
    op.create_index(op.f('ix_ruledata_store_id'), 'ruledata', ['store_id'], unique=False)
    op.create_index(op.f('ix_singlebrand_id'), 'singlebrand', ['id'], unique=False)
    op.create_index(op.f('ix_socialrelationship_id'), 'socialrelationship', ['id'], unique=False)
    op.create_index(op.f('ix_station_id'), 'station', ['id'], unique=False)
    op.create_index(op.f('ix_store_id'), 'store', ['id'], unique=False)
    op.create_index(op.f('ix_storerelationship_id'), 'storerelationship', ['id'], unique=False)
    op.create_index(op.f('ix_svmdata_id'), 'svmdata', ['id'], unique=False)
    op.create_index(op.f('ix_svmdata_store_id'), 'svmdata', ['store_id'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_role_id'), 'user_role', ['id'], unique=False)
    op.create_index(op.f('ix_warning_id'), 'warning', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_warning_id'), table_name='warning')
    op.drop_index(op.f('ix_user_role_id'), table_name='user_role')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_svmdata_store_id'), table_name='svmdata')
    op.drop_index(op.f('ix_svmdata_id'), table_name='svmdata')
    op.drop_index(op.f('ix_storerelationship_id'), table_name='storerelationship')
    op.drop_index(op.f('ix_store_id'), table_name='store')
    op.drop_index(op.f('ix_station_id'), table_name='station')
    op.drop_index(op.f('ix_socialrelationship_id'), table_name='socialrelationship')
    op.drop_index(op.f('ix_singlebrand_id'), table_name='singlebrand')
    op.drop_index(op.f('ix_ruledata_store_id'), table_name='ruledata')
    op.drop_index(op.f('ix_ruledata_id'), table_name='ruledata')
    op.drop_index(op.f('ix_role_author_id'), table_name='role_author')
    op.drop_index(op.f('ix_role_id'), table_name='role')
    op.drop_index(op.f('ix_purchase_id'), table_name='purchase')
    op.drop_index(op.f('ix_predictrule_id'), table_name='predictrule')
    # ### end Alembic commands ###
