#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint, request, url_for, jsonify
import decimal

from sqlalchemy import desc, or_

from api import db
from api.extensions import like_filter
from api.models.user import Department,Station
from api.models.store_Info import Store, PersonInfo
from api.schemas.store import add_store_schema, \
    storeinfo_by_depart_id_schema, storeinfo_by_store_name_schema, storeinfo_by_storeid_schema, \
    store_info_schema, del_store_schema, add_personinfo_schema, personinfo_by_name_schema, \
    personinfo_by_id_schema, person_info_schema, del_personinfo_schema, personinfo_by_store_id_schema, \
    storeinfo_by_personid_schema, personinfo_by_storeandpersoninfo_id_schema, paginate_test_schema, \
    storeinfo_by_departboss_id_schema, storeinfo_by_store_nameandpersonname_schema, storeinfo_by_role_id_schema, \
    personinfo_by_role_id_schema, storeinfo_by_store_multiplequery_schema,personinfo_by_name_notid_schema
from api.serializer.person import person_info_ser

from api.views.base import common_response, SysStatus

blue_print = Blueprint('store', __name__, url_prefix='/api/store')


# 添加店铺
@blue_print.route('/addStore', methods=['POST'])
def add_store():
    """
        @api {post} api/store/addStore  添加店铺
        @apiVersion 0.0.1
        @apiName add_store
        @apiGroup store
        @apiDescription 添加店铺
        @apiParam {String}  store_name      (必须)    店铺名称
        @apiParam {int}  department_id    (必须，稽查所表中必须先有数据)    所属稽查所id
        @apiParam {int}  person_id    (必须，法人信息表中必须先有数据)    零售户法人信息id
        @apiParam {String}  picture    (可选)    店铺俯视图
        @apiParam {String}  business_number    (必须)    烟草经营许可证号
        @apiParam {Boolean}  is_bigillegal  (可选)    是否为违法大户
        @apiParam {date}  business_start    (可选)    烟草经营许可证有效期始
        @apiParam {date}  business_termi    (可选)    烟草经营许可证有效期止
        @apiParam {string}  longitude    (必须)    地址经度
        @apiParam {string}  latitude    (必须)    地址纬度
        @apiParam {String}  address    (可选)    经营地址
        @apiParam {Enum}  state    (可选)    经营状态
        @apiParam {String}  store_category    (可选)    零售户合理定量类别
        @apiParam {Boolean}  is_chain   (可选)    是否连锁
        @apiParam {Boolean}  is_suspension   (可选)    是否暂停货源
        @apiParam {Enum}  business_format    (可选)    经营业态
        @apiParam {Enum}  administrative    (可选)    行政区划分
        @apiParam {Enum}  market_type    (可选)    市场类型
        @apiParam {String}  phone    (可选)    主呼电话
        @apiParam {string}  settlement_account      (可选)    电子结算账号
        @apiParam {Enum}  circle     (可选)   商圈
        @apiParam {Boolean}  is_downgrade      (可选)    是否有降级降档情况
        @apiParam {string}  car_1      (可选)    车辆牌照1
        @apiParam {string}  car_2      (可选)    车辆牌照2
        @apiParam {string}  car_3      (可选)    车辆牌照3
        @apiParam {string}  car_photo1      (可选)    车辆牌照图1
        @apiParam {string}  car_photo2      (可选)    车辆牌照图2
        @apiParam {string}  car_photo3      (可选)    车辆牌照图3
        @apiParam {string}  operators1      (可选)    日常经营人1
        @apiParam {Enum}  license_ship1    (可选)    与持证人关系1
        @apiParam {string}  operators2      (可选)    日常经营人2
        @apiParam {Enum}  license_ship2    (可选)    与持证人关系2
        @apiParam {string}  operators3      (可选)    日常经营人3
        @apiParam {Enum}  license_ship3    (可选)    与持证人关系3
        @apiParam {Enum}  special_category    (可选)    特殊群体类别
        @apiParam {Enum}  special_History    (可选)    特殊历史类别
        @apiParamExample {json} Request-Example:
            {
                "store_name":"金华市香香食品便利店",
                "department_id":1,
                "person_id":1522,
                "picture":"18125412365",
                "business_number":"3307274582488",
                "is_bigillegal":"True",
                "business_start":"2018-08-08",
                "business_termi":"2020-10-10",
                "longitude":"119.526345",
                "latitude":"29.451287",
                "address":"金华市婺城区义乌街151号",
                "state":"NARMAL",
                "store_category":"B3",
                "is_chain":"True",
                "is_suspension":"False",
                "business_format":"SHIZA",
                "administrative":"BENJI",
                "market_type":"URBAN",
                "phone":"13665884899",
                "settlement_account":"54125412578545",
                "circle":"XUEQU",
                "is_downgrade":"True",
                "car_1":"ldskggelgk",
                "car_2":"kdsjkgjdkj",
                "car_3":"dskgjkjg",
                "car_photo1":"dksgkjg",
                "car_photo2":"djgdjkgj",
                "car_photo3":"dksjgkjjk",
                "operators1":"李翠花",
                "license_ship1":"EMPLOY",
                "operators2":"linda",
                "license_ship2":"RELATION",
                "operators3":"诸葛亮",
                "license_ship3":"OTHER",
                "special_category":"NORMAL",
                "special_History":"VIOLENCE"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "店铺添加成功"
            }

        @apiErrorExample {json} Error-Response:
           {
                "sys_status": "FAIL",
                "data": "金华市香香食品便利店",
                "message": "该零售户已被添加"
            }
    """
    params = add_store_schema(request.json or '')
    store_name = params.get('store_name')
    department_id = params.get('department_id')
    person_id = params.get('person_id')
    picture = params.get('picture')
    business_number = params.get('business_number')
    is_bigillegal = params.get('is_bigillegal')
    business_start = params.get('business_start')
    business_termi = params.get('business_termi')
    longitude = params.get('longitude')
    latitude = params.get('latitude')
    address = params.get('address')
    state = params.get('state')
    store_category = params.get('store_category')
    is_chain = params.get('is_chain')
    is_suspension = params.get('is_suspension')
    business_format = params.get('business_format')
    administrative = params.get('administrative')
    market_type = params.get('market_type')
    phone = params.get('phone')
    settlement_account = params.get('settlement_account')
    circle = params.get('circle')
    is_downgrade = params.get('is_downgrade')
    car_1 = params.get('car_1')
    car_2 = params.get('car_2')
    car_3 = params.get('car_3')
    car_photo1 = params.get('car_photo1')
    car_photo2 = params.get('car_photo2')
    car_photo3 = params.get('car_photo3')
    operators1 = params.get('operators1')
    license_ship1 = params.get('license_ship1')
    operators2 = params.get('operators2')
    license_ship2 = params.get('license_ship2')
    operators3 = params.get('operators3')
    license_ship3 = params.get('license_ship3')
    special_category = params.get('special_category')
    special_History = params.get('special_History')
    store = Store.query.filter(Store.business_number == business_number, Store.is_delete == 0).first()
    if store:
        return common_response(SysStatus.FAIL, store.store_name, '该零售户已被添加')
    else:
        store = Store(store_name=store_name, department_id=department_id, person_id=person_id,
                      picture=picture, business_number=business_number,
                      is_bigillegal=is_bigillegal, business_start=business_start, business_termi=business_termi,
                      longitude=longitude,
                      latitude=latitude, state=state, store_category=store_category, is_chain=is_chain,
                      is_suspension=is_suspension, business_format=business_format,
                      administrative=administrative, market_type=market_type, settlement_account=settlement_account,
                      circle=circle,is_downgrade=is_downgrade, address=address, phone=phone, car_1=car_1, car_2=car_2, car_3=car_3,
                      car_photo1=car_photo1,car_photo2=car_photo2, car_photo3=car_photo3, operators1=operators1, license_ship1=license_ship1,
                      operators2=operators2,license_ship2=license_ship2, operators3=operators3, license_ship3=license_ship3,special_category=special_category,
                      special_History=special_History)
        db.session.add(store)
        db.session.commit()
        return common_response(SysStatus.SUCCESS, None, '店铺添加成功')


