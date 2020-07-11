#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint, request, flash, session
from sqlalchemy import desc

from api.extensions import db
from api.models.user import Station, Department, User
from api.schemas.station import add_station_schema, add_department_schema, del_station_schema, del_department_schema, \
    station_info_schema, department_info_schema,get_AllUser_byStationid_schema, get_AllInfo_byRole_schema,\
    get_AllDepart_byStation_schema,departname_info_by_departid_schema,station_info_by_station_name_schema
from api.views.base import common_response, SysStatus

blue_print = Blueprint('station', __name__, url_prefix='/api/station')


# 添加专卖局
@blue_print.route('/addStation', methods=['POST'])
def add_station():
    """
        @api {POST} api/station/addStation  添加专卖局
        @apiVersion 0.0.1
        @apiName add_station
        @apiGroup station
        @apiDescription 添加专卖局
        @apiParam {String}  station_name      (必须)    专卖局名称
        @apiParamExample {json} Request-Example:
            {
                 "station_name":"打鸡血专卖局"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "专卖局添加成功"
            }
    """
    params = add_station_schema(request.json or '')
    station_name = params.get('station_name')
    station = Station.query.filter(Station.station_name == station_name,Station.is_delete == 0).first()
    if station:
        return common_response(SysStatus.FAIL, station.station_name, '该专卖局已被添加')
    else:
        station = Station.query.filter(Station.station_name == station_name, Station.is_delete == 1).first()
        if station:
            station.is_delete = 0
            station.update(params)
            db.session.commit()
            return common_response(SysStatus.SUCCESS, None, '专卖局添加成功')
        else:
            station = Station(station_name=station_name)
            db.session.add(station)
            db.session.commit()
            return common_response(SysStatus.SUCCESS, None, '专卖局添加成功')


# 修改专卖局
@blue_print.route('/modifyStationInfo', methods=['POST'])
def station_modify():
    """
        @api {post} api/station/modifyStationInfo  修改专卖局
        @apiVersion 0.0.1
        @apiName station_modify
        @apiGroup station
        @apiDescription 修改专卖局
        @apiParam {int}  station_id     (必须)    专卖局id
        @apiParam {String}  station_name      (可选)    专卖局名称
        @apiParamExample {json} Request-Example:
            {
                "station_id":9,
                "station_name":"打哈欠专卖局"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "专卖局信息修改成功"
            }
    """
    params = station_info_schema(request.json or '')
    print(params)
    station_id = params.get('station_id')
    station = Station.query.filter(Station.id == station_id,Station.is_delete == 0)
    params.pop('station_id')
    station.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '专卖局信息修改成功')


# 删除专卖局
@blue_print.route('/delStation', methods=['POST'])
def delete_station():
    """
        @api {POST} api/station/delStation  删除专卖局
        @apiVersion 0.0.1
        @apiName delete_station
        @apiGroup station
        @apiDescription 删除专卖局
        @apiParam {String}  station_name      (必须)    专卖局名称
        @apiParam {int}  station_id     (必须)    专卖局id
        @apiParamExample {json} Request-Example:
            {
                "station_name":"打哈欠专卖局",
                "station_id":9
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "专卖局删除成功"
            }
    """
    params = del_station_schema(request.json or '')
    station_name = params.get('station_name')
    station_id = params.get('station_id')
    is_delete = 1
    station = Station.query.filter(Station.id == station_id, Station.station_name == station_name,Station.is_delete == 0).first()
    station.is_delete = is_delete
    station.save()
    return common_response(SysStatus.SUCCESS, station.is_delete, '专卖局删除成功')


