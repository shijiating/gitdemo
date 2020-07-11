#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request
import datetime
from sqlalchemy import desc, and_, or_, not_
import decimal
from api import db
from api.models.user import User
from api.models.store_Info import Store
from api.models.task import Audit, HidePicture
from api.models.user import User, Station, Department
from api.schemas.task import add_audit_schema, auditinfo_by_id_schema, audit_info_schema, \
    del_audit_schema, auditinfo_by_store_id_schema, add_hidepicture_schema, hidepicureinfo_by_auditid_schema, \
    hidepicureinfo_by_storeid_schema, hidepicure_info_schema, del_hidepicure_schema, auditinfo_by_store_id_with_hidepicture_schema,auditinfo_by_task_id_schema

from api.views.base import common_response, SysStatus

blue_print = Blueprint('task', __name__, url_prefix='/api/task')


# 稽查记录表部分
# 添加稽查记录
@blue_print.route('/addAudit', methods=['POST'])
def add_audit():
    """
        @api {post} api/task/addAudit  添加稽查记录
        @apiVersion 0.0.1
        @apiName addAudit
        @apiGroup task
        @apiDescription 添加稽查记录
        @apiParam {int}  store_id    (必须，零售商户必须先有数据)    零售商户id
        @apiParam {int}  inspector_id    (必须，用户表中必须先有数据)    稽查人员id
        @apiParam {date}  audit_date    (必须)    稽查时间
        @apiParam {String}  audit_pic1    (可选)    稽查情况照片1
        @apiParam {String}  audit_pic2      (可选)    稽查情况照片2
        @apiParam {String}  audit_pic3    (可选)    稽查情况照片3
        @apiParam {string}  audit_pic4    (可选)    稽查情况照片4
        @apiParam {string}  audit_pic5    (可选)    稽查情况照片5
        @apiParam {String}  audit_pic6    (可选)    稽查情况照片6
        @apiParam {Boolean}  audit_result     (可选)   稽查结果反馈
        @apiParam {String}  audit_note    (可选)    稽查情况备注
        @apiParam {Boolean}  is_opensale     (可选)   是否公开摆卖
        @apiParam {Enum}  measures     (可选)   采取措施
        @apiParam {Boolean}  is_holdcertificate     (可选)   是否持证经营
        @apiParam {Boolean}  is_opencertificate     (可选)   是否亮证经营
        @apiParam {Boolean}  is_saleticket     (可选)   是否销售烟票
        @apiParam {Boolean}  is_saleskyprice     (可选)   是否存在天价烟销售
        @apiParam {Boolean}  is_potentially_illegal     (可选)   是否有潜在违法行为
        @apiParam {String}  score    (可选)    评分
        @apiParamExample {json} Request-Example:
            {
                "store_id":5,
                "inspector_id":4,
                "audit_date":"2020-05-10",
                "audit_pic1":"2451245",
                "audit_pic2":"14586",
                "audit_pic3":"akdkjg",
                "audit_pic4":"sdgjg",
                "audit_pic5":"dasgsegj",
                "audit_pic6":"dsgkj",
                "audit_result":"True",
                "audit_note":"稽查good",
                "is_opensale":"True",
                "measures":"ORDER",
                "is_holdcertificate":"True",
                "is_opencertificate":"True",
                "is_saleticket":"True",
                "is_saleskyprice":"True",
                "is_potentially_illegal":"True",
                "score":"85"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": 1(新增记录id),
                "message": "稽查记录添加成功"
            }
    """
    params = add_audit_schema(request.json or '')
    store_id = params.get('store_id')
    inspector_id = params.get('inspector_id')
    audit_date = params.get('audit_date')
    audit_pic1 = params.get('audit_pic1')
    audit_pic2 = params.get('audit_pic2')
    audit_pic3 = params.get('audit_pic3')
    audit_pic4 = params.get('audit_pic4')
    audit_pic5 = params.get('audit_pic5')
    audit_pic6 = params.get('audit_pic6')
    audit_result = params.get('audit_result')
    audit_note = params.get('audit_note')
    is_opensale = params.get('is_opensale')
    measures = params.get('measures')
    is_holdcertificate = params.get('is_holdcertificate')
    is_opencertificate = params.get('is_opencertificate')
    is_saleticket = params.get('is_saleticket')
    is_saleskyprice = params.get('is_saleskyprice')
    is_potentially_illegal = params.get('is_potentially_illegal')
    score = decimal.Decimal(params.get('score'))
    # datestr = datetime.datetime.now().strftime('%Y-%m%-d%')
    audit = Audit(store_id=store_id, inspector_id=inspector_id,
                  audit_date=audit_date, audit_pic1=audit_pic1, audit_pic2=audit_pic2, audit_pic3=audit_pic3,
                  audit_pic4=audit_pic4, audit_pic5=audit_pic5, audit_pic6=audit_pic6, audit_result=audit_result,
                  audit_note=audit_note,
                  is_opensale=is_opensale, measures=measures, is_holdcertificate=is_holdcertificate,
                  is_opencertificate=is_opencertificate,
                  is_saleticket=is_saleticket, is_saleskyprice=is_saleskyprice,
                  is_potentially_illegal=is_potentially_illegal, score=score)
    db.session.add(audit)
    db.session.commit()
    data = audit.id
    return common_response(SysStatus.SUCCESS, data, '稽查记录添加成功')


