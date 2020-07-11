#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api import db
from api.models.rule import PredictRule, RuleData
from api.schemas.rule import modify_rule_schema, del_rule_schema, add_rule_schema, highrisk_store,search_rule
from api.schemas.store import storeinfo_by_storeid_schema
from api.serializer.store import rule_score_ser
from api.views.base import common_response, SysStatus

blue_print = Blueprint('rule', __name__, url_prefix='/api/rule')


# 修改预警规则
@blue_print.route('/modifyRuleInfo', methods=['POST'])
def rule_modify():
    """
        @api {post} api/rule/modifyRuleInfo  修改预警规则
        @apiVersion 0.0.1
        @apiName rule_modify
        @apiGroup rule
        @apiDescription 修改预警规则
        @apiParam {int}  rule_id     (必须)    规则id
        @apiParam {tinyint}  is_delete      (可选)    是否删除
        @apiParam {String}  rule_name    (可选)    规则名称
        @apiParam {int}  parameter1    (可选)    参数一
        @apiParam {int}  parameter2    (可选)    参数二
        @apiParam {int}  parameter3    (可选)    参数三
        @apiParam {int}  parameter4  (可选)    参数四
        @apiParam {int}  score1    (可选)    分数一
        @apiParam {int}  score2    (可选)    分数二
        @apiParam {int}  score3    (可选)    分数三
        @apiParam {int}  score4    (可选)    分数四
        @apiParam {String}  describe_rule    (可选)    预警参数描述
        @apiParam {date}  modifydate    (可选)    修改日期
        @apiParamExample {json} Request-Example:
            {
                "score1":5,
                "rule_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "规则修改成功"
            }
    """
    params = modify_rule_schema(request.json or '')
    rule_id = params.get('rule_id')
    rule = PredictRule.query.filter(PredictRule.id == rule_id)
    params.pop('rule_id')
    rule.update(params)
    db.session.commit()
    return common_response(SysStatus.SUCCESS, None, '规则修改成功')

# 停用规则
@blue_print.route('/delRule', methods=['POST'])
def delete_rule():
    """
        @api {POST} api/rule/delRule  停用规则
        @apiVersion 0.0.1
        @apiName delete_rule
        @apiGroup rule
        @apiDescription 停用规则
        @apiParam {String}  rule_name      (必须)    规则名称
        @apiParam {int}  rule_id     (必须)    规则id
        @apiParamExample {json} Request-Example:
            {
                "rule_name":"person_nativeplace",
                "rule_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "规则停用成功"
            }
    """
    params = del_rule_schema(request.json or '')
    rule_name = params.get('rule_name')
    rule_id = params.get('rule_id')
    is_delete = 1
    rule = PredictRule.query.filter(PredictRule.id == rule_id, PredictRule.rule_name == rule_name).first()
    rule.is_delete = is_delete
    rule.save()
    return common_response(SysStatus.SUCCESS, rule.is_delete, '规则停用成功')

# 启用规则
@blue_print.route('/staRule', methods=['POST'])
def start_rule():
    """
        @api {POST} api/rule/staRule  启用规则
        @apiVersion 0.0.1
        @apiName start_rule
        @apiGroup rule
        @apiDescription 启用规则
        @apiParam {String}  rule_name      (必须)    规则名称
        @apiParam {int}  rule_id     (必须)    规则id
        @apiParamExample {json} Request-Example:
            {
                "rule_name":"person_nativeplace",
                "rule_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "规则启用成功"
            }
    """
    params = add_rule_schema(request.json or '')
    rule_name = params.get('rule_name')
    rule_id = params.get('rule_id')
    is_delete = 0
    rule = PredictRule.query.filter(PredictRule.id == rule_id, PredictRule.rule_name == rule_name).first()
    rule.is_delete = is_delete
    rule.save()
    return common_response(SysStatus.SUCCESS, rule.is_delete, '规则启用成功')


