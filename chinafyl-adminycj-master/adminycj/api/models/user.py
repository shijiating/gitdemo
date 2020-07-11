from enum import unique, Enum

from sqlalchemy import Column

from api.extensions import db
from api.models.base import BaseModel, Model
from werkzeug.security import generate_password_hash, check_password_hash


@unique
class RoleEnum(Enum):
    ADMIN = '超级管理员'
    STATION_ADMIN = '专卖局负责人'
    DEPART_ADMIN = '稽查所负责人'
    USER = '普通用户'
    CAPTAIN_ADMIN = '稽查大队负责人'


# 局表
class Station(BaseModel, Model):
    __tablename__ = 'station'
    station_name = Column(db.String(50), comment='专卖局名称')


# 稽查所表
class Department(BaseModel, Model):
    __tablename__ = 'department'
    depart_name = Column(db.String(50), comment='稽查所名称')
    station_id = Column(db.ForeignKey('station.id'), comment='专卖局id', nullable=False)
    # is_captain = Column(db.Boolean(), server_default=db.text("False"), comment="是否是稽查大队，True是 False不是", index=True)

# 用户表
class User(BaseModel, Model):
    __tablename__ = 'user'
    account = Column(db.String(64), comment='账户', nullable=False)
    user_name = Column(db.String(50), comment='真实姓名')
    password = Column(db.String(500), comment='密码', nullable=False)
    station_id = Column(db.ForeignKey('station.id'), comment=' 局id')
    department_id = Column(db.ForeignKey('department.id'), comment='稽查所id')
    role_id = Column(db.ForeignKey('role.id'), comment=' 角色id', nullable=False)

    def __init__(self, *args, **kwargs):
        account = kwargs.get('account')
        user_name = kwargs.get('user_name')
        station_id = kwargs.get('station_id')
        department_id = kwargs.get('department_id')
        role_id = kwargs.get('role_id')
        password = kwargs.get('password')

        self.account = account
        self.user_name = user_name
        self.password = generate_password_hash(password)
        self.station_id = station_id
        self.department_id = department_id
        self.role_id = role_id

    def check_password(self,raw_password):
        return check_password_hash(self.password,raw_password)

        


# 角色表
class Role(BaseModel, Model):
    __tablename__ = 'role'
    role_name = Column(db.Enum(RoleEnum), comment='角色名称')



# 权限表
class Authorities(BaseModel, Model):
    _tablename_ = 'authorities'
    author_name = Column(db.String(100), comment='权限名称',nullable=False)


# 用户角色关联表
class UserRole(BaseModel, Model):
    _tablename_ = 'userRole'
    user_id = Column(db.ForeignKey('user.id'), comment='用户id')
    role_id = Column(db.ForeignKey('role.id'), comment=' 角色id', nullable=False)


# 角色权限关联表_
class RoleAuthor(BaseModel, Model):
    _tablename_ = 'roleAuthor'
    role_id = Column(db.ForeignKey('role.id'), comment=' 角色id', nullable=False)
    author_id = Column(db.ForeignKey('authorities.id'), comment='权限id')
