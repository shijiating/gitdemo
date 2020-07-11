from enum import unique, Enum
from sqlalchemy import Column
from api import db
from api.models.base import BaseModel, Model


@unique
class StateEnum(Enum):
    NARMAL = '正常经营'
    CLOSE = '停业'
    REST = '歇业'
    ORDERCLOSE = '责令停业'


@unique
class LicenseShipEnum(Enum):
    EMPLOY = '雇佣关系'
    RELATION = '亲戚关系'
    SELF = '本人'
    OTHER = '其他'


@unique
class SpecialGroupEnum(Enum):
    NORMAL = '普通'
    DEMOLITION = '拆迁户'
    DISABILITY = '残疾人'
    UNEMPLOY = '下岗失业人员'
    LOWLIVE = '低保户'
    ARMY = '军烈属'
    POVERTY = '特困户'
    OTHER = '其他'

@unique
class SpecialHistoryEnum(Enum):
    VIOLENCE = '暴力抗法历史'
    PSYCHOSIS = '精神病史'
    IMPORTUNE = '胡搅蛮缠史'
    COMPLAINT = '投诉钉子户'
    COMPLEX = '社会关系特别复杂'
    NOSPECIAL = '无'


@unique
class BusinessFormatEnum(Enum):
    SHIZA = '食杂店'
    WULEYE = '娱乐服务业'
    CHAOSHI = '超市'
    BIANLI = '便利店'
    YANJIU = '烟酒商店'
    SHANGCHANG = '商场'
    OTHER = '其他'


@unique
class AdminiEnum(Enum):
    BENJI = '市辖区'
    WUCHENG = '婺城区'
    JINDONG = '金东区'
    LANXI = '兰溪市'
    PUJIANG = '浦江县'
    YIWU = '义乌市'
    DONGYANG = '东阳市'
    PANAN = '磐安县'
    YONGKANG = '永康市'
    WUYI = '武义县'


@unique
class MarketTypeEnum(Enum):
    COUNTRYSIDE = '农村'
    TOWNSHIP = '乡镇'
    COUNTRYTOWN = '县城城区'
    URBAN = '市区'

@unique
class CircleEnum(Enum):
    ZHENGWU = '政务（商务）区'
    XUEQU = '学区'
    JUMINQU = '居民区（村）'
    SHANGYEQU = '商业区'
    GONGYEQU = '工业区'
    LVKEZHONGZHUAN = '旅客中转区'
    JIMAOSHICHANG = '集贸市场'
    WULEQU = '娱乐（旅游）区'


# 社会关系表
class Social_relationship(BaseModel, Model):
    __tablename__ = 'socialrelationship'
    relationship_name = Column(db.String(128), comment='关系名称')


# 零售户社会关系表
class Store_relationship(BaseModel, Model):
    __tablename__ = 'storerelationship'
    social_relationshipid = Column(db.ForeignKey('storerelationship.id'), comment='所属稽查所id')
    store1_id = Column(db.ForeignKey('store.id'), comment='所属稽查所id')
    store2_id = Column(db.ForeignKey('store.id'), comment='所属稽查所id')


class PersonInfo(BaseModel, Model):
    __tablename__ = 'personinfo'
    name = Column(db.String(20), comment='法人姓名', nullable=False, index = True)
    sex = Column(db.String(20), comment='性别', nullable=False)
    id_card = Column(db.String(128), comment='法人身份证号', nullable=False)
    id_address = Column(db.String(128), comment='身份证住址', )
    birthday = Column(db.Date(), comment='出生日期')
    nation = Column(db.String(128), comment='民族')
    census_register = Column(db.String(128), comment='户籍', )
    phone = Column(db.String(128), comment='联系电话', )
    address = Column(db.String(128), comment='当前住址', )
    # level_education = Column(db.String(128), comment='文化程度')