# 通过稽查记录id获取详细信息
@blue_print.route('/getauditInfoByid', methods=['POST'])
def get_auditinfo_by_id():
    """
            @api {POST} api/task/getauditInfoByid 通过稽查记录id获取详细信息
            @apiVersion 0.0.1
            @apiName getauditInfoByid
            @apiGroup task
            @apiDescription 通过稽查记录id获取详细信息
            @apiParam {int}  audit_id     (必须)    稽查记录id
            @apiParamExample {json} Request-Example:
                {
                    "audit_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 1,
                            "store_id": 5,
                            "store_name": "金华市婺城区周根花便利店",
                            "inspector_id": 4,
                            "user_name": "专卖城区二所稽查员张飞",
                            "audit_date": "2020-05-10",
                            "audit_pic1": "2451245",
                            "audit_pic2": "14586",
                            "audit_pic3": "akdkjg",
                            "audit_pic4": "sdgjg",
                            "audit_pic5": "dasgsegj",
                            "audit_pic6": "dsgkj",
                            "audit_result": true,
                            "audit_note": "稽查good",
                            "is_opensale": true,
                            "measures": {
                                "ORDER": "责令整改"
                            },
                            "is_holdcertificate": true,
                            "is_opencertificate": true,
                            "is_saleticket": true,
                            "is_saleskyprice": true,
                            "is_potentially_illegal": true,
                            "score": "85.00"
                        }
                    ],
                    "message": " "
                }
    """
    params = auditinfo_by_id_schema(request.json or '')
    audit_id = params.get('audit_id')
    data = db.session.query(Audit).join(Store, User).filter(Audit.id == audit_id, Audit.is_delete == 0,
                                                            User.id == Audit.inspector_id).with_entities(
        Audit.id,
        Audit.store_id,
        Store.store_name,
        Audit.inspector_id,
        User.user_name,
        Audit.audit_date,
        Audit.audit_pic1,
        Audit.audit_pic2,
        Audit.audit_pic3,
        Audit.audit_pic4,
        Audit.audit_pic5,
        Audit.audit_pic6,
        Audit.audit_result,
        Audit.audit_note,
        Audit.is_opensale,
        Audit.measures,
        Audit.is_holdcertificate,
        Audit.is_opencertificate,
        Audit.is_saleticket,
        Audit.is_saleskyprice,
        Audit.is_potentially_illegal,
        Audit.score
    ).order_by(Audit.id).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 修改稽查信息
