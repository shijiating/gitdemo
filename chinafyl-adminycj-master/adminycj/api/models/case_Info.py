from enum import unique, Enum

from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


@unique
class CigarAttributeEnum(Enum):
    COUNTERFEIT = '假冒烟'
    SMUGGLE = '走私烟'
    DOMESTIC = '国产烟'


# 违法案件信息表
class Case(BaseModel, Model):
    __tablename__ = 'case'
    caseId = Column(db.String(128), comment='案件编号', nullable=False, index = True)
    store_id = Column(db.ForeignKey('store.id'), comment=' 零售户id', index = True)
    case_date = Column(db.DateTime(), comment='案发时间')
    case_value = Column(db.DECIMAL(10, 2), comment='案值')
    count = Column(db.DECIMAL(10, 2), comment='卷烟数量（条数）')
    case_nature = Column(db.String(128), comment='案件性质')
    is_criminal = Column(db.Boolean(), server_default=db.text("False"), comment="有无刑事处罚，True有 False没有", index=True)
    smoke_property01 = Column(db.Boolean(), server_default=db.text("False"), comment="是否为非流烟，True是 False否", index=True)
    smoke_property02 = Column(db.Boolean(), server_default=db.text("False"), comment="是否为假冒烟，True是 False否", index=True)
    smoke_property03 = Column(db.Boolean(), server_default=db.text("False"), comment="是否为走私烟，True是 False否", index=True)

# # 违法案件信息表
# class Casetest(BaseModel, Model):
#     __tablename__ = 'casetest'
#     caseId = Column(db.String(128), comment='案件编号', nullable=False)
#     store_id = Column(db.ForeignKey('store.id'), comment=' 零售户id')
#     case_date = Column(db.DateTime(), comment='案发时间')
#     case_value = Column(db.DECIMAL(10, 2), comment='案值')
#     count = Column(db.DECIMAL(10, 2), comment='卷烟数量（条数）')
#     case_nature = Column(db.String(128), comment='案件性质')
#     is_criminal = Column(db.Boolean(), server_default=db.text("False"), comment="有无刑事处罚，True有 False没有", index=True)
#     smoke_property01 = Column(db.Boolean(), server_default=db.text("False"), comment="是否为非流烟，True是 False否", index=True)
#     smoke_property02 = Column(db.Boolean(), server_default=db.text("False"), comment="是否为假冒烟，True是 False否", index=True)
#     smoke_property03 = Column(db.Boolean(), server_default=db.text("False"), comment="是否为走私烟，True是 False否", index=True)

# 案件涉烟详情表
class Case_cigar(BaseModel, Model):
    __tablename__ = 'casecigar'
    case_id = Column(db.ForeignKey('case.id'), comment=' 违法案件id', index = True)
    store_name = Column(db.String(128), comment='违法零售户名', index = True)
    business_number = Column(db.String(200), comment='违法零售户许可证号')
    case_date = Column(db.DateTime(), comment='案发时间',index = True)
    case_nature = Column(db.String(128), comment='案件性质')
    cigar_property = Column(db.Enum(CigarAttributeEnum), comment='涉烟属性')
    singlebrandname = Column(db.String(128), comment='品规名')
    count = Column(db.DECIMAL(10, 2), comment='卷烟数量')
    cigar_codefront = Column(db.String(128), comment='前16位喷码', index = True)
    cigar_codebehind = Column(db.String(128), comment='后16位喷码', index = True)
    origin_area = Column(db.String(128), comment='来源地')



# 喷码表
# class Code_table(BaseModel, Model):
#     __tablename__ = 'codetable'
#     singlebrand_id = Column(db.ForeignKey('singlebrand.id'), comment='品规id', nullable=False)
#     case_cigarid = Column(db.ForeignKey('casecigar.id'), comment='违法涉烟详情id', nullable=False)
#     cigar_codefront = Column(db.String(128), comment='前16位喷码', nullable=False)
#     cigar_codebehind = Column(db.String(128), comment='后16位喷码', nullable=False)


