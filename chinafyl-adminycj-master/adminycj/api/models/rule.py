from api.extensions import db
from api.models.base import BaseModel, Model
from sqlalchemy import Column
from enum import unique, Enum

@unique
class BusinessFormatEnum(Enum):
    TOP = '高'
    MIDDLE = '中'
    LOW = '低'

# 经营业态表
class Business_Format(BaseModel, Model):
    __tablename__ = 'businessformat'
    business_format = Column(db.String(50), comment='经营业态')
    degree = Column(db.Enum(BusinessFormatEnum), comment='经营业态等级')


# 月份表
class MonthTable(BaseModel, Model):
    __tablename__ = 'monthtable'
    month = Column(db.Integer, comment='月份')
    degree = Column(db.Integer, comment='敏感月等级')


# 行政区表
class Canton(BaseModel, Model):
    __tablename__ = 'canton'
    canton = Column(db.String(128), comment='行政区')
    is_cantonsensitivity = Column(db.Boolean(), server_default=db.text("False"), comment="行政区是否敏感，True敏感 False不敏感",
                                  index=True)


# 品规表
class SingleBrand(BaseModel, Model):
    __tablename__ = 'singlebrand'
    singlebrand_name = Column(db.String(128), comment='品规名称')
    wholesale_price = Column(db.DECIMAL(8, 2), comment='批发价')
    retail_price = Column(db.DECIMAL(8, 2), comment='零售价')
    is_sale = Column(db.Boolean(), server_default=db.text("False"), comment="是否在销",
                     index=True)


# 品规月度进货增长率表
class MonthlyPurchaseGrowthRate(BaseModel, Model):
    __tablename__ = 'mon_pur_growthrate'
    singlebrand_id = Column(db.ForeignKey('singlebrand.id'), comment='品规名称id')
    parameter1 = Column(db.DECIMAL(8, 2), comment='参数一')
    parameter2 = Column(db.DECIMAL(8, 2), comment='参数二')
    parameter3 = Column(db.DECIMAL(8, 2), comment='参数三')
    parameter4 = Column(db.DECIMAL(8, 2), comment='参数四')
    score1 = Column(db.Integer, comment='分数一')
    score2 = Column(db.Integer, comment='分数二')
    score3 = Column(db.Integer, comment='分数三')
    score4 = Column(db.Integer, comment='分数四')
    score5 = Column(db.Integer, comment='分数五')
    describe = Column(db.String(128), comment='预警参数描述')
    modifydate = Column(db.Date(), comment='修改日期')


# 预测规则表
class PredictRule(BaseModel, Model):
    __tablename__ = 'predictrule'
    rule_name = Column(db.String(128), comment='规则名称')
    parameter1 = Column(db.Integer, comment='参数一')
    parameter2 = Column(db.Integer, comment='参数二')
    parameter3 = Column(db.Integer, comment='参数三')
    parameter4 = Column(db.Boolean(), server_default=db.text("False"), comment="参数",
                        index=True)
    score1 = Column(db.Integer, comment='分数一')
    score2 = Column(db.Integer, comment='分数二')
    score3 = Column(db.Integer, comment='分数三')
    score4 = Column(db.Integer, comment='分数四')
    describe_rule = Column(db.String(128), comment='预警参数描述')
    modifydate = Column(db.Date(), comment='修改日期')


