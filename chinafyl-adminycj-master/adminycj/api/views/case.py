#!/usr/bin/env python
# -*- coding:utf-8 -*-
import simplejson
from flask import Blueprint, request, session

from sqlalchemy import desc, and_, or_, not_
import decimal
from api import db
from api.models.case_Info import Case, Purchase, Case_cigar, Brand, ExcelInAndOut
from api.models.user import Station, Department
from api.models.rule import SingleBrand
from api.models.store_Info import Store
from api.serializer.case import purchase_info_ser, casecigar_info_ser, brand_info_ser, excel_inandout_info_ser
from api.schemas.case import add_caseinfo_schema, caseinfo_by_id_schema, case_info_schema, del_case_schema, \
    caseinfo_by_store_id_schema, caseinfo_by_select_schema, caseinfo_by_store_name_schema, \
    caseinfo_by_storenameandselect_schema, \
    purchaseinfo_by_id_schema, purchaseinfo_by_store_id_schema, casecigarinfo_by_id_schema, \
    casecigarinfo_by_case_id_schema, \
    casecigarinfo_by_store_id_schema, brandinfo_by_id_schema, brandinfo_by_purchase_id_schema, \
    brandinfo_by_store_id_schema, \
    excel_inandout_info_by_caseid_schema, scan_code_upload_info_schema, del_inandout_caseid_schema, \
    get_all_singlename_by_caseid_schema, get_uncomplish_singlename_by_caseid_schema, \
    get_complish_singlename_by_caseid_schema, \
    get_all_singlenamecount_by_caseid_schema, get_complish_singlenamecount_by_caseid_schema, \
    get_uncomplish_singlenamecount_by_caseid_schema, excel_inandout_info_by_caseid_page_schema, \
    caseinfo_by_role_id_schema, get_purchaseinfo_by_timeandstore_id_schema,inter_casecigarinfo_schema,\
    inter_casecigarinfo_by_departid_schema,casecigarinfo_by_timeandstore_id_schema

from api.views.base import common_response, SysStatus

blue_print = Blueprint('case', __name__, url_prefix='/api/case')


# 添加违法案件信息
@blue_print.route('/addCase', methods=['POST'])
def add_case():
    """
        @api {post} api/case/addCase  添加违法案件信息
        @apiVersion 0.0.1
        @apiName addCase
        @apiGroup case
        @apiDescription 添加违法案件信息
        @apiParam {String}  caseId    (必须)    案件编号
        @apiParam {int}  store_id    (必须,零售商户表必须有此数据)    零售商户id
        @apiParam {date}  case_date    (可选)    案发时间
        @apiParam {String}  case_value      (可选)    案值
        @apiParam {String}  count    (可选)    卷烟数量（条数）
        @apiParam {string}  case_nature    (可选)    案件性质
        @apiParam {Boolean}  is_criminal     (可选)   有无刑事处罚，True有 False没有
        @apiParam {Boolean}  smoke_property01    (可选)    是否为非流烟，True是 False否
        @apiParam {Boolean}  smoke_property02    (可选)    是否为假冒烟，True是 False否
        @apiParam {Boolean}  smoke_property03    (可选)    是否为走私烟，True是 False否
        @apiParamExample {json} Request-Example:
            {
                "store_id":5,
                "caseId":"541254521",
                "case_date":"2020-04-01",
                "case_value":"4521.12",
                "count":"125.45",
                "case_nature":"未在当地企业进货",
                "is_criminal":"False",
                "smoke_property01":"True",
                "smoke_property02":"False",
                "smoke_property03":"False"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": 1828(违法案件id),
                "message": "违法信息添加成功"
            }

        @apiErrorExample {json} Error-Response:
            {
                 "sys_status": "FAIL",
                 "data": 1,
                 "message": "该违法信息已被添加"
            }

    """
    params = add_caseinfo_schema(request.json or '')
    caseId = params.get('caseId')
    store_id = params.get('store_id')
    case_date = params.get('case_date')
    case_value = decimal.Decimal(params.get('case_value'))
    count = decimal.Decimal(params.get('count'))
    case_nature = params.get('case_nature')
    is_criminal = params.get('is_criminal')
    smoke_property01 = params.get('smoke_property01')
    smoke_property02 = params.get('smoke_property02')
    smoke_property03 = params.get('smoke_property03')
    case = Case.query.filter(Case.caseId == caseId, Case.is_delete == 0).first()
    if case:
        return common_response(SysStatus.FAIL, case.caseId, '该违法信息已被添加')
    else:
        case = Case(caseId=caseId, store_id=store_id, case_date=case_date, case_value=case_value, count=count,
                    case_nature=case_nature, is_criminal=is_criminal, smoke_property01=smoke_property01,
                    smoke_property02=smoke_property02,
                    smoke_property03=smoke_property03)
        db.session.add(case)
        db.session.commit()
        data = case.id
        return common_response(SysStatus.SUCCESS, data, '违法信息添加成功')


# 通过违法信息id获取违法违法信息
@blue_print.route('/getcaseInfoByid', methods=['POST'])
def get_caseinfo_by_id():
    """
            @api {POST} api/case/getcaseInfoByid 通过违法信息id获取违法违法信息
            @apiVersion 0.0.1
            @apiName getcaseInfoByid
            @apiGroup case
            @apiDescription 通过违法信息id获取违法违法信息
            @apiParam {int}  case_id     (必须)    违法信息id
            @apiParamExample {json} Request-Example:
                {
                    "case_id":5
                }
            @apiSuccessExample {json} Success-Response:
              {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 5,
                            "caseId": "3307810201910137",
                            "store_id": 7093,
                            "store_name": "兰溪市辅仁杂货店",
                            "case_date": "2019-10-06 08:35:00",
                            "case_value": "21765.70",
                            "count": "58.20",
                            "case_nature": "未在当地烟草专卖批发企业进货",
                            "is_criminal": false,
                            "smoke_property01": true,
                            "smoke_property02": false,
                            "smoke_property03": false
                        }
                    ],
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {
                    "case_id":1
                }
            @apiSuccessExample {json} Success-Response:
              {
                "sys_status": "SUCCESS",
                "data": [
                    {
                        "id": 1,
                        "caseId": "3307830201910267",
                        "store_id": null,
                        "case_date": "2019-10-21 21:09:00",
                        "case_value": "2300.65",
                        "count": "8.40",
                        "case_nature": "销售非法生产的烟草专卖品、销售无标志的外国卷烟",
                        "is_criminal": true,
                        "smoke_property01": false,
                        "smoke_property02": true,
                        "smoke_property03": true
                    }
                ],
                "message": " "
            }
    """
    params = caseinfo_by_id_schema(request.json or '')
    case_id = params.get('case_id')
    casedata = db.session.query(Case).filter(Case.id == case_id,Case.is_delete == 0).first()
    if casedata.store_id:
        data = db.session.query(Store).filter(Case.id == case_id, Case.is_delete == 0,
                                              Store.id == Case.store_id).with_entities(
            Case.id,
            Case.caseId,
            Case.store_id,
            Store.store_name,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).all()
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    else:
        data = db.session.query(Case).filter(Case.id == case_id, Case.is_delete == 0).with_entities(
            Case.id,
            Case.caseId,
            Case.store_id,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).all()
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')


# 修改违法案件信息
@blue_print.route('/modifyCaseInfo', methods=['POST'])
def case_modify():
    """
        @api {post} api/case/modifyCaseInfo  修改违法案件信息
        @apiVersion 0.0.1
        @apiName modifyCaseInfo
        @apiGroup case
        @apiDescription 修改违法案件信息
        @apiParam {int}  case_id    (必须)    违法信息id
        @apiParam {String}  caseId    (必须)    案件编号
        @apiParam {int}  store_id    (必须,零售商户表必须有此数据)    零售商户id
        @apiParam {date}  case_date    (可选)    案发时间
        @apiParam {String}  case_value      (可选)    案值
        @apiParam {String}  count    (可选)    卷烟数量（条数）
        @apiParam {string}  case_nature    (可选)    案件性质
        @apiParam {Boolean}  is_criminal     (可选)   有无刑事处罚，True有 False没有
        @apiParam {Boolean}  smoke_property01    (可选)    是否为非流烟，True是 False否
        @apiParam {Boolean}  smoke_property02    (可选)    是否为假冒烟，True是 False否
        @apiParam {Boolean}  smoke_property03    (可选)    是否为走私烟，True是 False否
        @apiParamExample {json} Request-Example:
            {
                "case_id":1828,
                "store_id":5,
                "caseId":"541254521",
                "case_date":"2020-04-01",
                "case_value":"6666.66",
                "count":"5000",
                "case_nature":"未在当地企业进货",
                "is_criminal":"True",
                "smoke_property01":"True",
                "smoke_property02":"False",
                "smoke_property03":"True"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "违法信息修改成功"
            }
    """
    params = case_info_schema(request.json or '')
    case_id = params.get('case_id')
    case = Case.query.filter(Case.id == case_id, Case.is_delete == 0)
    params.pop('case_id')
    case.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '违法信息修改成功')