# 根据局id获取所辖稽查所 ,暂时未想好此接口向那些人开放，写成开放接口
@blue_print.route('/getAllDepartByStation', methods=['POST'])
def get_AllDepart_byStation():
    """
        @api {GET} api/station/getAllDepartByStation  根据局获取所辖稽查所/队
        @apiVersion 0.0.1
        @apiName get_AllDepart_byStation
        @apiGroup station
        @apiDescription 根据局id获取所辖稽查所/队,此接口使用了分页功能，page参数通过表单提交
        @apiParam {int}  station_id     (必须)    专卖局id
        @apiParam {int}  page     (必须)    页数
        @apiParam {int}  per_page     (必须)    每页的页数
        @apiParamExample {json} Request-Example:
            {
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
                            "id": 1,
                            "depart_name": "专卖城区二所",
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 2,
                            "depart_name": "专卖金西所",
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 3,
                            "depart_name": "金华市烟草专卖局（公司）",
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 4,
                            "depart_name": "专卖城区一所",
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 5,
                            "depart_name": "专卖金东所",
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 32,
                            "depart_name": "金华市烟草专卖局一大队",
                            "station_name": "金华市烟草专卖局（公司）"
                        }
                    ],
                    "count": 6
                },
                "message": " "
            }
        @apiErrorExample {json} Error-Response:
            {
                "sys_status": "FAIL",
                "data": null,
                "message": "无查询结果"
            }
    """
    params = get_AllDepart_byStation_schema(request.json or '')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    pagination = db.session.query(Station).join(Department).filter(Department.station_id == station_id,Department.is_delete == 0).with_entities(
        Department.id,
        Department.depart_name,
        Station.station_name
    ).order_by(Department.id).paginate(page,per_page=per_page,error_out=False)
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



#根据角色id和局id或者稽查所id获取所辖稽查所和稽查人员
@blue_print.route('/getAllByRole', methods =['POST'])
def get_AllInfo_byAdminid():
    """
            @api {POST} api/station/getAllByRole  根据角色id和和局id或者稽查所id获取所辖稽查所和稽查人员
            @apiVersion 0.0.1
            @apiName get_AllInfo_byAdminid
            @apiGroup station
            @apiDescription 这个接口是提供给系统管理员，局长，队长和稽查所所长使用,提供角色id和响应的局id或者所id，可以获取辖区的稽查所和稽查人员,此接口使用了分页功能，page参数通过表单提交
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {如果role_id为1，是系统管理员，可以获得所有的稽查所id和名字
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
                                "depart_name": "专卖城区二所"
                            },
                            {
                                "id": 2,
                                "depart_name": "专卖金西所"
                            },
                            {
                                "id": 3,
                                "depart_name": "金华市烟草专卖局（公司）"
                            },
                            {
                                "id": 4,
                                "depart_name": "专卖城区一所"
                            },
                            {
                                "id": 5,
                                "depart_name": "专卖金东所"
                            },
                            {
                                "id": 6,
                                "depart_name": "城区专卖管理所"
                            },
                            {
                                "id": 7,
                                "depart_name": "诸葛专卖管理所"
                            },
                            {
                                "id": 8,
                                "depart_name": "马涧专卖管理所"
                            }
                        ],
                        "count": 31
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {如何role_id 为2或者5，是局长或者队长，可以获取局下所有稽查所id和名称
                    "station_id":1,
                    "role_id":2,
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
                                "depart_name": "专卖城区二所"
                            },
                            {
                                "id": 2,
                                "depart_name": "专卖金西所"
                            },
                            {
                                "id": 3,
                                "depart_name": "金华市烟草专卖局（公司）"
                            },
                            {
                                "id": 4,
                                "depart_name": "专卖城区一所"
                            },
                            {
                                "id": 5,
                                "depart_name": "专卖金东所"
                            }
                        ],
                        "count": 5
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                { role_id为3，是稽查所所长，可以获取所辖稽查人员
                    "department_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 3,
                                "account": "10010011000",
                                "role_id": 3,
                                "department_id": 1,
                                "station_id": 1,
                                "user_name": "专卖城区二所所长"
                            },
                            {
                                "id": 4,
                                "account": "10010011001",
                                "role_id": 4,
                                "department_id": 1,
                                "station_id": 1,
                                "user_name": "专卖城区二所稽查员张飞"
                            }
                        ],
                        "count": 2
                    },
                    "message": " "
                }
            @apiErrorExample {json} Error-Response:
                {
                    "sys_status": "FAIL",
                    "data": null,
                    "message": "无查询结果"
                }
    """
    params = get_AllInfo_byRole_schema(request.json or '')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    page = params.get('page')
    per_page = params.get('per_page')
    if role_id == 1:
        pagination = Department.query.filter(Department.is_delete == 0).with_entities(
            Department.id,
            Department.depart_name
        ).order_by(Department.id).paginate(page, per_page=per_page, error_out=False)
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
        pagination = Department.query.filter(Department.station_id == station_id,Department.is_delete == 0).with_entities(
            Department.id,
            Department.depart_name
        ).order_by(Department.id).paginate(page,per_page=per_page,error_out=False)
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
    elif role_id == 3:
        pagination = User.query.filter(User.department_id == department_id,User.is_delete == 0).with_entities(
            User.id,
            User.account,
            User.role_id,
            User.department_id,
            User.station_id,
            User.user_name
        ).order_by(User.id).paginate(page,per_page=per_page,error_out=False)
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
        return common_response(SysStatus.FAIL, None, '无查询结果')





