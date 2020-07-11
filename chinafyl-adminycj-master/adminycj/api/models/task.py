from sqlalchemy import Column
from sqlalchemy.orm import relationship

from api.models.base import BaseModel, Model
from enum import unique, Enum
from api import db

@unique
class MeasuresEnum(Enum):
    ORAL = '口头教育'
    ORDER = '责令整改'
    COMMON = '一般案件'
    CORRECTION = '当场改正'


# class Task(BaseModel,Model):
#     __tablename__='task'
#     user_id=Column(db.ForeignKey('user.id'),comment='用户id',nullable = False)
#     store_id=Column(db.ForeignKey('store.id'),comment='零售户id',nullable=False)
#     inspector1_id=Column(db.ForeignKey('user.id'),comment='稽查人员1id',nullable=False)
#     inspector2_id=Column(db.ForeignKey('user.id'),comment='稽查人员2id')
#     inspector3_id=Column(db.ForeignKey('user.id'),comment='稽查人员3id')
#     inspector4_id = Column(db.ForeignKey('user.id'), comment='稽查人员4id')
#     inspector5_id = Column(db.ForeignKey('user.id'), comment='稽查人员5id')
#     status = Column(db.Boolean(), server_default=db.text("False"), comment='任务状态', index=True)
#     end_date=Column(db.Date(),comment='截止时间')
#     task_score = Column(db.String(128), comment='任务评价分数')
#     remark = Column(db.String(128), comment='备注')
#
#     user = relationship('User', foreign_keys=[user_id])
#     inspector1 = relationship('User', foreign_keys=[inspector1_id])
#     inspector2 = relationship('User', foreign_keys=[inspector2_id])
#     inspector3 = relationship('User', foreign_keys=[inspector3_id])
#     inspector4 = relationship('User', foreign_keys=[inspector4_id])
#     inspector5 = relationship('User', foreign_keys=[inspector5_id])


# 稽查记录表
class Audit(BaseModel, Model):
    __tablename__ = 'audit'
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', nullable=False, index = True)
    inspector_id = Column(db.ForeignKey('user.id'), comment='稽查人员id', nullable=False)
    audit_date = Column(db.Date(), comment='稽查时间', nullable=False)
    audit_pic1 = Column(db.String(128), comment='稽查情况照片1')
    audit_pic2 = Column(db.String(128), comment='稽查情况照片2')
    audit_pic3 = Column(db.String(128), comment='稽查情况照片3')
    audit_pic4 = Column(db.String(128), comment='稽查情况照片4')
    audit_pic5 = Column(db.String(128), comment='稽查情况照片5')
    audit_pic6 = Column(db.String(128), comment='稽查情况照片6')
    audit_result = Column(db.Boolean(), server_default=db.text("False"), comment='稽查结果反馈', index=True)
    audit_note = Column(db.String(255), comment='稽查情况备注')
    is_opensale = Column(db.Boolean(), server_default=db.text("False"), comment='是否公开摆卖', index=True)
    measures = Column(db.Enum(MeasuresEnum), comment='采取措施')
    is_holdcertificate = Column(db.Boolean(), server_default=db.text("False"), comment='是否持证经营', index=True)
    is_opencertificate = Column(db.Boolean(), server_default=db.text("False"), comment='是否亮证经营', index=True)
    is_saleticket = Column(db.Boolean(), server_default=db.text("False"), comment='是否销售烟票', index=True)
    is_saleskyprice = Column(db.Boolean(), server_default=db.text("False"), comment='是否存在天价烟销售', index=True)
    is_potentially_illegal = Column(db.Boolean(), server_default=db.text("False"), comment='是否有潜在违法行为', index=True)
    score = Column(db.DECIMAL(10, 2), comment='评分')
    # forecast_id = Column(db.ForeignKey('forecast.id'), comment='预测表id', nullable=False)
    # task_id = Column(db.ForeignKey('task.id'), comment='任务分配表id', nullable=False)

# 藏匿图表
class HidePicture(BaseModel, Model):
    __tablename__ = 'hidepicture'
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', nullable=False, index = True)
    audit_id = Column(db.ForeignKey('audit.id'), comment='稽查记录id', nullable=False, index = True)
    picture = Column(db.String(200), comment='藏匿图')
    graffiti = Column(db.String(200), comment='涂鸦')
    note = Column(db.String(128), comment='藏匿图文字备注')