@blue_print.route('/modifyAuditInfo', methods=['POST'])
def audit_modify():
    """
        @api {post} api/task/modifyAuditInfo  修改稽查信息
        @apiVersion 0.0.1
        @apiName modifyAuditInfo
        @apiGroup task
        @apiDescription 修改稽查信息
        @apiParam {int}  audit_id    (必须)    稽查记录id
        @apiParam {int}  store_id    (可选)    零售商户id
        @apiParam {int}  inspector_id    (可选)    稽查人员id
        @apiParam {date}  audit_date    (可选)    稽查时间
        @apiParam {String}  audit_pic1    (可选)    稽查情况照片1
        @apiParam {String}  audit_pic2      (可选)    稽查情况照片2
        @apiParam {String}  audit_pic3    (可选)    稽查情况照片3
        @apiParam {string}  audit_pic4    (可选)    稽查情况照片4
        @apiParam {string}  audit_pic5    (可选)    稽查情况照片5
        @apiParam {String}  audit_pic6    (可选)    稽查情况照片6
        @apiParam {Boolean}  result     (可选)   稽查结果反馈
        @apiParam {String}  audit_note    (可选)    稽查情况备注
        @apiParam {Boolean}  is_opensale     (可选)   是否公开摆卖
        @apiParam {Enum}  measures     (可选)   采取措施
        @apiParam {Boolean}  is_holdcertificate     (可选)   是否持证经营
        @apiParam {Boolean}  is_opencertificate     (可选)   是否亮证经营
        @apiParam {Boolean}  is_saleticket     (可选)   是否销售烟票
        @apiParam {Boolean}  is_saleskyprice     (可选)   是否存在天价烟销售
        @apiParam {Boolean}  is_potentially_illegal     (可选)   是否有潜在违法行为
        @apiParam {String}  score    (可选)    评分
        @apiParamExample {json} Request-Example:
            {
                "audit_id":1,
                "inspector_id":4,
                "audit_date":"2020-04-01",
                "audit_pic1":"2451245",
                "audit_pic2":"14586",
                "audit_pic3":"akdkjgdksgk",
                "audit_pic4":"sdgjg",
                "audit_pic5":"dasgsegj",
                "audit_pic6":"dsgkj",
                "audit_result":"False",
                "audit_note":"哈哈，颤抖吧，违法户们",
                "is_opensale":"True",
                "measures":"ORDER",
                "is_holdcertificate":"True",
                "is_opencertificate":"True",
                "is_saleticket":"True",
                "is_saleskyprice":"True",
                "is_potentially_illegal":"True",
                "score":"85"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": 1(该条稽查记录的id),
                "message": "稽查记录信息修改成功"
            }
    """
    params = audit_info_schema(request.json or '')
    audit_id = params.get('audit_id')
    audit = Audit.query.filter(Audit.id == audit_id, Audit.is_delete == 0)
    params.pop('audit_id')
    audit.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '稽查记录信息修改成功')


# 删除稽查信息
@blue_print.route('/delAudit', methods=['POST'])
def delete_audit():
    """
        @api {POST} api/task/delAudit  删除稽查信息
        @apiVersion 0.0.1
        @apiName delAudit
        @apiGroup task
        @apiDescription 删除稽查信息
        @apiParam {int}  audit_id     (必须)    稽查记录id
        @apiParamExample {json} Request-Example:
            {
                "audit_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "稽查信息删除成功"
            }
    """
    params = del_audit_schema(request.json or '')
    audit_id = params.get('audit_id')
    is_delete = 1
    audit = Audit.query.filter(Audit.id == audit_id, Audit.is_delete == 0).first()
    audit.is_delete = is_delete
    audit.save()
    return common_response(SysStatus.SUCCESS, audit.is_delete, '稽查信息删除成功')

# 根据店铺id获取稽查记录信息--有藏匿图
@blue_print.route('/getAuditInfoByStoreidwithHidePicture', methods=['POST'])
def get_audit_info_by_storeid_with_HidePicture():
    """
            @api {POST} api/task/getAuditInfoByStoreidwithHidePicture 根据店铺id获取稽查记录信息--有藏匿图
            @apiVersion 0.0.1
            @apiName getAuditInfoByStoreidwithHidePicture
            @apiGroup task
            @apiDescription 根据店铺id获取稽查记录信息，此接口使用了分页功能，因为是post方法，page参数通过表单形式提交
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
                            "store_name": "金华市婺城区周根花便利店",
                            "inspector_id": 4,
                            "user_name": "专卖城区二所稽查员张飞",
                            "audit_date": "2020-05-20",
                            "audit_pic1": "2451245",
                            "audit_pic2": "14586",
                            "audit_pic3": "akdkjgdksgk",
                            "audit_pic4": "sdgjg",
                            "audit_pic5": "dasgsegj",
                            "audit_pic6": "dsgkj",
                            "audit_result": false,
                            "audit_note": "哈哈，颤抖吧，违法户们",
                            "is_opensale": true,
                            "measures": {
                                "ORDER": "责令整改"
                            },
                            "is_holdcertificate": true,
                            "is_opencertificate": true,
                            "is_saleticket": true,
                            "is_saleskyprice": true,
                            "is_potentially_illegal": true,
                            "score": "85.00"
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
    """
    params = auditinfo_by_store_id_with_hidepicture_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(Audit).join(Store, User).filter(Audit.store_id == store_id,HidePicture.audit_id == Audit.id, Audit.is_delete == 0,
                                                                  User.id == Audit.inspector_id).with_entities(
        Audit.id,
        Audit.store_id,
        Store.store_name,
        Audit.inspector_id,
        User.user_name,
        Audit.audit_date,
        Audit.audit_pic1,
        Audit.audit_pic2,
        Audit.audit_pic3,
        Audit.audit_pic4,
        Audit.audit_pic5,
        Audit.audit_pic6,
        Audit.audit_result,
        Audit.audit_note,
        Audit.is_opensale,
        Audit.measures,
        Audit.is_holdcertificate,
        Audit.is_opencertificate,
        Audit.is_saleticket,
        Audit.is_saleskyprice,
        Audit.is_potentially_illegal,
        Audit.score
    ).order_by(desc(Audit.id)).paginate(page, per_page=per_page, error_out=False)
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