# 规则数据表
class RuleData(BaseModel, Model):
    __tablename__ = 'ruledata'
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', index = True)
    person_nativeplace = Column(db.Boolean(), server_default=db.text("False"), comment="主要经营人籍贯，True是 False否",
                                index=True)
    person01_nativeplace = Column(db.Boolean(), server_default=db.text("False"), comment="其他经营人1籍贯，True是 False否",
                                  index=True)
    person02_nativeplace = Column(db.Boolean(), server_default=db.text("False"), comment="其他经营人2籍贯，True是 False否",
                                  index=True)
    is_bigillegal = Column(db.Boolean(), server_default=db.text("False"), comment="是否为违法大户，True是 False否",
                           index=True)
    is_downgrade = Column(db.Boolean(), server_default=db.text("False"), comment="是否有降级将档情况，True是 False否",
                          index=True)
    month = Column(db.Integer, comment='当前月')
    canton_id = Column(db.Integer, comment='行政区id')
    is_criminal = Column(db.Boolean(), server_default=db.text("False"), comment="有无刑事处罚，True是 False否",
                         index=True)
    is_illegal = Column(db.Boolean(), server_default=db.text("False"), comment="近半年内是否有违法记录，True是 False否",
                        index=True)
    cigar_property_jia = Column(db.Boolean(), server_default=db.text("False"), comment="是否假冒烟，True是 False否",
                                index=True)
    cigar_property_fei = Column(db.Boolean(), server_default=db.text("False"), comment="是否非流烟，True是 False否",
                                index=True)
    cigar_property_zou = Column(db.Boolean(), server_default=db.text("False"), comment="是否走私烟，True是 False否",
                                index=True)
    logistics = Column(db.Integer, comment='物流')
    car = Column(db.Integer, comment='车辆')
    # settlement_account = Column(db.ForeignKey('store.settlement_account'), comment='电子结算账号')
    unlicensed_transport_times = Column(db.DECIMAL(8, 2), comment='无证运输烟草专卖品次数')
    unlicensed_transport_num = Column(db.DECIMAL(8, 2), comment='无证运输烟草专卖品条数')
    unlicensed_transport_price = Column(db.DECIMAL(8, 2), comment='无证运输烟草专卖品金额')
    purchase_illegcigar_times = Column(db.DECIMAL(8, 2), comment='未在当地进货次数')
    purchase_illegcigar_num = Column(db.DECIMAL(8, 2), comment='未在当地进货条数')
    purchase_illegcigar_price = Column(db.DECIMAL(8, 2), comment='未在当地进货金额')
    sell_illegcigar_times = Column(db.DECIMAL(8, 2), comment='销售非法生产的烟草专卖次数')
    sell_illegcigar_num = Column(db.DECIMAL(8, 2), comment='销售非法生产的烟草专卖条数')
    sell_illegcigar_price = Column(db.DECIMAL(8, 2), comment='销售非法生产的烟草专卖金额')
    over_postcigar_times = Column(db.DECIMAL(8, 2), comment='无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数')
    over_postcigar_num = Column(db.DECIMAL(8, 2), comment='无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数')
    over_postcigar_price = Column(db.DECIMAL(8, 2), comment='无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额')
    sell_abroadcigar_times = Column(db.DECIMAL(8, 2), comment='销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数')
    sell_abroadcigar_num = Column(db.DECIMAL(8, 2), comment='销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数')
    sell_abroadcigar_price = Column(db.DECIMAL(8, 2), comment='销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额')
    helpothers_transport_times = Column(db.DECIMAL(8, 2), comment='无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数')
    helpothers_transport_num = Column(db.DECIMAL(8, 2), comment='无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数')
    helpothers_transport_price = Column(db.DECIMAL(8, 2), comment='无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额')
    twoyear_illegaltimes = Column(db.Integer, comment='近两年历史违法次数')
    in_province_times = Column(db.DECIMAL(8, 2), comment='近一年码段外流情况（省内外流）次数')
    in_province_num = Column(db.DECIMAL(8, 2), comment='近一年码段外流情况（省内外流）条数')
    in_province_price = Column(db.DECIMAL(8, 2), comment='近一年码段外流情况（省内外流）金额')
    out_of_province_times = Column(db.DECIMAL(8, 2), comment='近一年码段外流情况（外流省外）次数')
    out_of_province_num = Column(db.DECIMAL(8, 2), comment='近一年码段外流情况（外流省外）条数')
    out_of_province_price = Column(db.DECIMAL(8, 2), comment='近一年码段外流情况（外流省外）金额')
    score = Column(db.Integer, comment='规则预测得分')