# 添加稽查所/队
@blue_print.route('/addDepartment', methods=['POST'])
def add_depart():
    """
        @api {POST} api/station/addDepartment  添加稽查所
        @apiVersion 0.0.1
        @apiName add_depart
        @apiGroup station
        @apiDescription 添加稽查所
        @apiParam {String}  depart_name      (必须)    稽查所名称
        @apiParam {int}  station_id     (必须)    专卖局id
        @apiParamExample {json} Request-Example:
            {
                "depart_name":"金华市专卖局第二大队",
                "station_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "稽查所/稽查队添加成功"
            }

        @apiErrorExample {json} Error-Response:
           {
                "sys_status": "FAIL",
                "data": "金华市专卖局第二大队",
                "message": "该稽查所/队已被添加"
            }
    """
    params = add_department_schema(request.json or '')
    depart_name = params.get('depart_name')
    station_id = params.get('station_id')
    # is_captain = params.get('is_captain')
    depart = Department.query.filter(Department.depart_name == depart_name,Department.station_id == station_id,Department.is_delete == 0).first()
    if depart:
        return common_response(SysStatus.FAIL, depart.depart_name, '该稽查所/队已被添加')
    else:
        depart = Department.query.filter(Department.depart_name == depart_name,Department.station_id == station_id, Department.is_delete == 1).first()
        if depart:
            depart.is_delete = 0
            depart.update(params)
            db.session.commit()
            return common_response(SysStatus.SUCCESS, None, '稽查所/稽查队添加成功')
        else:
            depart = Department(depart_name=depart_name, station_id=station_id)
            db.session.add(depart)
            db.session.commit()
            return common_response(SysStatus.SUCCESS, None, '稽查所/稽查队添加成功')


# 修改稽查所/队
@blue_print.route('/modifyDepartInfo', methods=['POST'])
def depart_modify():
    """
        @api {post} api/station/modifyDepartInfo  修改稽查所
        @apiVersion 0.0.1
        @apiName depart_modify
        @apiGroup station
        @apiDescription 修改稽查所
        @apiParam {int}  department_id     (必须)    稽查所id
        @apiParam {String}  depart_name      (可选)    稽查所名称
        @apiParam {int}  station_id      (可选)    专卖局id
        @apiParamExample {json} Request-Example:
            {
                "department_id":33,
                "depart_name":"金华市专卖局清风港稽查所",
                "station_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "稽查所信息修改成功"
            }
    """
    params = department_info_schema(request.json or '')
    department_id = params.get('department_id')
    depart = Department.query.filter(Department.id == department_id, Department.is_delete == 0)
    params.pop('department_id')
    depart.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '稽查所/队信息修改成功')