# 进货表（周）
class Purchase(BaseModel, Model):
    __tablename__ = 'purchase'
    store_id = Column(db.ForeignKey('store.id'), comment=' 零售户id',index = True)
    purchase_date = Column(db.Date(), comment='进货时间')
    purchase_week = Column(db.Integer, comment='周进货总量（条）')
    settlement_account = Column(db.String(128), comment='进货结算账号')
    required_count = Column(db.Integer, comment='要货总量')
    average_price = Column(db.DECIMAL(12, 8), comment='平均进货单价（元）')

# # 进货表（周）
# class Purchasetest(BaseModel, Model):
#     __tablename__ = 'purchasetest'
#     store_id = Column(db.ForeignKey('store.id'), comment=' 零售户id')
#     purchase_date = Column(db.Date(), comment='进货时间')
#     purchase_week = Column(db.Integer, comment='周进货总量（条）')
#     settlement_account = Column(db.String(128), comment='进货结算账号')
#     required_count = Column(db.Integer, comment='要货总量')
#     average_price = Column(db.DECIMAL(12, 8), comment='平均进货单价（元）')

# 进货明细表
class Brand(BaseModel, Model):
    __tablename_ = 'brand'
    purchase_id = Column(db.ForeignKey('purchase.id'), comment='进货记录id', nullable=False,index = True )
    cigar_name = Column(db.String(128), comment='品规名称')
    cigar_price = Column(db.DECIMAL(10, 2), comment='进货单价（元）')
    cigar_num = Column(db.Integer, comment='进货量（条）')


# # 销售表（周）
# class Sale(BaseModel, Model):
#     __tablename__ = 'sale'
#     store_id = Column(db.ForeignKey('store.id'), comment=' 零售户id', nullable=False)
#     sale_date = Column(db.Date(), comment='销售时间')
#     sell_week = Column(db.DECIMAL(10, 1), comment='周销售总量（条）')
#     zh_count = Column(db.DECIMAL(10, 1), comment='中华进货量（条）')
#     lq_count = Column(db.DECIMAL(10, 1), comment='利群进货量（条）')
#
#
# # 支付宝交易记录表
# class Aplipay(BaseModel, Model):
#     _tablename_ = 'alipay'
#     store_id = Column(db.ForeignKey('store.id'), comment=' 零售户id', nullable=False)
#     alipay_date = Column(db.Date(), comment='卷烟扫码销售时间')
#     alipay_kind = Column(db.String(128), comment='销售卷烟品规')
#     alipay_count = Column(db.DECIMAL(6, 1), comment='销售卷烟数量（包）')
#     alipay_values = Column(db.DECIMAL(8, 2), comment='销售卷烟金额')
#     consumer_code = Column(db.String(128), comment='消费者消费2088码')


# 码段外流表
class CodeSegment(BaseModel, Model):
    __tablename__ = 'codesegment'
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', nullable=False)
    out_date = Column(db.Date(), comment='外流时间')
    cigar_name = Column(db.String(128), comment='外流品规名称')
    out_count = Column(db.DECIMAL(8, 1), comment='外流条数（条）')
    spray_code = Column(db.String(16), comment='喷码后16位')
    out_place = Column(db.String(128), comment='外流地')


# excel导入表
class ExcelInAndOut(BaseModel, Model):
    __tablename__ = 'excelinandout'
    input_caseid = Column(db.String(128), comment='案件编号')
    user_id = Column(db.Integer, comment='稽查员用户id')
    singlebrand_id = Column(db.String(128), comment='规格id')
    singlebrand_name = Column(db.String(128), comment='品规名')
    code_front = Column(db.String(16), comment='喷码前16位')
    code_behind = Column(db.String(16), comment='喷码后16位')
    count = Column(db.DECIMAL(8, 1), comment='条数')

