#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sqlalchemy import Column
from api.models.base import BaseModel, Model
from enum import unique, Enum
from api import db


@unique
class ModelEnum(Enum):
    SVM = 'SVM'
    BP = 'BP'
    RULE = 'RULE'


@unique
class ForeEnum(Enum):
    TOP = '高危'
    MIDDLE = '中危'
    LOW = '低危'


# 预测表
class Forecast(BaseModel, Model):
    __tablename__ = 'forecast'
    store_id = Column(db.ForeignKey('store.id'), comment='零售户id', nullable=False, index = True)
    forecast_date = Column(db.Date(), comment='预测时间')
    mode = Column(db.Enum(ModelEnum), comment='预测模型')
    result = Column(db.DECIMAL(6, 2), comment='预测违法可能性')


# 预警分级表
class Warning(BaseModel, Model):
    _tablename_ = 'warning'
    mode = Column(db.Enum(ModelEnum), comment='预测模型')
    warning_param1 = Column(db.DECIMAL(6, 2), comment='预警等级参数1')
    warning_param2 = Column(db.DECIMAL(6, 2), comment='预警等级参数2')
    warning_param3 = Column(db.DECIMAL(6, 2), comment='预警等级参数3')


# 预测零售户表
class Forecast_store(BaseModel, Model):
    _tablename_ = 'forecast_store'
    forecast_store_id = Column(db.ForeignKey('store.id'),comment='预测零售户id',nullable = False, index = True)
    forecast_mode = Column(db.String(50), comment="预测模型")
    forecast_result = Column(db.Enum(ForeEnum), comment='预测结果等级（高中低）')
    station_id = Column(db.ForeignKey('station.id'), comment='零售户所属专卖局id')
    department_id = Column(db.ForeignKey('department.id'), comment='零售户所属稽查所id')
    forecast_date = Column(db.Date(), comment='预测时间')