# 计算高危用户的分数构成
@blue_print.route('/getHighRiskStore', methods=['POST'])
def get_HighRiskStore():
    """
            @api {POST} api/rule/getHighRiskStore 根据零售户id查询分数构成及预测案由
            @apiVersion 0.0.1
            @apiName getHighriskStore
            @apiGroup rule
            @apiDescription 根据零售户id查询分数构成及预测案由
            @apiParam {int}  store_id     (必须)    经营户id
            @apiParamExample {json} Request-Example:
                {
                    "store_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    第一行是零售户id，
                    依次40个规则得分，
                    最后一行为预测案由
                }
    """
    params = highrisk_store(request.json or '')
    store_id = params.get('store_id')
    engine = create_engine("mysql+mysqldb://ycj:@Ycj2020@127.0.0.1:3306/ycj0527", max_overflow=5)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(PredictRule.is_delete,PredictRule.parameter1,PredictRule.parameter2,PredictRule.parameter3,
                        PredictRule.parameter4,PredictRule.score1,PredictRule.score2,PredictRule.score3,PredictRule.score4).all()
    # 规则的启停标识
    qt1 = res[0][0]
    qt2 = res[1][0]
    qt3 = res[2][0]
    qt4 = res[3][0]
    qt5 = res[4][0]
    qt6 = res[5][0]
    qt7 = res[6][0]
    qt8 = res[7][0]
    qt9 = res[8][0]
    qt10 = res[9][0]
    qt11 = res[10][0]
    qt12 = res[11][0]
    qt13 = res[12][0]
    qt14 = res[13][0]
    qt15 = res[14][0]
    qt16 = res[15][0]
    qt17 = res[16][0]
    qt18 = res[17][0]
    qt19 = res[18][0]
    qt20 = res[19][0]
    qt21 = res[20][0]
    qt22 = res[21][0]
    qt23 = res[22][0]
    qt24 = res[23][0]
    qt25 = res[24][0]
    qt26 = res[25][0]
    qt27 = res[26][0]
    qt28 = res[27][0]
    qt29 = res[28][0]
    qt30 = res[29][0]
    qt31 = res[30][0]
    qt32 = res[31][0]
    qt33 = res[32][0]
    qt34 = res[33][0]
    qt35 = res[34][0]
    qt36 = res[35][0]
    qt37 = res[36][0]
    qt38 = res[37][0]
    qt39 = res[38][0]

    hostHometownSensitive = res[0][4]  # 主要负责经营人籍贯敏感
    score_hostHometownSensitive = res[0][5]
    other1HometownSensitive = res[1][4]  # 其他经营人1籍贯敏感
    score_other1HometownSensitive = res[1][5]
    other2HometownSensitive = res[2][4]  # 其他经营人2籍贯敏感
    score_other2HometownSensitive = res[2][5]
    bigIllegal = res[3][4]  # 是否为违法大户
    score_bigIllegal = res[3][5]
    downShift = res[4][4]  # 降档降级情况
    score_downShift = res[4][5]
    highMonth = res[5][1]
    midMonth = res[5][2]
    lowMonth = res[5][3]
    score_highMonth = res[5][5]
    score_midMonth = res[5][6]
    score_lowMonth = res[5][7]
    senDistrict = res[6][4]  # 行政敏感区
    score_senDistrict = res[6][5]
    isCriPenalties = res[7][4]  # 有无刑事处罚
    score_isCriPenalties = res[7][5]
    isIllegalWithinThePastSixMonths = res[8][4]  # 近半年内是否有违法记录
    score_isIllegalWithinThePastSixMonths = res[8][5]
    shamSmoking = res[9][4]  # 涉假冒烟
    score_shamSmoking = res[9][5]
    smugglingCigarettes = res[10][4]  # 涉走私烟
    score_smugglingCigarettes = res[10][5]
    feiCigarettes = res[11][4]  # 涉非流烟
    score_feiCigarettes = res[11][5]
    logisticsAssociation = res[12][4]  # 物流关联
    score_logisticsAssociation = res[12][5]
    isLinkedAccount = res[13][4]  # 车辆关联
    score_isLinkedAccount = res[13][5]

    C1NumberOfUnlTobMonShipments = res[14][1]  # 无证运输烟草专卖品次数参数1
    C2NumberOfUnlTobMonShipments = res[14][2]  # 无证运输烟草专卖品次数参数2
    C3NumberOfUnlTobMonShipments = res[14][3]  # 无证运输烟草专卖品次数参数3
    score_C1NumberOfUnlTobMonShipments = res[14][5]
    score_C2NumberOfUnlTobMonShipments = res[14][6]
    score_C3NumberOfUnlTobMonShipments = res[14][7]
    score_C4NumberOfUnlTobMonShipments = res[14][8]

    T1NumberOfUnlTobMonShipments = res[15][1]  # 无证运输烟草专卖品条数
    T2NumberOfUnlTobMonShipments = res[15][2]  # 无证运输烟草专卖品条数
    T3NumberOfUnlTobMonShipments = res[15][3]  # 无证运输烟草专卖品条数
    score_T1NumberOfUnlTobMonShipments = res[15][5]
    score_T2NumberOfUnlTobMonShipments = res[15][6]
    score_T3NumberOfUnlTobMonShipments = res[15][7]
    score_T4NumberOfUnlTobMonShipments = res[15][8]

    J1NumberOfUnlTobMonShipments = res[16][1]  # 无证运输烟草专卖品金额参数1
    J2NumberOfUnlTobMonShipments = res[16][2]  # 无证运输烟草专卖品金额参数2
    J3NumberOfUnlTobMonShipments = res[16][3]  # 无证运输烟草专卖品金额参数3
    score_J1NumberOfUnlTobMonShipments = res[16][5]
    score_J2NumberOfUnlTobMonShipments = res[16][6]
    score_J3NumberOfUnlTobMonShipments = res[16][7]
    score_J4NumberOfUnlTobMonShipments = res[16][8]

    C1NumberOfLocalPurchases = res[17][1]  # 未在当地进货次数参数1
    C2NumberOfLocalPurchases = res[17][2]  # 未在当地进货次数参数2
    C3NumberOfLocalPurchases = res[17][3]  # 未在当地进货次数参数3
    score_C1NumberOfLocalPurchases = res[17][5]
    score_C2NumberOfLocalPurchases = res[17][6]
    score_C3NumberOfLocalPurchases = res[17][7]
    score_C4NumberOfLocalPurchases = res[17][8]

    T1NumberOfLocalPurchases = res[18][1]  # 未在当地进货条数参数1
    T2NumberOfLocalPurchases = res[18][2]  # 未在当地进货条数参数2
    T3NumberOfLocalPurchases = res[18][3]  # 未在当地进货条数参数3
    score_T1NumberOfLocalPurchases = res[18][5]
    score_T2NumberOfLocalPurchases = res[18][6]
    score_T3NumberOfLocalPurchases = res[18][7]
    score_T4NumberOfLocalPurchases = res[18][8]

    J1NumberOfLocalPurchases = res[19][1]  # 未在当地进货金额参数1
    J2NumberOfLocalPurchases = res[19][2]  # 未在当地进货金额参数2
    J3NumberOfLocalPurchases = res[19][3]  # 未在当地进货金额参数3
    score_J1NumberOfLocalPurchases = res[19][5]
    score_J2NumberOfLocalPurchases = res[19][6]
    score_J3NumberOfLocalPurchases = res[19][7]
    score_J4NumberOfLocalPurchases = res[19][8]

    C1NumberOfMonSalOfUllProTobacco = res[20][1]  # 销售非法生产的烟草专卖次数参数1
    C2NumberOfMonSalOfUllProTobacco = res[20][2]  # 销售非法生产的烟草专卖次数参数2
    C3NumberOfMonSalOfUllProTobacco = res[20][3]  # 销售非法生产的烟草专卖次数参数3
    score_C1NumberOfMonSalOfUllProTobacco = res[20][5]
    score_C2NumberOfMonSalOfUllProTobacco = res[20][6]
    score_C3NumberOfMonSalOfUllProTobacco = res[20][7]
    score_C4NumberOfMonSalOfUllProTobacco = res[20][8]

    T1NumberOfMonSalOfUllProTobacco = res[21][1]  # 销售非法生产的烟草专卖条数参数1
    T2NumberOfMonSalOfUllProTobacco = res[21][2]  # 销售非法生产的烟草专卖条数参数2
    T3NumberOfMonSalOfUllProTobacco = res[21][3]  # 销售非法生产的烟草专卖条数参数3
    score_T1NumberOfMonSalOfUllProTobacco = res[21][5]
    score_T2NumberOfMonSalOfUllProTobacco = res[21][6]
    score_T3NumberOfMonSalOfUllProTobacco = res[21][7]
    score_T4NumberOfMonSalOfUllProTobacco = res[21][8]

    J1NumberOfMonSalOfUllProTobacco = res[22][1]  # 销售非法生产的烟草专卖金额参数1
    J2NumberOfMonSalOfUllProTobacco = res[22][2]  # 销售非法生产的烟草专卖金额参数2
    J3NumberOfMonSalOfUllProTobacco = res[22][3]  # 销售非法生产的烟草专卖金额参数3
    score_J1NumberOfMonSalOfUllProTobacco = res[22][5]
    score_J2NumberOfMonSalOfUllProTobacco = res[22][6]
    score_J3NumberOfMonSalOfUllProTobacco = res[22][7]
    score_J4NumberOfMonSalOfUllProTobacco = res[22][8]

    C1NumberOfTobPermitMail = res[23][1]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数参数1
    C2NumberOfTobPermitMail = res[23][2]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数参数2
    C3NumberOfTobPermitMail = res[23][3]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数参数3
    score_C1NumberOfTobPermitMail = res[23][5]
    score_C2NumberOfTobPermitMail = res[23][6]
    score_C3NumberOfTobPermitMail = res[23][7]
    score_C4NumberOfTobPermitMail = res[23][8]

    T1NumberOfTobPermitMail = res[24][1]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数参数1
    T2NumberOfTobPermitMail = res[24][2]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数参数2
    T3NumberOfTobPermitMail = res[24][3]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数参数3
    score_T1NumberOfTobPermitMail = res[24][5]
    score_T2NumberOfTobPermitMail = res[24][6]
    score_T3NumberOfTobPermitMail = res[24][7]
    score_T4NumberOfTobPermitMail = res[24][8]

    J1NumberOfTobPermitMail = res[25][1]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额参数1
    J2NumberOfTobPermitMail = res[25][2]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额参数2
    J3NumberOfTobPermitMail = res[25][3]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额参数3
    score_J1NumberOfTobPermitMail = res[25][5]
    score_J2NumberOfTobPermitMail = res[25][6]
    score_J3NumberOfTobPermitMail = res[25][7]
    score_J4NumberOfTobPermitMail = res[25][8]

    C1NumberOfUnmForCigSold = res[26][1]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数参数1
    C2NumberOfUnmForCigSold = res[26][2]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数参数2
    C3NumberOfUnmForCigSold = res[26][3]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数参数3
    score_C1NumberOfUnmForCigSold = res[26][5]
    score_C2NumberOfUnmForCigSold = res[26][6]
    score_C3NumberOfUnmForCigSold = res[26][7]
    score_C4NumberOfUnmForCigSold = res[26][8]

    T1NumberOfUnmForCigSold = res[27][1]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数参数1
    T2NumberOfUnmForCigSold = res[27][2]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数参数2
    T3NumberOfUnmForCigSold = res[27][3]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数参数3
    score_T1NumberOfUnmForCigSold = res[27][5]
    score_T2NumberOfUnmForCigSold = res[27][6]
    score_T3NumberOfUnmForCigSold = res[27][7]
    score_T4NumberOfUnmForCigSold = res[27][8]

    J1NumberOfUnmForCigSold = res[28][1]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额参数1
    J2NumberOfUnmForCigSold = res[28][2]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额参数2
    J3NumberOfUnmForCigSold = res[28][3]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额参数3
    score_J1NumberOfUnmForCigSold = res[28][5]
    score_J2NumberOfUnmForCigSold = res[28][6]
    score_J3NumberOfUnmForCigSold = res[28][7]
    score_J4NumberOfUnmForCigSold = res[28][8]

    C1NumberOfTobMonTraWitTobMonPermit = res[29][1]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数参数1
    C2NumberOfTobMonTraWitTobMonPermit = res[29][2]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数参数2
    C3NumberOfTobMonTraWitTobMonPermit = res[29][3]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数参数3
    score_C1NumberOfTobMonTraWitTobMonPermit = res[29][5]
    score_C2NumberOfTobMonTraWitTobMonPermit = res[29][6]
    score_C3NumberOfTobMonTraWitTobMonPermit = res[29][7]
    score_C4NumberOfTobMonTraWitTobMonPermit = res[29][8]

    T1NumberOfTobMonTraWitTobMonPermit = res[30][1]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数参数1
    T2NumberOfTobMonTraWitTobMonPermit = res[30][2]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数参数2
    T3NumberOfTobMonTraWitTobMonPermit = res[30][3]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数参数3
    score_T1NumberOfTobMonTraWitTobMonPermit = res[30][5]
    score_T2NumberOfTobMonTraWitTobMonPermit = res[30][6]
    score_T3NumberOfTobMonTraWitTobMonPermit = res[30][7]
    score_T4NumberOfTobMonTraWitTobMonPermit = res[30][8]

    J1NumberOfTobMonTraWitTobMonPermit = res[31][1]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额参数1
    J2NumberOfTobMonTraWitTobMonPermit = res[31][2]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额参数2
    J3NumberOfTobMonTraWitTobMonPermit = res[31][3]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额参数3
    score_J1NumberOfTobMonTraWitTobMonPermit = res[31][5]
    score_J2NumberOfTobMonTraWitTobMonPermit = res[31][6]
    score_J3NumberOfTobMonTraWitTobMonPermit = res[31][7]
    score_J4NumberOfTobMonTraWitTobMonPermit = res[31][8]

    t1heNumberTwoYears = res[32][1]  # 近两年历史违法次数参数1
    t2heNumberTwoYears = res[32][2]  # 近两年历史违法次数参数2
    t3heNumberTwoYears = res[32][3]  # 近两年历史违法次数参数3
    score_t1heNumberTwoYears = res[32][5]
    score_t2heNumberTwoYears = res[32][6]
    score_t3heNumberTwoYears = res[32][7]
    score_t4heNumberTwoYears = res[32][8]

    C1OutOfProvince = res[33][1]  # 近一年码段外流情况（省内外流）次数参数1
    C2OutOfProvince = res[33][2]  # 近一年码段外流情况（省内外流）次数参数2
    C3OutOfProvince = res[33][3]  # 近一年码段外流情况（省内外流）次数参数3
    score_C1OutOfProvince = res[33][5]
    score_C2OutOfProvince = res[33][6]
    score_C3OutOfProvince = res[33][7]
    score_C4OutOfProvince = res[33][8]

    T1OutOfProvince = res[34][1]  # 近一年码段外流情况（省内外流）条数参数1
    T2OutOfProvince = res[34][2]  # 近一年码段外流情况（省内外流）条数参数2
    T3OutOfProvince = res[34][3]  # 近一年码段外流情况（省内外流）条数参数3
    score_T1OutOfProvince = res[34][5]
    score_T2OutOfProvince = res[34][6]
    score_T3OutOfProvince = res[34][7]
    score_T4OutOfProvince = res[34][8]

    J1OutOfProvince = res[35][1]  # 近一年码段外流情况（省内外流）金额参数1
    J2OutOfProvince = res[35][2]  # 近一年码段外流情况（省内外流）金额参数2
    J3OutOfProvince = res[35][3]  # 近一年码段外流情况（省内外流）金额参数3
    score_J1OutOfProvince = res[35][5]
    score_J2OutOfProvince = res[35][6]
    score_J3OutOfProvince = res[35][7]
    score_J4OutOfProvince = res[35][8]

    C1ProvinceOut = res[36][1]  # 近一年码段外流情况（外流省外）次数参数1
    C2ProvinceOut = res[36][2]  # 近一年码段外流情况（外流省外）次数参数2
    C3ProvinceOut = res[36][3]  # 近一年码段外流情况（外流省外）次数参数3
    score_C1ProvinceOut = res[36][5]
    score_C2ProvinceOut = res[36][6]
    score_C3ProvinceOut = res[36][7]
    score_C4ProvinceOut = res[36][8]

    T1ProvinceOut = res[37][1]  # 近一年码段外流情况（外流省外）条数参数1
    T2ProvinceOut = res[37][2]  # 近一年码段外流情况（外流省外）条数参数2
    T3ProvinceOut = res[37][3]  # 近一年码段外流情况（外流省外）条数参数3
    score_T1ProvinceOut = res[37][5]
    score_T2ProvinceOut = res[37][6]
    score_T3ProvinceOut = res[37][7]
    score_T4ProvinceOut = res[37][8]

    J1ProvinceOut = res[38][1]  # 近一年码段外流情况（外流省外）金额参数1
    J2ProvinceOut = res[38][2]  # 近一年码段外流情况（外流省外）金额参数2
    J3ProvinceOut = res[38][3]  # 近一年码段外流情况（外流省外）金额参数3
    score_J1ProvinceOut = res[38][5]
    score_J2ProvinceOut = res[38][6]
    score_J3ProvinceOut = res[38][7]
    score_J4ProvinceOut = res[38][8]

    # 规则模块计算
    scoreone = 0
    scoretwo = 0
    scorethree = 0
    scorefour = 0
    scorefive = 0
    scoresix = 0
    scoreseven = 0
    scoreeight = 0
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0
    score6 = 0
    score7 = 0
    score8 = 0
    score9 = 0
    score10 = 0
    score11 = 0
    score12 = 0
    score13 = 0
    score14 = 0
    score15 = 0
    score16 = 0
    score17 = 0
    score18 = 0
    score19 = 0
    score20 = 0
    score21 = 0
    score22 = 0
    score23 = 0
    score24 = 0
    score25 = 0
    score26 = 0
    score27 = 0
    score28 = 0
    score29 = 0
    score30 = 0
    score31 = 0
    score32 = 0
    score33 = 0
    score34 = 0
    score35 = 0
    score36 = 0
    score37 = 0
    score38 = 0
    score39 = 0
    res = session.query(RuleData.person_nativeplace,RuleData.person01_nativeplace,RuleData.person02_nativeplace,
                        RuleData.is_bigillegal,RuleData.is_downgrade,RuleData.month,RuleData.canton_id,
                        RuleData.is_criminal,RuleData.is_illegal,RuleData.cigar_property_jia,RuleData.cigar_property_zou,
                        RuleData.cigar_property_fei,RuleData.logistics,RuleData.car,
                         RuleData.unlicensed_transport_times,RuleData.unlicensed_transport_num,
                         RuleData.unlicensed_transport_price,RuleData.purchase_illegcigar_times,
                         RuleData.purchase_illegcigar_num,RuleData.purchase_illegcigar_price,
                         RuleData.sell_illegcigar_times,RuleData.sell_illegcigar_num,RuleData.sell_illegcigar_price,
                         RuleData.over_postcigar_times,RuleData.over_postcigar_num,RuleData.over_postcigar_price,
                         RuleData.sell_abroadcigar_times, RuleData.sell_abroadcigar_num, RuleData.sell_abroadcigar_price,
                         RuleData.helpothers_transport_times,RuleData.helpothers_transport_num,
                         RuleData.helpothers_transport_price,RuleData.in_province_times,RuleData.in_province_num,
                        RuleData.twoyear_illegaltimes,
                         RuleData.in_province_price,RuleData.out_of_province_times,RuleData.out_of_province_num,
                         RuleData.out_of_province_price).filter(RuleData.store_id == store_id).all()

    if qt1 == 0:
        # 主要经营人籍贯
        if res[0][0] == hostHometownSensitive:
            score1 = score_hostHometownSensitive
        else:
            score1 = 0
    if qt2 == 0:
        # 其他经营人1籍贯
        if res[0][1] == other1HometownSensitive:
            score2 = score_other1HometownSensitive
        else:
            score2 = 0
    if qt3 == 0:
        # 其他经营人1籍贯
        if res[0][2] == other2HometownSensitive:
            score3 = score_other2HometownSensitive
        else:
            score3 = 0
    if qt4 == 0:
        # 是否为违法大户
        if res[0][3] == bigIllegal:
            score4 = score_bigIllegal
        else:
            score4 = 0
    if qt5 == 0:
        # 是否有降级将档情况
        if res[0][4] == downShift:
            score5 = score_downShift
        else:
            score5 = 0
    if qt6 == 0:
        # 当前月
        if res[0][5] == highMonth:
            score6 = score_highMonth
        elif res[0][5] == midMonth:
            score6 = score_midMonth
        elif res[0][5] == lowMonth:
            score6 = score_lowMonth
        else:
            score6 = 0
    if qt7 == 0:
        # 行政区id
        if res[0][6] == senDistrict:
            score7 = score_senDistrict
        else:
            score7 = 0
    if qt8 == 0:
        # 有无刑事处罚
        if res[0][7] == isCriPenalties:
            score8 = score_isCriPenalties
        else:
            score8 = 0
    if qt9 == 0:
        # 近半年内是否有违法记录
        if res[0][8] == isIllegalWithinThePastSixMonths:
            score9 = score_isIllegalWithinThePastSixMonths
        else:
            score9 = 0
    if qt10 == 0:
        # 是否假冒烟
        if res[0][9] == shamSmoking:
            score10 = score_shamSmoking
        else:
            score10 = 0
    if qt11 == 0:
        # 是否走私烟
        if res[0][10] == smugglingCigarettes:
            score11 = score_smugglingCigarettes
        else:
            score11 = 0
    if qt12 == 0:
        # 是否非流烟
        if res[0][11] == feiCigarettes:
            score12 = score_feiCigarettes
        else:
            score12 = 0
    if qt13 == 0:
        # 物流
        if res[0][12] == logisticsAssociation:
            score13 = score_logisticsAssociation
        else:
            score13 = 0
    if qt14 == 0:
        # 车辆
        if res[0][13] == isLinkedAccount:
            score14 = score_isLinkedAccount
        else:
            score14 = 0
    if qt15 == 0:
        # 无证运输烟草专卖品次数
        if res[0][14] != 0:
            if C1NumberOfUnlTobMonShipments == 0 and C3NumberOfUnlTobMonShipments == 0:
                if 0 <= res[0][14] <= C2NumberOfUnlTobMonShipments:
                    score15 = score_C2NumberOfUnlTobMonShipments
                elif res[0][14] > C2NumberOfUnlTobMonShipments:
                    score15 = score_C3NumberOfUnlTobMonShipments
            if C1NumberOfUnlTobMonShipments != 0 and C3NumberOfUnlTobMonShipments == 0:
                if 0 <= res[0][14] <= C1NumberOfUnlTobMonShipments:
                    score15 = score_C1NumberOfUnlTobMonShipments
                elif C1NumberOfUnlTobMonShipments < res[0][14] <= C2NumberOfUnlTobMonShipments:
                    score15 = score_C2NumberOfUnlTobMonShipments
                elif res[0][14] > C2NumberOfUnlTobMonShipments:
                    score15 = score_C3NumberOfUnlTobMonShipments
            if C1NumberOfUnlTobMonShipments != 0 and C3NumberOfUnlTobMonShipments != 0:
                if 0 <= res[0][14] <= C1NumberOfUnlTobMonShipments:
                    score15 = score_C1NumberOfUnlTobMonShipments
                elif C1NumberOfUnlTobMonShipments < res[0][14] <= C2NumberOfUnlTobMonShipments:
                    score15 = score_C2NumberOfUnlTobMonShipments
                elif C2NumberOfUnlTobMonShipments < res[0][14] <= C3NumberOfUnlTobMonShipments:
                    score15 = score_C3NumberOfUnlTobMonShipments
                elif res[0][14] > C3NumberOfUnlTobMonShipments:
                    score15 = score_C4NumberOfUnlTobMonShipments
    if qt16 == 0:
        # 无证运输烟草专卖品条数
        if res[0][15] != 0:
            if T1NumberOfUnlTobMonShipments == 0 and T3NumberOfUnlTobMonShipments == 0:
                if 0 <= res[0][15] <= T2NumberOfUnlTobMonShipments:
                    score16 = score_T2NumberOfUnlTobMonShipments
                elif res[0][15] > T2NumberOfUnlTobMonShipments:
                    score16 = score_T3NumberOfUnlTobMonShipments
            if T1NumberOfUnlTobMonShipments != 0 and T3NumberOfUnlTobMonShipments == 0:
                if 0 <= res[0][15] <= T1NumberOfUnlTobMonShipments:
                    score16 = score_T1NumberOfUnlTobMonShipments
                elif T1NumberOfUnlTobMonShipments < res[0][15] <= T2NumberOfUnlTobMonShipments:
                    score16 = score_T2NumberOfUnlTobMonShipments
                elif res[0][15] > T2NumberOfUnlTobMonShipments:
                    score16 = score_T3NumberOfUnlTobMonShipments
            if T1NumberOfUnlTobMonShipments != 0 and T3NumberOfUnlTobMonShipments != 0:
                if 0 <= res[0][15] <= T1NumberOfUnlTobMonShipments:
                    score16 = score_T1NumberOfUnlTobMonShipments
                elif T1NumberOfUnlTobMonShipments < res[0][15] <= T2NumberOfUnlTobMonShipments:
                    score16 = score_T2NumberOfUnlTobMonShipments
                elif T2NumberOfUnlTobMonShipments < res[0][15] <= T3NumberOfUnlTobMonShipments:
                    score16 = score_T3NumberOfUnlTobMonShipments
                elif res[0][15] > T3NumberOfUnlTobMonShipments:
                    score16 = score_T4NumberOfUnlTobMonShipments
    if qt17 == 0:
        # 无证运输烟草专卖品金额
        if res[0][16] != 0:
            if J1NumberOfUnlTobMonShipments == 0 and J3NumberOfUnlTobMonShipments == 0:
                if 0 <= res[0][16] <= J2NumberOfUnlTobMonShipments:
                    score17 = score_J2NumberOfUnlTobMonShipments
                elif res[0][16] > J2NumberOfUnlTobMonShipments:
                    score17 = score_J3NumberOfUnlTobMonShipments
            if J1NumberOfUnlTobMonShipments != 0 and J3NumberOfUnlTobMonShipments == 0:
                if 0 <= res[0][16] <= J1NumberOfUnlTobMonShipments:
                    score17 = score_J1NumberOfUnlTobMonShipments
                elif J1NumberOfUnlTobMonShipments < res[0][16] <= J2NumberOfUnlTobMonShipments:
                    score17 = score_J2NumberOfUnlTobMonShipments
                elif res[0][16] > J2NumberOfUnlTobMonShipments:
                    score17 = score_J3NumberOfUnlTobMonShipments
            if J1NumberOfUnlTobMonShipments != 0 and J3NumberOfUnlTobMonShipments != 0:
                if 0 <= res[0][16] <= J1NumberOfUnlTobMonShipments:
                    score17 = score_J1NumberOfUnlTobMonShipments
                elif J1NumberOfUnlTobMonShipments < res[0][16] <= J2NumberOfUnlTobMonShipments:
                    score17 = score_J2NumberOfUnlTobMonShipments
                elif J2NumberOfUnlTobMonShipments < res[0][16] <= J3NumberOfUnlTobMonShipments:
                    score17 = score_J3NumberOfUnlTobMonShipments
                elif res[0][16] > J3NumberOfUnlTobMonShipments:
                    score17 = score_J4NumberOfUnlTobMonShipments
    if qt18 == 0:
        # 未在当地进货次数
        if res[0][17] != 0:
            if C1NumberOfLocalPurchases == 0 and C3NumberOfLocalPurchases == 0:
                if 0 <= res[0][17] < C2NumberOfLocalPurchases:
                    score18 = score_C2NumberOfLocalPurchases
                elif res[0][17] >= C2NumberOfLocalPurchases:
                    score18 = score_C3NumberOfLocalPurchases
            if C1NumberOfLocalPurchases != 0 and C3NumberOfLocalPurchases == 0:
                if 0 <= res[0][17] < C1NumberOfLocalPurchases:
                    score18 = score_C1NumberOfLocalPurchases
                elif C1NumberOfLocalPurchases <= res[0][17] < C2NumberOfLocalPurchases:
                    score18 = score_C2NumberOfLocalPurchases
                elif res[0][17] >= C2NumberOfLocalPurchases:
                    score18 = score_C3NumberOfLocalPurchases
            if C1NumberOfLocalPurchases != 0 and C3NumberOfLocalPurchases != 0:
                if 0 <= res[0][17] < C1NumberOfLocalPurchases:
                    score18 = score_C1NumberOfLocalPurchases
                elif C1NumberOfLocalPurchases <= res[0][17] < C2NumberOfLocalPurchases:
                    score18 = score_C2NumberOfLocalPurchases
                elif C2NumberOfLocalPurchases <= res[0][17] < C3NumberOfLocalPurchases:
                    score18 = score_C3NumberOfLocalPurchases
                elif res[0][17] >= C3NumberOfLocalPurchases:
                    score18 = score_C4NumberOfLocalPurchases
    if qt19 == 0:
        # 未在当地进货条数
        if res[0][18] != 0:
            if T1NumberOfLocalPurchases == 0 and T3NumberOfLocalPurchases == 0:
                if 0 <= res[0][18] < T2NumberOfLocalPurchases:
                    score19 = score_T2NumberOfLocalPurchases
                elif res[0][18] >= T2NumberOfLocalPurchases:
                    score19 = score_T3NumberOfLocalPurchases
            if T1NumberOfLocalPurchases != 0 and T3NumberOfLocalPurchases == 0:
                if 0 <= res[0][18] < T1NumberOfLocalPurchases:
                    score19 = score_T1NumberOfLocalPurchases
                elif T1NumberOfLocalPurchases <= res[0][18] < T2NumberOfLocalPurchases:
                    score19 = score_T2NumberOfLocalPurchases
                elif res[0][18] >= T2NumberOfLocalPurchases:
                    score19 = score_T3NumberOfLocalPurchases
            if T1NumberOfLocalPurchases != 0 and T3NumberOfLocalPurchases != 0:
                if 0 <= res[0][18] < T1NumberOfLocalPurchases:
                    score19 = score_T1NumberOfLocalPurchases
                elif T1NumberOfLocalPurchases <= res[0][18] < T2NumberOfLocalPurchases:
                    score19 = score_T2NumberOfLocalPurchases
                elif T2NumberOfLocalPurchases <= res[0][18] < T3NumberOfLocalPurchases:
                    score19 = score_T3NumberOfLocalPurchases
                elif res[0][18] >= T3NumberOfLocalPurchases:
                    score19 = score_T4NumberOfLocalPurchases
    if qt20 == 0:
        # 未在当地进货金额
        if res[0][19] != 0:
            if J1NumberOfLocalPurchases == 0 and J3NumberOfLocalPurchases == 0:
                if 0 <= res[0][19] < J2NumberOfLocalPurchases:
                    score20 = score_J2NumberOfLocalPurchases
                elif res[0][19] >= J2NumberOfLocalPurchases:
                    score20 = score_J3NumberOfLocalPurchases
            if J1NumberOfLocalPurchases != 0 and J3NumberOfLocalPurchases == 0:
                if 0 <= res[0][19] < J1NumberOfLocalPurchases:
                    score20 = score_J1NumberOfLocalPurchases
                elif J1NumberOfLocalPurchases <= res[0][19] < J2NumberOfLocalPurchases:
                    score20 = score_J2NumberOfLocalPurchases
                elif res[0][19] >= J2NumberOfLocalPurchases:
                    score20 = score_J3NumberOfLocalPurchases
            if J1NumberOfLocalPurchases != 0 and J3NumberOfLocalPurchases != 0:
                if 0 <= res[0][19] < J1NumberOfLocalPurchases:
                    score20 = score_J1NumberOfLocalPurchases
                elif J1NumberOfLocalPurchases <= res[0][19] < J2NumberOfLocalPurchases:
                    score20 = score_J2NumberOfLocalPurchases
                elif J2NumberOfLocalPurchases <= res[0][19] < J3NumberOfLocalPurchases:
                    score20 = score_J3NumberOfLocalPurchases
                elif res[0][19] >= J3NumberOfLocalPurchases:
                    score20 = score_J4NumberOfLocalPurchases
    if qt21 == 0:
        # 销售非法生产的烟草专卖次数
        if res[0][20] != 0:
            if C1NumberOfMonSalOfUllProTobacco == 0 and C3NumberOfMonSalOfUllProTobacco == 0:
                if 0 <= res[0][20] <= C2NumberOfMonSalOfUllProTobacco:
                    score21 = score_C2NumberOfMonSalOfUllProTobacco
                elif res[0][20] > C2NumberOfMonSalOfUllProTobacco:
                    score21 = score_C3NumberOfMonSalOfUllProTobacco
            if C1NumberOfMonSalOfUllProTobacco != 0 and C3NumberOfMonSalOfUllProTobacco == 0:
                if 0 <= res[0][20] <= C1NumberOfMonSalOfUllProTobacco:
                    score21 = score_C1NumberOfMonSalOfUllProTobacco
                elif C1NumberOfMonSalOfUllProTobacco < res[0][20] <= C2NumberOfMonSalOfUllProTobacco:
                    score21 = score_C2NumberOfMonSalOfUllProTobacco
                elif res[0][20] > C2NumberOfMonSalOfUllProTobacco:
                    score21 = score_C3NumberOfMonSalOfUllProTobacco
            if C1NumberOfMonSalOfUllProTobacco != 0 and C3NumberOfMonSalOfUllProTobacco != 0:
                if 0 <= res[0][20] <= C1NumberOfMonSalOfUllProTobacco:
                    score21 = score_C1NumberOfMonSalOfUllProTobacco
                elif C1NumberOfMonSalOfUllProTobacco < res[0][20] <= C2NumberOfMonSalOfUllProTobacco:
                    score21 = score_C2NumberOfMonSalOfUllProTobacco
                elif C2NumberOfMonSalOfUllProTobacco < res[0][20] <= C3NumberOfMonSalOfUllProTobacco:
                    score21 = score_C3NumberOfMonSalOfUllProTobacco
                elif res[0][20] > C3NumberOfMonSalOfUllProTobacco:
                    score21 = score_C4NumberOfMonSalOfUllProTobacco
    if qt22 == 0:
        # 销售非法生产的烟草专卖条数
        if res[0][21] != 0:
            if T1NumberOfMonSalOfUllProTobacco == 0 and T3NumberOfMonSalOfUllProTobacco == 0:
                if 0 <= res[0][21] <= T2NumberOfMonSalOfUllProTobacco:
                    score22 = score_T2NumberOfMonSalOfUllProTobacco
                elif res[0][21] > T2NumberOfMonSalOfUllProTobacco:
                    score22 = score_T3NumberOfMonSalOfUllProTobacco
            if T1NumberOfMonSalOfUllProTobacco != 0 and T3NumberOfMonSalOfUllProTobacco == 0:
                if 0 <= res[0][21] <= T1NumberOfMonSalOfUllProTobacco:
                    score22 = score_T1NumberOfMonSalOfUllProTobacco
                elif T1NumberOfMonSalOfUllProTobacco < res[0][21] <= T2NumberOfMonSalOfUllProTobacco:
                    score22 = score_T2NumberOfMonSalOfUllProTobacco
                elif res[0][21] > T2NumberOfMonSalOfUllProTobacco:
                    score22 = score_T3NumberOfMonSalOfUllProTobacco
            if T1NumberOfMonSalOfUllProTobacco != 0 and T3NumberOfMonSalOfUllProTobacco != 0:
                if 0 <= res[0][21] <= T1NumberOfMonSalOfUllProTobacco:
                    score22 = score_T1NumberOfMonSalOfUllProTobacco
                elif T1NumberOfMonSalOfUllProTobacco < res[0][21] <= T2NumberOfMonSalOfUllProTobacco:
                    score22 = score_T2NumberOfMonSalOfUllProTobacco
                elif T2NumberOfMonSalOfUllProTobacco < res[0][21] <= T3NumberOfMonSalOfUllProTobacco:
                    score22 = score_T3NumberOfMonSalOfUllProTobacco
                elif res[0][21] > T3NumberOfMonSalOfUllProTobacco:
                    score22 = score_T4NumberOfMonSalOfUllProTobacco
    if qt23 == 0:
        # 销售非法生产的烟草专卖金额
        if res[0][22] != 0:
            if J1NumberOfMonSalOfUllProTobacco == 0 and J3NumberOfMonSalOfUllProTobacco == 0:
                if 0 <= res[0][22] <= J2NumberOfMonSalOfUllProTobacco:
                    score23 = score_J2NumberOfMonSalOfUllProTobacco
                elif res[0][22] > J2NumberOfMonSalOfUllProTobacco:
                    score23 = score_J3NumberOfMonSalOfUllProTobacco
            if J1NumberOfMonSalOfUllProTobacco != 0 and J3NumberOfMonSalOfUllProTobacco == 0:
                if 0 <= res[0][22] <= J1NumberOfMonSalOfUllProTobacco:
                    score23 = score_J1NumberOfMonSalOfUllProTobacco
                elif J1NumberOfMonSalOfUllProTobacco < res[0][22] <= J2NumberOfMonSalOfUllProTobacco:
                    score23 = score_J2NumberOfMonSalOfUllProTobacco
                elif res[0][22] > J2NumberOfMonSalOfUllProTobacco:
                    score23 = score_J3NumberOfMonSalOfUllProTobacco
            if J1NumberOfMonSalOfUllProTobacco != 0 and J3NumberOfMonSalOfUllProTobacco != 0:
                if 0 <= res[0][22] <= J1NumberOfMonSalOfUllProTobacco:
                    score23 = score_J1NumberOfMonSalOfUllProTobacco
                elif J1NumberOfMonSalOfUllProTobacco < res[0][22] <= J2NumberOfMonSalOfUllProTobacco:
                    score23 = score_J2NumberOfMonSalOfUllProTobacco
                elif J2NumberOfMonSalOfUllProTobacco < res[0][22] <= J3NumberOfMonSalOfUllProTobacco:
                    score23 = score_J3NumberOfMonSalOfUllProTobacco
                elif res[0][22] > J3NumberOfMonSalOfUllProTobacco:
                    score23 = score_J4NumberOfMonSalOfUllProTobacco
    if qt24 == 0:
        # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数
        if res[0][23] != 0:
            if C1NumberOfTobPermitMail == 0 and C3NumberOfTobPermitMail == 0:
                if 0 <= res[0][23] < C2NumberOfTobPermitMail:
                    score24 = score_C2NumberOfTobPermitMail
                elif res[0][23] >= C2NumberOfTobPermitMail:
                    score24 = score_C3NumberOfTobPermitMail
            if C1NumberOfTobPermitMail != 0 and C3NumberOfTobPermitMail == 0:
                if 0 <= res[0][23] < C1NumberOfTobPermitMail:
                    score24 = score_C1NumberOfTobPermitMail
                elif C1NumberOfTobPermitMail <= res[0][23] < C2NumberOfTobPermitMail:
                    score24 = score_C2NumberOfTobPermitMail
                elif res[0][23] >= C2NumberOfTobPermitMail:
                    score24 = score_C3NumberOfTobPermitMail
            if C1NumberOfTobPermitMail != 0 and C3NumberOfTobPermitMail != 0:
                if 0 <= res[0][23] < C1NumberOfTobPermitMail:
                    score24 = score_C1NumberOfTobPermitMail
                elif C1NumberOfTobPermitMail <= res[0][23] < C2NumberOfTobPermitMail:
                    score24 = score_C2NumberOfTobPermitMail
                elif C2NumberOfTobPermitMail <= res[0][23] < C3NumberOfTobPermitMail:
                    score24 = score_C3NumberOfTobPermitMail
                elif res[0][23] >= C3NumberOfTobPermitMail:
                    score24 = score_C4NumberOfTobPermitMail
    if qt25 == 0:
        # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数
        if res[0][24] != 0:
            if T1NumberOfTobPermitMail == 0 and T3NumberOfTobPermitMail == 0:
                if 0 <= res[0][24] < T2NumberOfTobPermitMail:
                    score25 = score_T2NumberOfTobPermitMail
                elif res[0][24] >= T2NumberOfTobPermitMail:
                    score25 = score_T3NumberOfTobPermitMail
            if T1NumberOfTobPermitMail != 0 and T3NumberOfTobPermitMail == 0:
                if 0 <= res[0][24] < T1NumberOfTobPermitMail:
                    score25 = score_T1NumberOfTobPermitMail
                elif T1NumberOfTobPermitMail <= res[0][24] < T2NumberOfTobPermitMail:
                    score25 = score_T2NumberOfTobPermitMail
                elif res[0][24] >= T2NumberOfTobPermitMail:
                    score25 = score_T3NumberOfTobPermitMail
            if T1NumberOfTobPermitMail != 0 and T3NumberOfTobPermitMail != 0:
                if 0 <= res[0][24] < T1NumberOfTobPermitMail:
                    score25 = score_T1NumberOfTobPermitMail
                elif T1NumberOfTobPermitMail <= res[0][24] < T2NumberOfTobPermitMail:
                    score25 = score_T2NumberOfTobPermitMail
                elif T2NumberOfTobPermitMail <= res[0][24] < T3NumberOfTobPermitMail:
                    score25 = score_T3NumberOfTobPermitMail
                elif res[0][24] >= T3NumberOfTobPermitMail:
                    score25 = score_T4NumberOfTobPermitMail
    if qt26 == 0:
        # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额
        if res[0][25] != 0:
            if J1NumberOfTobPermitMail == 0 and J3NumberOfTobPermitMail == 0:
                if 0 <= res[0][25] <= J2NumberOfTobPermitMail:
                    score26 = score_J2NumberOfTobPermitMail
                elif res[0][25] > J2NumberOfTobPermitMail:
                    score26 = score_J3NumberOfTobPermitMail
            if J1NumberOfTobPermitMail != 0 and J3NumberOfTobPermitMail == 0:
                if 0 <= res[0][25] <= J1NumberOfTobPermitMail:
                    score26 = score_J1NumberOfTobPermitMail
                elif J1NumberOfTobPermitMail < res[0][25] <= J2NumberOfTobPermitMail:
                    score26 = score_J2NumberOfTobPermitMail
                elif res[0][25] > J2NumberOfTobPermitMail:
                    score26 = score_J3NumberOfTobPermitMail
            if J1NumberOfTobPermitMail != 0 and J3NumberOfTobPermitMail != 0:
                if 0 <= res[0][25] <= J1NumberOfTobPermitMail:
                    score26 = score_J1NumberOfTobPermitMail
                elif J1NumberOfTobPermitMail < res[0][25] <= J2NumberOfTobPermitMail:
                    score26 = score_J2NumberOfTobPermitMail
                elif J2NumberOfTobPermitMail < res[0][25] <= J3NumberOfTobPermitMail:
                    score26 = score_J3NumberOfTobPermitMail
                elif res[0][25] > J3NumberOfTobPermitMail:
                    score26 = score_J4NumberOfTobPermitMail
    if qt27 == 0:
        # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数
        if res[0][26] != 0:
            if C1NumberOfUnmForCigSold == 0 and C3NumberOfUnmForCigSold == 0:
                if 0 <= res[0][26] < C2NumberOfUnmForCigSold:
                    score27 = score_C2NumberOfUnmForCigSold
                elif res[0][26] >= C2NumberOfUnmForCigSold:
                    score27 = score_C3NumberOfUnmForCigSold
            if C1NumberOfUnmForCigSold != 0 and C3NumberOfUnmForCigSold == 0:
                if 0 <= res[0][26] < C1NumberOfUnmForCigSold:
                    score27 = score_C1NumberOfUnmForCigSold
                elif C1NumberOfUnmForCigSold <= res[0][26] < C2NumberOfUnmForCigSold:
                    score27 = score_C2NumberOfUnmForCigSold
                elif res[0][26] >= C2NumberOfUnmForCigSold:
                    score27 = score_C3NumberOfUnmForCigSold
            if C1NumberOfUnmForCigSold != 0 and C3NumberOfUnmForCigSold != 0:
                if 0 <= res[0][26] < C1NumberOfUnmForCigSold:
                    score27 = score_C1NumberOfUnmForCigSold
                elif C1NumberOfUnmForCigSold <= res[0][26] < C2NumberOfUnmForCigSold:
                    score27 = score_C2NumberOfUnmForCigSold
                elif C2NumberOfUnmForCigSold <= res[0][26] < C3NumberOfUnmForCigSold:
                    score27 = score_C3NumberOfUnmForCigSold
                elif res[0][26] >= C3NumberOfUnmForCigSold:
                    score27 = score_C4NumberOfUnmForCigSold
    if qt28 == 0:
        # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数
        if res[0][27] != 0:
            if T1NumberOfUnmForCigSold == 0 and T3NumberOfUnmForCigSold == 0:
                if 0 <= res[0][27] < T2NumberOfUnmForCigSold:
                    score28 = score_T2NumberOfUnmForCigSold
                elif res[0][27] >= T2NumberOfUnmForCigSold:
                    score28 = score_T3NumberOfUnmForCigSold
            if T1NumberOfUnmForCigSold != 0 and T3NumberOfUnmForCigSold == 0:
                if 0 <= res[0][27] < T1NumberOfUnmForCigSold:
                    score28 = score_T1NumberOfUnmForCigSold
                elif T1NumberOfUnmForCigSold <= res[0][27] < T2NumberOfUnmForCigSold:
                    score28 = score_T2NumberOfUnmForCigSold
                elif res[0][27] >= T2NumberOfUnmForCigSold:
                    score28 = score_T3NumberOfUnmForCigSold
            if T1NumberOfUnmForCigSold != 0 and T3NumberOfUnmForCigSold != 0:
                if 0 <= res[0][27] < T1NumberOfUnmForCigSold:
                    score28 = score_T1NumberOfUnmForCigSold
                elif T1NumberOfUnmForCigSold <= res[0][27] < T2NumberOfUnmForCigSold:
                    score28 = score_T2NumberOfUnmForCigSold
                elif T2NumberOfUnmForCigSold <= res[0][27] < T3NumberOfUnmForCigSold:
                    score28 = score_T3NumberOfUnmForCigSold
                elif res[0][27] >= T3NumberOfUnmForCigSold:
                    score28 = score_T4NumberOfUnmForCigSold
    if qt29 == 0:
        # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额
        if res[0][28] != 0:
            if J1NumberOfUnmForCigSold == 0 and J3NumberOfUnmForCigSold == 0:
                if 0 <= res[0][28] <= J2NumberOfUnmForCigSold:
                    score29 = score_J2NumberOfUnmForCigSold
                elif res[0][28] > J2NumberOfUnmForCigSold:
                    score29 = score_J3NumberOfUnmForCigSold
            if J1NumberOfUnmForCigSold != 0 and J3NumberOfUnmForCigSold == 0:
                if 0 <= res[0][28] <= J1NumberOfUnmForCigSold:
                    score29 = score_J1NumberOfUnmForCigSold
                elif J1NumberOfUnmForCigSold < res[0][28] <= J2NumberOfUnmForCigSold:
                    score29 = score_J2NumberOfUnmForCigSold
                elif res[0][28] > J2NumberOfUnmForCigSold:
                    score298 = score_J3NumberOfUnmForCigSold
            if J1NumberOfUnmForCigSold != 0 and J3NumberOfUnmForCigSold != 0:
                if 0 <= res[0][28] <= J1NumberOfUnmForCigSold:
                    score29 = score_J1NumberOfUnmForCigSold
                elif J1NumberOfUnmForCigSold < res[0][28] <= J2NumberOfUnmForCigSold:
                    score29 = score_J2NumberOfUnmForCigSold
                elif J2NumberOfUnmForCigSold < res[0][28] <= J3NumberOfUnmForCigSold:
                    score29 = score_J3NumberOfUnmForCigSold
                elif res[0][28] > J3NumberOfUnmForCigSold:
                    score29 = score_J4NumberOfUnmForCigSold
    if qt30 == 0:
        # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数
        if res[0][29] != 0:
            if C1NumberOfTobMonTraWitTobMonPermit == 0 and C3NumberOfTobMonTraWitTobMonPermit == 0:
                if 0 <= res[0][29] < C2NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C2NumberOfTobMonTraWitTobMonPermit
                elif res[0][29] >= C2NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C3NumberOfTobMonTraWitTobMonPermit
            if C1NumberOfTobMonTraWitTobMonPermit != 0 and C3NumberOfTobMonTraWitTobMonPermit == 0:
                if 0 <= res[0][29] < C1NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C1NumberOfTobMonTraWitTobMonPermit
                elif C1NumberOfTobMonTraWitTobMonPermit <= res[0][29] < C2NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C2NumberOfTobMonTraWitTobMonPermit
                elif res[0][29] >= C2NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C3NumberOfTobMonTraWitTobMonPermit
            if C1NumberOfTobMonTraWitTobMonPermit != 0 and C3NumberOfTobMonTraWitTobMonPermit != 0:
                if 0 <= res[0][29] < C1NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C1NumberOfTobMonTraWitTobMonPermit
                elif C1NumberOfTobMonTraWitTobMonPermit <= res[0][29] < C2NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C2NumberOfTobMonTraWitTobMonPermit
                elif C2NumberOfTobMonTraWitTobMonPermit <= res[0][29] < C3NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C3NumberOfTobMonTraWitTobMonPermit
                elif res[0][29] >= C3NumberOfTobMonTraWitTobMonPermit:
                    score30 = score_C4NumberOfTobMonTraWitTobMonPermit
    if qt31 == 0:
        # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数
        if res[0][30] != 0:
            if T1NumberOfTobMonTraWitTobMonPermit == 0 and T3NumberOfTobMonTraWitTobMonPermit == 0:
                if 0 <= res[0][30] < T2NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T2NumberOfTobMonTraWitTobMonPermit
                elif res[0][30] >= T2NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T3NumberOfTobMonTraWitTobMonPermit
            if T1NumberOfTobMonTraWitTobMonPermit != 0 and T3NumberOfTobMonTraWitTobMonPermit == 0:
                if 0 <= res[0][30] < T1NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T1NumberOfTobMonTraWitTobMonPermit
                elif T1NumberOfTobMonTraWitTobMonPermit <= res[0][30] < T2NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T2NumberOfTobMonTraWitTobMonPermit
                elif res[0][30] >= T2NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T3NumberOfTobMonTraWitTobMonPermit
            if T1NumberOfTobMonTraWitTobMonPermit != 0 and T3NumberOfTobMonTraWitTobMonPermit != 0:
                if 0 <= res[0][30] < T1NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T1NumberOfTobMonTraWitTobMonPermit
                elif T1NumberOfTobMonTraWitTobMonPermit <= res[0][30] < T2NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T2NumberOfTobMonTraWitTobMonPermit
                elif T2NumberOfTobMonTraWitTobMonPermit <= res[0][30] < T3NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T3NumberOfTobMonTraWitTobMonPermit
                elif res[0][30] >= T3NumberOfTobMonTraWitTobMonPermit:
                    score31 = score_T4NumberOfTobMonTraWitTobMonPermit
    if qt32 == 0:
        # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额
        if res[0][31] != 0:
            if J1NumberOfTobMonTraWitTobMonPermit == 0 and J3NumberOfTobMonTraWitTobMonPermit == 0:
                if 0 <= res[0][31] <= J2NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J2NumberOfTobMonTraWitTobMonPermit
                elif res[0][31] > J2NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J3NumberOfTobMonTraWitTobMonPermit
            if J1NumberOfTobMonTraWitTobMonPermit != 0 and J3NumberOfTobMonTraWitTobMonPermit == 0:
                if 0 <= res[0][31] <= J1NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J1NumberOfTobMonTraWitTobMonPermit
                elif J1NumberOfTobMonTraWitTobMonPermit < res[0][31] <= J2NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J2NumberOfTobMonTraWitTobMonPermit
                elif res[0][31] > J2NumberOfTobMonTraWitTobMonPermit:
                    score32 += score_J3NumberOfTobMonTraWitTobMonPermit
            if J1NumberOfTobMonTraWitTobMonPermit != 0 and J3NumberOfTobMonTraWitTobMonPermit != 0:
                if 0 <= res[0][31] <= J1NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J1NumberOfTobMonTraWitTobMonPermit
                elif J1NumberOfTobMonTraWitTobMonPermit < res[0][31] <= J2NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J2NumberOfTobMonTraWitTobMonPermit
                elif J2NumberOfTobMonTraWitTobMonPermit < res[0][31] <= J3NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J3NumberOfTobMonTraWitTobMonPermit
                elif res[0][31] > J3NumberOfTobMonTraWitTobMonPermit:
                    score32 = score_J4NumberOfTobMonTraWitTobMonPermit
    if qt33 == 0:
        # 近两年历史违法次数
        if res[0][32] != 0:
            if t1heNumberTwoYears == 0 and t3heNumberTwoYears == 0:
                if 0 <= res[0][32] < t2heNumberTwoYears:
                    score33 = score_t2heNumberTwoYears
                elif res[0][32] >= t2heNumberTwoYears:
                    score33 = score_t3heNumberTwoYears
            if t1heNumberTwoYears != 0 and t3heNumberTwoYears == 0:
                if 0 <= res[0][32] < t1heNumberTwoYears:
                    score33 = score_t1heNumberTwoYears
                elif t1heNumberTwoYears <= res[0][32] < t2heNumberTwoYears:
                    score33 = score_t2heNumberTwoYears
                elif res[0][32] >= t2heNumberTwoYears:
                    score33 = score_t3heNumberTwoYears
            if t1heNumberTwoYears != 0 and t3heNumberTwoYears != 0:
                if 0 <= res[0][32] < t1heNumberTwoYears:
                    score33 = score_t1heNumberTwoYears
                elif t1heNumberTwoYears <= res[0][32] < t2heNumberTwoYears:
                    score33 = score_t2heNumberTwoYears
                elif t2heNumberTwoYears <= res[0][32] < t3heNumberTwoYears:
                    score33 = score_t3heNumberTwoYears
                elif res[0][32] >= T3NumberOfUnmForCigSold:
                    score33 = score_t4heNumberTwoYears
    if qt34 == 0:
        # 近一年码段外流情况（省内外流）次数
        if res[0][33] != 0:
            if C1OutOfProvince == 0 and C2OutOfProvince == 0:
                if 0 <= res[0][33] < C2OutOfProvince:
                    score34 = score_C2OutOfProvince
                elif res[0][33] >= C2OutOfProvince:
                    score34 = score_C3OutOfProvince
            if C1OutOfProvince != 0 and C2OutOfProvince == 0:
                if 0 <= res[0][33] < C1OutOfProvince:
                    score34 = score_C1OutOfProvince
                elif C1OutOfProvince <= res[0][33] < C2OutOfProvince:
                    score34 = score_C2OutOfProvince
                elif res[0][33] >= C2OutOfProvince:
                    score34 = score_C3OutOfProvince
            if C1OutOfProvince != 0 and C3OutOfProvince != 0:
                if 0 <= res[0][33] < C1OutOfProvince:
                    score34 = score_C1OutOfProvince
                elif C1OutOfProvince <= res[0][33] < C2OutOfProvince:
                    score34 = score_C2OutOfProvince
                elif C2OutOfProvince <= res[0][33] < C3OutOfProvince:
                    score34 = score_C3OutOfProvince
                elif res[0][33] >= C3OutOfProvince:
                    score34 = score_C4OutOfProvince

    if qt35 == 0:
        # 近一年码段外流情况（省内外流）条数
        if res[0][34] != 0:
            if T1OutOfProvince == 0 and T3OutOfProvince == 0:
                if 0 <= res[0][34] < T2OutOfProvince:
                    score35 = score_T2OutOfProvince
                elif res[0][34] >= T2OutOfProvince:
                    score35 = score_T3OutOfProvince
            if T1OutOfProvince != 0 and T3OutOfProvince == 0:
                if 0 <= res[0][34] < T1OutOfProvince:
                    score35 = score_T1OutOfProvince
                elif T1OutOfProvince <= res[0][34] < T2OutOfProvince:
                    score35 = score_T2OutOfProvince
                elif res[0][34] >= T2OutOfProvince:
                    score35 = score_T3OutOfProvince
            if T1OutOfProvince != 0 and T3OutOfProvince != 0:
                if 0 <= res[0][34] < T1OutOfProvince:
                    score35 = score_T1OutOfProvince
                elif T1OutOfProvince <= res[0][34] < T2OutOfProvince:
                    score35 = score_T2OutOfProvince
                elif T2OutOfProvince <= res[0][34] < T3OutOfProvince:
                    score35 = score_T3OutOfProvince
                elif res[0][34] >= T3OutOfProvince:
                    score35 = score_T4OutOfProvince
    if qt36 == 0:
        # 近一年码段外流情况（省内外流）金额
        if res[0][35] != 0:
            if J1OutOfProvince == 0 and J3OutOfProvince == 0:
                if 0 <= res[0][35] < J2OutOfProvince:
                    score36 = score_J2OutOfProvince
                elif res[0][35] >= J2OutOfProvince:
                    score36 = score_J3OutOfProvince
            if J1OutOfProvince != 0 and J3OutOfProvince == 0:
                if 0 <= res[0][35] < J1OutOfProvince:
                    score36 = score_J1OutOfProvince
                elif J1OutOfProvince <= res[0][35] < J2OutOfProvince:
                    score36 = score_J2OutOfProvince
                elif res[0][35] >= J2OutOfProvince:
                    score36 = score_J3OutOfProvince
            if J1OutOfProvince != 0 and J3OutOfProvince != 0:
                if 0 <= res[0][35] < J1OutOfProvince:
                    score36 = score_J1OutOfProvince
                elif J1OutOfProvince <= res[0][35] < J2OutOfProvince:
                    score36 = score_J2OutOfProvince
                elif J2OutOfProvince <= res[0][35] < J3OutOfProvince:
                    score36 = score_J3OutOfProvince
                elif res[0][35] >= J3OutOfProvince:
                    score36 = score_J4OutOfProvince
    if qt37 == 0:
        # 近一年码段外流情况（外流省外）次数
        if res[0][36] != 0:
            if C1ProvinceOut == 0 and C3ProvinceOut == 0:
                if 0 <= res[0][36] < C2ProvinceOut:
                    score37 = score_C2ProvinceOut
                elif res[0][36] >= C2ProvinceOut:
                    score37 = score_C3ProvinceOut
            if C1ProvinceOut != 0 and C3ProvinceOut == 0:
                if 0 <= res[0][36] < C1ProvinceOut:
                    score37 = score_C1ProvinceOut
                elif C1ProvinceOut <= res[0][36] < C2ProvinceOut:
                    score37 = score_C2ProvinceOut
                elif res[0][36] >= C2ProvinceOut:
                    score37 = score_C3ProvinceOut
            if C1ProvinceOut != 0 and C3ProvinceOut != 0:
                if 0 <= res[0][36] < C1ProvinceOut:
                    score37 = score_C1ProvinceOut
                elif C1ProvinceOut <= res[0][36] < C2ProvinceOut:
                    score37 = score_C2ProvinceOut
                elif C2ProvinceOut <= res[0][36] < C3ProvinceOut:
                    score37 = score_C3ProvinceOut
                elif res[0][36] >= C3ProvinceOut:
                    score37 = score_C4ProvinceOut
    if qt38 == 0:
        # 近一年码段外流情况（外流省外）条数
        if res[0][37] != 0:
            if T1ProvinceOut == 0 and T3ProvinceOut == 0:
                if 0 <= res[0][37] < T2ProvinceOut:
                    score38 = score_T2ProvinceOut
                elif res[0][37] >= T2ProvinceOut:
                    score38 = score_T3ProvinceOut
            if T1ProvinceOut != 0 and T3ProvinceOut == 0:
                if 0 <= res[0][37] < T1ProvinceOut:
                    score38 = score_T1ProvinceOut
                elif T1ProvinceOut <= res[0][37] < T3ProvinceOut:
                    score38 = score_T2ProvinceOut
                elif res[0][37] >= T2ProvinceOut:
                    score38 = score_T3ProvinceOut
            if T1ProvinceOut != 0 and T3ProvinceOut != 0:
                if 0 <= res[0][37] < T1ProvinceOut:
                    score38 = score_T1ProvinceOut
                elif T1ProvinceOut <= res[0][37] < T2ProvinceOut:
                    score38 = score_T2ProvinceOut
                elif T2ProvinceOut <= res[0][37] < T3ProvinceOut:
                    score38 = score_T3ProvinceOut
                elif res[0][37] >= T3ProvinceOut:
                    score38 = score_T4ProvinceOut
    if qt39 == 0:
        # 近一年码段外流情况（外流省外）金额
        if res[0][38] != 0:
            if J1ProvinceOut == 0 and J3ProvinceOut == 0:
                if 0 <= res[0][38] < J2ProvinceOut:
                    score39 = score_J2ProvinceOut
                elif res[0][38] >= J2ProvinceOut:
                    score39 = score_J3ProvinceOut
            if J1ProvinceOut != 0 and J3ProvinceOut == 0:
                if 0 <= res[0][38] < J1ProvinceOut:
                    score39 = score_J1ProvinceOut
                elif J1ProvinceOut <= res[0][38] < J2ProvinceOut:
                    score39 = score_J2ProvinceOut
                elif res[0][38] >= J2ProvinceOut:
                    score39 = score_J3ProvinceOut
            if J1ProvinceOut != 0 and J3ProvinceOut != 0:
                if 0 <= res[0][38] < J1ProvinceOut:
                    score39 = score_J1ProvinceOut
                elif J1ProvinceOut <= res[0][38] < J2ProvinceOut:
                    score39 = score_J2ProvinceOut
                elif J2ProvinceOut <= res[0][38] < J3ProvinceOut:
                    score39 = score_J3ProvinceOut
                elif res[0][38] >= J3ProvinceOut:
                    score39 = score_J4ProvinceOut
    scoreone = score15 + score16 +score17
    scoretwo = score18 + score19 +score20
    scorethree = score21 + score22 +score23
    scorefour = score24 + score25 +score26
    scorefive = score27 + score28 +score29
    scoresix = score30 + score31 +score32
    scoreseven = score34 + score35 +score36
    scoreeight = score37 + score38 +score39
    score_all =[scoreone,scoretwo,scorethree,scorefour,scorefive,scoresix,scoreseven,scoreeight]
    max=score_all[0]
    for j in range(len(score_all)):
        if score_all[j] > max:
            max = score_all[j]
        if j == 0:
            anyou = "无证运输烟草专卖品"
        elif j == 1:
            anyou = "未在当地进货"
        elif j == 2:
            anyou = "销售非法生产的烟草专卖"
        elif j == 3:
            anyou = "无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定"
        elif j == 4:
            anyou = "销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟"
        elif j == 5:
            anyou = "无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品"
        elif j == 6:
            anyou = "近一年码段外流情况（省内外流）"
        elif j == 7:
            anyou = "近一年码段外流情况（外流省外）"
    data = [
        store_id,
        score1,
        score2,
        score3,
        score4,
        score5,
        score6,
        score7,
        score8,
        score9,
        score10,
        score11,
        score12,
        score13,
        score14,
        score15,
        score16,
        score17,
        score18,
        score19,
        score20,
        score21,
        score22,
        score23,
        score24,
        score25,
        score26,
        score27,
        score28,
        score29,
        score30,
        score31,
        score32,
        score33,
        score34,
        score35,
        score36,
        score37,
        score38,
        score39,
        anyou
    ]
    if data:
        return common_response(SysStatus.SUCCESS, data, '查询成功')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 根据零售户id获取分数构成及预测案由