# 直接通过get方法获取所有零售户信息
@blue_print.route('/getAllStoreInfo', methods=['GET'])
def get_all_storeinfo():
    """
            @api {GET} api/store/getAllStoreInfo 直接获取所有零售户信息
            @apiVersion 0.0.1
            @apiName getAllStoreInfo
            @apiGroup store
            @apiDescription 直接获取所有零售户信息,此处使用了分页功能，因为是get方法，所以page参数通过访问地址访问，通过per_page指定每页显示多少条数据
            @apiSuccessExample {json} Success-Response:
                {
                   示例:http://39.96.52.170:5000/api/store/getAllStoreInfo?page=2&per_page=8  可以获取第二页的8条内容
                }
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = db.session.query(PersonInfo).join(Store, Department).filter(Store.is_delete == 0).with_entities(
        Store.store_name,
        Store.id,
        Store.department_id,
        Department.depart_name,
        Store.person_id,
        PersonInfo.name,
        Store.picture,
        Store.business_number,
        Store.is_bigillegal,
        Store.business_start,
        Store.business_termi,
        Store.longitude,
        Store.latitude,
        Store.address,
        Store.state,
        Store.store_category,
        Store.is_chain,
        Store.is_suspension,
        Store.business_format,
        Store.administrative,
        Store.market_type,
        Store.phone,
        Store.settlement_account,
        Store.circle,
        Store.is_downgrade,
        Store.car_1,
        Store.car_2,
        Store.car_3,
        Store.car_photo1,
        Store.car_photo2,
        Store.car_photo3,
        Store.operators1,
        Store.license_ship1,
        Store.operators2,
        Store.license_ship2,
        Store.operators3,
        Store.license_ship3,
        Store.special_category,
        Store.special_History
    ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
    storedata = pagination.items
    count = pagination.total
    data = {
        'data': storedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 查询某个稽查所下所有零售户
@blue_print.route('/getAllStoreInfoByDepartid', methods=['POST'])
def get_all_storeinfo_by_departid():
    """
            @api {POST} api/store/getAllStoreInfoByDepartid 查询某个稽查所下所有零售户
            @apiVersion 0.0.1
            @apiName getAllStoreInfoByDepartid
            @apiGroup store
            @apiDescription 查询某个稽查所下所有零售户,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  department_id     (必须)    稽查所/队id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "department_id":1,
                    "page":2,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
    """
    params = storeinfo_by_depart_id_schema(request.json or '')
    department_id = params.get('department_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(PersonInfo).join(Store, Department).filter(Store.department_id == department_id,
                                                                             Store.is_delete == 0).with_entities(
        Store.store_name,
        Store.id,
        Store.department_id,
        Department.depart_name,
        Store.person_id,
        PersonInfo.name,
        Store.picture,
        Store.business_number,
        Store.is_bigillegal,
        Store.business_start,
        Store.business_termi,
        Store.longitude,
        Store.latitude,
        Store.address,
        Store.state,
        Store.store_category,
        Store.is_chain,
        Store.is_suspension,
        Store.business_format,
        Store.administrative,
        Store.market_type,
        Store.phone,
        Store.settlement_account,
        Store.circle,
        Store.is_downgrade,
        Store.car_1,
        Store.car_2,
        Store.car_3,
        Store.car_photo1,
        Store.car_photo2,
        Store.car_photo3,
        Store.operators1,
        Store.license_ship1,
        Store.operators2,
        Store.license_ship2,
        Store.operators3,
        Store.license_ship3,
        Store.special_category,
        Store.special_History
    ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
    storedata = pagination.items
    count = pagination.total
    data = {
        'data': storedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过零售户名查询零售户--模糊查询--分页
@blue_print.route('/getAllStoreInfoByStorename', methods=['POST'])
def get_all_storeinfo_by_storename():
    """
                @api {POST} api/store/getAllStoreInfoByStorename 通过零售户名查询零售户--模糊查询--分页
                @apiVersion 0.0.1
                @apiName getAllStoreInfoByStorename
                @apiGroup store
                @apiDescription 通过零售户名查询零售户
                @apiParam {string}  store_name     (必须)    零售户名称
                @apiParam {int}  page     (必须)    页数
                @apiParam {int}  per_page     (必须)    每页的页数
                @apiParam {int}  role_id     (必须)    角色id
                @apiParam {int}  station_id     (可选)    专卖局id
                @apiParam {int}  department_id     (可选)    稽查所id
                @apiParamExample {json} Request-Example:
                { role_id为1是系统管理员，可以查询全部数据，不需要专卖局id和稽查所id
                    "store_name":"文丽烟店",
                    "page":1,
                    "per_page":8,
                    "role_id":1
                }
                @apiSuccessExample {json} Success-Response:
                    {
                        "sys_status": "SUCCESS",
                        "data": {
                            "data": [
                                {
                                    "store_name": "金华市婺城区文丽烟店",
                                    "id": 924,
                                    "department_id": 1,
                                    "depart_name": "专卖城区二所",
                                    "person_id": 924,
                                    "name": "高文丽",
                                    "picture": null,
                                    "business_number": "330701203202",
                                    "is_bigillegal": false,
                                    "business_start": "2016-09-12",
                                    "business_termi": "2021-09-01",
                                    "longitude": "119.657161000000",
                                    "latitude": "29.084430000000",
                                    "address": "金华市婺城区宾虹路439弄2幢",
                                    "state": {
                                        "NARMAL": "正常经营"
                                    },
                                    "store_category": "D4",
                                    "is_chain": false,
                                    "is_suspension": false,
                                    "business_format": {
                                        "YANJIU": "烟酒商店"
                                    },
                                    "administrative": {
                                        "BENJI": "市辖区"
                                    },
                                    "market_type": {
                                        "URBAN": "市区"
                                    },
                                    "phone": "15355894148",
                                    "settlement_account": " ",
                                    "circle": {
                                        "ZHENGWU": "政务（商务）区"
                                    },
                                    "is_downgrade": null,
                                    "car_1": null,
                                    "car_2": null,
                                    "car_3": null,
                                    "car_photo1": null,
                                    "car_photo2": null,
                                    "car_photo3": null,
                                    "operators1": "高文丽",
                                    "license_ship1": null,
                                    "operators2": null,
                                    "license_ship2": null,
                                    "operators3": null,
                                    "license_ship3": null,
                                    "special_category": {
                                        "NORMAL": "普通"
                                    },
                                    "special_History": null
                                }
                            ],
                            "count": 1
                        },
                        "message": " "
                    }
                @apiParamExample {json} Request-Example:
                { 如果是role_id为2或者5时，搜索范围是全局,如果局长或者队长是station_id = 1(金华市总局)，搜索范围和系统管理员一样，可以看到整个金华市
                    "store_name":"文丽烟店",
                    "page":1,
                    "per_page":8,
                    "role_id":2,
                    "station_id":1
                }
                @apiSuccessExample {json} Success-Response:
                     {
                        "sys_status": "SUCCESS",
                        "data": {
                            "data": [
                                {
                                    "store_name": "金华市婺城区文丽烟店",
                                    "id": 924,
                                    "department_id": 1,
                                    "depart_name": "专卖城区二所",
                                    "person_id": 924,
                                    "name": "高文丽",
                                    "picture": null,
                                    "business_number": "330701203202",
                                    "is_bigillegal": false,
                                    "business_start": "2016-09-12",
                                    "business_termi": "2021-09-01",
                                    "longitude": "119.657161000000",
                                    "latitude": "29.084430000000",
                                    "address": "金华市婺城区宾虹路439弄2幢",
                                    "state": {
                                        "NARMAL": "正常经营"
                                    },
                                    "store_category": "D4",
                                    "is_chain": false,
                                    "is_suspension": false,
                                    "business_format": {
                                        "YANJIU": "烟酒商店"
                                    },
                                    "administrative": {
                                        "BENJI": "市辖区"
                                    },
                                    "market_type": {
                                        "URBAN": "市区"
                                    },
                                    "phone": "15355894148",
                                    "settlement_account": " ",
                                    "circle": {
                                        "ZHENGWU": "政务（商务）区"
                                    },
                                    "is_downgrade": null,
                                    "car_1": null,
                                    "car_2": null,
                                    "car_3": null,
                                    "car_photo1": null,
                                    "car_photo2": null,
                                    "car_photo3": null,
                                    "operators1": "高文丽",
                                    "license_ship1": null,
                                    "operators2": null,
                                    "license_ship2": null,
                                    "operators3": null,
                                    "license_ship3": null,
                                    "special_category": {
                                        "NORMAL": "普通"
                                    },
                                    "special_History": null
                                }
                            ],
                            "count": 1
                        },
                        "message": " "
                    }
                @apiParamExample {json} Request-Example:
               { role_id 为3或者4，查询范围在稽查所内
                    "store_name":"文丽烟店",
                    "page":1,
                    "per_page":8,
                    "role_id":3,
                    "station_id":1,
                    "department_id":1
                }
                @apiSuccessExample {json} Success-Response:
                     {
                        "sys_status": "SUCCESS",
                        "data": {
                            "data": [
                                {
                                    "store_name": "金华市婺城区文丽烟店",
                                    "id": 924,
                                    "department_id": 1,
                                    "depart_name": "专卖城区二所",
                                    "person_id": 924,
                                    "name": "高文丽",
                                    "picture": null,
                                    "business_number": "330701203202",
                                    "is_bigillegal": false,
                                    "business_start": "2016-09-12",
                                    "business_termi": "2021-09-01",
                                    "longitude": "119.657161000000",
                                    "latitude": "29.084430000000",
                                    "address": "金华市婺城区宾虹路439弄2幢",
                                    "state": {
                                        "NARMAL": "正常经营"
                                    },
                                    "store_category": "D4",
                                    "is_chain": false,
                                    "is_suspension": false,
                                    "business_format": {
                                        "YANJIU": "烟酒商店"
                                    },
                                    "administrative": {
                                        "BENJI": "市辖区"
                                    },
                                    "market_type": {
                                        "URBAN": "市区"
                                    },
                                    "phone": "15355894148",
                                    "settlement_account": " ",
                                    "circle": {
                                        "ZHENGWU": "政务（商务）区"
                                    },
                                    "is_downgrade": null,
                                    "car_1": null,
                                    "car_2": null,
                                    "car_3": null,
                                    "car_photo1": null,
                                    "car_photo2": null,
                                    "car_photo3": null,
                                    "operators1": "高文丽",
                                    "license_ship1": null,
                                    "operators2": null,
                                    "license_ship2": null,
                                    "operators3": null,
                                    "license_ship3": null,
                                    "special_category": {
                                        "NORMAL": "普通"
                                    },
                                    "special_History": null
                                }
                            ],
                            "count": 1
                        },
                        "message": " "
                    }
    """
    params = storeinfo_by_store_name_schema(request.json or '')
    store_name = params.get('store_name')
    page = params.get('page')
    per_page = params.get('per_page')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    if role_id == 1:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(
            Store.store_name.like("%" + store_name + "%") if store_name is not None else "",
            Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 5:
        if station_id == 1:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                Store.store_name.like("%" + store_name + "%") if store_name is not None else "",
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                Department.station_id == station_id).filter(Store.department_id == Department.id).filter(
                Store.store_name.like("%" + store_name + "%") if store_name is not None else "",
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id == 4:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(
            Store.department_id == department_id).filter(
            Store.store_name.like("%" + store_name + "%") if store_name is not None else "",
            Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过零售户id获取零售户详细信息
@blue_print.route('/getStoreInfoByStoreid', methods=['POST'])
def get_storeinfo_by_storeid():
    """
            @api {POST} api/store/getStoreInfoByStoreid 通过零售户id获取零售户详细信息
            @apiVersion 0.0.1
            @apiName getStoreInfoByStoreid
            @apiGroup store
            @apiDescription 通过零售户id获取零售户详细信息
            @apiParam {int}  store_id     (必须)    零售商户id
            @apiParamExample {json} Request-Example:
                {
                    "store_id":5
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "store_name": "金华市婺城区周根花便利店",
                            "id": 5,
                            "department_id": 1,
                            "depart_name": "专卖城区二所",
                            "person_id": 5,
                            "name": "周根花",
                            "picture": null,
                            "business_number": "330701102270",
                            "is_bigillegal": false,
                            "business_start": "2016-10-18",
                            "business_termi": "2021-10-08",
                            "longitude": "119.566353000000",
                            "latitude": "28.932751000000",
                            "address": "金华市婺城区安地镇七间屋村",
                            "state": {
                                "NARMAL": "正常经营"
                            },
                            "store_category": "L4",
                            "is_chain": false,
                            "is_suspension": false,
                            "business_format": {
                                "SHIZA": "食杂店"
                            },
                            "administrative": {
                                "BENJI": "市辖区"
                            },
                            "market_type": {
                                "COUNTRYSIDE": "农村"
                            },
                            "phone": "13486936713",
                            "settlement_account": " ",
                            "circle": {
                                "ZHENGWU": "政务（商务）区"
                            },
                            "is_downgrade": null,
                            "car_1": null,
                            "car_2": null,
                            "car_3": null,
                            "car_photo1": null,
                            "car_photo2": null,
                            "car_photo3": null,
                            "operators1": "郑渊",
                            "license_ship1": null,
                            "operators2": null,
                            "license_ship2": null,
                            "operators3": null,
                            "license_ship3": null,
                            "special_category": {
                                "NORMAL": "普通"
                            },
                            "special_History": null
                        }
                    ],
                    "message": " "
                }
    """
    params = storeinfo_by_storeid_schema(request.json or '')
    store_id = params.get('store_id')
    data = db.session.query(PersonInfo).join(Store, Department).filter(Store.id == store_id,
                                                                       Store.is_delete == 0).with_entities(
        Store.store_name,
        Store.id,
        Store.department_id,
        Department.depart_name,
        Store.person_id,
        PersonInfo.name,
        Store.picture,
        Store.business_number,
        Store.is_bigillegal,
        Store.business_start,
        Store.business_termi,
        Store.longitude,
        Store.latitude,
        Store.address,
        Store.state,
        Store.store_category,
        Store.is_chain,
        Store.is_suspension,
        Store.business_format,
        Store.administrative,
        Store.market_type,
        Store.phone,
        Store.settlement_account,
        Store.circle,
        Store.is_downgrade,
        Store.car_1,
        Store.car_2,
        Store.car_3,
        Store.car_photo1,
        Store.car_photo2,
        Store.car_photo3,
        Store.operators1,
        Store.license_ship1,
        Store.operators2,
        Store.license_ship2,
        Store.operators3,
        Store.license_ship3,
        Store.special_category,
        Store.special_History
    ).order_by(Store.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 修改店铺信息
@blue_print.route('/modifyStoreInfo', methods=['POST'])
def store_modify():
    """
        @api {post} api/store/modifyStoreInfo  修改店铺信息
        @apiVersion 0.0.1
        @apiName store_modify
        @apiGroup store
        @apiDescription 修改店铺信息
        @apiParam {int}  store_id     (必须)    店铺id
        @apiParam {String}  store_name      (可选)    店铺名称
        @apiParam {int}  department_id    (可选)    所属稽查所id
        @apiParam {int}  person_id    (可选)    零售户法人信息id
        @apiParam {String}  picture    (可选)    店铺俯视图
        @apiParam {String}  business_number    (可选)    烟草经营许可证号
        @apiParam {Boolean}  is_bigillegal  (可选)    是否为违法大户
        @apiParam {date}  business_start    (可选)    烟草经营许可证有效期始
        @apiParam {date}  business_termi    (可选)    烟草经营许可证有效期止
        @apiParam {string}  longitude    (可选)    地址经度
        @apiParam {string}  latitude    (可选)    地址纬度
        @apiParam {String}  address    (可选)    经营地址
        @apiParam {Enum}  state    (可选)    经营状态
        @apiParam {String}  store_category    (可选)    零售户合理定量类别
        @apiParam {Boolean}  is_chain   (可选)    是否连锁
        @apiParam {Boolean}  is_suspension   (可选)    是否暂停货源
        @apiParam {Enum}  business_format    (可选)    经营业态
        @apiParam {Enum}  administrative    (可选)    行政区划分
        @apiParam {Enum}  market_type    (可选)    市场类型
        @apiParam {String}  phone    (可选)    主呼电话
        @apiParam {string}  settlement_account      (可选)    电子结算账号
        @apiParam {Enum}  circle     (可选)   商圈
        @apiParam {Boolean}  is_downgrade      (可选)    是否有降级降档情况
        @apiParam {string}  car_1      (可选)    车辆牌照1
        @apiParam {string}  car_2      (可选)    车辆牌照2
        @apiParam {string}  car_3      (可选)    车辆牌照3
        @apiParam {string}  car_photo1      (可选)    车辆牌照图1
        @apiParam {string}  car_photo2      (可选)    车辆牌照图2
        @apiParam {string}  car_photo3      (可选)    车辆牌照图3
        @apiParam {string}  operators1      (可选)    日常经营人1
        @apiParam {Enum}  license_ship1    (可选)    与持证人关系1
        @apiParam {string}  operators2      (可选)    日常经营人2
        @apiParam {Enum}  license_ship2    (可选)    与持证人关系2
        @apiParam {string}  operators3      (可选)    日常经营人3
        @apiParam {Enum}  license_ship3    (可选)    与持证人关系3
        @apiParam {Enum}  special_category    (可选)    特殊群体类别
        @apiParam {Enum}  special_History    (可选)    特殊历史类别
        @apiParamExample {json} Request-Example:
            {
                "longitude":"129.4587412",
                "store_id":34248
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "零售户信息修改成功"
            }
    """
    params = store_info_schema(request.json or '')
    store_id = params.get('store_id')
    store = Store.query.filter(Store.id == store_id, Store.is_delete == 0)
    params.pop('store_id')
    store.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '零售户信息修改成功')


# 删除店铺
@blue_print.route('/delStore', methods=['POST'])
def delete_store():
    """
        @api {POST} api/store/delStore  删除店铺
        @apiVersion 0.0.1
        @apiName delete_store
        @apiGroup store
        @apiDescription 删除店铺
        @apiParam {String}  store_name      (必须)    店铺名称
        @apiParam {int}  store_id     (必须)    店铺id
        @apiParamExample {json} Request-Example:
           {
                "store_name":"金华市香香食品便利店",
                "store_id":34248
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "零售户删除成功"
            }
    """
    params = del_store_schema(request.json or '')
    store_name = params.get('store_name')
    store_id = params.get('store_id')
    is_delete = 1
    store = Store.query.filter(Store.id == store_id, Store.store_name == store_name, Store.is_delete == 0).first()
    store.is_delete = is_delete
    store.save()
    return common_response(SysStatus.SUCCESS, store.is_delete, '零售户删除成功')


# 添加法人信息
@blue_print.route('/addPersonInfo', methods=['POST'])
def add_PersonInfo():
    """
        @api {post} api/store/addPersonInfo  添加法人信息
        @apiVersion 0.0.1
        @apiName addPersonInfo
        @apiGroup store
        @apiDescription 添加法人信息
        @apiParam {String}  name      (必须)    法人姓名
        @apiParam {String}  sex    (必须)    性别
        @apiParam {String}  id_card    (必须)    零售户法人信息id
        @apiParam {String}  id_address    (可选)    身份证住址
        @apiParam {date}  birthday    (可选)    出生日期
        @apiParam {string}  nation    (可选)    民族
        @apiParam {string}  census_register    (可选)    籍贯
        @apiParam {String}  phone    (可选)    联系电话
        @apiParam {String}  address    (可选)    地址
        @apiParamExample {json} Request-Example:
           {
                "name":"李三黑",
                "sex":"男性",
                "id_card":"341282199503026057",
                "id_address":"金华市婺城区浙江师范大学",
                "birthday":"1995-08-08",
                "nation":"汉族",
                "census_register":"金华市婺城区",
                "phone":"18225879332",
                "address":"金华市婺城区义乌街151号"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "法人添加成功"
            }

        @apiErrorExample {json} Error-Response:
            {
                 "sys_status": "FAIL",
                 "data": "李三黑",
                 "message": "该法人已被添加"
            }

    """
    params = add_personinfo_schema(request.json or '')
    name = params.get('name')
    sex = params.get('sex')
    id_card = params.get('id_card')
    id_address = params.get('id_address')
    birthday = params.get('birthday')
    nation = params.get('nation')
    census_register = params.get('census_register')
    phone = params.get('phone')
    address = params.get('address')
    personinfo = PersonInfo.query.filter(PersonInfo.id_card == id_card, PersonInfo.is_delete == 0).first()
    if personinfo:
        return common_response(SysStatus.FAIL, personinfo.name, '该法人已被添加')
    else:
        personinfo = PersonInfo(name=name, sex=sex, id_card=id_card, id_address=id_address, birthday=birthday,
                                nation=nation, census_register=census_register, address=address, phone=phone)
        db.session.add(personinfo)
        db.session.commit()
        return common_response(SysStatus.SUCCESS, None, '法人添加成功')


# 通过角色id查询法人信息
@blue_print.route('/getAllPersonInfobyroleid', methods=['POST'])
def get_all_personinfo_by_role_id():
    """
            @api {POST} api/store/getAllPersonInfobyroleid 通过角色id查询法人信息
            @apiVersion 0.0.1
            @apiName getAllPersonInfobyroleid
            @apiGroup store
            @apiDescription 通过角色id查询法人信息,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  department_id     (可选)    稽查所id
             @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParamExample {json} Request-Example:
                { role_id为1是系统管理员，不需要专卖局id和稽查所id
                    "role_id":1,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 1,
                                "name": "王建玲",
                                "sex": "女性",
                                "id_card": "330721195905153626",
                                "id_address": "浙江省金华市婺城区安地镇安地村812号",
                                "birthday": "1959-05-15",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "浙江省金华市婺城区安地镇安地村812号"
                            },
                            {
                                "id": 2,
                                "name": "余寿忠",
                                "sex": "女性",
                                "id_card": "330721196309103811",
                                "id_address": "金华市婺城区箬阳乡箬阳村",
                                "birthday": "1963-09-10",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "金华市婺城区箬阳乡箬阳村"
                            },
                            {
                                "id": 3,
                                "name": "陈宝琴",
                                "sex": "女性",
                                "id_card": "330721196301293825",
                                "id_address": "金华市婺城区箬阳乡石井坑村坑口自然村58号",
                                "birthday": "1963-01-29",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "金华市婺城区箬阳乡石井坑村坑口自然村58号"
                            },
                            {
                                "id": 4,
                                "name": "李基虎",
                                "sex": "女性",
                                "id_card": "330721195706233834",
                                "id_address": "浙江省金华市婺城区箬阳乡黄阳村020号",
                                "birthday": "1957-06-23",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "浙江省金华市婺城区箬阳乡黄阳村020号"
                            },
                            {
                                "id": 5,
                                "name": "周根花",
                                "sex": "女性",
                                "id_card": "330721194401133723",
                                "id_address": "浙江省金华市婺城区安地镇七间屋村",
                                "birthday": "1944-01-13",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "浙江省金华市婺城区安地镇七间屋村"
                            },
                            {
                                "id": 6,
                                "name": "汪惠珍",
                                "sex": "男性",
                                "id_card": "330721196005143726",
                                "id_address": "浙江省金华市婺城区安地镇西周村44号",
                                "birthday": "1960-05-14",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "安地镇西周村"
                            },
                            {
                                "id": 7,
                                "name": "翁春仙",
                                "sex": "男性",
                                "id_card": "330721195704283627",
                                "id_address": "安地镇上傅村",
                                "birthday": "1957-04-28",
                                "nation": "汉",
                                "census_register": null,
                                "phone": "15957956263",
                                "address": "安地镇上傅村"
                            },
                            {
                                "id": 8,
                                "name": "申雪香",
                                "sex": "女性",
                                "id_card": "330721196312153625",
                                "id_address": "浙江省金华市婺城区安地镇下傅村193号",
                                "birthday": "1963-12-15",
                                "nation": "汉",
                                "census_register": null,
                                "phone": null,
                                "address": "安地镇下傅村"
                            }
                        ],
                        "count": 34248
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                { role_id为2或者5时，不需要稽查所id，查询范围是整个局，如果局id是station_id = 1,则查询范围是整个金华市，其他的查询范围是整个分局
                    "role_id":5,
                    "page":1,
                    "per_page":8,
                    "station_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
            @apiParamExample {json} Request-Example:
                { role_id是3或者4，查询范围是整个稽查所
                    "department_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8,
                    "station_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
    """
    params = personinfo_by_role_id_schema(request.json or '')
    department_id = params.get('department_id')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    if role_id == 1:
        pagination = PersonInfo.query.filter(PersonInfo.is_delete == 0).with_entities(
            PersonInfo.id,
            PersonInfo.name,
            PersonInfo.sex,
            PersonInfo.id_card,
            PersonInfo.id_address,
            PersonInfo.birthday,
            PersonInfo.nation,
            PersonInfo.census_register,
            PersonInfo.phone,
            PersonInfo.address
        ).order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 5:
        if station_id == 1:
            pagination = PersonInfo.query.filter(PersonInfo.is_delete == 0).with_entities(
                PersonInfo.id,
                PersonInfo.name,
                PersonInfo.sex,
                PersonInfo.id_card,
                PersonInfo.id_address,
                PersonInfo.birthday,
                PersonInfo.nation,
                PersonInfo.census_register,
                PersonInfo.phone,
                PersonInfo.address
            ).order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                Department.station_id == station_id).filter(Store.department_id == Department.id,
                                                            Store.is_delete == 0).filter(PersonInfo.id == Store.person_id,
                                                                                         PersonInfo.is_delete == 0).with_entities(
                PersonInfo.id,
                PersonInfo.name,
                PersonInfo.sex,
                PersonInfo.id_card,
                PersonInfo.id_address,
                PersonInfo.birthday,
                PersonInfo.nation,
                PersonInfo.census_register,
                PersonInfo.phone,
                PersonInfo.address
            ).order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id == 4:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(Store.department_id == department_id,
                                                                                 Store.is_delete == 0).filter(
            PersonInfo.id == Store.person_id, PersonInfo.is_delete == 0).with_entities(
            PersonInfo.id,
            PersonInfo.name,
            PersonInfo.sex,
            PersonInfo.id_card,
            PersonInfo.id_address,
            PersonInfo.birthday,
            PersonInfo.nation,
            PersonInfo.census_register,
            PersonInfo.phone,
            PersonInfo.address
        ).order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    return common_response(SysStatus.FAIL, None, '您无权查询')


# 直接通过get方法获取所有法人信息
@blue_print.route('/getAllPersonInfo', methods=['GET'])
def get_all_personinfo():
    """
            @api {GET} api/store/getAllPersonInfo 直接获取所有法人信息
            @apiVersion 0.0.1
            @apiName getAllPersonInfo
            @apiGroup store
            @apiDescription 直接获取所有法人信息,此处使用了分页功能，因为是get方法，所以page参数通过访问地址访问，per_page参数指定每页显示多少内容
            @apiSuccessExample {json} Success-Response:
                {
                   示例:http://39.96.52.170:5000/api/store/getAllPersonInfo?page=2&per_page=8  可以获取第二页的8条内容
                }
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = PersonInfo.query.filter(PersonInfo.is_delete == 0).with_entities(
        PersonInfo.id,
        PersonInfo.name,
        PersonInfo.sex,
        PersonInfo.id_card,
        PersonInfo.id_address,
        PersonInfo.birthday,
        PersonInfo.nation,
        PersonInfo.census_register,
        PersonInfo.phone,
        PersonInfo.address
    ).order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
    storedata = pagination.items
    count = pagination.total
    data = {
        'data': storedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')
# 通过法人姓名查询法人--模糊查询--分页--不带角色
@blue_print.route('/getAllPersonInfoBynamenotroleid', methods=['POST'])
def get_all_personinfo_by_name_notid():
    """
                @api {POST} api/store/getAllPersonInfoBynamenotroleid 通过法人姓名查询法人--模糊查询--分页--不带角色
                @apiVersion 0.0.1
                @apiName getAllPersonInfoBynamenotroleid
                @apiGroup store
                @apiDescription 通过法人姓名查询法人,使用分页和模糊查询,不使用角色id
                @apiParam {string}  name     (必须)    法人姓名
                @apiParam {int}  page     (必须)    页数
                @apiParam {int}  per_page     (必须)    每页的页数
                @apiParamExample {json} Request-Example:
                {
                    "name":"文丽",
                    "page":1,
                    "per_page":8,
                }
                @apiSuccessExample {json} Success-Response:
                   {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 924,
                                "name": "高文丽",
                                "sex": "女性",
                                "id_card": "330702197204260445",
                                "id_address": "三江街道宾虹路439弄西2幢1单元601",
                                "birthday": "1972-04-26",
                                "nation": "汉",
                                "census_register": "浙江省金华市婺城区",
                                "phone": null,
                                "address": "宾虹路439号2幢"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = personinfo_by_name_notid_schema(request.json or '')
    name = params.get('name')
    page = params.get('page')
    per_page = params.get('per_page')
    person_data = PersonInfo.query.filter(like_filter(name, PersonInfo.name),
                                              PersonInfo.is_delete == 0).with_entities(*person_info_ser) \
            .order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
    data = {'data': person_data.items, 'count': person_data.total}
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过法人姓名查询法人--模糊查询--分页
@blue_print.route('/getAllPersonInfoByname', methods=['POST'])
def get_all_personinfo_by_name():
    """
                @api {POST} api/store/getAllPersonInfoByname 通过法人姓名查询法人--模糊查询--分页
                @apiVersion 0.0.1
                @apiName getAllPersonInfoByname
                @apiGroup store
                @apiDescription 通过法人姓名查询法人,使用分页和模糊查询
                @apiParam {string}  name     (必须)    法人姓名
                @apiParam {int}  page     (必须)    页数
                @apiParam {int}  per_page     (必须)    每页的页数
                @apiParam {int}  role_id     (必须)    角色id
                @apiParam {int}  station_id     (可选)    专卖局id
                @apiParam {int}  department_id     (可选)    稽查所id
                @apiParamExample {json} Request-Example:
                {role_id为1是系统管理员，不需要专卖局id和稽查所id
                    "name":"文丽",
                    "page":1,
                    "per_page":8,
                    "role_id":1
                }
                @apiSuccessExample {json} Success-Response:
                  {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 924,
                                "name": "高文丽",
                                "sex": "女性",
                                "id_card": "330702197204260445",
                                "id_address": "三江街道宾虹路439弄西2幢1单元601",
                                "birthday": "1972-04-26",
                                "nation": "汉",
                                "census_register": "浙江省金华市婺城区",
                                "phone": null,
                                "address": "宾虹路439号2幢"
                            }
                        ],
                        "count": 1
                    },
                    "message": "成功"
                }
                @apiParamExample {json} Request-Example:
                { role_id为2或者5时，不需要稽查所id，查询范围是整个局，如果局id是station_id = 1,则查询范围是整个金华市，其他的查询范围是整个分局
                    "name":"文丽",
                    "page":1,
                    "per_page":8,
                    "role_id":2,
                    "station_id":1
                }
                @apiSuccessExample {json} Success-Response:
                 {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 924,
                                "name": "高文丽",
                                "sex": "女性",
                                "id_card": "330702197204260445",
                                "id_address": "三江街道宾虹路439弄西2幢1单元601",
                                "birthday": "1972-04-26",
                                "nation": "汉",
                                "census_register": "浙江省金华市婺城区",
                                "phone": null,
                                "address": "宾虹路439号2幢"
                            }
                        ],
                        "count": 1
                    },
                    "message": "成功"
                }
                @apiParamExample {json} Request-Example:
                {role_id是3或者4，查询范围是整个稽查所
                    "name":"文丽",
                    "page":1,
                    "per_page":8,
                    "role_id":3,
                     "station_id":1,
                    "department_id":1
                }
                @apiSuccessExample {json} Success-Response:
                 {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 924,
                                "name": "高文丽",
                                "sex": "女性",
                                "id_card": "330702197204260445",
                                "id_address": "三江街道宾虹路439弄西2幢1单元601",
                                "birthday": "1972-04-26",
                                "nation": "汉",
                                "census_register": "浙江省金华市婺城区",
                                "phone": null,
                                "address": "宾虹路439号2幢"
                            }
                        ],
                        "count": 1
                    },
                    "message": "成功"
                }
    """
    params = personinfo_by_name_schema(request.json or '')
    name = params.get('name')
    page = params.get('page')
    per_page = params.get('per_page')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    if role_id == 1:
        person_data = PersonInfo.query.filter(like_filter(name, PersonInfo.name),
                                              PersonInfo.is_delete == 0).with_entities(*person_info_ser) \
            .order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
        data = {'data': person_data.items, 'count': person_data.total}
        return common_response(SysStatus.SUCCESS, data)

    if role_id == 2 or role_id == 5:
        if station_id == 1:
            person_data = PersonInfo.query.filter(like_filter(name, PersonInfo.name),
                                                  PersonInfo.is_delete == 0).with_entities(*person_info_ser) \
                .order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
            data = {'data': person_data.items, 'count': person_data.total}
            return common_response(SysStatus.SUCCESS, data)
        else:
            person_data = PersonInfo.query.join(Store, Department) \
                .filter(Department.station_id == station_id,PersonInfo.is_delete.is_(False),Store.is_delete.is_(False),
                        like_filter(keyword=name, column=PersonInfo.name)) \
                .with_entities(*person_info_ser).order_by(PersonInfo.id).paginate(page, per_page=per_page, error_out=False)
            data = {'data': person_data.items, 'count': person_data.total}
            return common_response(SysStatus.SUCCESS, data)

    if role_id == 3 or role_id == 4:
        person_data = PersonInfo.query.join(Store, Department) \
            .filter(Store.department_id == department_id,
                    PersonInfo.is_delete.is_(False),
                    Store.is_delete.is_(False),
                    like_filter(keyword=name, column=PersonInfo.name)) \
            .with_entities(*person_info_ser).order_by(PersonInfo.id).paginate(page=page, per_page=per_page,
                                                                              error_out=False)

        data = {'data': person_data.items, 'count': person_data.total}
        return common_response(SysStatus.SUCCESS, data)


# 通过法人id获取法人详细信息
@blue_print.route('/getPersonInfoByid', methods=['POST'])
def get_personinfo_by_id():
    """
            @api {POST} api/store/getPersonInfoByid 通过法人id获取法人详细信息
            @apiVersion 0.0.1
            @apiName getPersonInfoByid
            @apiGroup store
            @apiDescription 通过法人id获取法人详细信息
            @apiParam {int}  person_id     (必须)    法人id
            @apiParamExample {json} Request-Example:
                {
                    "person_id":1524
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 1524,
                            "name": "陈桂芳",
                            "sex": "女性",
                            "id_card": "330721195408286727",
                            "id_address": "浙江省金华市婺城区罗埠镇府前路2号",
                            "birthday": "1954-08-28",
                            "nation": "汉",
                            "census_register": null,
                            "phone": null,
                            "address": "罗埠镇商贸街"
                        }
                    ],
                    "message": " "
                }
    """
    params = personinfo_by_id_schema(request.json or '')
    person_id = params.get('person_id')
    data = PersonInfo.query.filter(PersonInfo.id == person_id, PersonInfo.is_delete == 0).with_entities(
        PersonInfo.id,
        PersonInfo.name,
        PersonInfo.sex,
        PersonInfo.id_card,
        PersonInfo.id_address,
        PersonInfo.birthday,
        PersonInfo.nation,
        PersonInfo.census_register,
        PersonInfo.phone,
        PersonInfo.address
    ).order_by(PersonInfo.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 修改法人信息
@blue_print.route('/modifyPersonInfo', methods=['POST'])
def person_modify():
    """
        @api {post} api/store/modifyPersonInfo  修改法人信息
        @apiVersion 0.0.1
        @apiName modifyPersonInfo
        @apiGroup store
        @apiDescription 修改法人信息
        @apiParam {int}  person_id      (必须)    法人id
        @apiParam {String}  name      (可选)    法人姓名
        @apiParam {String}  sex    (可选)    性别
        @apiParam {String}  id_card    (可选)    零售户法人信息id
        @apiParam {String}  id_address    (可选)    身份证住址
        @apiParam {date}  birthday    (可选)    出生日期
        @apiParam {string}  nation    (可选)    民族
        @apiParam {string}  census_register    (可选)    籍贯
        @apiParam {String}  phone    (可选)    联系电话
        @apiParam {String}  address    (可选)    地址
        @apiParamExample {json} Request-Example:
            {
                "person_id":34248,
                "name":"李旋风"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "法人信息修改成功"
            }
    """
    params = person_info_schema(request.json or '')
    person_id = params.get('person_id')
    person = PersonInfo.query.filter(PersonInfo.id == person_id, PersonInfo.is_delete == 0)
    params.pop('person_id')
    person.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '法人信息修改成功')


# 删除法人信息
@blue_print.route('/delPersoninfo', methods=['POST'])
def delete_personinfo():
    """
        @api {POST} api/store/delPersoninfo  删除法人信息
        @apiVersion 0.0.1
        @apiName delPersoninfo
        @apiGroup store
        @apiDescription 删除法人信息
        @apiParam {String}  name      (必须)    法人姓名
        @apiParam {int}  person_id     (必须)    法人id
        @apiParamExample {json} Request-Example:
            {
                "name":"李旋风",
                "person_id":34248
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "法人删除成功"
            }
    """
    params = del_personinfo_schema(request.json or '')
    name = params.get('name')
    person_id = params.get('person_id')
    is_delete = 1
    person = PersonInfo.query.filter(PersonInfo.id == person_id, PersonInfo.name == name,
                                     PersonInfo.is_delete == 0).first()
    person.is_delete = is_delete
    person.save()
    return common_response(SysStatus.SUCCESS, person.is_delete, '法人删除成功')


# 根据店铺id获取法人信息
@blue_print.route('/getPersonInfoByStoreid', methods=['POST'])
def get_personinfo_by_storeid():
    """
        @api {POST} api/store/getPersonInfoByStoreid 根据店铺id获取法人信息
        @apiVersion 0.0.1
        @apiName getPersonInfoByStoreid
        @apiGroup store
        @apiDescription 根据店铺id获取法人信息
        @apiParam {int}  store_id     (必须)    零售商户id
        @apiParamExample {json} Request-Example:
            {
                "store_id":5
            }
        @apiSuccessExample {json} Success-Response:
           {
                "sys_status": "SUCCESS",
                "data": [
                    {
                        "id": 5,
                        "name": "周根花",
                        "sex": "女性",
                        "id_card": "330721194401133723",
                        "id_address": "浙江省金华市婺城区安地镇七间屋村",
                        "birthday": "1944-01-13",
                        "nation": "汉",
                        "census_register": null,
                        "phone": null,
                        "address": "浙江省金华市婺城区安地镇七间屋村"
                    }
                ],
                "message": " "
            }
    """
    params = personinfo_by_store_id_schema(request.json or '')
    store_id = params.get('store_id')
    store = Store.query.filter(Store.id == store_id).first()
    person_id = store.person_id
    data = PersonInfo.query.filter(PersonInfo.id == person_id, PersonInfo.is_delete == 0).with_entities(
        PersonInfo.id,
        PersonInfo.name,
        PersonInfo.sex,
        PersonInfo.id_card,
        PersonInfo.id_address,
        PersonInfo.birthday,
        PersonInfo.nation,
        PersonInfo.census_register,
        PersonInfo.phone,
        PersonInfo.address
    ).order_by(PersonInfo.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据法人id获取店铺信息
@blue_print.route('/getStoreInfoBypersonid', methods=['POST'])
def get_storeinfo_by_personid():
    """
            @api {POST} api/store/getStoreInfoBypersonid 根据法人id获取店铺信息
            @apiVersion 0.0.1
            @apiName getStoreInfoBypersonid
            @apiGroup store
            @apiDescription 根据法人id获取店铺信息
            @apiParam {int}  person_id     (必须)    法人id
            @apiParamExample {json} Request-Example:
                {
                    "person_id":5
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "store_name": "金华市婺城区周根花便利店",
                            "id": 5,
                            "department_id": 1,
                            "depart_name": "专卖城区二所",
                            "person_id": 5,
                            "name": "周根花",
                            "picture": null,
                            "business_number": "330701102270",
                            "is_bigillegal": false,
                            "business_start": "2016-10-18",
                            "business_termi": "2021-10-08",
                            "longitude": "119.566353000000",
                            "latitude": "28.932751000000",
                            "address": "金华市婺城区安地镇七间屋村",
                            "state": {
                                "NARMAL": "正常经营"
                            },
                            "store_category": "L4",
                            "is_chain": false,
                            "is_suspension": false,
                            "business_format": {
                                "SHIZA": "食杂店"
                            },
                            "administrative": {
                                "BENJI": "市辖区"
                            },
                            "market_type": {
                                "COUNTRYSIDE": "农村"
                            },
                            "phone": "13486936713",
                            "settlement_account": " ",
                            "circle": {
                                "ZHENGWU": "政务（商务）区"
                            },
                            "is_downgrade": null,
                            "car_1": null,
                            "car_2": null,
                            "car_3": null,
                            "car_photo1": null,
                            "car_photo2": null,
                            "car_photo3": null,
                            "operators1": "郑渊",
                            "license_ship1": null,
                            "operators2": null,
                            "license_ship2": null,
                            "operators3": null,
                            "license_ship3": null,
                            "special_category": {
                                "NORMAL": "普通"
                            },
                            "special_History": null
                        }
                    ],
                    "message": " "
                }
    """
    params = storeinfo_by_personid_schema(request.json or '')
    person_id = params.get('person_id')
    data = db.session.query(PersonInfo).join(Store, Department).filter(Store.person_id == person_id,
                                                                       Store.is_delete == 0).with_entities(
        Store.store_name,
        Store.id,
        Store.department_id,
        Department.depart_name,
        Store.person_id,
        PersonInfo.name,
        Store.picture,
        Store.business_number,
        Store.is_bigillegal,
        Store.business_start,
        Store.business_termi,
        Store.longitude,
        Store.latitude,
        Store.address,
        Store.state,
        Store.store_category,
        Store.is_chain,
        Store.is_suspension,
        Store.business_format,
        Store.administrative,
        Store.market_type,
        Store.phone,
        Store.settlement_account,
        Store.circle,
        Store.is_downgrade,
        Store.car_1,
        Store.car_2,
        Store.car_3,
        Store.car_photo1,
        Store.car_photo2,
        Store.car_photo3,
        Store.operators1,
        Store.license_ship1,
        Store.operators2,
        Store.license_ship2,
        Store.operators3,
        Store.license_ship3,
        Store.special_category,
        Store.special_History
    ).order_by(Store.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 稽查所所长查询本所下所有零售户/队长查询本局下所有零售户
@blue_print.route('/getAllStoreInfodepartbossid', methods=['POST'])
def get_all_storeinfo_by_departbossid():
    """
            @api {POST} api/store/getAllStoreInfodepartbossid 稽查所所长查询本所下所有零售户
            @apiVersion 0.0.1
            @apiName getAllStoreInfodepartbossid
            @apiGroup store
            @apiDescription 稽查所所长查询本所下所有零售户,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParam {int}  station_id     (可选)    专卖局id
             @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                { role_id 为3 时，是所长，station_id不需要,返回本所下所有零售商户
                    "department_id":1,
                    "role_id":3,
                    "page":2,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
            @apiParamExample {json} Request-Example:
               { role_id 为5 时，是队长，队长查询范围是整个专卖局，station_id为1，是金华市总局,不为1时，是分局，可以查到整个金华市，不需要department_id
                    "station_id":1,
                    "role_id":5,
                    "page":2,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
            @apiParamExample {json} Request-Example:
                { role_id 为5 时，是队长，队长查询范围是整个专卖局，station_id为4，是分局局，不需要department_id
                    "station_id":4,
                    "role_id":5,
                    "page":2,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
    """
    params = storeinfo_by_departboss_id_schema(request.json or '')
    department_id = params.get('department_id')
    station_id = params.get('station_id')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    if role_id == 3:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(Store.department_id == department_id,
                                                                                 Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 5:
        if station_id == 1:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(Department.station_id == station_id,Store.department_id == Department.id,
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    return common_response(SysStatus.FAIL, None, '您无权查询')


# 通过零售户名或者法人名称查询零售户-模糊查询
@blue_print.route('/getAllStoreInfoByStorenameAndPersonname', methods=['POST'])
def get_all_storeinfo_by_storenameandpersonname():
    """
                @api {POST} api/store/getAllStoreInfoByStorenameAndPersonname 通过零售户名或者法人名称查询零售户-模糊查询
                @apiVersion 0.0.1
                @apiName getAllStoreInfoByStorenameAndPersonname
                @apiGroup store
                @apiDescription 通过零售户名或者法人名称查询零售户
                @apiParam {string}  name     (必须)    零售户名称或者法人名称
                @apiParam {int}  role_id     (必须)    角色id
                @apiParam {int}  station_id     (可选)    专卖局id
                @apiParam {int}  department_id     (可选)    稽查所id
                @apiParamExample {json} Request-Example:
                    { role_id为1，系统管理员，可以查询所有数据
                        "name":"文丽烟店",
                        "role_id":1
                    }
                @apiSuccessExample {json} Success-Response:
                   {
                        "sys_status": "SUCCESS",
                        "data": [
                            {
                                "store_name": "金华市婺城区文丽烟店",
                                "id": 924,
                                "department_id": 1,
                                "depart_name": "专卖城区二所",
                                "person_id": 924,
                                "name": "高文丽",
                                "picture": null,
                                "business_number": "330701203202",
                                "is_bigillegal": false,
                                "business_start": "2016-09-12",
                                "business_termi": "2021-09-01",
                                "longitude": "119.657161000000",
                                "latitude": "29.084430000000",
                                "address": "金华市婺城区宾虹路439弄2幢",
                                "state": {
                                    "NARMAL": "正常经营"
                                },
                                "store_category": "D4",
                                "is_chain": false,
                                "is_suspension": false,
                                "business_format": {
                                    "YANJIU": "烟酒商店"
                                },
                                "administrative": {
                                    "BENJI": "市辖区"
                                },
                                "market_type": {
                                    "URBAN": "市区"
                                },
                                "phone": "15355894148",
                                "settlement_account": " ",
                                "circle": {
                                    "ZHENGWU": "政务（商务）区"
                                },
                                "is_downgrade": null,
                                "car_1": null,
                                "car_2": null,
                                "car_3": null,
                                "car_photo1": null,
                                "car_photo2": null,
                                "car_photo3": null,
                                "operators1": "高文丽",
                                "license_ship1": null,
                                "operators2": null,
                                "license_ship2": null,
                                "operators3": null,
                                "license_ship3": null,
                                "special_category": {
                                    "NORMAL": "普通"
                                },
                                "special_History": null
                            }
                        ],
                        "message": " "
                    }
            @apiParamExample {json} Request-Example:
                    { role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
                        "name":"沈美香",
                        "role_id":5,
                        "station_id":1
                    }
            @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": [
                    {
                        "store_name": "金华市婺城区沈美香副食店",
                        "id": 926,
                        "department_id": 1,
                        "depart_name": "专卖城区二所",
                        "person_id": 926,
                        "name": "沈美香",
                        "picture": null,
                        "business_number": "330701103983",
                        "is_bigillegal": false,
                        "business_start": "2016-08-31",
                        "business_termi": "2021-08-15",
                        "longitude": "119.659419000000",
                        "latitude": "29.087638000000",
                        "address": "金华市婺城区中村社区中南巷10幢3单元102室",
                        "state": {
                            "NARMAL": "正常经营"
                        },
                        "store_category": "D7",
                        "is_chain": false,
                        "is_suspension": false,
                        "business_format": {
                            "SHIZA": "食杂店"
                        },
                        "administrative": {
                            "BENJI": "市辖区"
                        },
                        "market_type": {
                            "URBAN": "市区"
                        },
                        "phone": "15325891963",
                        "settlement_account": " ",
                        "circle": {
                            "ZHENGWU": "政务（商务）区"
                        },
                        "is_downgrade": null,
                        "car_1": null,
                        "car_2": null,
                        "car_3": null,
                        "car_photo1": null,
                        "car_photo2": null,
                        "car_photo3": null,
                        "operators1": "沈美香",
                        "license_ship1": null,
                        "operators2": null,
                        "license_ship2": null,
                        "operators3": null,
                        "license_ship3": null,
                        "special_category": {
                            "NORMAL": "普通"
                        },
                        "special_History": null
                    }
                ],
                "message": " "
            }
            @apiParamExample {json} Request-Example:
                    { role_id为3或者4时，是所长或者稽查人员，查询范围是整个稽查所
                        "name":"沈美香",
                        "role_id":3,
                        "department_id":1
                    }
            @apiSuccessExample {json} Success-Response:
            {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "store_name": "金华市婺城区沈美香副食店",
                            "id": 926,
                            "department_id": 1,
                            "depart_name": "专卖城区二所",
                            "person_id": 926,
                            "name": "沈美香",
                            "picture": null,
                            "business_number": "330701103983",
                            "is_bigillegal": false,
                            "business_start": "2016-08-31",
                            "business_termi": "2021-08-15",
                            "longitude": "119.659419000000",
                            "latitude": "29.087638000000",
                            "address": "金华市婺城区中村社区中南巷10幢3单元102室",
                            "state": {
                                "NARMAL": "正常经营"
                            },
                            "store_category": "D7",
                            "is_chain": false,
                            "is_suspension": false,
                            "business_format": {
                                "SHIZA": "食杂店"
                            },
                            "administrative": {
                                "BENJI": "市辖区"
                            },
                            "market_type": {
                                "URBAN": "市区"
                            },
                            "phone": "15325891963",
                            "settlement_account": " ",
                            "circle": {
                                "ZHENGWU": "政务（商务）区"
                            },
                            "is_downgrade": null,
                            "car_1": null,
                            "car_2": null,
                            "car_3": null,
                            "car_photo1": null,
                            "car_photo2": null,
                            "car_photo3": null,
                            "operators1": "沈美香",
                            "license_ship1": null,
                            "operators2": null,
                            "license_ship2": null,
                            "operators3": null,
                            "license_ship3": null,
                            "special_category": {
                                "NORMAL": "普通"
                            },
                            "special_History": null
                        }
                    ],
                    "message": " "
                }
    """
    params = storeinfo_by_store_nameandpersonname_schema(request.json or '')
    name = params.get('name')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    if role_id == 1:
        data = db.session.query(PersonInfo).join(Store, Department).filter(
            or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                PersonInfo.name.like("%" + name + "%") if name is not None else ""),
            Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).all()
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 5:
        if station_id == 1:
            data = db.session.query(PersonInfo).join(Store, Department).filter(
                or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                    PersonInfo.name.like("%" + name + "%") if name is not None else ""),
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).all()
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            data = db.session.query(PersonInfo).join(Store, Department).filter(Department.station_id == station_id,
                                                                               Store.department_id == Department.id).filter(
                or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                    PersonInfo.name.like("%" + name + "%") if name is not None else ""),
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).all()
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id == 4:
        data = db.session.query(PersonInfo).join(Store, Department).filter(Store.department_id == department_id).filter(
            or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                PersonInfo.name.like("%" + name + "%") if name is not None else ""),
            Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).all()
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过角色id查询零售户
@blue_print.route('/getAllStoreInfodepartroleid', methods=['POST'])
def get_all_storeinfo_by_role_id():
    """
            @api {POST} api/store/getAllStoreInfodepartroleid 通过角色id查询零售户
            @apiVersion 0.0.1
            @apiName getAllStoreInfodepartroleid
            @apiGroup store
            @apiDescription 通过角色id查询零售户,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  department_id     (可选)    稽查所id
             @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParamExample {json} Request-Example:
                {role_id为1，系统管理员，可以查询所有数据
                    "role_id":1,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
            @apiParamExample {json} Request-Example:
                {role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
                    "role_id":2,
                    "page":1,
                    "per_page":8,
                    "station_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
            @apiParamExample {json} Request-Example:
                {role_id为3或者4时，是所长或者稽查人员，查询范围是整个稽查所
                    "department_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
    """
    params = storeinfo_by_role_id_schema(request.json or '')
    department_id = params.get('department_id')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    if role_id == 1:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 5:
        if station_id == 1:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                Department.station_id == station_id).filter(Store.department_id == Department.id,
                                                            Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id == 4:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(Store.department_id == department_id,
                                                                                 Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    return common_response(SysStatus.FAIL, None, '您无权查询')


# 综合查询零售户-模糊查询
@blue_print.route('/getAllStoreInfoBymultiplequery', methods=['POST'])
def get_all_storeinfo_by_multiple_query():
    """
                @api {POST} api/store/getAllStoreInfoBymultiplequery 综合查询零售户-模糊查询
                @apiVersion 0.0.1
                @apiName getAllStoreInfoBymultiplequery
                @apiGroup store
                @apiDescription 综合查询零售户,店铺名--法人名--电话号码--车牌号
                @apiParam {string}  name     (必须)    零售户名称或者法人名称
                @apiParam {int}  role_id     (必须)    角色id
                @apiParam {int}  station_id     (可选)    专卖局id
                @apiParam {int}  department_id     (可选)    稽查所id
                @apiParam {int}  page     (必须)    页数
                @apiParam {int}  per_page     (必须)    每页的页数
                @apiParamExample {json} Request-Example:
                    { 如何role_id为1时，专卖局id和稽查所id不需要添加,查询范围是所有
                        "name":"文丽烟店",
                        "role_id":1,
                        "page":1,
                        "per_page":8
                    }
                @apiSuccessExample {json} Success-Response:
                    {
                        "sys_status": "SUCCESS",
                        "data": {
                            "data": [
                                {
                                    "store_name": "金华市婺城区文丽烟店",
                                    "id": 924,
                                    "department_id": 1,
                                    "depart_name": "专卖城区二所",
                                    "person_id": 924,
                                    "name": "高文丽",
                                    "picture": null,
                                    "business_number": "330701203202",
                                    "is_bigillegal": false,
                                    "business_start": "2016-09-12",
                                    "business_termi": "2021-09-01",
                                    "longitude": "119.657161000000",
                                    "latitude": "29.084430000000",
                                    "address": "金华市婺城区宾虹路439弄2幢",
                                    "state": {
                                        "NARMAL": "正常经营"
                                    },
                                    "store_category": "D4",
                                    "is_chain": false,
                                    "is_suspension": false,
                                    "business_format": {
                                        "YANJIU": "烟酒商店"
                                    },
                                    "administrative": {
                                        "BENJI": "市辖区"
                                    },
                                    "market_type": {
                                        "URBAN": "市区"
                                    },
                                    "phone": "15355894148",
                                    "settlement_account": " ",
                                    "circle": {
                                        "ZHENGWU": "政务（商务）区"
                                    },
                                    "is_downgrade": null,
                                    "car_1": null,
                                    "car_2": null,
                                    "car_3": null,
                                    "car_photo1": null,
                                    "car_photo2": null,
                                    "car_photo3": null,
                                    "operators1": "高文丽",
                                    "license_ship1": null,
                                    "operators2": null,
                                    "license_ship2": null,
                                    "operators3": null,
                                    "license_ship3": null,
                                    "special_category": {
                                        "NORMAL": "普通"
                                    },
                                    "special_History": null
                                }
                            ],
                            "count": 1
                        },
                        "message": " "
                    }
            @apiParamExample {json} Request-Example:
                    {添加role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
                        "name":"沈美香",
                        "role_id":2,
                        "station_id":1,
                        "page":1,
                        "per_page":8
                    }
            @apiSuccessExample {json} Success-Response:
           {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "store_name": "金华市婺城区沈美香副食店",
                            "id": 926,
                            "department_id": 1,
                            "depart_name": "专卖城区二所",
                            "person_id": 926,
                            "name": "沈美香",
                            "picture": null,
                            "business_number": "330701103983",
                            "is_bigillegal": false,
                            "business_start": "2016-08-31",
                            "business_termi": "2021-08-15",
                            "longitude": "119.659419000000",
                            "latitude": "29.087638000000",
                            "address": "金华市婺城区中村社区中南巷10幢3单元102室",
                            "state": {
                                "NARMAL": "正常经营"
                            },
                            "store_category": "D7",
                            "is_chain": false,
                            "is_suspension": false,
                            "business_format": {
                                "SHIZA": "食杂店"
                            },
                            "administrative": {
                                "BENJI": "市辖区"
                            },
                            "market_type": {
                                "URBAN": "市区"
                            },
                            "phone": "15325891963",
                            "settlement_account": " ",
                            "circle": {
                                "ZHENGWU": "政务（商务）区"
                            },
                            "is_downgrade": null,
                            "car_1": null,
                            "car_2": null,
                            "car_3": null,
                            "car_photo1": null,
                            "car_photo2": null,
                            "car_photo3": null,
                            "operators1": "沈美香",
                            "license_ship1": null,
                            "operators2": null,
                            "license_ship2": null,
                            "operators3": null,
                            "license_ship3": null,
                            "special_category": {
                                "NORMAL": "普通"
                            },
                            "special_History": null
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
            @apiParamExample {json} Request-Example:
                    {role_id为3或者4时，专卖局id不需要添加,查询范围是本稽查所内
                        "name":"沈美香",
                        "role_id":3,
                        "department_id":1,
                        "page":1,
                        "per_page":8
                    }
            @apiSuccessExample {json} Success-Response:
           {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "store_name": "金华市婺城区沈美香副食店",
                            "id": 926,
                            "department_id": 1,
                            "depart_name": "专卖城区二所",
                            "person_id": 926,
                            "name": "沈美香",
                            "picture": null,
                            "business_number": "330701103983",
                            "is_bigillegal": false,
                            "business_start": "2016-08-31",
                            "business_termi": "2021-08-15",
                            "longitude": "119.659419000000",
                            "latitude": "29.087638000000",
                            "address": "金华市婺城区中村社区中南巷10幢3单元102室",
                            "state": {
                                "NARMAL": "正常经营"
                            },
                            "store_category": "D7",
                            "is_chain": false,
                            "is_suspension": false,
                            "business_format": {
                                "SHIZA": "食杂店"
                            },
                            "administrative": {
                                "BENJI": "市辖区"
                            },
                            "market_type": {
                                "URBAN": "市区"
                            },
                            "phone": "15325891963",
                            "settlement_account": " ",
                            "circle": {
                                "ZHENGWU": "政务（商务）区"
                            },
                            "is_downgrade": null,
                            "car_1": null,
                            "car_2": null,
                            "car_3": null,
                            "car_photo1": null,
                            "car_photo2": null,
                            "car_photo3": null,
                            "operators1": "沈美香",
                            "license_ship1": null,
                            "operators2": null,
                            "license_ship2": null,
                            "operators3": null,
                            "license_ship3": null,
                            "special_category": {
                                "NORMAL": "普通"
                            },
                            "special_History": null
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }

    """
    params = storeinfo_by_store_multiplequery_schema(request.json or '')
    name = params.get('name')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    page = params.get('page')
    per_page = params.get('per_page')
    if role_id == 1:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(
            or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                PersonInfo.name.like("%" + name + "%") if name is not None else "",
                Store.phone.like("%" + name + "%") if name is not None else "",
                Store.car_1.like("%" + name + "%") if name is not None else "",
                Store.car_2.like("%" + name + "%") if name is not None else "",
                Store.car_3.like("%" + name + "%") if name is not None else "",
                PersonInfo.phone.like("%" + name + "%") if name is not None else ""),
            Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 5:
        if station_id == 1:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(
                or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                    PersonInfo.name.like("%" + name + "%") if name is not None else "",
                    Store.phone.like("%" + name + "%") if name is not None else "",
                    Store.car_1.like("%" + name + "%") if name is not None else "",
                    Store.car_2.like("%" + name + "%") if name is not None else "",
                    Store.car_3.like("%" + name + "%") if name is not None else "",
                    PersonInfo.phone.like("%" + name + "%") if name is not None else ""),
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(PersonInfo).join(Store, Department).filter(Department.station_id == station_id,
                                                                                     Store.department_id == Department.id).filter(
                or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                    PersonInfo.name.like("%" + name + "%") if name is not None else "",
                    Store.phone.like("%" + name + "%") if name is not None else "",
                    Store.car_1.like("%" + name + "%") if name is not None else "",
                    Store.car_2.like("%" + name + "%") if name is not None else "",
                    Store.car_3.like("%" + name + "%") if name is not None else "",
                    PersonInfo.phone.like("%" + name + "%") if name is not None else ""),
                Store.is_delete == 0).with_entities(
                Store.store_name,
                Store.id,
                Store.department_id,
                Department.depart_name,
                Store.person_id,
                PersonInfo.name,
                Store.picture,
                Store.business_number,
                Store.is_bigillegal,
                Store.business_start,
                Store.business_termi,
                Store.longitude,
                Store.latitude,
                Store.address,
                Store.state,
                Store.store_category,
                Store.is_chain,
                Store.is_suspension,
                Store.business_format,
                Store.administrative,
                Store.market_type,
                Store.phone,
                Store.settlement_account,
                Store.circle,
                Store.is_downgrade,
                Store.car_1,
                Store.car_2,
                Store.car_3,
                Store.car_photo1,
                Store.car_photo2,
                Store.car_photo3,
                Store.operators1,
                Store.license_ship1,
                Store.operators2,
                Store.license_ship2,
                Store.operators3,
                Store.license_ship3,
                Store.special_category,
                Store.special_History
            ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
            storedata = pagination.items
            count = pagination.total
            data = {
                'data': storedata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id == 4:
        pagination = db.session.query(PersonInfo).join(Store, Department).filter(
            Store.department_id == department_id).filter(
            or_(Store.store_name.like("%" + name + "%") if name is not None else "",
                PersonInfo.name.like("%" + name + "%") if name is not None else "",
                Store.phone.like("%" + name + "%") if name is not None else "",
                Store.car_1.like("%" + name + "%") if name is not None else "",
                Store.car_2.like("%" + name + "%") if name is not None else "",
                Store.car_3.like("%" + name + "%") if name is not None else "",
                PersonInfo.phone.like("%" + name + "%") if name is not None else ""),
            Store.is_delete == 0).with_entities(
            Store.store_name,
            Store.id,
            Store.department_id,
            Department.depart_name,
            Store.person_id,
            PersonInfo.name,
            Store.picture,
            Store.business_number,
            Store.is_bigillegal,
            Store.business_start,
            Store.business_termi,
            Store.longitude,
            Store.latitude,
            Store.address,
            Store.state,
            Store.store_category,
            Store.is_chain,
            Store.is_suspension,
            Store.business_format,
            Store.administrative,
            Store.market_type,
            Store.phone,
            Store.settlement_account,
            Store.circle,
            Store.is_downgrade,
            Store.car_1,
            Store.car_2,
            Store.car_3,
            Store.car_photo1,
            Store.car_photo2,
            Store.car_photo3,
            Store.operators1,
            Store.license_ship1,
            Store.operators2,
            Store.license_ship2,
            Store.operators3,
            Store.license_ship3,
            Store.special_category,
            Store.special_History
        ).order_by(Store.id).paginate(page, per_page=per_page, error_out=False)
        storedata = pagination.items
        count = pagination.total
        data = {
            'data': storedata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