# 删除违法案件信息
@blue_print.route('/delCase', methods=['POST'])
def delete_case():
    """
        @api {POST} api/case/delCase  删除违法案件信息
        @apiVersion 0.0.1
        @apiName delCase
        @apiGroup case
        @apiDescription 删除违法案件信息
        @apiParam {int}  case_id     (必须)    违法信息id
        @apiParamExample {json} Request-Example:
            {
                "case_id":1828
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "违法信息删除成功"
            }
    """
    params = del_case_schema(request.json or '')
    case_id = params.get('case_id')
    is_delete = 1
    case = Case.query.filter(Case.id == case_id, Case.is_delete == 0).first()
    case.is_delete = is_delete
    case.save()
    return common_response(SysStatus.SUCCESS, case.is_delete, '违法信息删除成功')


# 根据店铺id获取违法案件信息
@blue_print.route('/getCaseInfoByStoreid', methods=['POST'])
def get_case_info_by_storeid():
    """
            @api {POST} api/case/getCaseInfoByStoreid 根据店铺id获取违法案件信息
            @apiVersion 0.0.1
            @apiName getCaseInfoByStoreid
            @apiGroup case
            @apiDescription 根据店铺id获取违法案件信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  store_id     (必须)    零售商户id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "store_id":5,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 1828,
                                "caseId": "541254521",
                                "store_id": 5,
                                "store_name": "金华市婺城区周根花便利店",
                                "case_date": "2020-04-01 00:00:00",
                                "case_value": "6666.66",
                                "count": "5000.00",
                                "case_nature": "未在当地企业进货",
                                "is_criminal": true,
                                "smoke_property01": true,
                                "smoke_property02": false,
                                "smoke_property03": true
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = caseinfo_by_store_id_schema(request.json or '')
    page = params.get('page')
    store_id = params.get('store_id')
    per_page = params.get('per_page')
    pagination = db.session.query(Store).filter(Case.store_id == store_id, Case.is_delete == 0,
                                                Store.id == store_id).with_entities(
        Case.id,
        Case.caseId,
        Case.store_id,
        Store.store_name,
        Case.case_date,
        Case.case_value,
        Case.count,
        Case.case_nature,
        Case.is_criminal,
        Case.smoke_property01,
        Case.smoke_property02,
        Case.smoke_property03
    ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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


# 根据店铺名称获取违法案件信息-模糊查询--分页
@blue_print.route('/getCaseInfoByStorename', methods=['POST'])
def get_case_info_by_storename():
    """
            @api {POST} api/case/getCaseInfoByStorename 根据店铺名称获取违法案件信息-模糊查询--分页
            @apiVersion 0.0.1
            @apiName getCaseInfoByStorename
            @apiGroup case
            @apiDescription 根据店铺名称获取违法案件信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {str}  store_name     (必须)    零售商户名称
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParamExample {json} Request-Example:
                {如何role_id为1时，专卖局id和稽查所id不需要添加,查询范围是所有
                    "store_name":"周根花便利店",
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
                                "store_name": "金华市婺城区周根花便利店",
                                "id": 1828,
                                "caseId": "541254521",
                                "store_id": 5,
                                "case_date": "2020-04-01 00:00:00",
                                "case_value": "6666.66",
                                "count": "5000.00",
                                "case_nature": "未在当地企业进货",
                                "is_criminal": true,
                                "smoke_property01": true,
                                "smoke_property02": false,
                                "smoke_property03": true
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
               {添加role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
                    "store_name":"周根花便利店",
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
                                "store_name": "金华市婺城区周根花便利店",
                                "id": 1828,
                                "caseId": "541254521",
                                "store_id": 5,
                                "case_date": "2020-04-01 00:00:00",
                                "case_value": "6666.66",
                                "count": "5000.00",
                                "case_nature": "未在当地企业进货",
                                "is_criminal": true,
                                "smoke_property01": true,
                                "smoke_property02": false,
                                "smoke_property03": true
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {role_id为3或者4时，专卖局id不需要添加,查询范围是本稽查所内
                    "store_name":"周根花便利店",
                    "page":1,
                    "per_page":8,
                    "role_id":3,
                    "department_id":1
                }
            @apiSuccessExample {json} Success-Response:
              {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "store_name": "金华市婺城区周根花便利店",
                                "id": 1828,
                                "caseId": "541254521",
                                "store_id": 5,
                                "case_date": "2020-04-01 00:00:00",
                                "case_value": "6666.66",
                                "count": "5000.00",
                                "case_nature": "未在当地企业进货",
                                "is_criminal": true,
                                "smoke_property01": true,
                                "smoke_property02": false,
                                "smoke_property03": true
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = caseinfo_by_store_name_schema(request.json or '')
    page = params.get('page')
    store_name = params.get('store_name')
    per_page = params.get('per_page')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    if role_id == 1:
        # pagination = db.session.query(Case).join(Store).filter(Store.store_name == store_name,Store.is_delete == 0).with_entities(
        pagination = db.session.query(Case).join(Store).filter(
            Store.store_name.like("%" + store_name + "%") if store_name is not None else "", Store.is_delete == 0,
                                                                                             Case.is_delete == 0).with_entities(
            Store.store_name,
            Case.id,
            Case.caseId,
            Case.store_id,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
            pagination = db.session.query(Case).join(Store).filter(
                Store.store_name.like("%" + store_name + "%") if store_name is not None else "", Store.is_delete == 0,
                                                                                                 Case.is_delete == 0).with_entities(
                Store.store_name,
                Case.id,
                Case.caseId,
                Case.store_id,
                Case.case_date,
                Case.case_value,
                Case.count,
                Case.case_nature,
                Case.is_criminal,
                Case.smoke_property01,
                Case.smoke_property02,
                Case.smoke_property03
            ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
            pagination = db.session.query(Case).join(Store, Department).filter(Department.station_id == station_id,
                                                                               Store.department_id == Department.id).filter(
                Store.store_name.like("%" + store_name + "%") if store_name is not None else "", Store.is_delete == 0,
                                                                                                 Case.is_delete == 0).with_entities(
                Store.store_name,
                Case.id,
                Case.caseId,
                Case.store_id,
                Case.case_date,
                Case.case_value,
                Case.count,
                Case.case_nature,
                Case.is_criminal,
                Case.smoke_property01,
                Case.smoke_property02,
                Case.smoke_property03
            ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
        pagination = db.session.query(Case).join(Store, Department).filter(Store.department_id == department_id).filter(
            Store.store_name.like("%" + store_name + "%") if store_name is not None else "", Store.is_delete == 0,
                                                                                             Case.is_delete == 0).with_entities(
            Store.store_name,
            Case.id,
            Case.caseId,
            Case.store_id,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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


# 通过角色id查询违法案件信息
@blue_print.route('/getAllCaseInfobyroleid', methods=['POST'])
def get_all_caseinfo_by_role_id():
    """
            @api {POST} api/case/getAllCaseInfobyroleid 通过角色id查询违法案件信息
            @apiVersion 0.0.1
            @apiName getAllCaseInfobyroleid
            @apiGroup case
            @apiDescription 通过角色id查询违法案件信息,因为是post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  department_id     (可选)    稽查所id
             @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParamExample {json} Request-Example:
                {如何role_id为1时，专卖局id和稽查所id不需要添加,查询范围是所有
                    "role_id":1,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    省略
                }
            @apiParamExample {json} Request-Example:
                 {添加role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
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
                {role_id为3或者4时，专卖局id不需要添加,查询范围是本稽查所内
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
    params = caseinfo_by_role_id_schema(request.json or '')
    department_id = params.get('department_id')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    if role_id == 1:
        pagination = db.session.query(Case).join(Store).filter(Case.is_delete == 0,Case.store_id == Store.id
                                                               ).with_entities(
            Case.id,
            Case.caseId,
            Case.store_id,
            Store.store_name,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
            pagination = db.session.query(Case).join(Store).filter(Case.is_delete == 0, Case.store_id == Store.id
                                                                   ).with_entities(
                Case.id,
                Case.caseId,
                Case.store_id,
                Store.store_name,
                Case.case_date,
                Case.case_value,
                Case.count,
                Case.case_nature,
                Case.is_criminal,
                Case.smoke_property01,
                Case.smoke_property02,
                Case.smoke_property03
            ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
            pagination = db.session.query(Case).join(Store, Department).filter(Department.station_id == station_id).filter(
                Store.department_id == Department.id,
                Store.is_delete == 0).filter(Case.store_id == Store.id, Case.is_delete == 0).with_entities(
                Case.id,
                Case.caseId,
                Case.store_id,
                Store.store_name,
                Case.case_date,
                Case.case_value,
                Case.count,
                Case.case_nature,
                Case.is_criminal,
                Case.smoke_property01,
                Case.smoke_property02,
                Case.smoke_property03
            ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
        pagination = db.session.query(Case).join(Store, Department).filter(Store.department_id == department_id,
                                                                           Store.is_delete == 0).filter(
            Case.store_id == Store.id, Case.is_delete == 0).with_entities(
            Case.id,
            Case.caseId,
            Case.store_id,
            Store.store_name,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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


# 直接通过get方法获取所有违法案件信息
@blue_print.route('/getAllCaseInfo', methods=['GET'])
def get_all_caseinfo():
    """
            @api {GET} api/case/getAllCaseInfo 直接通过get方法获取所有违法案件信息
            @apiVersion 0.0.1
            @apiName getAllCaseInfo
            @apiGroup case
            @apiDescription 直接通过get方法获取所有违法案件信息,此处使用了分页功能，因为是get方法，所以page参数通过访问地址访问，通过per_page指定每页显示多少条数据
            @apiSuccessExample {json} Success-Response:
                {
                   示例:http://39.96.52.170:5000/api/case/getAllCaseInfo?page=2&per_page=8  可以获取第二页的8条内容
                }
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = db.session.query(Store).filter(Case.is_delete == 0, Case.store_id == Store.id).with_entities(
        Case.id,
        Case.caseId,
        Case.store_id,
        Store.store_name,
        Case.case_date,
        Case.case_value,
        Case.count,
        Case.case_nature,
        Case.is_criminal,
        Case.smoke_property01,
        Case.smoke_property02,
        Case.smoke_property03
    ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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


# 根据店铺和筛选条件获取违法案件信息--模糊查询--分页
@blue_print.route('/getCaseInfoByselect', methods=['POST'])
def get_case_info_by_storeandselect():
    """
            @api {POST} api/case/getCaseInfoByselect 根据店铺和筛选条件获取违法案件信息
            @apiVersion 0.0.1
            @apiName getCaseInfoByselect
            @apiGroup case
            @apiDescription 根据店铺和筛选条件获取违法案件信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {str}  store_name     (可选)    零售商户名称
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParam {str}  low_case_value     (可选)    案值的下界,案值和时间必须成对出现
            @apiParam {str}  high_case_value     (可选)    案值的上界
            @apiParam {Date}  low_case_data     (可选)    日期的下界
            @apiParam {Date}  high_case_data     (可选)    日期的上界
            @apiParam {str}  case_nature     (可选)    案件性质
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiDescription  案值和日期必须成对出现，不选择案值时，案值的两个参数是空字符串；不选择日期时，日期的两个参数必须是"1988-01-01";
            @apiParamExample {json} Request-Example:
                {如何role_id为1时，专卖局id和稽查所id不需要添加,查询范围是所有
                	"store_name":"周根花",
                    "page":1,
                    "per_page":8,
                    "low_case_data":"2001-01-01",
                    "high_case_data":"2020-10-10",
                    "low_case_value":"10",
                    "high_case_value":"500000",
                    "role_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "store_name": "金华市婺城区周根花便利店",
                                "id": 1828,
                                "caseId": "541254521",
                                "store_id": 5,
                                "case_date": "2020-04-01 00:00:00",
                                "case_value": "6666.66",
                                "count": "5000.00",
                                "case_nature": "未在当地企业进货",
                                "is_criminal": true,
                                "smoke_property01": true,
                                "smoke_property02": false,
                                "smoke_property03": true
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {添加role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
                   "store_name":"周根花",
                    "page":1,
                    "per_page":8,
                    "low_case_data":"2001-01-01",
                    "high_case_data":"2020-10-10",
                    "low_case_value":"10",
                    "high_case_value":"500000",
                    "role_id":2,
                    "station_id":1
                }
            @apiSuccessExample {json} Success-Response:
              {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "store_name": "金华市婺城区周根花便利店",
                            "id": 1828,
                            "caseId": "541254521",
                            "store_id": 5,
                            "case_date": "2020-04-01 00:00:00",
                            "case_value": "6666.66",
                            "count": "5000.00",
                            "case_nature": "未在当地企业进货",
                            "is_criminal": true,
                            "smoke_property01": true,
                            "smoke_property02": false,
                            "smoke_property03": true
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
            @apiParamExample {json} Request-Example:
                {role_id为3或者4时，专卖局id不需要添加,查询范围是本稽查所内
                   "store_name":"周根花",
                    "page":1,
                    "per_page":8,
                    "low_case_data":"2001-01-01",
                    "high_case_data":"2020-10-10",
                    "low_case_value":"10",
                    "high_case_value":"500000",
                    "role_id":3,
                    "department_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "store_name": "金华市婺城区周根花便利店",
                                "id": 1828,
                                "caseId": "541254521",
                                "store_id": 5,
                                "case_date": "2020-04-01 00:00:00",
                                "case_value": "6666.66",
                                "count": "5000.00",
                                "case_nature": "未在当地企业进货",
                                "is_criminal": true,
                                "smoke_property01": true,
                                "smoke_property02": false,
                                "smoke_property03": true
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = caseinfo_by_storenameandselect_schema(request.json or '')
    page = params.get('page')
    store_name = params.get('store_name')
    per_page = params.get('per_page')
    low_case_value = params.get('low_case_value')
    low_case_data = params.get('low_case_data')
    high_case_data = params.get('high_case_data')
    high_case_value = params.get('high_case_value')
    case_nature = params.get('case_nature')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    map = [Store.is_delete == 0, Case.is_delete == 0]
    if store_name:
        map.append(Store.store_name.like("%" + store_name + "%") if store_name is not None else "")
    if high_case_data and low_case_data:
        map.append(and_(Case.case_date >= low_case_data, Case.case_date <= high_case_data))
    if low_case_value and high_case_value:
        # map.append(or_(Case.case_value == None,and_(Case.case_value >= low_case_value,Case.case_value <= high_case_value)))
        map.append(
            or_(Case.case_value == None, and_(Case.case_value >= low_case_value, Case.case_value <= high_case_value)))
    if case_nature:
        map.append(Case.case_nature.like("%" + case_nature + "%") if case_nature is not None else "")
    if role_id == 1:
        pagination = db.session.query(Case).join(Store).filter(*map).with_entities(
            Store.store_name,
            Case.id,
            Case.caseId,
            Case.store_id,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
            pagination = db.session.query(Case).join(Store).filter(*map).with_entities(
                Store.store_name,
                Case.id,
                Case.caseId,
                Case.store_id,
                Case.case_date,
                Case.case_value,
                Case.count,
                Case.case_nature,
                Case.is_criminal,
                Case.smoke_property01,
                Case.smoke_property02,
                Case.smoke_property03
            ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
            pagination = db.session.query(Case).join(Store, Department).filter(Department.station_id == station_id,
                                                                               Store.department_id == Department.id).filter(
                *map).with_entities(
                Store.store_name,
                Case.id,
                Case.caseId,
                Case.store_id,
                Case.case_date,
                Case.case_value,
                Case.count,
                Case.case_nature,
                Case.is_criminal,
                Case.smoke_property01,
                Case.smoke_property02,
                Case.smoke_property03
            ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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
        pagination = db.session.query(Case).join(Store, Department).filter(Store.department_id == department_id).filter(
            *map).with_entities(
            Store.store_name,
            Case.id,
            Case.caseId,
            Case.store_id,
            Case.case_date,
            Case.case_value,
            Case.count,
            Case.case_nature,
            Case.is_criminal,
            Case.smoke_property01,
            Case.smoke_property02,
            Case.smoke_property03
        ).order_by(Case.id).paginate(page, per_page=per_page, error_out=False)
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


# 进货详细记录相关接口
# 通过进货记录id查询进货详细信息
@blue_print.route('/getPurchaseInfoByid', methods=['POST'])
def get_purchaseinfo_by_id():
    """
            @api {POST} api/case/getPurchaseInfoByid 通过进货记录id查询进货详细信息
            @apiVersion 0.0.1
            @apiName getPurchaseInfoByid
            @apiGroup case
            @apiDescription 通过进货记录id查询进货详细信息
            @apiParam {int}  purchase_id     (必须)    进货记录id
            @apiParamExample {json} Request-Example:
                {
                    "purchase_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 1,
                            "store_id": 5,
                            "store_name": "金华市婺城区沈美香副食店",
                            "purchase_date": "2020-04-04",
                            "purchase_week": 8,
                            "settlement_account": "458874554412",
                            "required_count": 122,
                            "average_price": "145.00"
                        }
                    ],
                    "message": " "
                }
    """
    params = purchaseinfo_by_id_schema(request.json or '')
    purchase_id = params.get('purchase_id')
    data = db.session.query(Purchase).join(Store).filter(Purchase.id == purchase_id,
                                                         Purchase.is_delete == 0).with_entities(*purchase_info_ser
                                                                                                ).order_by(
        Purchase.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据店铺id获取进货详细信息
@blue_print.route('/getPurchaseInfoByStoreid', methods=['POST'])
def get_purchase_info_by_storeid():
    """
            @api {POST} api/case/getPurchaseInfoByStoreid 根据店铺id获取进货详细信息
            @apiVersion 0.0.1
            @apiName getPurchaseInfoByStoreid
            @apiGroup case
            @apiDescription 根据店铺id获取进货详细信息,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  store_id     (必须)    零售商户id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "store_id":5,
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
                                "store_id": 5,
                                "store_name": "金华市婺城区沈美香副食店",
                                "purchase_date": "2020-04-04",
                                "purchase_week": 8,
                                "settlement_account": "458874554412",
                                "required_count": 122,
                                "average_price": "145.00"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = purchaseinfo_by_store_id_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(Purchase).join(Store).filter(Purchase.store_id == store_id,
                                                               Purchase.is_delete == 0).with_entities(
        *purchase_info_ser
    ).order_by(desc(Purchase.id)).paginate(page, per_page=per_page, error_out=False)
    purdata = pagination.items
    count = pagination.total
    data = {
        'data': purdata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据store_id和进货时间查询店铺进货信息
@blue_print.route('getPurchaseInfobyTimeandStore_id', methods=['POST'])
def get_purchaseinfo_by_timeandstore_id():
    """
               @api {POST} api/case/getPurchaseInfobyTimeandStore_id 通过POST获取某店铺该时间段内的全部进货信息
               @apiVersion 0.0.1
               @apiName getPurchaseInfobyTimeandStore_id
               @apiGroup case
               @apiDescription 直接获取所有某一售户信息查询时间段内进货记录,使用分页
               @apiParam {int}  store_id     (必须)    零售户id
               @apiParam {int}  page     (必须)    页数
               @apiParam {int}  per_page     (必须)    每页的页数
               @apiParam {int}  start_date     (必须)    起始时间
               @apiParam {int}  end_date     (必须)    终止时间
               @apiParamExample {json} Request-Example:
                {
                    "store_id":1,
                    "page":1,
                    "per_page":8
                    "start_date":"2020-03-01",
                    "end_date":"2020-04-01"
                }
            @apiSuccessExample {json} Success-Response:
               {
                     "sys_status": "SUCCESS",
            "data": {
                "data": [
                    {
                        "id": 1,
                        "store_id": 1,
                        "purchase_date": "2020-03-14",
                        "purchase_week": 50,
                        "settlement_account": "1234564789645",
                        "required_count": 80,
                        "average_price": "10.00"
                    },
                    {
                        "id": 4,
                        "store_id": 1,
                        "purchase_date": "2020-03-21",
                        "purchase_week": 60,
                        "settlement_account": "4612235",
                        "required_count": 90,
                        "average_price": "5.00"
                    }
                ],
                "count": 2
            },
            "message": " "
                        }
       """
    params = get_purchaseinfo_by_timeandstore_id_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    start_date = params.get('start_date')
    end_date = params.get('end_date')
    pagination = Purchase.query.join(Store).filter(Purchase.store_id == store_id,
                                                   and_(Purchase.purchase_date >= start_date,
                                                        Purchase.purchase_date <= end_date),
                                                   Purchase.is_delete == 0) \
        .with_entities(*purchase_info_ser).order_by(Purchase.id).paginate(page, per_page=per_page, error_out=False)
    # pagination = Purchase.query.filter(Purchase.store_id == store_id, and_(Purchase.purchase_date >= start_date,Purchase.purchase_date <= end_date), Purchase.is_delete == 0).with_entities(
    #     *purchase_info_ser
    # ).order_by(Purchase.id).paginate(page, per_page=per_page, error_out=False)
    purchasedata = pagination.items
    count = pagination.total
    data = {
        'data': purchasedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 案件涉烟详情表接口
# 通过案件涉烟详情id查询案件涉烟详情
@blue_print.route('/getcasecigarInfoByid', methods=['POST'])
def get_casecigarinfo_by_id():
    """
            @api {POST} api/case/getcasecigarInfoByid 通过案件涉烟详情id查询案件涉烟详情
            @apiVersion 0.0.1
            @apiName getcasecigarInfoByid
            @apiGroup case
            @apiDescription 通过案件涉烟详情id查询案件涉烟详情
            @apiParam {int}  casecigar_id     (必须)    案件涉烟详情id
            @apiParamExample {json} Request-Example:
                {
                    "casecigar_id":5
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 5,
                            "case_id": 1,
                            "store_name": "东阳市横店嘉苑副食商行",
                            "business_number": "330783109758",
                            "case_date": "2019-10-21 21:09:00",
                            "case_nature": "销售非法生产的烟草专卖品、销售无标志的外国卷烟",
                            "cigar_property": {
                                "COUNTERFEIT": "假冒烟"
                            },
                            "singlebrandname": "中华(硬)",
                            "count": "0.40",
                            "cigar_codefront": null,
                            "cigar_codebehind": null,
                            "origin_area": "东阳市"
                        }
                    ],
                    "message": " "
                }
    """
    params = casecigarinfo_by_id_schema(request.json or '')
    casecigar_id = params.get('casecigar_id')
    data = db.session.query(Case_cigar).filter(Case_cigar.id == casecigar_id,
                                                                 Case_cigar.is_delete == 0).with_entities(
        *casecigar_info_ser
    ).order_by(Case_cigar.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据店铺id获取案件涉烟详情
@blue_print.route('/getcasecigarInfoByStoreid', methods=['POST'])
def get_casecigarinfo_by_storeid():
    """
            @api {POST} api/case/getcasecigarInfoByStoreid 根据店铺id获取案件涉烟详情
            @apiVersion 0.0.1
            @apiName getcasecigarInfoByStoreid
            @apiGroup case
            @apiDescription 根据店铺id获取案件涉烟详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  store_id     (必须)    零售商户id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "store_id":2723,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
               {
               省略
                }
    """
    params = casecigarinfo_by_store_id_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(Case_cigar).join(Case).filter(Case.store_id == store_id,
                                                                             Case.is_delete == 0).with_entities(
        *casecigar_info_ser
    ).order_by(
        Case_cigar.id).paginate(page, per_page=per_page, error_out=False)
    casedata = pagination.items
    count = pagination.total
    data = {
        'data': casedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')

# 根据store_id和案件发生时间查询案件涉烟详情
@blue_print.route('getcasecigarInfobyTimeandStore_id', methods=['POST'])
def get_casecigarinfo_by_timeandstore_id():
    """
               @api {POST} api/case/getcasecigarInfobyTimeandStore_id 通过POST获取某店铺该时间段内的涉烟详情信息
               @apiVersion 0.0.1
               @apiName getcasecigarInfobyTimeandStore_id
               @apiGroup case
               @apiDescription 直接获取所有某一售户信息查询时间段内涉烟详情信息,使用分页
               @apiParam {int}  store_id     (必须)    零售户id
               @apiParam {int}  page     (必须)    页数
               @apiParam {int}  per_page     (必须)    每页的页数
               @apiParam {int}  start_date     (必须)    起始时间
               @apiParam {int}  end_date     (必须)    终止时间
               @apiParamExample {json} Request-Example:
                {
                    "store_id":15523,
                    "page":1,
                    "per_page":8
                    "start_date":"2019-03-01",
                    "end_date":"2020-04-01"
                }
            @apiSuccessExample {json} Success-Response:
               {
               省略
                   }
       """
    params = casecigarinfo_by_timeandstore_id_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    start_date = params.get('start_date')
    end_date = params.get('end_date')
    pagination = db.session.query(Case_cigar).join(Case).filter(Case.store_id == store_id,
                                                   and_(Case.case_date >= start_date,
                                                        Case.case_date <= end_date),
                                                   Case.is_delete == 0) \
        .with_entities(*casecigar_info_ser).order_by(Case_cigar.id).paginate(page, per_page=per_page, error_out=False)
    # pagination = Purchase.query.filter(Purchase.store_id == store_id, and_(Purchase.purchase_date >= start_date,Purchase.purchase_date <= end_date), Purchase.is_delete == 0).with_entities(
    #     *purchase_info_ser
    # ).order_by(Purchase.id).paginate(page, per_page=per_page, error_out=False)
    purchasedata = pagination.items
    count = pagination.total
    data = {
        'data': purchasedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据违法案件id获取进案件涉烟详情
@blue_print.route('/getcasecigarInfoByCaseid', methods=['POST'])
def get_casecigarinfo_by_caseid():
    """
            @api {POST} api/case/getcasecigarInfoByCaseid 根据违法案件id获取进案件涉烟详情
            @apiVersion 0.0.1
            @apiName getcasecigarInfoByCaseid
            @apiGroup case
            @apiDescription 根据违法案件id获取进案件涉烟详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  case_id     (必须)    违法案件id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "case_id":16,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
               {
                   省略
                }
    """
    params = casecigarinfo_by_case_id_schema(request.json or '')
    case_id = params.get('case_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(Case_cigar).filter(Case_cigar.case_id == case_id,
                                                                       Case_cigar.is_delete == 0).with_entities(
        *casecigar_info_ser
    ).order_by(Case_cigar.id).paginate(page, per_page=per_page, error_out=False)
    casedata = pagination.items
    count = pagination.total
    data = {
        'data': casedata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# #获取本地区互流关联信息
# @blue_print.route('/getintercasecigarInfoBy', methods=['POST'])
# def get_intercasecigarinfo():
#     """
#     """
#     params = inter_casecigarinfo_schema(request.json or '')
#     role_id = params.get('role_id')
#     date_start = params.get('date_start')
#     date_end = params.get('date_end')
#     department_id = params.get('department_id')
#     station_id = params.get('station_id')
#     # page = params.get('page')
#     # per_page = params.get('per_page')
#     map = []
#     if role_id == 1:
#         cigardata = db.session.query(Case_cigar.cigar_codebehind, Case_cigar.case_id,Case_cigar.case_date,
#                                      Case_cigar.business_number).filter(or_(Case_cigar.cigar_codebehind.startswith('JHYC'),
#                 Case_cigar.cigar_codebehind.startswith('jhyc')),Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end).distinct().all()
#         for i in cigardata:
#             business_number = i.business_number
#             query_business_number = i.cigar_codebehind[4:16]
#             case_id = i.case_id
#             inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
#                 Store.store_name,
#                 Store.id
#             ).order_by(Store.id).all()
#             outputstore = db.session.query(Store).filter(Store.business_number == query_business_number).with_entities(
#                 Store.store_name,
#                 Store.id
#             ).order_by(Store.id).all()
#             data = {
#                 "流出店铺": outputstore,
#                 "流入店铺": inputstore,
#                 "案件编号": case_id,
#                 "business_number": business_number,
#                 "query_business_number": query_business_number
#             }
#             map.append(data)
#         if map:
#             return common_response(SysStatus.SUCCESS, map, ' ')
#         else:
#             return common_response(SysStatus.FAIL, None, '无查询结果')
#     if role_id == 2 or role_id == 5:
#         if station_id == 1:
#             cigardata = db.session.query(Case_cigar.cigar_codebehind, Case_cigar.case_id,Case_cigar.case_date,
#                                          Case_cigar.business_number).filter(Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end,
#                 or_(Case_cigar.cigar_codebehind.startswith('JHYC'),
#                     Case_cigar.cigar_codebehind.startswith('jhyc'))).distinct().all()
#             for i in cigardata:
#                 business_number = i.business_number
#                 query_business_number = i.cigar_codebehind[4:16]
#                 case_id = i.case_id
#                 inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
#                     Store.store_name,
#                     Store.id
#                 ).order_by(Store.id).all()
#                 outputstore = db.session.query(Store).filter(
#                     Store.business_number == query_business_number).with_entities(
#                     Store.store_name,
#                     Store.id
#                 ).order_by(Store.id).all()
#                 data = {
#                     "流出店铺": outputstore,
#                     "流入店铺": inputstore,
#                     "案件编号": case_id,
#                     "business_number": business_number,
#                     "query_business_number": query_business_number
#                 }
#                 map.append(data)
#             if map:
#                 return common_response(SysStatus.SUCCESS, map, ' ')
#             else:
#                 return common_response(SysStatus.FAIL, None, '无查询结果')
#         else:
#             cigardata = db.session.query(Case_cigar.cigar_codebehind,Case_cigar.case_date, Case_cigar.case_id,Case_cigar.business_number).join(Case).filter(or_(Case_cigar.cigar_codebehind.startswith('JHYC'),
#                     Case_cigar.cigar_codebehind.startswith('jhyc')),Department.station_id == station_id,Store.department_id == Department.id,Case.store_id == Store.id,Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end).distinct().all()
#             for i in cigardata:
#                 business_number = i.business_number
#                 query_business_number = i.cigar_codebehind[4:16]
#                 case_id = i.case_id
#                 inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
#                     Store.store_name,
#                     Store.id
#                 ).order_by(Store.id).all()
#                 outputstore = db.session.query(Store).filter(
#                     Store.business_number == query_business_number).with_entities(
#                     Store.store_name,
#                     Store.id
#                 ).order_by(Store.id).all()
#                 data = {
#                     "流出店铺": outputstore,
#                     "流入店铺": inputstore,
#                     "案件编号": case_id,
#                     "business_number": business_number,
#                     "query_business_number": query_business_number
#                 }
#                 map.append(data)
#             if map:
#                 return common_response(SysStatus.SUCCESS, map, ' ')
#             else:
#                 return common_response(SysStatus.FAIL, None, '无查询结果')
#
#     if role_id == 3:
#         cigardata = db.session.query(Case_cigar.cigar_codebehind,Case_cigar.case_id,Case_cigar.case_date,Case_cigar.business_number).join(Case).filter(Store.department_id == department_id,Case.store_id == Store.id,Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end,or_(Case_cigar.cigar_codebehind.startswith('JHYC'),Case_cigar.cigar_codebehind.startswith('jhyc'))).distinct().all()
#         for i in cigardata:
#             business_number = i.business_number
#             query_business_number = i.cigar_codebehind[4:16]
#             case_id = i.case_id
#             inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
#                 Store.store_name,
#                 Store.id
#             ).order_by(Store.id).all()
#             outputstore = db.session.query(Store).filter(Store.business_number == query_business_number).with_entities(
#                 Store.store_name,
#                 Store.id
#             ).order_by(Store.id).all()
#             data = {
#                 "流出店铺":outputstore,
#                 "流入店铺":inputstore,
#                 "案件编号":case_id,
#                 "business_number":business_number,
#                 "query_business_number":query_business_number
#             }
#             map.append(data)
#         if map:
#             return common_response(SysStatus.SUCCESS, map, ' ')
#         else:
#             return common_response(SysStatus.FAIL, None, '无查询结果')
#     else:
#         return common_response(SysStatus.FAIL, None, '您无权查看')

#获取本地区互流关联信息
@blue_print.route('/getintercasecigarInfoBy', methods=['POST'])
def get_intercasecigarinfo():
    """
            @api {POST} api/case/getintercasecigarInfoBy 获取本地区互流关联信息
            @apiVersion 0.0.1
            @apiName getcasecigarInfoBy
            @apiGroup case
            @apiDescription 获取本地区互流关联信息,获取流入店铺。流出店铺
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {Date}  date_end     (必须)    日期的下界
            @apiParam {Date}  date_start     (必须)    日期的上界
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParamExample {json} Request-Example:
                 {role_id为1，系统管理员，可以查询所有数据
                    "date_start":"2001-01-01",
                    "date_end":"2020-10-10",
                    "role_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
               省略
                }
            @apiParamExample {json} Request-Example:
                 {role_id为2或者5时，是局长或者队长，查询范围是整个专卖局，如果station_id是1，查询范围是整个金华市，如果是其他值，查询范围是整个分局
                   "station_id":1,
                    "date_start":"2001-01-01",
                    "date_end":"2020-10-10",
                    "role_id":2
                }
            @apiSuccessExample {json} Success-Response:
               {
               省略
                }
            @apiParamExample {json} Request-Example:
                 {role_id为3或者4时，是所长或者稽查人员，查询范围是整个稽查所
                    "date_start":"2001-01-01",
                    "date_end":"2020-10-10",
                    "role_id":3,
                    "department_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
               省略
                }
    """
    params = inter_casecigarinfo_schema(request.json or '')
    role_id = params.get('role_id')
    date_start = params.get('date_start')
    date_end = params.get('date_end')
    department_id = params.get('department_id')
    station_id = params.get('station_id')
    # page = params.get('page')
    # per_page = params.get('per_page')
    map = []
    storelist = []
    storelist_new = []
    if role_id == 1:
        cigardata = db.session.query(Case_cigar.cigar_codebehind, Case_cigar.case_id,Case_cigar.case_date,
                                     Case_cigar.business_number,Case_cigar.store_name).filter(or_(Case_cigar.cigar_codebehind.startswith('JHYC'),
                Case_cigar.cigar_codebehind.startswith('jhyc')),Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end).distinct().all()
        for i in cigardata:
            business_number = i.business_number
            query_business_number = i.cigar_codebehind[4:16]
            case_id = i.case_id
            inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
                Store.store_name,
                Store.id,
                Store.longitude,
                Store.latitude
            ).order_by(Store.id).all()
            outputstore = db.session.query(Store).filter(Store.business_number == query_business_number).with_entities(
                Store.store_name,
                Store.id,
                Store.longitude,
                Store.latitude
            ).order_by(Store.id).all()
            if outputstore:
                storelist.append(inputstore)
                storelist.append(outputstore)
                data = {
                    "流出店铺": outputstore,
                    "流入店铺": inputstore,
                    "案件编号": case_id,
                    "business_number": business_number,
                    "query_business_number": query_business_number
                }
                map.append(data)
            else:
                pass
        for id in storelist:
            if id not in storelist_new:
                storelist_new.append(id)
        data = {"店铺汇总":storelist_new,"data":map}
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 5:
        if station_id == 1:
            cigardata = db.session.query(Case_cigar.cigar_codebehind, Case_cigar.case_id,Case_cigar.case_date,
                                         Case_cigar.business_number).filter(Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end,
                or_(Case_cigar.cigar_codebehind.startswith('JHYC'),
                    Case_cigar.cigar_codebehind.startswith('jhyc'))).distinct().all()
            for i in cigardata:
                business_number = i.business_number
                query_business_number = i.cigar_codebehind[4:16]
                case_id = i.case_id
                inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
                    Store.store_name,
                    Store.id,
                    Store.longitude,
                    Store.latitude
                ).order_by(Store.id).all()
                outputstore = db.session.query(Store).filter(
                    Store.business_number == query_business_number).with_entities(
                    Store.store_name,
                    Store.id,
                    Store.longitude,
                    Store.latitude
                ).order_by(Store.id).all()
                if outputstore:
                    storelist.append(inputstore)
                    storelist.append(outputstore)
                    data = {
                        "流出店铺": outputstore,
                        "流入店铺": inputstore,
                        "案件编号": case_id,
                        "business_number": business_number,
                        "query_business_number": query_business_number
                    }
                    map.append(data)
                else:
                    pass
            for id in storelist:
                if id not in storelist_new:
                    storelist_new.append(id)
            data = {"店铺汇总": storelist_new, "data": map}
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            cigardata = db.session.query(Case_cigar.cigar_codebehind,Case_cigar.case_date, Case_cigar.case_id,Case_cigar.business_number).join(Case).filter(or_(Case_cigar.cigar_codebehind.startswith('JHYC'),
                    Case_cigar.cigar_codebehind.startswith('jhyc')),Department.station_id == station_id,Store.department_id == Department.id,Case.store_id == Store.id,Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end).distinct().all()
            for i in cigardata:
                business_number = i.business_number
                query_business_number = i.cigar_codebehind[4:16]
                case_id = i.case_id
                inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
                    Store.store_name,
                    Store.id,
                    Store.longitude,
                    Store.latitude
                ).order_by(Store.id).all()
                outputstore = db.session.query(Store).filter(
                    Store.business_number == query_business_number).with_entities(
                    Store.store_name,
                    Store.id,
                    Store.longitude,
                    Store.latitude
                ).order_by(Store.id).all()
                if outputstore:
                    storelist.append(inputstore)
                    storelist.append(outputstore)
                    data = {
                        "流出店铺": outputstore,
                        "流入店铺": inputstore,
                        "案件编号": case_id,
                        "business_number": business_number,
                        "query_business_number": query_business_number
                    }
                    map.append(data)
                else:
                    pass
            for id in storelist:
                if id not in storelist_new:
                    storelist_new.append(id)
            data = {"店铺汇总": storelist_new, "data": map}
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')

    if role_id == 3:
        cigardata = db.session.query(Case_cigar.cigar_codebehind,Case_cigar.case_id,Case_cigar.case_date,Case_cigar.business_number).join(Case).filter(Store.department_id == department_id,Case.store_id == Store.id,Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end,or_(Case_cigar.cigar_codebehind.startswith('JHYC'),Case_cigar.cigar_codebehind.startswith('jhyc'))).distinct().all()
        for i in cigardata:
            business_number = i.business_number
            query_business_number = i.cigar_codebehind[4:16]
            case_id = i.case_id
            inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
                Store.store_name,
                Store.id,
                Store.longitude,
                Store.latitude
            ).order_by(Store.id).all()
            outputstore = db.session.query(Store).filter(Store.business_number == query_business_number).with_entities(
                Store.store_name,
                Store.id,
                Store.longitude,
                Store.latitude
            ).order_by(Store.id).all()
            if outputstore:
                storelist.append(inputstore)
                storelist.append(outputstore)
                data = {
                    "流出店铺":outputstore,
                    "流入店铺":inputstore,
                    "案件编号":case_id,
                    "business_number":business_number,
                    "query_business_number":query_business_number
                }
                map.append(data)
            else:
                pass
        for id in storelist:
            if id not in storelist_new:
                storelist_new.append(id)
        data = {"店铺汇总": storelist_new, "data": map}
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    else:
        return common_response(SysStatus.FAIL, None, '您无权查看')

#通过稽查所id获取本地区互流相关信息
@blue_print.route('/getintercasecigarInfoBydepartid', methods=['POST'])
def get_intercasecigarinfo_by_departid():
    """
            @api {POST} api/case/getintercasecigarInfoBydepartid 通过稽查所id获取本地区互流相关信息
            @apiVersion 0.0.1
            @apiName getintercasecigarInfoBydepartid
            @apiGroup case
            @apiDescription 通过稽查所id获取本地区互流相关信息,获取流入店铺。流出店铺
            @apiParam {Date}  date_end     (必须)    日期的下界
            @apiParam {Date}  date_start     (必须)    日期的上界
            @apiParam {int}  department_id     (必须)    稽查所id
            @apiParamExample {json} Request-Example:
                 {
                    "date_start":"2001-01-01",
                    "date_end":"2020-10-10",
                    "department_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
               省略
                }
    """
    params = inter_casecigarinfo_by_departid_schema(request.json or '')
    date_start = params.get('date_start')
    date_end = params.get('date_end')
    department_id = params.get('department_id')
    map = []
    storelist = []
    storelist_new = []
    cigardata = db.session.query(Case_cigar.cigar_codebehind,Case_cigar.case_id,Case_cigar.case_date,Case_cigar.business_number).join(Case).filter(Store.department_id == department_id,Case.store_id == Store.id,Case_cigar.case_date >= date_start,Case_cigar.case_date <= date_end,or_(Case_cigar.cigar_codebehind.startswith('JHYC'),Case_cigar.cigar_codebehind.startswith('jhyc'))).distinct().all()
    for i in cigardata:
        business_number = i.business_number
        query_business_number = i.cigar_codebehind[4:16]
        case_id = i.case_id
        inputstore = db.session.query(Store).filter(Store.business_number == business_number).with_entities(
                Store.store_name,
                Store.id,
                Store.longitude,
                Store.latitude
            ).order_by(Store.id).all()
        outputstore = db.session.query(Store).filter(Store.business_number == query_business_number).with_entities(
                Store.store_name,
                Store.id,
                Store.longitude,
                Store.latitude
            ).order_by(Store.id).all()
        if outputstore:
            storelist.append(inputstore)
            storelist.append(outputstore)
            data = {
                    "流出店铺":outputstore,
                    "流入店铺":inputstore,
                    "案件编号":case_id,
                    "business_number":business_number,
                    "query_business_number":query_business_number
                }
            map.append(data)
        else:
            pass
    for id in storelist:
        if id not in storelist_new:
            storelist_new.append(id)
    data = {"店铺汇总": storelist_new, "data": map}
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')



# 进货明细表部分接口
# 通过进货明细id查询进货明细详情
@blue_print.route('/getBrandInfoByid', methods=['POST'])
def get_brandinfo_by_id():
    """
            @api {POST} api/case/getBrandInfoByid 通过进货明细id查询进货明细详情
            @apiVersion 0.0.1
            @apiName getBrandInfoByid
            @apiGroup case
            @apiDescription 通过进货明细id查询进货明细详情
            @apiParam {int}  brand_id     (必须)    进货明细id
            @apiParamExample {json} Request-Example:
                {
                    "brand_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 1,
                            "purchase_id": 1,
                            "cigar_name": "中华软",
                            "cigar_price": "45.00",
                            "cigar_num": 20
                        }
                    ],
                    "message": " "
                }
    """
    params = brandinfo_by_id_schema(request.json or '')
    brand_id = params.get('brand_id')
    data = Brand.query.filter(Brand.id == brand_id, Brand.is_delete == 0).with_entities(*brand_info_ser
                                                                                        ).order_by(Brand.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据店铺id获取进货明细详情
@blue_print.route('/getbrandInfoByStoreid', methods=['POST'])
def get_brandinfo_by_storeid():
    """
            @api {POST} api/case/getbrandInfoByStoreid 根据店铺id获取进货明细详情
            @apiVersion 0.0.1
            @apiName getbrandInfoByStoreid
            @apiGroup case
            @apiDescription 根据店铺id获取进货明细详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  store_id     (必须)    零售商户id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "store_id":5,
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
                                "purchase_id": 1,
                                "cigar_name": "中华软",
                                "cigar_price": "45.00",
                                "cigar_num": 20
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = brandinfo_by_store_id_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(Brand).join(Purchase).filter(Purchase.store_id == store_id,
                                                               Purchase.is_delete == 0).with_entities(*brand_info_ser
                                                                                                      ).order_by(
        Brand.id).paginate(page, per_page=per_page, error_out=False)
    branddata = pagination.items
    count = pagination.total
    data = {
        'data': branddata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据进货表id查询进货明细详情
@blue_print.route('/getbrandInfoBypurchaseid', methods=['POST'])
def get_brandinfo_by_purchaseid():
    """
            @api {POST} api/case/getbrandInfoBypurchaseid 根据进货表id查询进货明细详情
            @apiVersion 0.0.1
            @apiName getbrandInfoBypurchaseid
            @apiGroup case
            @apiDescription 根据进货表id查询进货明细详情,此处使用了分页，post方法，page参数通过表单提交,per_page指定每页多少条数据
            @apiParam {int}  purchase_id     (必须)    进货表id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "purchase_id":1,
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
                                "purchase_id": 1,
                                "cigar_name": "中华软",
                                "cigar_price": "45.00",
                                "cigar_num": 20
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = brandinfo_by_purchase_id_schema(request.json or '')
    purchase_id = params.get('purchase_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = Brand.query.filter(Brand.purchase_id == purchase_id, Brand.is_delete == 0).with_entities(
        *brand_info_ser
    ).order_by(Brand.id).paginate(page, per_page=per_page, error_out=False)
    branddata = pagination.items
    count = pagination.total
    data = {
        'data': branddata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# excel导入导出部分接口
# 通过get获取excel导入表中的全部信息
@blue_print.route('/getAllExcelInandOutInfo', methods=['GET'])
def get_all_excel_inandout_info():
    """
            @api {GET} api/case/getAllExcelInandOutInfo 通过get获取excel导入表中的全部信息
            @apiVersion 0.0.1
            @apiName getAllExcelInandOutInfo
            @apiGroup excel导入导出
            @apiDescription 直接获取所有零售户信息,未使用分页
            @apiSuccessExample {json} Success-Response:
                {

                }
    """
    data = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0).with_entities(*excel_inandout_info_ser
                                                                                  ).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号获取excel导入表中符合该案件编号的详细信息
@blue_print.route('/getAllExcelInandOutInfobycaseid', methods=['POST'])
def get_all_excel_inandout_bycaseid_info():
    """
            @api {POST} api/case/getAllExcelInandOutInfobycaseid 通过案件编号获取excel导入表中的详细信息
            @apiVersion 0.0.1
            @apiName getAllExcelInandOutInfobycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号获取excel导入表中的详细信息,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004132145"
                }
            @apiSuccessExample {json} Success-Response:
                {

                }
    """
    params = excel_inandout_info_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                      ExcelInAndOut.is_delete == 0).with_entities(*excel_inandout_info_ser
                                                                                  ).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号获取excel导入表中符合该案件编号的详细信息__带分页
@blue_print.route('/getAllExcelInandOutInfobycaseidBypagi', methods=['POST'])
def get_all_excel_inandout_bycaseid_page_info():
    """
            @api {POST} api/case/getAllExcelInandOutInfobycaseidBypagi 通过案件编号获取excel导入表中符合该案件编号的详细信息__带分页
            @apiVersion 0.0.1
            @apiName getAllExcelInandOutInfobycaseidBypagi
            @apiGroup excel导入导出
            @apiDescription 通过案件编号获取excel导入表中符合该案件编号的详细信息__带分页,使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004132145",
                     "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 1044,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "thisresultStr123",
                                "code_behind": "thisresultStr234",
                                "count": "1.00"
                            },
                            {
                                "id": 1045,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            },
                            {
                                "id": 1046,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            },
                            {
                                "id": 1047,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            },
                            {
                                "id": 1048,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            },
                            {
                                "id": 1049,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            },
                            {
                                "id": 1050,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            },
                            {
                                "id": 1051,
                                "input_caseid": "202004132145",
                                "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                                "singlebrand_name": "长白山(海蓝)",
                                "code_front": "",
                                "code_behind": "",
                                "count": "1.00"
                            }
                        ],
                        "count": 96
                    },
                    "message": " "
                }
    """
    params = excel_inandout_info_by_caseid_page_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                            ExcelInAndOut.is_delete == 0).with_entities(*excel_inandout_info_ser
                                                                                        ).paginate(page,
                                                                                                   per_page=per_page,
                                                                                                   error_out=False)
    exceldata = pagination.items
    count = pagination.total
    data = {
        'data': exceldata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 扫码获取32位码录入数据库
@blue_print.route('/ScanCodeUpload', methods=['POST'])
def scan_code_upload_info():
    """
            @api {POST} api/case/ScanCodeUpload 扫码获取32位码录入数据库
            @apiVersion 0.0.1
            @apiName ScanCodeUpload
            @apiGroup excel导入导出
            @apiDescription 扫码获取32位码录入数据库
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParam {string}  singlebrand_name     (必须)    案件编号
            @apiParam {string}  code_front     (必须)    案件编号
            @apiParam {string}  code_behind     (必须)    案件编号
            @apiParam {int}  user_id     (必须)    案件编号
            @apiParamExample {json} Request-Example:
            {
                    "input_caseid":"202004120845",
                    "singlebrand_name":"长白山(海蓝)",
                    "code_front":"zscd124574584875",
                    "code_behind":"",
                    "user_id":1
                }
            @apiSuccessExample {json} Success-Response:
            {
                    "sys_status": "FAIL",
                    "data": null,
                    "message": "请输入完整的32位喷码"
                }
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845",
                    "singlebrand_name":"长白山(海蓝)",
                    "code_front":"zs48596458487548",
                    "code_behind":"4185425568951485",
                    "user_id":1
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 2,
                            "input_caseid": "202004120845",
                            "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                            "singlebrand_name": "长白山(海蓝)",
                            "code_front": "zs48596458487548",
                            "code_behind": "4185425568951485",
                            "count": "1.00"
                        },
                        {
                            "id": 1,
                            "input_caseid": "202004120845",
                            "singlebrand_id": "2af3e4119e1b466e810de5365d5bcf3e",
                            "singlebrand_name": "长白山(海蓝)",
                            "code_front": "zsc458574584875",
                            "code_behind": "418542556895",
                            "count": "1.00"
                        }
                    ],
                    "message": "喷码录入成功"
                }
    """
    params = scan_code_upload_info_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    singlebrand_name = params.get('singlebrand_name')
    code_front = params.get('code_front')
    code_behind = params.get('code_behind')
    user_id = params.get('user_id')
    if code_front == '' or code_behind == '':
        return common_response(SysStatus.FAIL, None, '请输入完整的32位喷码')
    else:
        data = ExcelInAndOut.query.filter(ExcelInAndOut.code_front == code_front,
                                          ExcelInAndOut.code_behind == code_behind,
                                          ExcelInAndOut.is_delete == 0).first()
        if data:
            return common_response(SysStatus.FAIL, data.code_behind, '该喷码已经录入')
        else:
            data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                              ExcelInAndOut.singlebrand_name == singlebrand_name,
                                              ExcelInAndOut.is_delete == 0, ExcelInAndOut.code_front == '').first()
            if data:
                data.update(user_id=user_id, code_front=code_front, code_behind=code_behind)
                db.session.commit()
                inputdata = ExcelInAndOut.query.filter(ExcelInAndOut.user_id == user_id,
                                                       ExcelInAndOut.is_delete == 0).with_entities(
                    *excel_inandout_info_ser).order_by(desc(ExcelInAndOut.id)).limit(20).all()
                return common_response(SysStatus.SUCCESS, inputdata, '喷码录入成功')
            else:
                data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                                  ExcelInAndOut.is_delete == 0, ExcelInAndOut.code_front == '').all()
                if data:
                    return common_response(SysStatus.SUCCESS, None, '该品规录入完成，请选择其他品规')
                else:
                    return common_response(SysStatus.FAIL, None, '该案件编号录入完成，请选择其他案件编号')


# 通过get获取excel表中未完成的案件编号
@blue_print.route('/getUncomplishCaseidInfo', methods=['GET'])
def get_uncomplish_caseid_info():
    """
            @api {GET} api/case/getUncomplishCaseidInfo 通过get获取excel表中未完成的案件编号
            @apiVersion 0.0.1
            @apiName getUncomplishCaseidInfo
            @apiGroup excel导入导出
            @apiDescription 通过get获取excel表中未完成的案件编号,未使用分页
            @apiSuccessExample {json} Success-Response:
                {

                }
    """
    data = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0, ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.input_caseid
    ).distinct().all()
    count = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0, ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.input_caseid
    ).distinct().count()
    data = {
        'data': data,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过get获取excel表中已经完成的案件编号
@blue_print.route('/getcomplishCaseidInfo', methods=['GET'])
def get_complish_caseid_info():
    """
            @api {GET} api/case/getcomplishCaseidInfo 通过get获取excel表中已经完成的案件编号
            @apiVersion 0.0.1
            @apiName getcomplishCaseidInfo
            @apiGroup excel导入导出
            @apiDescription 通过get获取excel表中已经完成的案件编号,未使用分页
            @apiSuccessExample {json} Success-Response:
                {

                }
    """
    allcasedata = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0).with_entities(
        ExcelInAndOut.input_caseid
    ).distinct().all()
    allcasedatacount = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0).with_entities(
        ExcelInAndOut.input_caseid
    ).distinct().count()
    uncomplishdata = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0,
                                                ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.input_caseid
    ).distinct().all()
    unconplishdatacount = ExcelInAndOut.query.filter(ExcelInAndOut.is_delete == 0,
                                                     ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.input_caseid
    ).distinct().count()
    for i in range(len(allcasedata)):
        for j in allcasedata:
            if j in uncomplishdata:
                allcasedata.remove(j)
    count = allcasedatacount - unconplishdatacount
    data = {
        'data': allcasedata,
        'count': count
    }
    if data['count'] == 0:
        return common_response(SysStatus.FAIL, None, '无已经完成的案件编号')
    else:
        return common_response(SysStatus.SUCCESS, data, ' ')


# 删除某个案件编号的全部信息
@blue_print.route('/DelCaseidInfo', methods=['POST'])
def del_import_caseid_info():
    """
            @api {POST} api/case/DelCaseidInfo 删除某个案件编号的全部信息
            @apiVersion 0.0.1
            @apiName DelCaseidInfo
            @apiGroup excel导入导出
            @apiDescription 删除某个案件编号的全部信息,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"199821225455"
                }
            @apiSuccessExample {json} Success-Response:
                {

                }
    """
    params = del_inandout_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    is_delete = 1
    data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid).update(
        {ExcelInAndOut.is_delete: is_delete})
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '删除成功')