class Store(BaseModel, Model):
    __tablename__ = 'store'
    store_name = Column(db.String(128), comment='零售户名称', nullable=False, index = True)
    department_id = Column(db.ForeignKey('department.id'), comment='所属稽查所id', nullable=False, index = True)
    person_id = Column(db.ForeignKey('personinfo.id'), comment='零售户法人信息id', nullable=False, index = True)
    # license_number = Column(db.String(128), comment='营业执照号', nullable=False)
    # customer_code = Column(db.String(128), comment='客户编码', nullable=False)
    picture = Column(db.String(200), comment='店铺俯视图')
    business_number = Column(db.String(200), comment='烟草经营许可证号')
    # business_date = Column(db.Date(), comment='烟草经营许可证发证日期')
    # business_office = Column(db.String(200), comment='烟草经营许可证发证机关')
    is_bigillegal = Column(db.Boolean(), server_default=db.text("False"), comment="是否是违法大户")
    business_start = Column(db.Date(), comment='许可证有效期限起')
    business_termi = Column(db.Date(), comment='许可证有效期限止')
    longitude = Column(db.String(20), comment='地址经度', nullable=False)
    latitude = Column(db.String(20), comment='地址维度', nullable=False)
    address = Column(db.String(200), comment='经营地址')
    state = Column(db.Enum(StateEnum), comment='经营状态')
    store_category = Column(db.String(20), comment='零售户合理定量类别')
    is_chain = Column(db.Boolean(), server_default=db.text("False"), comment="是否连锁，True连锁 False不连锁")
    is_suspension = Column(db.Boolean(), server_default=db.text("False"), comment="是否暂停货源，True是 False不是")
    business_format = Column(db.Enum(BusinessFormatEnum), comment='经营业态')
    administrative = Column(db.Enum(AdminiEnum), comment='行政区划')
    market_type = Column(db.Enum(MarketTypeEnum), comment='市场类型')
    phone = Column(db.String(20), comment='主呼电话')
    settlement_account = Column(db.String(200), comment='电子结算账号')
    circle = Column(db.Enum(CircleEnum), comment='商圈')
    is_downgrade = Column(db.Boolean(), server_default=db.text("False"), comment="是否有降级降档情况，True有 False没有", index=True)
    car_1 = Column(db.String(200), comment='车辆牌照1')
    car_2 = Column(db.String(200), comment='车辆牌照2')
    car_3 = Column(db.String(200), comment='车辆牌照3')
    car_photo1 = Column(db.String(200), comment='车辆牌照图1')
    car_photo2 = Column(db.String(200), comment='车辆牌照图2')
    car_photo3 = Column(db.String(200), comment='车辆牌照图3')
    operators1 = Column(db.String(200), comment='日常经营人1')
    license_ship1 = Column(db.Enum(LicenseShipEnum), comment='与持证人关系1')
    operators2 = Column(db.String(200), comment='日常经营人2')
    license_ship2 = Column(db.Enum(LicenseShipEnum), comment='与持证人关系2')
    operators3 = Column(db.String(200), comment='日常经营人3')
    license_ship3 = Column(db.Enum(LicenseShipEnum), comment='与持证人关系3')
    special_History = Column(db.Enum(SpecialHistoryEnum), comment='特殊历史类别')
    special_category = Column(db.Enum(SpecialGroupEnum), comment='特殊群体类别')


# 限量表
class Limit(BaseModel, Model):
    __tablename__ = 'limit'
    subbrand_id = Column(db.ForeignKey('singlebrand.id'), comment='品规id')
    A2 = Column(db.Integer, comment='A2零售户限量')
    A3 = Column(db.Integer, comment='A3零售户限量')
    A4 = Column(db.Integer, comment='A4零售户限量')
    A5 = Column(db.Integer, comment='A5零售户限量')
    B1 = Column(db.Integer, comment='B1零售户限量')
    B2 = Column(db.Integer, comment='B2零售户限量')
    B3 = Column(db.Integer, comment='B3零售户限量')
    B4 = Column(db.Integer, comment='B4零售户限量')
    C1 = Column(db.Integer, comment='C1零售户限量')
    C2 = Column(db.Integer, comment='C2零售户限量')
    C3 = Column(db.Integer, comment='C3零售户限量')
    C4 = Column(db.Integer, comment='C4零售户限量')
    D1 = Column(db.Integer, comment='D1零售户限量')
    D2 = Column(db.Integer, comment='D2零售户限量')
    D3 = Column(db.Integer, comment='D3零售户限量')
    D4 = Column(db.Integer, comment='D4零售户限量')
    E1 = Column(db.Integer, comment='E1零售户限量')
    E2 = Column(db.Integer, comment='E2零售户限量')
    E3 = Column(db.Integer, comment='E3零售户限量')
    E4 = Column(db.Integer, comment='E4零售户限量')
    F1 = Column(db.Integer, comment='F1零售户限量')
    F2 = Column(db.Integer, comment='F2零售户限量')
    F3 = Column(db.Integer, comment='F3零售户限量')
    F4 = Column(db.Integer, comment='F4零售户限量')
    G1 = Column(db.Integer, comment='G1零售户限量')
    G2 = Column(db.Integer, comment='G2零售户限量')
    G3 = Column(db.Integer, comment='G3零售户限量')
    G4 = Column(db.Integer, comment='G4零售户限量')
    H1 = Column(db.Integer, comment='H1零售户限量')
    H2 = Column(db.Integer, comment='H2零售户限量')
    L2 = Column(db.Integer, comment='L2零售户限量')
    L3 = Column(db.Integer, comment='L3零售户限量')
    L4 = Column(db.Integer, comment='L4零售户限量')
    L5 = Column(db.Integer, comment='L5零售户限量')
    T1 = Column(db.Integer, comment='T1零售户限量')
    T2 = Column(db.Integer, comment='T2零售户限量')
    limit_startdate = Column(db.Date(), comment='限量起始日期')
    limit_enddate = Column(db.Date(), comment='限量截止日期')


# 商圈表
class Circle(BaseModel, Model):
    __tablename__ = 'circle'
    store_circle_name = Column(db.String(120), comment='零售户商圈名称')
    is_sensitive = Column(db.Boolean(), server_default=db.text("False"), comment="是否为敏感商圈，True敏感 False不敏感")