@blue_print.route('/getRuleScoreByStoreId', methods=['POST'])
def get_rule_score():
    """
            @api {POST} api/rule/getStoreInfoByStoreId 根据零售户id获取分数构成及预测案由
            @apiVersion 0.0.1
            @apiName getStoreInfoByStoreId
            @apiGroup store
            @apiDescription 根据零售户id获取分数构成及预测案由
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
                        }
                    ],
                    "message": " "
                }
    """
    # 获取该零售户规则得分
    params = storeinfo_by_storeid_schema(request.json or '')
    store_id = params.get('store_id')
    score = db.session.query(RuleData).filter(RuleData.store_id == store_id, RuleData.is_delete == 0).with_entities(
        *rule_score_ser).one()
    # 计算八个案由各自总分预测案由
    unlicensed_transport = score.unlicensed_transport_times + score.unlicensed_transport_num + score.unlicensed_transport_price
    purchase_illegcigar = score.purchase_illegcigar_times + score.purchase_illegcigar_num + score.purchase_illegcigar_price
    sell_illegcigar = score.sell_illegcigar_times + score.sell_illegcigar_num + score.sell_illegcigar_price
    over_postcigar = score.over_postcigar_times + score.over_postcigar_num + score.over_postcigar_price
    sell_abroadcigar = score.sell_abroadcigar_times + score.sell_abroadcigar_num + score.sell_abroadcigar_price
    helpothers_transport = score.helpothers_transport_times + score.helpothers_transport_num + score.helpothers_transport_price
    in_province = score.in_province_times + score.in_province_num + score.in_province_price
    out_of_province = score.out_of_province_times + score.out_of_province_num + score.out_of_province_price
    case_score = [unlicensed_transport, purchase_illegcigar, sell_illegcigar, over_postcigar, sell_abroadcigar,
                  helpothers_transport, in_province, out_of_province]
    forecast_case = []
    case_name = ["无证运输烟草专卖品", "未在当地进货", "销售非法生产的烟草专卖", "无烟草专卖准运证运输烟草专卖品邮寄、异地携带烟叶、烟草制品超过有关规定",
                 "销售无标识外国卷烟或销售出口倒流国产卷烟或销售没收的非法进口卷烟", "无烟草专卖准运证运输烟草专卖品为无烟草专卖品准运证者承运烟草专卖品", "省内互流", "外流省外"]
    max_index = [i for i, x in enumerate(case_score) if x == max(case_score)]
    for i in max_index:
        forecast_case.append(case_name[i])
    data = {"预测案由": forecast_case, "得分": score,"八大案由分数":case_score}
    if data:
        return common_response(SysStatus.SUCCESS, data, '查询成功')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 查询规则