# 通过案件编号获取该案件编号下全部品规
@blue_print.route('/getAllsinglenamebycaseid', methods=['POST'])
def get_allsinglename_by_caseid():
    """
            @api {POST} api/case/getAllsinglenamebycaseid 通过案件编号获取该案件编号下全部品规
            @apiVersion 0.0.1
            @apiName getAllsinglenamebycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号获取该案件编号下全部品规,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845"
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "singlebrand_name": "长白山(海蓝)"
                            },
                            {
                                "singlebrand_name": "长白山(777)"
                            }
                        ],
                        "count": 2
                    },
                    "message": " "
                }
    """
    params = get_all_singlename_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                      ExcelInAndOut.is_delete == 0).with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().all()
    count = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                       ExcelInAndOut.is_delete == 0).with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().count()
    data = {
        'data': data,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号获取该案件编号下未完成的品规
@blue_print.route('/getUncomplishsinglenamebycaseid', methods=['POST'])
def get_unconplish_singlename_by_caseid():
    """
            @api {POST} api/case/getUncomplishsinglenamebycaseid 通过案件编号获取该案件编号下未完成的品规
            @apiVersion 0.0.1
            @apiName getUncomplishsinglenamebycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号获取该案件编号下未完成的品规,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845"
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "singlebrand_name": "长白山(海蓝)"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = get_uncomplish_singlename_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                      ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().all()
    count = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                       ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().count()
    data = {
        'data': data,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号获取该案件编号下已经完成的品规
@blue_print.route('/getcomplishsinglenamebycaseid', methods=['POST'])
def get_conplish_singlename_by_caseid():
    """
            @api {POST} api/case/getcomplishsinglenamebycaseid 通过案件编号获取该案件编号下已经完成的品规
            @apiVersion 0.0.1
            @apiName getcomplishsinglenamebycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号获取该案件编号下已经完成的品规,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845"
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "singlebrand_name": "长白山(777)"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = get_complish_singlename_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    alldata = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                         ExcelInAndOut.is_delete == 0).with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().all()
    allcount = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                          ExcelInAndOut.is_delete == 0).with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().count()
    undata = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                        ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().all()
    uncount = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                         ExcelInAndOut.code_front == '').with_entities(
        ExcelInAndOut.singlebrand_name
    ).distinct().count()
    for i in range(len(alldata)):
        for j in alldata:
            if j in undata:
                alldata.remove(j)
    count = allcount - uncount
    data = {
        'data': alldata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号和品规名称获取该案件编号下该品规的全部数量
@blue_print.route('/getAllsinglenamecountbycaseid', methods=['POST'])
def get_allsinglenamecount_by_caseid():
    """
            @api {POST} api/case/getAllsinglenamecountbycaseid 通过案件编号和品规名称获取该案件编号下该品规的全部数量
            @apiVersion 0.0.1
            @apiName getAllsinglenamecountbycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号和品规名称获取该案件编号下该品规的全部数量,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParam {string}  singlebrand_name     (必须)    品规
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845",
                    "singlebrand_name":"长白山(海蓝)"
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": 105,
                    "message": " "
                }
    """
    params = get_all_singlenamecount_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    singlebrand_name = params.get('singlebrand_name')
    data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid,
                                      ExcelInAndOut.is_delete == 0,
                                      ExcelInAndOut.singlebrand_name == singlebrand_name).count()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号和品规名称获取该案件编号下该品规的未完成数量