# 根据店铺id获取稽查记录信息
@blue_print.route('/getAuditInfoByStoreid', methods=['POST'])
def get_audit_info_by_storeid():
    """
            @api {POST} api/task/getAuditInfoByStoreid 根据店铺id获取稽查记录信息
            @apiVersion 0.0.1
            @apiName getAuditInfoByStoreid
            @apiGroup task
            @apiDescription 根据店铺id获取稽查记录信息，此接口使用了分页功能，因为是post方法，page参数通过表单形式提交
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
                            "store_name": "金华市婺城区周根花便利店",
                            "inspector_id": 4,
                            "user_name": "专卖城区二所稽查员张飞",
                            "audit_date": "2020-05-20",
                            "audit_pic1": "2451245",
                            "audit_pic2": "14586",
                            "audit_pic3": "akdkjgdksgk",
                            "audit_pic4": "sdgjg",
                            "audit_pic5": "dasgsegj",
                            "audit_pic6": "dsgkj",
                            "audit_result": false,
                            "audit_note": "哈哈，颤抖吧，违法户们",
                            "is_opensale": true,
                            "measures": {
                                "ORDER": "责令整改"
                            },
                            "is_holdcertificate": true,
                            "is_opencertificate": true,
                            "is_saleticket": true,
                            "is_saleskyprice": true,
                            "is_potentially_illegal": true,
                            "score": "85.00"
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
    """
    params = auditinfo_by_store_id_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = db.session.query(Audit).join(Store, User).filter(Audit.store_id == store_id, Audit.is_delete == 0,
                                                                  User.id == Audit.inspector_id).with_entities(
        Audit.id,
        Audit.store_id,
        Store.store_name,
        Audit.inspector_id,
        User.user_name,
        Audit.audit_date,
        Audit.audit_pic1,
        Audit.audit_pic2,
        Audit.audit_pic3,
        Audit.audit_pic4,
        Audit.audit_pic5,
        Audit.audit_pic6,
        Audit.audit_result,
        Audit.audit_note,
        Audit.is_opensale,
        Audit.measures,
        Audit.is_holdcertificate,
        Audit.is_opencertificate,
        Audit.is_saleticket,
        Audit.is_saleskyprice,
        Audit.is_potentially_illegal,
        Audit.score
    ).order_by(desc(Audit.id)).paginate(page, per_page=per_page, error_out=False)
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


# 藏匿图表部分
# 添加藏匿图
@blue_print.route('/addHidePictur', methods=['POST'])
def add_hide_picture():
    """
        @api {post} api/task/addHidePictur  添加藏匿图
        @apiVersion 0.0.1
        @apiName addHidePictur
        @apiGroup task
        @apiDescription 添加藏匿图
        @apiParam {int}  store_id    (必须)    零售户id
        @apiParam {int}  audit_id    (必须)    稽查记录id
        @apiParam {String}  picture    (必须)    藏匿图
        @apiParam {String}  graffiti    (必须)    涂鸦
        @apiParam {string}  note    (可选)    标记点文字备注
        @apiParamExample {json} Request-Example:
            {
                "store_id":5,
                "audit_id":1,
                "picture":"djglajegjssjgksjg",
                "graffiti":"djglagsggsgsgs",
                "note":"藏钱地方在......"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": 1,
                "message": "藏匿图添加成功"
            }

    """
    params = add_hidepicture_schema(request.json or '')
    store_id = params.get('store_id')
    audit_id = params.get('audit_id')
    picture = params.get('picture')
    graffiti = params.get('graffiti')
    note = params.get('note')
    hidepicure = HidePicture(store_id=store_id, audit_id=audit_id, picture=picture, note=note, graffiti=graffiti)
    db.session.add(hidepicure)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, hidepicure.id, '藏匿图添加成功')