@blue_print.route('/SearchRule', methods=['POST'])
def Search_rule():
    """
        @api {POST} api/rule/SearchRule  查询规则
        @apiVersion 0.0.1
        @apiName SearchRule
        @apiGroup rule
        @apiDescription 查询规则
        @apiParam {int}  rule_id     (必须)    规则id
        @apiParamExample {json} Request-Example:
            {
                "rule_id":"1,4,5"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": [
                    [
                        {
                            "id": 1,
                            "is_delete": false,
                            "rule_name": "person_nativeplace",
                            "parameter1": null,
                            "parameter2": null,
                            "parameter3": null,
                            "parameter4": true,
                            "score1": 5,
                            "score2": 0,
                            "score3": null,
                            "score4": null
                        }
                    ],
                    [
                        {
                            "id": 4,
                            "is_delete": false,
                            "rule_name": "is_bigillegal",
                            "parameter1": null,
                            "parameter2": null,
                            "parameter3": null,
                            "parameter4": true,
                            "score1": 5,
                            "score2": 0,
                            "score3": null,
                            "score4": null
                        }
                    ],
                    [
                        {
                            "id": 5,
                            "is_delete": false,
                            "rule_name": "is_downgrade",
                            "parameter1": null,
                            "parameter2": null,
                            "parameter3": null,
                            "parameter4": true,
                            "score1": 2,
                            "score2": 0,
                            "score3": null,
                            "score4": null
                        }
                    ]
                ],
                "message": "规则查询成功"
            }
    """
    params = search_rule(request.json or '')
    rule_id = params.get('rule_id')
    fenge = rule_id.split(',')
    data_all = []
    for i in range(len(fenge)):
        data = db.session.query(PredictRule).filter(PredictRule.id == fenge[i]).with_entities(
            PredictRule.id,
            PredictRule.is_delete,
            PredictRule.rule_name,
            PredictRule.parameter1,
            PredictRule.parameter2,
            PredictRule.parameter3,
            PredictRule.parameter4,
            PredictRule.score1,
            PredictRule.score2,
            PredictRule.score3,
            PredictRule.score4
        ).order_by(PredictRule.id).all()
        data_all.append(data)
    if data:
        return common_response(SysStatus.SUCCESS, data_all, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')