@blue_print.route('/getUncomplishsinglenamecountbycaseid', methods=['POST'])
def get_unconplish_singlenamecount_by_caseid():
    """
            @api {POST} api/case/getUncomplishsinglenamecountbycaseid 通过案件编号和品规名称获取该案件编号下该品规的未完成数量
            @apiVersion 0.0.1
            @apiName getUncomplishsinglenamecountbycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号和品规名称获取该案件编号下该品规的未完成数量,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParam {string}  singlebrand_name     (必须)    品规
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845",
                    "singlebrand_name":"长白山(海蓝)",
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": 103,
                    "message": " "
                }
    """
    params = get_uncomplish_singlenamecount_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    singlebrand_name = params.get('singlebrand_name')
    data = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                      ExcelInAndOut.singlebrand_name == singlebrand_name,
                                      ExcelInAndOut.code_front == '').count()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过案件编号和品规名称获取该案件编号下该品规的已经完成数量
@blue_print.route('/getcomplishsinglenamecountbycaseid', methods=['POST'])
def get_conplish_singlenamecount_by_caseid():
    """
            @api {POST} api/case/getcomplishsinglenamecountbycaseid 通过案件编号和品规名称获取该案件编号下该品规的已经完成数量
            @apiVersion 0.0.1
            @apiName getcomplishsinglenamecountbycaseid
            @apiGroup excel导入导出
            @apiDescription 通过案件编号和品规名称获取该案件编号下该品规的已经完成数量,未使用分页
            @apiParam {string}  input_caseid     (必须)    案件编号
            @apiParam {string}  singlebrand_name     (必须)    品规
            @apiParamExample {json} Request-Example:
                {
                    "input_caseid":"202004120845",
                    "singlebrand_name":"长白山(海蓝)"
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": 2,
                    "message": " "
                }
    """
    params = get_complish_singlenamecount_by_caseid_schema(request.json or '')
    input_caseid = params.get('input_caseid')
    singlebrand_name = params.get('singlebrand_name')
    alldata = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                         ExcelInAndOut.singlebrand_name == singlebrand_name).count()
    undata = ExcelInAndOut.query.filter(ExcelInAndOut.input_caseid == input_caseid, ExcelInAndOut.is_delete == 0,
                                        ExcelInAndOut.singlebrand_name == singlebrand_name,
                                        ExcelInAndOut.code_front == '').count()
    data = alldata - undata
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')