# 通过稽查记录id获取藏匿图信息
@blue_print.route('/getHidepictureInfoByauditid', methods=['POST'])
def get_hidepicture_info_by_audit_id():
    """
            @api {POST} api/task/getHidepictureInfoByauditid 通过稽查记录id获取藏匿图信息
            @apiVersion 0.0.1
            @apiName getHidepictureInfoByauditid
            @apiGroup task
            @apiDescription 通过稽查记录id获取藏匿图信息
            @apiParam {int}  audit_id     (必须)    稽查记录id
            @apiParamExample {json} Request-Example:
                {
                    "audit_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 1,
                            "store_id": 5,
                            "audit_id": 1,
                            "graffiti": "djglagsggsgsgs",
                            "picture": "djglajegjssjgksjg",
                            "note": "藏钱地方在......"
                        }
                    ],
                    "message": " "
                }
    """
    params = hidepicureinfo_by_auditid_schema(request.json or '')
    audit_id = params.get('audit_id')
    data = HidePicture.query.filter(HidePicture.audit_id == audit_id, HidePicture.is_delete == 0).with_entities(
        HidePicture.id,
        HidePicture.store_id,
        HidePicture.audit_id,
        HidePicture.graffiti,
        HidePicture.picture,
        HidePicture.note
    ).order_by(desc(HidePicture.id)).limit(3).all()
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 通过零售商户id获取藏匿图信息
@blue_print.route('/getHidePictureInfoByStoreid', methods=['POST'])
def get_hide_picture_info_by_store_id():
    """
            @api {POST} api/task/getHidePictureInfoByStoreid 通过零售商户id获取藏匿图信息
            @apiVersion 0.0.1
            @apiName getHidePictureInfoByStoreid
            @apiGroup task
            @apiDescription 通过零售商户id获取藏匿图信息
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
                                "audit_id": 1,
                                "picture": "djglajegjssjgksjg",
                                "graffiti": "djglagsggsgsgs",
                                "note": "藏钱地方在......"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = hidepicureinfo_by_storeid_schema(request.json or '')
    store_id = params.get('store_id')
    page = params.get('page')
    per_page = params.get('per_page')
    pagination = HidePicture.query.filter(HidePicture.store_id == store_id, HidePicture.is_delete == 0).with_entities(
        HidePicture.id,
        HidePicture.store_id,
        HidePicture.audit_id,
        HidePicture.picture,
        HidePicture.graffiti,
        HidePicture.note
    ).order_by(desc(HidePicture.id)).paginate(page, per_page=per_page, error_out=False)
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


# 修改藏匿图信息
@blue_print.route('/modifyHidepictureInfo', methods=['POST'])
def hidepicture_modify():
    """
        @api {post} api/task/modifyHidepictureInfo  修改藏匿图信息
        @apiVersion 0.0.1
        @apiName modifyHidepictureInfo
        @apiGroup task
        @apiDescription 修改藏匿图信息
        @apiParam {int}  hidepicture_id    (必须)    藏匿图id
        @apiParam {int}  store_id    (可选)    零售户id
        @apiParam {int}  audit_id    (可选)    稽查记录id
        @apiParam {String}  picture    (可选)    藏匿图
        @apiParam {String}  graffiti    (可选)    涂鸦
        @apiParam {string}  note    (可选)    标记点文字备注
        @apiParamExample {json} Request-Example:
            {
                "hidepicture_id":1,
                "store_id":5,
                "audit_id":1,
                "picture":"17.145",
                "graffiti":"sgghskg",
                "note":"藏烟的地方在床下"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "藏匿图信息修改成功"
            }
    """
    params = hidepicure_info_schema(request.json or '')
    hidepicture_id = params.get('hidepicture_id')
    hidepicture = HidePicture.query.filter(HidePicture.id == hidepicture_id, HidePicture.is_delete == 0)
    params.pop('hidepicture_id')
    hidepicture.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '藏匿图信息修改成功')


# 删除藏匿图信息
@blue_print.route('/delHidePicture', methods=['POST'])
def delete_hidepicture():
    """
        @api {POST} api/task/delHidePicture  删除藏匿图信息
        @apiVersion 0.0.1
        @apiName delHidePicture
        @apiGroup task
        @apiDescription 删除藏匿图信息
        @apiParam {int}  hidepicture_id     (必须)    藏匿图id
        @apiParamExample {json} Request-Example:
            {
                "hidepicture_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "藏匿图信息删除成功"
            }
    """
    params = del_hidepicure_schema(request.json or '')
    hidepicture_id = params.get('hidepicture_id')
    is_delete = 1
    hidepicture = HidePicture.query.filter(HidePicture.id == hidepicture_id, HidePicture.is_delete == 0).first()
    hidepicture.is_delete = is_delete
    hidepicture.save()
    return common_response(SysStatus.SUCCESS, hidepicture.is_delete, '藏匿图信息删除成功')