# 通过稽查所id获取稽查所名字
@blue_print.route('/getDepartnameBydepartid', methods=['POST'])
def get_departname_by_departid():
    """
        @api {post} api/station/getDepartnameBydepartid  通过稽查所id获取稽查所名字
        @apiVersion 0.0.1
        @apiName getDepartnameBydepartid
        @apiGroup station
        @apiDescription 通过稽查所id获取稽查所名字
        @apiParam {int}  department_id     (必须)    稽查所id
        @apiParamExample {json} Request-Example:
            {
                "department_id":1
            }
        @apiSuccessExample {json} Success-Response:
           {
                "sys_status": "SUCCESS",
                "data": [
                    {
                        "depart_name": "专卖城区二所",
                        "station_id": 1,
                        "station_name": "金华市烟草专卖局（公司）"
                    }
                ],
                "message": "成功"
            }
    """
    params = departname_info_by_departid_schema(request.json or '')
    department_id = params.get('department_id')
    data = db.session.query(Station).join(Department).filter(Department.id == department_id,Department.is_delete == 0).with_entities(
        Department.depart_name,
        Department.station_id,
        Station.station_name
    ).all()
    if data:
        return common_response(SysStatus.SUCCESS,data,'')
    else:
        return common_response(SysStatus.FAIL,None,'无查询结果')



# 删除稽查所
@blue_print.route('/delDepartment', methods=['POST'])
def del_depart():
    """
        @api {POST} api/station/delDepartment  删除稽查所
        @apiVersion 0.0.1
        @apiName del_depart
        @apiGroup station
        @apiDescription 删除稽查所
        @apiParam {String}  depart_name      (必须)    稽查所名称
        @apiParam {int}  department_id     (必须)    稽查所id
        @apiParamExample {json} Request-Example:
            {
                "depart_name":"金华市专卖局清风港稽查所",
                "department_id":33
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "稽查所删除成功"
            }
    """
    params = del_department_schema(request.json or '')
    depart_name = params.get('depart_name')
    department_id = params.get('department_id')
    is_delete = 1
    depart = Department.query.filter(Department.id == department_id, Department.depart_name == depart_name, Department.is_delete == 0).first()
    depart.is_delete = is_delete
    depart.save()
    return common_response(SysStatus.SUCCESS, depart.is_delete, '稽查所删除成功')

