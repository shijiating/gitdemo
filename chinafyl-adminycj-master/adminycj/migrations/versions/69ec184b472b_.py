"""empty message

Revision ID: 69ec184b472b
Revises: 04061023d93b
Create Date: 2020-05-30 22:30:44.730935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '69ec184b472b'
down_revision = '04061023d93b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('businessformat', 'degree',
               existing_type=mysql.INTEGER(display_width=11),
               comment='经营业态等级',
               existing_comment='业态等级',
               existing_nullable=True)
    op.add_column('forecast_store', sa.Column('forecast_result', sa.Enum('TOP', 'MIDDLE', 'LOW', name='foreenum'), nullable=True, comment='预测结果等级（高中低）'))
    op.alter_column('forecast_store', 'forecast_mode',
               existing_type=mysql.VARCHAR(length=50),
               comment='预测模型（综合/规则）',
               existing_comment='预测模型',
               existing_nullable=True)
    op.alter_column('forecast_store', 'forecast_store_id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='预测违法零售户id',
               existing_comment='预测零售户id',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('forecast_store', 'forecast_store_id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='预测零售户id',
               existing_comment='预测违法零售户id',
               existing_nullable=False)
    op.alter_column('forecast_store', 'forecast_mode',
               existing_type=mysql.VARCHAR(length=50),
               comment='预测模型',
               existing_comment='预测模型（综合/规则）',
               existing_nullable=True)
    op.drop_column('forecast_store', 'forecast_result')
    op.alter_column('businessformat', 'degree',
               existing_type=mysql.INTEGER(display_width=11),
               comment='业态等级',
               existing_comment='经营业态等级',
               existing_nullable=True)
    # ### end Alembic commands ###
