#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, session
import pymysql
from api.extensions import db
import decimal
from sqlalchemy import desc, and_
from api import db
import datetime
import calendar
from api.models.task import Audit
from api.models.forecast import Forecast, Warning, ModelEnum, Forecast_store
from api.models.store_Info import Store, PersonInfo
from api.schemas.forecast import statistic_schema, forecast_result_schema, forecast_warning_params_schema, \
    warning_params_schema, forecast_store_schema
from api.serializer.store import forecast_ser
from api.views.base import common_response, SysStatus, get_this_monday

blue_print = Blueprint('forecast', __name__, url_prefix='/api/forecast')


# 测试接口，获取规则和综合模型预测结果
@blue_print.route('/getForecastResult', methods=['GET'])
def get_forecast_result():
    forecast_result = {
        "forecast_result": {
            "rule_result": {
                "TOP": [{
                    "store_name": "金华市婺城区绿茵副食品店",
                    "person_name": "胡桂云",
                    "administrative": "BENJI",
                    "longitude": 119.66,
                    "latitude": 29.09,
                    "phone": "15236542658",
                    "address": "金华市婺城区义乌街151号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }, {
                    "store_name": "金华市婺城区紫月烟酒行",
                    "person_name": "郑丽华",
                    "administrative": "BENJI",
                    "longitude": 119.656189,
                    "latitude": 29.083574,
                    "phone": "82458264",
                    "address": "金华市婺城区李渔路紫东苑16幢02A",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }],
                "MIDDLE": [{
                    "store_name": "金华市婺城区文丽烟店",
                    "person_name": "高文丽",
                    "administrative": "BENJI",
                    "longitude": 119.687161,
                    "latitude": 29.08443,
                    "phone": "15355894148",
                    "address": "金华市婺城区宾虹路439弄2幢",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }, {
                    "store_name": "金华市婺城区戚记烟酒店",
                    "person_name": "戚海清",
                    "administrative": "BENJI",
                    "longitude": 119.607786,
                    "latitude": 29.08961,
                    "phone": "15267308916",
                    "address": "金华市婺城区亚峰路华夏营业房10-1号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }],
                "LOW": [{
                    "store_name": "金华市婺城区沈美香副食店",
                    "person_name": "沈美香",
                    "administrative": "BENJI",
                    "longitude": 119.639419,
                    "latitude": 29.087638,
                    "phone": "15325891963",
                    "address": "金华市婺城区中村社区中南巷10幢3单元102室",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }]
            },
            "comprehensive_result": {
                "TOP": [{
                    "store_name": "金华市婺城区徐设波副食便利店",
                    "person_name": "徐设波",
                    "administrative": "BENJI",
                    "longitude": 119.66,
                    "latitude": 29.11,
                    "phone": "13735714658",
                    "address": "金华市婺城区亚峰路113号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }, {
                    "store_name": "金华市婺城区开怀副食品商店",
                    "person_name": "郑开怀",
                    "administrative": "BENJI",
                    "longitude": 119.665189,
                    "latitude": 29.083274,
                    "phone": "13065955982",
                    "address": "金华市婺城区中村路76号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }],
                "MIDDLE": [{
                    "store_name": "金华市婺城区慧琦副食品店",
                    "person_name": "周锦盛",
                    "administrative": "BENJI",
                    "longitude": 119.56,
                    "latitude": 29.07,
                    "phone": "15236542658",
                    "address": "金华市婺城区碧云路206号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }, {
                    "store_name": "金华市婺城区金法良副食便利店",
                    "person_name": "金法良",
                    "administrative": "BENJI",
                    "longitude": 119.59,
                    "latitude": 29.09,
                    "phone": "13738982819",
                    "address": "金华市婺城区景品路16号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }],
                "LOW": [{
                    "store_name": "金华市婺城区王文娟副食便利店",
                    "person_name": "王文娟",
                    "administrative": "BENJI",
                    "longitude": 119.90,
                    "latitude": 29.09,
                    "phone": "18857904790",
                    "address": "金华市婺城区江南街道金钱寺社区明星路32号",
                    "case_name": "未在当地进货",
                    "forecast_date": "2020-3-26 ",
                    "result": "违法"
                }]
            },
        }
    }
    # json_form = json.dumps(json_dic)
    return common_response(SysStatus.SUCCESS, forecast_result, '成功')


# 查询预警等级参数
@blue_print.route('/getWarningParams', methods=['POST'])
def get_warning_params():
    """
           @api {post} /api/forecast/getWarningParams  查询预警等级参数
           @apiVersion 0.0.1
           @apiName Warning_params
           @apiGroup forecast
           @apiDescription 查询预警等级参数
           @apiParam {enum}  model_warning_params     (必须)    查询模型(RULE or BP)
           @apiParamExample {json} Request-Example:
               {
                     "model_warning_params":"RULE"
               }
           @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                   "data": {
                       "param1": "0.30",
                       "param2": "0.60",
                       "param3": "0.80"
                   },
                  "message": "预警等级参数查询成功"
               }
           @apiParamExample {json} Request-Example:
               {
                     "model_warning_params":"BP"
               }
           @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                   "data": {
                        "param1": "0.60",
                        "param2": null,
                       "param3": null
                   },
                  "message": "预警等级参数查询成功"
               }
    """
    mode = forecast_warning_params_schema(request.json)
    mode = mode.get('model_warning_params')
    params = Warning.query.filter(Warning.mode == mode).with_entities(Warning.warning_param1,
                                                                      Warning.warning_param2,
                                                                      Warning.warning_param3).first()
    param1 = params.warning_param1
    param2 = params.warning_param2
    param3 = params.warning_param3
    data = {"param1": param1, "param2": param2, "param3": param3}
    if data:
        return common_response(SysStatus.SUCCESS, data, '预警等级参数查询成功')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 修改预警等级参数
@blue_print.route('/modifyWarningParams', methods=['POST'])
def modify_warning_params():
    """
        @api {post} api/forecast/modifyWarningParams   修改预警等级参数
        @apiVersion 0.0.1
        @apiName modify_warning_params
        @apiGroup forecast
        @apiDescription 修改预警等级参数
        @apiParam {enum}  model_warning_params     (必须)    模型(RULE or BP)
        @apiParam {number}  param1    (可选)    预警参数1(必须两位精度，两位小数，大于0且小于1)
        @apiParam {number}  param2     (可选)    预警参数2(必须两位精度，两位小数，大于0且小于1)
        @apiParam {number}  param3     (可选)    预警参数3(必须两位精度，两位小数，大于0且小于1)
        @apiParamExample {json} Request-Example:
             {
                     "model_warning_params":"RULE",
                     "param1":"0.30",
                     "param2":"0.60",
                     "param3":"0.80"
             }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "模型预警参数修改成功"
            }
    """
    data = warning_params_schema(request.json or '')
    mode = data.get('model_warning_params')
    param1 = data.get('param1')
    param2 = data.get('param2')
    param3 = data.get('param3')
    waring = Warning.query.filter(Warning.mode == mode).first()
    waring.warning_param1 = param1
    waring.warning_param2 = param2
    waring.warning_param3 = param3
    waring.save()
    return common_response(SysStatus.SUCCESS, None, '模型预警参数修改成功')


# 查询规则模型或者综合模型预测结果
@blue_print.route('/getForecastResultByModel', methods=['POST'])
def get_forecast_result_by_model():
    """
         @api {POST} api/forecast/getForecastResultByModel 查询规则模型或者综合模型预测结果
         @apiVersion 0.0.1
         @apiName getForecastResultByModel
         @apiGroup forecast
         @apiDescription 查询规则模型或者综合模型预测结果 注意： 为了达到实时更改预警参数就能实时查询预测结果，
         所以接口里进行预测结果的重新筛选，不用forecast_store表里的预测结果。如果预警参数修改，则forecast_store表里保存的预测结果有一周时间延迟。
         @apiParam {enum}  forecast_model     (必须)    预测模型
         @apiParamExample {json} Request-Example:
         {
                  "forecast_model":"Rule" (or "Comprehensive"(综合模型）)
         }
         @apiSuccessExample {json} Success-Response:
             {
                 ""sys_status": "SUCCESS",
                 "data": {
                     "TOP": [
                        {
                            "id": 7,
                            "store_name": "金华市婺城区开怀副食品商店",
                           "name": "郑开怀",
                           "phone": "13065955982",
                           "administrative": {
                                 "BENJI": "本级"
                           },
                           "longitude": "119.66",
                          "latitude": "29.09",
                          "address": "金华市婺城区中村路76号",
                          "forecast_date": "2020-03-23",
                          "result": "0.89"
                        },
                        {
                           "id": 6,
                           "store_name": "金华市婺城区徐设波副食便利店",
                           "name": "徐设波",
                           "phone": "13735714658",
                           "administrative": {
                              "BENJI": "本级"
                           },
                           "longitude": "119.66",
                           "latitude": "29.10",
                           "address": "金华市婺城区亚峰路113号",
                           "forecast_date": "2020-03-23",
                           "result": "0.85"
                        },
                        {
                          "id": 2,
                          ...同上
                        },
                        {
                          "id": 1,
                           ...同上
                        }
                     ],
                     "MIDDLE": [
                       {
                          "id": 10,
                          "store_name": "金华市婺城区王文娟副食便利店",
                          "name": "王文娟",
                          "phone": "13357056183",
                          "administrative": {
                               "BENJI": "本级"
                         },
                          "longitude": "119.66",
                          "latitude": "29.09",
                          "address": "金华市婺城区江南街道金钱寺社区明星路32号",
                          "forecast_date": "2020-03-23",
                          "result": "0.75"
                       },
                       {
                          "id": 9,
                          ...同上
                       },
                       {
                         "id": 8,
                         ...同上
                       },
                       {
                        "id": 3,
                         ...同上
                       }
                    ],
                   "LOW": [
                      {
                        "id": 11,
                        "store_name": "金华市婺城区金松烟酒店",
                        "name": "钱金松",
                        "phone": "15925758598",
                        "administrative": {
                            "BENJI": "本级"
                        },
                         "longitude": "119.65",
                         "latitude": "29.09",
                         "address": "金华市婺城区江南街道中村路127弄35号",
                         "forecast_date": "2020-03-23",
                         "result": "0.45"
                      },
                      {
                         "id": 4,
                           ...同上
                      }
                   ]
                 },
                "message": "规则模型预测结果查询成功"
                综合模型预测结果同上，不再赘述
             }
    """
    # 为了达到实时更改预警参数就能实时查询预测结果，所以接口里进行预测结果的重新筛选，不用forecast_store表里的预测结果。
    this_monday = get_this_monday()

    # 预警参数表查规则预警等级参数
    params = Warning.query.filter(Warning.mode == "RULE").with_entities(Warning.warning_param1,
                                                                        Warning.warning_param2,
                                                                        Warning.warning_param3).first()
    param1 = params.warning_param1
    param2 = params.warning_param2
    param3 = params.warning_param3

    # forecast表查bp预测违法零售户id列表bp_store_id
    bp_store_id = []
    bp_illegal = Forecast.query.filter(Forecast.result == 1, Forecast.mode == ModelEnum.BP,
                                       Forecast.forecast_date == this_monday) \
        .with_entities(Forecast.store_id).all()
    for bp in bp_illegal:
        bp_store_id.append(bp[0])
    # print(bp_store_id)

    # forecast表查svm预测违法零售户id列表svm_store_id
    svm_store_id = []
    svm_illegal = Forecast.query.filter(Forecast.result == 1, Forecast.mode == ModelEnum.SVM,
                                        Forecast.forecast_date == this_monday) \
        .with_entities(Forecast.store_id).all()
    for svm in svm_illegal:
        svm_store_id.append(svm[0])
    # print(svm_store_id)

    # forecast表查规则预测高中低危零售户id列表top_rule、middle_rule、low_rule
    top_rule = []
    middle_rule = []
    low_rule = []
    rule_illegal = Forecast.query.filter(Forecast.mode == ModelEnum.RULE, Forecast.result > param1,
                                         Forecast.forecast_date == this_monday) \
        .with_entities(Forecast.store_id, Forecast.result).all()
    for ru in rule_illegal:
        store_id = ru[0]
        rule_result = float(ru[1])
        if rule_result >= param3:
            top_rule.append(store_id)
        elif rule_result > param2:
            middle_rule.append(store_id)
        else:
            low_rule.append(store_id)

    # 根据综合模型的高中低危判断规则得到最终零售户id列表top_all、middle_all、low_all
    top_all = []
    middle_all = []
    low_all = []
    for r in top_rule:
        if r not in bp_store_id and r not in svm_store_id:
            middle_all.append(r)
        else:
            top_all.append(r)
    for m in middle_rule:
        if m not in bp_store_id and m not in svm_store_id:
            low_all.append(m)
        else:
            middle_all.append(m)
    for l in low_rule:
        low_all.append(l)

    # 规则预测结果查询,根据零售户id从三个表里join查store_name、person_name、administrative、longitude、latitude、phone、address、forecast_date、result
    top_rule_data = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
        .join(Forecast, Forecast.store_id == Store.id) \
        .filter(Store.id.in_(top_rule), Forecast.forecast_date == get_this_monday(), Forecast.mode == ModelEnum.RULE) \
        .with_entities(*forecast_ser).order_by(Store.id).all()
    middle_rule_data = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
        .join(Forecast, Forecast.store_id == Store.id) \
        .filter(Store.id.in_(middle_rule), Forecast.forecast_date == get_this_monday(), Forecast.mode == ModelEnum.RULE) \
        .with_entities(*forecast_ser).order_by(Store.id).all()
    low__rule_data = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
        .join(Forecast, Forecast.store_id == Store.id) \
        .filter(Store.id.in_(low_rule), Forecast.forecast_date == get_this_monday(), Forecast.mode == ModelEnum.RULE) \
        .with_entities(*forecast_ser).order_by(Store.id).all()

    # 综合预测结果查询,根据零售户id从三个表里join查store_name、person_name、administrative、longitude、latitude、phone、address、forecast_date、result
    top_data = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
        .join(Forecast, Forecast.store_id == Store.id) \
        .filter(Store.id.in_(top_all), Forecast.forecast_date == get_this_monday(), Forecast.mode == ModelEnum.RULE) \
        .with_entities(*forecast_ser).order_by(Store.id).all()
    middle_data = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
        .join(Forecast, Forecast.store_id == Store.id) \
        .filter(Store.id.in_(middle_all), Forecast.forecast_date == get_this_monday(), Forecast.mode == ModelEnum.RULE) \
        .with_entities(*forecast_ser).order_by(Store.id).all()
    low_data = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
        .join(Forecast, Forecast.store_id == Store.id) \
        .filter(Store.id.in_(low_all), Forecast.forecast_date == get_this_monday(), Forecast.mode == ModelEnum.RULE) \
        .with_entities(*forecast_ser).order_by(Store.id).all()

    # 根据前端传回的forecast_model返回对应的查询结果
    model = forecast_result_schema(request.json)
    model = model.get('forecast_model')
    if model == "Rule":
        rule_result = {"TOP": top_rule_data, "MIDDLE": middle_rule_data, "LOW": low__rule_data}
        return common_response(SysStatus.SUCCESS, rule_result, '规则模型预测结果查询成功')
    elif model == "Comprehensive":
        comprehensive_result = {"TOP": top_data, "MIDDLE": middle_data, "LOW": low_data}
        return common_response(SysStatus.SUCCESS, comprehensive_result, '综合模型预测结果查询成功')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据角色权限查询规则模型或者综合模型预测结果
# 1管理员查询所有零售户
# 2局长和5稽查大队长查询本局零售户
# 3所长和4稽查员查询本所零售户预测结果
@blue_print.route('/getForecastStore', methods=['POST'])
def get_forecast_store():
    """
            @api {POST} api/forecast/getForecastStore 根据角色权限查询规则模型或者综合模型预测结果（新）
            @apiVersion 0.0.1
            @apiName getForecastStore
            @apiGroup forecast
            @apiDescription 根据角色权限查询规则模型或者综合模型预测结果（新）
            @apiParam {enum}  mode     (必须)    预测模型
            @apiParam {number}  role_id    (必须)    当前登陆用户角色id
            @apiParam {number}  station_id     (必须)    当前登陆用户局id
            @apiParam {number}  department_id     (可选)   当前登陆用户所id
            @apiParamExample {json} Request-Example:
            {
                     "mode":"Rule" ，(or "Comprehensive"(综合模型）)
                     “role_id”：“2”，
                     “station_id”：“1”
            }
            @apiSuccessExample {json} Success-Response:
                {
                    ""sys_status": "SUCCESS",
                    "data": {
                      类似旧接口，不再赘述
                    },
                   "message": "规则模型预测结果查询成功"
                }
       """
    this_monday = get_this_monday()
    today = datetime.date.today()
    params = forecast_store_schema(request.json or '')
    role_id = params.get('role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    mode = params.get('mode')
    # date = params.get('date')
# 1金华局长查询八区所有零售户
    if role_id == 2 and station_id == 1:
        forecast_store = Store.query.join(Forecast_store, Forecast_store.forecast_store_id == Store.id) \
                    .join(PersonInfo, Store.person_id == PersonInfo.id) \
                    .filter(Forecast_store.forecast_mode == mode, and_(Forecast_store.forecast_date >= this_monday, Forecast_store.forecast_date <= today))\
                    .with_entities(
                Store.id,
                Store.store_name,
                PersonInfo.name,
                Store.phone,
                Store.administrative,
                Store.longitude,
                Store.latitude,
                Store.address,
                Forecast_store.created_at,
                Forecast_store.forecast_result,
        ).order_by(Store.id).all()

# 2小局长和5稽查大队长查询本局零售户
    elif role_id == 2 or role_id == 5:
        # departids = Department.query.filter(Department.station_id == station_id).with_entities(Department.id)
        # print(type(departids))
        forecast_store = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
                    .join(Forecast_store, Forecast_store.forecast_store_id == Store.id) \
                    .filter(Forecast_store.forecast_mode == mode,Forecast_store.station_id == station_id, and_(Forecast_store.forecast_date >= this_monday,Forecast_store.forecast_date <= today))\
            .with_entities(
                Store.id,
                Store.store_name,
                PersonInfo.name,
                Store.phone,
                Store.administrative,
                Store.longitude,
                Store.latitude,
                Store.address,
                Forecast_store.created_at,
                Forecast_store.forecast_result,
        ).order_by(Store.id).all()
# 3所长和4稽查员查询本所零售户预测结果
    elif role_id == 3 or role_id == 4:
        forecast_store = Store.query.join(PersonInfo, Store.person_id == PersonInfo.id) \
            .join(Forecast_store, Forecast_store.forecast_store_id == Store.id) \
            .filter(Forecast_store.forecast_mode == mode, Forecast_store.station_id == station_id, Forecast_store.department_id == department_id, and_(Forecast_store.forecast_date >= this_monday,Forecast_store.forecast_date <= today)) \
            .with_entities(
            Store.id,
            Store.store_name,
            PersonInfo.name,
            Store.phone,
            Store.administrative,
            Store.longitude,
            Store.latitude,
            Store.address,
            Forecast_store.created_at,
            Forecast_store.forecast_result,
        ).order_by(Store.id).all()
    count = len(forecast_store)
    print(count)
    if count > 0:
        return common_response(SysStatus.SUCCESS, forecast_store, '预测结果查询成功')
    elif count == 0:
        return common_response(SysStatus.SUCCESS, forecast_store, '无查询结果')
    else:
        return common_response(SysStatus.FAIL, None, '查询 失败')



# 得到预测到的零售户店铺数量、实际违法店铺数量、重叠数量
def compute_count(month, start_date, end_date):
    # rule预测出的零售户
    forecast_store_rule = Forecast_store.query.filter(Forecast_store.forecast_mode == "rule",
                                                      and_(Forecast_store.created_at >= start_date,
                                                           Forecast_store.created_at <= end_date)).with_entities(
        Forecast_store.forecast_store_id)
    # print(forecast_store_rule)
    # 综合模型预测出的零售户
    forecast_store_comprehensive = Forecast_store.query.filter(Forecast_store.forecast_mode == "comprehensive",
                                                               and_(Forecast_store.created_at >= start_date,
                                                                    Forecast_store.created_at <= end_date)).with_entities(
        Forecast_store.forecast_store_id)
    # 查货的零售户
    real_store = Audit.query.filter(Audit.audit_result == 1, and_(Audit.audit_date >= start_date,
                                                                  Audit.audit_date <= end_date)).with_entities(
        Audit.store_id)

    # 去除rule与综合模型预测出的重叠零售户得到最终forecast_store
    forecast_store = forecast_store_rule
    for fsc in forecast_store_comprehensive:
        for fsr in forecast_store_rule:
            if fsc[0] == fsr[0]:
                break
        if fsc[0] != fsr[0]:
            forecast_store.append(fsc)

    forecast_store_rule_count = forecast_store_rule.count()  # rule预测出的零售户数量
    forecast_store_comprehensive_count = forecast_store_comprehensive.count()  # 综合模型预测出的零售户数量
    real_store_count = real_store.count()  # 查货的零售户数量
    forecast_store_count = forecast_store.count()  # 预测出的零售户数量
    overlap_count = 0
    for rs in real_store:
        for fs in forecast_store:
            if rs[0] == fs[0]:
                overlap_count += 1

    # rule_count = 0   #rule重叠数
    # comprehensive_count = 0   #综合模型重叠数
    # for rs in real_store:
    #     for fsr in forecast_store_rule:
    #         if rs[0] == fsr[0]:
    #             rule_count += 1
    #     for fsm in forecast_store_comprehensive:
    #         if rs[0] == fsm[0]:
    #             comprehensive_count +=1

    # 预测零售户数
    # print("fsrc:",forecast_store_rule_count)
    # print(forecast_store_comprehensive_count)
    # print(forecast_store_count)
    # 真实违法零售户数
    # print(real_store_count)
    # 重叠数
    # print(rule_count)
    # print(comprehensive_count)
    # print(overlap_count)
    # 根据前端传回的forecast_model返回对应的查询结果

    # if mode == "rule":
    #     rule_result = {"forecast_store": forecast_store_rule_count, "real_store": real_store_count, "overlap": rule_count}
    #     return common_response(SysStatus.SUCCESS, rule_result, '规则模型预测结果查询成功')
    # elif mode == "Comprehensive":
    #     comprehensive_result = {"forecast_store": forecast_store_comprehensive_count, "real_store": real_store_count, "overlap": comprehensive_count}
    #     return common_response(SysStatus.SUCCESS, comprehensive_result, '综合模型预测结果查询成功')
    # else:
    #     return common_response(SysStatus.FAIL, None, '无查询结果')
    if forecast_store_count == 0:
        return {"month": month, "forecast_store": 0, "real_store": real_store_count, "overlap": 0}
    else:
        result = {"month": month, "forecast_store": forecast_store_count, "real_store": real_store_count,
                  "overlap": overlap_count}
        return result


@blue_print.route('/getForecastStatistic', methods=['POST'])
def get_forecast_statistic():
    # 当天日期
    date_today = datetime.date.today()
    # 当月一号
    date_month_start = datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
    print(date_month_start)
    # 月份比对
    date_month = datetime.date.today().month

    mode_rule = "rule"
    mode_comprehensive = "comprehensive"
    params = statistic_schema(request.json or '')
    start_year = params.get('start_year')
    start_month = params.get('start_month')
    end_year = params.get('end_year')
    end_month = params.get('end_month')
    list = []

    # month_dayrange = (calendar.monthrange(datetime.date.today().year, month))[1]
    # print(month_dayrange)

    # 判断年月计算预测数，真实数，重叠数
    if start_year == 0 or end_month == 0 or start_month == 0 or end_month == 0:
        return common_response(SysStatus.FAIL, None, '请先选择一个正确的日期范围！')
    else:
        if start_year == end_year:
            if start_month == end_month:
                month_dayrange = (calendar.monthrange(start_year, start_month))[1]
                start_date = datetime.date(start_year, start_month, 1)
                end_date = datetime.date(start_year, start_month, month_dayrange)
                month = str(start_date.year) + "." + str(start_month)
                d = compute_count(month, start_date, end_date)
                list.append(d)
                return common_response(SysStatus.SUCCESS, list, '预测结果查询成功')
            elif start_month < end_month:
                for m in (range(start_month, end_month + 1)):
                    month_dayrange = (calendar.monthrange(start_year, m))[1]
                    start_date = datetime.date(start_year, m, 1)
                    end_date = datetime.date(start_year, m, month_dayrange)
                    month = str(start_date.year) + "." + str(m)
                    d = compute_count(month, start_date, end_date)
                    list.append(d)
                return common_response(SysStatus.SUCCESS, list, '预测结果查询成功')
            else:
                return common_response(SysStatus.FAIL, None, '请确保起始月份大于终止月份！')
        elif start_year < end_year:
            for y in range(start_year, end_year + 1):
                if y == start_year:
                    for m in range(start_month, 13):
                        month_dayrange = (calendar.monthrange(start_year, m))[1]
                        start_date = datetime.date(start_year, m, 1)
                        end_date = datetime.date(start_year, m, month_dayrange)
                        month = str(y) + "." + str(m)
                        d = compute_count(month, start_date, end_date)
                        list.append(d)
                elif y == end_year:
                    for m in range(1, end_month + 1):
                        month_dayrange = (calendar.monthrange(end_year, m))[1]
                        start_date = datetime.date(end_year, m, 1)
                        end_date = datetime.date(end_year, m, month_dayrange)
                        month = str(y) + "." + str(m)
                        d = compute_count(month, start_date, end_date)
                        list.append(d)
                else:
                    for m in range(1, 13):
                        month_dayrange = (calendar.monthrange(y, m))[1]
                        start_date = datetime.date(y, m, 1)
                        end_date = datetime.date(y, m, month_dayrange)
                        month = str(y) + "." + str(m)
                        d = compute_count(month, start_date, end_date)
                        list.append(d)
            return common_response(SysStatus.SUCCESS, list, '预测结果查询成功')
        else:
            return common_response(SysStatus.FAIL, None, '请确保起始年份大于终止年份！')
