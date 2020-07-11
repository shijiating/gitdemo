from sqlalchemy import Column, func
from api.models.base import BaseModel, Model
from enum import unique, Enum
from api import db


# @unique
# class SensitivetimeEnum(Enum):
#     TOP = '高'
#     MIDDLE = '中'
#     LOW = '低'


class Svmdata(BaseModel, Model):
    __tablename__ = 'svmdata'
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', nullable=False, index = True)
    whole_illegaltimes = Column(db.Integer, comment='历史总违法次数')
    twoyear_illegaltimes = Column(db.Integer, comment='近两年内违法次数')
    is_halfyear_illegal = Column(db.Integer, comment='近半年内是否有违法记录,True 有 False 没有')
    maximum_cigar_num = Column(db.DECIMAL(10, 2), comment='最大涉烟条数')
    outofprovince_times = Column(db.Integer, comment="码段外流次数")
    maximum_outofprovince_num = Column(db.DECIMAL(10, 2), comment='最大外流条数')
    is_criminal = Column(db.Integer, comment='是否有过刑事处罚 True 是  False 否')
    format = Column(db.Integer, comment='经营业态')
    is_sensitivecircle = Column(db.Integer, comment='是否处于敏感商圈')
    is_downgrade = Column(db.Integer, comment='是否有过降级降档  True 是  False 否',)
    is_bigillegal = Column(db.Boolean(), server_default=db.text("False"), comment='是否违法大户  True 是  False 否')
    is_sensitive_canton = Column(db.Integer, comment='法人是否是敏感籍贯  True 是  False  否',)
    is_sensitive_nativeplace = Column(db.Integer, comment='是否处于敏感行政区  True 是  False  否')
    purchase_change = Column(db.DECIMAL(10, 2), comment='进货量增长率')
    required_differ = Column(db.DECIMAL(10, 2), comment='要货量-进货量差值')
    purchase_price = Column(db.DECIMAL(10, 2), comment='平均进货单价增长率')
    sensitive_month= Column(db.Integer, comment="敏感时间等级")
    result = Column(db.Integer,comment="预测结果")


class BpData(Model):
    __tablename__ = 'bpdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = Column(db.DateTime(), server_default=func.now(), comment="创建时间")
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', nullable=False, index = True)
    whole_illegaltimes = Column(db.Integer, comment='历史总违法次数')
    twoyear_illegaltimes = Column(db.Integer, comment='近两年内违法次数')
    is_halfyear_illegal = Column(db.Boolean(), server_default=db.text("False"), comment='近半年内是否有违法记录,True 有 False 没有')
    is_criminal = Column(db.Boolean(), server_default=db.text("False"), comment='是否有过刑事处罚 True 是  False 否')
    format = Column(db.Integer, comment='经营业态')
    is_sensitivecircle = Column(db.Integer, comment='是否处于敏感商圈')
    is_downgrade = Column(db.Boolean(), server_default=db.text("False"), comment='是否有过降级降档  True 是  False 否')
    is_bigillegal = Column(db.Boolean(), server_default=db.text("False"), comment='是否违法大户  True 是  False 否')
    is_sensitive_canton = Column(db.Boolean(), server_default=db.text("False"), comment='法人是否是敏感籍贯  True 是  False  否')
    purchase_change = Column(db.FLOAT(4), comment='进货量增长率a')
    required_differ = Column(db.FLOAT(2), comment='要货量-进货量差值a')
    purchase_price = Column(db.FLOAT(4), comment='平均进货单价增长率a')
    sensitive_month = Column(db.Integer, comment="敏感时间等级")
    is_delete = Column(db.Boolean(), server_default=db.text("False"), comment="是否删除，True已删 False未删")
    bp_result = Column(db.FLOAT(4), comment="预测结果")