#直接使用get方法获取所有专卖局
@blue_print.route('/getAllStation', methods =['GET'])
def get_All_Station():
    """
        @api {GET} api/station/getAllStation 直接获取所有专卖局
        @apiVersion 0.0.1
        @apiName get_All_Station
        @apiGroup station
        @apiDescription 直接获取所有专卖局,此处使用了分页功能，因为是get方法，所以page参数指定访问第几页，per_page参数指定一页多少条
        @apiParamExample {json} Request-Example:
            {
            示例:http://39.96.52.170:5000/api/station/getAllStation?page=1&per_page=8
                }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 1,
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 2,
                            "station_name": "兰溪市烟草专卖局（分公司）"
                        },
                        {
                            "id": 3,
                            "station_name": "东阳市烟草专卖局（分公司）"
                        },
                        {
                            "id": 4,
                            "station_name": "义乌市烟草专卖局（分公司）"
                        },
                        {
                            "id": 5,
                            "station_name": "永康市烟草专卖局（分公司）"
                        },
                        {
                            "id": 6,
                            "station_name": "浦江县烟草专卖局（分公司）"
                        },
                        {
                            "id": 7,
                            "station_name": "武义县烟草专卖局（分公司）"
                        },
                        {
                            "id": 8,
                            "station_name": "磐安县烟草专卖局（分公司）"
                        }
                    ],
                    "count": 8
                },
                "message": " "
            }
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = Station.query.filter(Station.is_delete == 0).with_entities(
        Station.id,
        Station.station_name
    ).order_by(Station.id).paginate(page,per_page=per_page,error_out=False)
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

#直接使用get方法获取所有的稽查所
@blue_print.route('/getAllDepart', methods =['GET'])
def get_All_Depart():
    """
         @api {GET} api/station/getAllDepart 直接获取所有稽查所
         @apiVersion 0.0.1
         @apiName get_All_Depart
         @apiGroup station
         @apiDescription 直接获取所有稽查所，此处使用了分页功能，因为是get方法，所以page参数指定访问第几页，per_page参数指定一页多少条
         @apiParamExample {json} Request-Example:
            {
            示例:http://39.96.52.170:5000/api/station/getAllDepart?page=1&per_page=8
                }
         @apiSuccessExample {json} Success-Response:
             {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 1,
                            "depart_name": "专卖城区二所",
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 2,
                            "depart_name": "专卖金西所",
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 3,
                            "depart_name": "金华市烟草专卖局（公司）",
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 4,
                            "depart_name": "专卖城区一所",
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 5,
                            "depart_name": "专卖金东所",
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）"
                        },
                        {
                            "id": 6,
                            "depart_name": "城区专卖管理所",
                            "station_id": 2,
                            "station_name": "兰溪市烟草专卖局（分公司）"
                        },
                        {
                            "id": 7,
                            "depart_name": "诸葛专卖管理所",
                            "station_id": 2,
                            "station_name": "兰溪市烟草专卖局（分公司）"
                        },
                        {
                            "id": 8,
                            "depart_name": "马涧专卖管理所",
                            "station_id": 2,
                            "station_name": "兰溪市烟草专卖局（分公司）"
                        }
                    ],
                    "count": 33
                },
                "message": " "
            }
     """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = db.session.query(Station).join(Department).filter(Department.is_delete == 0).with_entities(
        Department.id,
        Department.depart_name,
        Department.station_id,
        Station.station_name
    ).order_by(Department.id).paginate(page,per_page=per_page,error_out=False)
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

#直接使用get方法获取所有的稽查人员
@blue_print.route('/getAllUser', methods =['GET'])
def get_All_User():
    """
            @api {GET} api/station/getAllUser 直接获取所有稽查人员
            @apiVersion 0.0.1
            @apiName get_All_User
            @apiGroup station
            @apiDescription 直接获取所有稽查人员，此处使用了分页功能，因为是get方法，所以page参数指定访问第几页，per_page参数指定一页多少条
            @apiParamExample {json} Request-Example:
            {
            示例:http://39.96.52.170:5000/api/station/getAllUser?page=1&per_page=8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 1,
                                "user_name": "系统管理员",
                                "department_id": null,
                                "station_id": 1,
                                "role_id": 1,
                                "account": "12311110000"
                            },
                            {
                                "id": 2,
                                "user_name": "专卖城区二所所长",
                                "department_id": null,
                                "station_id": 1,
                                "role_id": 2,
                                "account": "10010001000"
                            },
                            {
                                "id": 3,
                                "user_name": "专卖城区二所所长",
                                "department_id": 1,
                                "station_id": 1,
                                "role_id": 3,
                                "account": "10010011000"
                            },
                            {
                                "id": 4,
                                "user_name": "专卖城区二所稽查员张飞",
                                "department_id": 1,
                                "station_id": 1,
                                "role_id": 4,
                                "account": "10010011001"
                            },
                            {
                                "id": 5,
                                "user_name": "金华市烟草专卖局一队队长",
                                "department_id": 32,
                                "station_id": 1,
                                "role_id": 5,
                                "account": "10010021001"
                            }
                        ],
                        "count": 5
                    },
                    "message": " "
                }
    """
    page = request.args.get('page',1,type=int)
    per_page = request.args.get('per_page',1,type=int)
    pagination = User.query.filter(User.is_delete == 0).with_entities(
        User.id,
        User.user_name,
        User.department_id,
        User.station_id,
        User.role_id,
        User.account
    ).order_by(User.id).paginate(page,per_page=per_page,error_out=False)
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

# 根据局id和局长角色id获取所辖稽查人员
@blue_print.route('/getAllUserByStationid', methods=['POST'])
def get_AllUser_byStationid():
    """
        @api {POST} api/station/getAllUserByStationid  根据局id获取所辖稽查人员
        @apiVersion 0.0.1
        @apiName getAllUserByStationid
        @apiGroup station
        @apiDescription 根据局id获取所辖稽查人员,此接口使用了分页功能，page参数通过表单提交,per_page参数指定一页有多获取多少数据
        @apiParam {int}  station_id     (必须)    专卖局id
        @apiParam {int}  role_id     (必须)    专卖局id
        @apiParam {int}  page     (必须)    页数
        @apiParam {int}  per_page     (必须)    每页的页数
        @apiParamExample {json} Request-Example:
            {
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
                            "id": 1,
                            "account": "12311110000",
                            "role_id": 1,
                            "department_id": null,
                            "station_id": 1,
                            "user_name": "系统管理员"
                        },
                        {
                            "id": 2,
                            "account": "10010001000",
                            "role_id": 2,
                            "department_id": null,
                            "station_id": 1,
                            "user_name": "专卖城区二所所长"
                        },
                        {
                            "id": 3,
                            "account": "10010011000",
                            "role_id": 3,
                            "department_id": 1,
                            "station_id": 1,
                            "user_name": "专卖城区二所所长"
                        },
                        {
                            "id": 4,
                            "account": "10010011001",
                            "role_id": 4,
                            "department_id": 1,
                            "station_id": 1,
                            "user_name": "专卖城区二所稽查员张飞"
                        },
                        {
                            "id": 5,
                            "account": "10010021001",
                            "role_id": 5,
                            "department_id": 32,
                            "station_id": 1,
                            "user_name": "金华市烟草专卖局一队队长"
                        }
                    ],
                    "count": 5
                },
                "message": " "
            }
        @apiErrorExample {json} Error-Response:
            {
                "sys_status": "FAIL",
                "data": null,
                "message": "无查询结果"
            }
    """
    params = get_AllUser_byStationid_schema(request.json or '')
    page = params.get('page')
    role_id = params.get('role_id')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    if role_id == 2 :
        pagination = User.query.filter(User.station_id == station_id,User.is_delete == 0).with_entities(
            User.id,
            User.account,
            User.role_id,
            User.department_id,
            User.station_id,
            User.user_name
        ).order_by(User.id).paginate(page,per_page=per_page,error_out=False)
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
        return common_response(SysStatus.FAIL, None, '您无权查询')


#通过专卖局名称获取专卖局详细信息--分页—--杨--模糊查询
@blue_print.route('/getStationInfoByStationname',methods = ['POST'])
def get_stationinfo_by_station_name():
    """
            @api {POST} api/station/getStationInfoByStationname 通过专卖局名称获取专卖局详细信息--分页—--杨--模糊查询
            @apiVersion 0.0.1
            @apiName getStationInfoByStationname
            @apiGroup station
            @apiDescription 通过专卖局名称获取专卖局详细信息--分页—--杨
            @apiParam {string}  station_name     (必须)    专卖局名称
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "station_name":"金华市",
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
                                "station_name": "金华市烟草专卖局（公司）"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = station_info_by_station_name_schema(request.json or '')
    station_name = params.get('station_name')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = Station.query.filter(Station.station_name.like("%" + station_name + "%") if station_name is not None else "", Station.is_delete == 0).with_entities(
        Station.id,
        Station.station_name
    ).order_by(Station.id).paginate(page, per_page=per_page, error_out=False)
    stationdata = pagination.items
    count = pagination.total
    data = {
        'data': stationdata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')

