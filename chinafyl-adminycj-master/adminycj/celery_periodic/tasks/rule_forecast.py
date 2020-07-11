from datetime import datetime
from typing import Any, Union
import pymysql
import datetime


# 数据库连接
# from pymysql.cursors import Cursor

# from celery_periodic import app


# @app.task
def rule_fore():
    conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    cursor = conn.cursor()
    # 插入前清空ruledata表中所有记录
    sql_delete = "DELETE FROM ruledata"
    cursor.execute(sql_delete)
    conn.commit()
    # 从store表中获取id,is_bigillegal,is_downgrade,administrative,person_id用store贯穿关联别的表
    sql_0 = "SELECT id,is_bigillegal,is_downgrade,administrative,person_id FROM store"
    cursor.execute(sql_0)
    res = cursor.fetchall()
    for i in range(len(res)):
        # 判断是否为违法大户
        if res[i][1] is None:
            isbigillegal = 0
        else:
            isbigillegal = res[i][1]
        # 判断是否降级降档
        if res[i][2] is None:
            isdowngrade = 0
        else:
            isdowngrade = res[i][2]
        # 根据法人信息判断是否为敏感籍贯
        sql_1 = "SELECT * FROM `personinfo` WHERE id=%s and (census_register like %s or  census_register like %s or census_register like %s) "
        cursor.execute(sql_1, (res[i][3], "%余干%", "%临海%", "%温岭%"))
        mgjgsz = cursor.fetchone()
        if mgjgsz is not None:
            mgjgsz = 1
        else:
            mgjgsz = 0
        # 从canton表中查询该行政区是否为敏感行政区
        if res[i][3] is None:
            iscanton = 0
        else:
            sql_2 = "SELECT is_cantonsensitivity FROM `canton` where canton = '" + str(res[i][3]) + "'"
            cursor.execute(sql_2)
            is_canton = cursor.fetchone()
            iscanton = is_canton[0]
        # 从monthtable表中查询当前月的敏感等级
        month = datetime.datetime.now().month
        sql_3 = "SELECT degree FROM monthtable where month ='" + str(month) + "'"
        cursor.execute(sql_3)
        is_month = cursor.fetchone()
        # 从Case表中获取is_criminal,smoke_property
        sql_4 = "SELECT is_criminal FROM `case` " \
                "where store_id = '" + str(res[i][0]) + "'"
        cursor.execute(sql_4)
        casecriminal = cursor.fetchone()
        if casecriminal is None:
            iscriminal = 0
        else:
            iscriminal = casecriminal[0]
        # 从case表中获取smoke_property
        sql_5 = "SELECT smoke_property01,smoke_property02,smoke_property03 FROM `case` " \
                "where store_id = '" + str(res[i][0]) + "'"
        cursor.execute(sql_5)
        smoke = cursor.fetchone()
        if smoke is None:
            jia = 0
            zou = 0
            fei = 0
        elif smoke[0] is None:
            jia = 0
        elif smoke[1] is None:
            zou = 0
        elif smoke[2] is None:
            fei = 0
        else:
            jia = smoke[0]
            zou = smoke[1]
            fei = smoke[2]
        # 从Case表中获取case_date
        sql_6 = "SELECT count(*) FROM `case` WHERE store_id = %s AND case_date BETWEEN %s AND %s"
        now_date = datetime.date.today()
        two_years_ago = now_date - datetime.timedelta(days=730)
        one_year_ago = now_date - datetime.timedelta(days=365)
        half_year_ago = now_date - datetime.timedelta(days=183)
        cursor.execute(sql_6, (res[i][0], two_years_ago, now_date))
        twoyear_illegaltimes = cursor.fetchone()
        if twoyear_illegaltimes is None:
            twoyear_illegaltimes = 0
        # 从case表中取出各违规案件次数，条数，金额
        sql_7 = "SELECT count(*),sum(count),sum(case_value) FROM `case` WHERE store_id = %s AND case_nature like %s"
        cursor.execute(sql_7, (res[i][0], "%无烟草专卖品准运证运输烟草%"))
        wzysyczmp = cursor.fetchone()
        if wzysyczmp[0] is None:
            wzysyczmp_t = 0
        else:
            wzysyczmp_t = wzysyczmp[0]
        if wzysyczmp[1] is None:
            wzysyczmp_n = 0
        else:
            wzysyczmp_n = wzysyczmp[1]
        if wzysyczmp[2] is None:
            wzysyczmp_p = 0
        else:
            wzysyczmp_p = wzysyczmp[2]

        cursor.execute(sql_7, (res[i][0], "%未在当地%"))
        wzddjh = cursor.fetchone()
        if wzddjh[0] is None:
            wzddjh_t = 0
        else:
            wzddjh_t = wzddjh[0]
        if wzddjh[1] is None:
            wzddjh_n = 0
        else:
            wzddjh_n = wzddjh[1]
        if wzddjh[2] is None:
            wzddjh_p = 0
        else:
            wzddjh_p = wzddjh[2]

        cursor.execute(sql_7, (res[i][0], "%销售非法生产的烟草专卖品%"))
        xsffscdyczm = cursor.fetchone()
        if xsffscdyczm[0] is None:
            xsffscdyczm_t = 0
        else:
            xsffscdyczm_t = xsffscdyczm[0]
        if xsffscdyczm[1] is None:
            xsffscdyczm_n = 0
        else:
            xsffscdyczm_n = xsffscdyczm[1]
        if xsffscdyczm[2] is None:
            xsffscdyczm_p = 0
        else:
            xsffscdyczm_p = xsffscdyczm[2]

        cursor.execute(sql_7, (res[i][0], "%邮寄%"))
        yjyd = cursor.fetchone()
        if yjyd[0] is None:
            yjyd_t = 0
        else:
            yjyd_t = yjyd[0]
        if yjyd[1] is None:
            yjyd_n = 0
        else:
            yjyd_n = yjyd[1]
        if yjyd[2] is None:
            yjyd_p = 0
        else:
            yjyd_p = yjyd[2]

        cursor.execute(sql_7, (res[i][0], "%无标志%"))
        wbs = cursor.fetchone()
        if wbs[0] is None:
            wbs_t = 0
        else:
            wbs_t = wbs[0]
        if wbs[1] is None:
            wbs_n = 0
        else:
            wbs_n = wbs[1]
        if wbs[2] is None:
            wbs_p = 0
        else:
            wbs_p = wbs[2]

        cursor.execute(sql_7, (res[i][0], "%无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品%"))
        cy = cursor.fetchone()
        if cy[0] is None:
            cy_t = 0
        else:
            cy_t = cy[0]
        if cy[1] is None:
            cy_n = 0
        else:
            cy_n = cy[1]
        if cy[2] is None:
            cy_p = 0
        else:
            cy_p = cy[2]

        sql_8 = "SELECT count(*),sum(count),sum(case_value) FROM `case` WHERE store_id = %s AND " \
                "case_nature like %s AND case_date BETWEEN %s AND %s"
        cursor.execute(sql_8, (1, "%近一年码段外流情况（省内外流）%", one_year_ago, now_date))
        oneyear_snwl = cursor.fetchone()
        if oneyear_snwl[0] == 0:
            oneyear_snwl_t = 0
        else:
            oneyear_snwl_t = 1
        if oneyear_snwl[1] is None:
            oneyear_snwl_n = 0
        else:
            oneyear_snwl_n = 1
        if oneyear_snwl[2] is None:
            oneyear_snwl_p = 0
        else:
            oneyear_snwl_p = 1
        sql_9 = "SELECT count(*),sum(count),sum(case_value) FROM `case` WHERE store_id = %s AND " \
                "case_nature like %s AND case_date BETWEEN %s AND %s"
        cursor.execute(sql_9, (res[i][0], "%近一年码段外流情况（外流省外）%", one_year_ago, now_date))
        oneyear_wlsw = cursor.fetchone()
        if oneyear_wlsw[0] == 0:
            oneyear_wlsw_t = 0
        else:
            oneyear_wlsw_t = 1
        if oneyear_wlsw[1] is None:
            oneyear_wlsw_n = 0
        else:
            oneyear_wlsw_n = 1
        if oneyear_wlsw[2] is None:
            oneyear_wlsw_p = 0
        else:
            oneyear_wlsw_p = 1
        # 插入
        sql_10 = "insert into ruledata(store_id,canton_id,is_bigillegal,is_downgrade,month,is_criminal," \
                 "cigar_property_jia,cigar_property_zou,cigar_property_fei,twoyear_illegaltimes," \
                 "unlicensed_transport_times,unlicensed_transport_num,unlicensed_transport_price," \
                 "purchase_illegcigar_times,purchase_illegcigar_num,purchase_illegcigar_price," \
                 "sell_illegcigar_times,sell_illegcigar_num,sell_illegcigar_price," \
                 "over_postcigar_times,over_postcigar_num,over_postcigar_price," \
                 "sell_abroadcigar_times,sell_abroadcigar_num,sell_abroadcigar_price," \
                 "helpothers_transport_times,helpothers_transport_num,helpothers_transport_price," \
                 "in_province_times,in_province_num,in_province_price," \
                 "out_of_province_times,out_of_province_num,out_of_province_price,person_nativeplace) " \
                 "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                 " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_10, (
            res[i][0], iscanton, isbigillegal, isdowngrade, is_month[0], iscriminal, jia,
            zou, fei, twoyear_illegaltimes[0], wzysyczmp_t, wzysyczmp_n, wzysyczmp_p,
            wzddjh_t, wzddjh_n, wzddjh_p, xsffscdyczm_t, xsffscdyczm_n, xsffscdyczm_p, yjyd_t, yjyd_n, yjyd_p,
            wbs_t, wbs_n, wbs_p, cy_t, cy_n, cy_p, oneyear_snwl_t, oneyear_snwl_n, oneyear_snwl_p, oneyear_wlsw_t,
            oneyear_wlsw_n, oneyear_wlsw_p, mgjgsz))
        conn.commit()

    # 变量赋值
    sqlStrOne = "select * from predictrule;"
    cursor.execute(sqlStrOne)
    res = cursor.fetchall()
    # 规则的启停标识
    qt1 = res[0][2]
    qt2 = res[1][2]
    qt3 = res[2][2]
    qt4 = res[3][2]
    qt5 = res[4][2]
    qt6 = res[5][2]
    qt7 = res[6][2]
    qt8 = res[7][2]
    qt9 = res[8][2]
    qt10 = res[9][2]
    qt11 = res[10][2]
    qt12 = res[11][2]
    qt13 = res[12][2]
    qt14 = res[13][2]
    qt15 = res[14][2]
    qt16 = res[15][2]
    qt17 = res[16][2]
    qt18 = res[17][2]
    qt19 = res[18][2]
    qt20 = res[19][2]
    qt21 = res[20][2]
    qt22 = res[21][2]
    qt23 = res[22][2]
    qt24 = res[23][2]
    qt25 = res[24][2]
    qt26 = res[25][2]
    qt27 = res[26][2]
    qt28 = res[27][2]
    qt29 = res[28][2]
    qt30 = res[29][2]
    qt31 = res[30][2]
    qt32 = res[31][2]
    qt33 = res[32][2]
    qt34 = res[33][2]
    qt35 = res[34][2]
    qt36 = res[35][2]
    qt37 = res[36][2]
    qt38 = res[37][2]
    qt39 = res[38][2]
    hostHometownSensitive = res[0][7]  # 主要负责经营人籍贯敏感
    score_hostHometownSensitive = res[0][8]
    other1HometownSensitive = res[1][7]  # 其他经营人1籍贯敏感
    score_other1HometownSensitive = res[1][8]
    other2HometownSensitive = res[2][7]  # 其他经营人2籍贯敏感
    score_other2HometownSensitive = res[2][8]
    bigIllegal = res[3][7]  # 是否为违法大户
    score_bigIllegal = res[3][8]
    downShift = res[4][7]  # 降档降级情况
    score_downShift = res[4][8]
    highMonth = res[5][4]
    midMonth = res[5][5]
    lowMonth = res[5][6]
    score_highMonth = res[5][8]
    score_midMonth = res[5][9]
    score_lowMonth = res[5][10]
    senDistrict = res[6][7]  # 行政敏感区
    score_senDistrict = res[6][8]
    isCriPenalties = res[7][7]  # 有无刑事处罚
    score_isCriPenalties = res[7][8]
    isIllegalWithinThePastSixMonths = res[8][7]  # 近半年内是否有违法记录
    score_isIllegalWithinThePastSixMonths = res[8][8]
    shamSmoking = res[9][7]  # 涉假冒烟
    score_shamSmoking = res[9][8]
    smugglingCigarettes = res[10][7]  # 涉走私烟
    score_smugglingCigarettes = res[10][8]
    feiCigarettes = res[11][7]  # 涉非流烟
    score_feiCigarettes = res[11][8]
    logisticsAssociation = res[12][7]  # 物流关联
    score_logisticsAssociation = res[12][8]
    isLinkedAccount = res[13][7]  # 车辆关联
    score_isLinkedAccount = res[13][8]

    C1NumberOfUnlTobMonShipments = res[14][4]  # 无证运输烟草专卖品次数参数1
    C2NumberOfUnlTobMonShipments = res[14][5]  # 无证运输烟草专卖品次数参数2
    C3NumberOfUnlTobMonShipments = res[14][6]  # 无证运输烟草专卖品次数参数3
    score_C1NumberOfUnlTobMonShipments = res[14][8]
    score_C2NumberOfUnlTobMonShipments = res[14][9]
    score_C3NumberOfUnlTobMonShipments = res[14][10]
    score_C4NumberOfUnlTobMonShipments = res[14][11]

    T1NumberOfUnlTobMonShipments = res[15][4]  # 无证运输烟草专卖品条数
    T2NumberOfUnlTobMonShipments = res[15][5]  # 无证运输烟草专卖品条数
    T3NumberOfUnlTobMonShipments = res[15][6]  # 无证运输烟草专卖品条数
    score_T1NumberOfUnlTobMonShipments = res[15][8]
    score_T2NumberOfUnlTobMonShipments = res[15][9]
    score_T3NumberOfUnlTobMonShipments = res[15][10]
    score_T4NumberOfUnlTobMonShipments = res[15][11]

    J1NumberOfUnlTobMonShipments = res[16][4]  # 无证运输烟草专卖品金额参数1
    J2NumberOfUnlTobMonShipments = res[16][5]  # 无证运输烟草专卖品金额参数2
    J3NumberOfUnlTobMonShipments = res[16][6]  # 无证运输烟草专卖品金额参数3
    score_J1NumberOfUnlTobMonShipments = res[16][8]
    score_J2NumberOfUnlTobMonShipments = res[16][9]
    score_J3NumberOfUnlTobMonShipments = res[16][10]
    score_J4NumberOfUnlTobMonShipments = res[16][11]

    C1NumberOfLocalPurchases = res[17][4]  # 未在当地进货次数参数1
    C2NumberOfLocalPurchases = res[17][5]  # 未在当地进货次数参数2
    C3NumberOfLocalPurchases = res[17][6]  # 未在当地进货次数参数3
    score_C1NumberOfLocalPurchases = res[17][8]
    score_C2NumberOfLocalPurchases = res[17][9]
    score_C3NumberOfLocalPurchases = res[17][10]
    score_C4NumberOfLocalPurchases = res[17][11]

    T1NumberOfLocalPurchases = res[18][4]  # 未在当地进货条数参数1
    T2NumberOfLocalPurchases = res[18][5]  # 未在当地进货条数参数2
    T3NumberOfLocalPurchases = res[18][6]  # 未在当地进货条数参数3
    score_T1NumberOfLocalPurchases = res[18][8]
    score_T2NumberOfLocalPurchases = res[18][9]
    score_T3NumberOfLocalPurchases = res[18][10]
    score_T4NumberOfLocalPurchases = res[18][11]

    J1NumberOfLocalPurchases = res[19][4]  # 未在当地进货金额参数1
    J2NumberOfLocalPurchases = res[19][5]  # 未在当地进货金额参数2
    J3NumberOfLocalPurchases = res[19][6]  # 未在当地进货金额参数3
    score_J1NumberOfLocalPurchases = res[19][8]
    score_J2NumberOfLocalPurchases = res[19][9]
    score_J3NumberOfLocalPurchases = res[19][10]
    score_J4NumberOfLocalPurchases = res[19][11]

    C1NumberOfMonSalOfUllProTobacco = res[20][4]  # 销售非法生产的烟草专卖次数参数1
    C2NumberOfMonSalOfUllProTobacco = res[20][5]  # 销售非法生产的烟草专卖次数参数2
    C3NumberOfMonSalOfUllProTobacco = res[20][6]  # 销售非法生产的烟草专卖次数参数3
    score_C1NumberOfMonSalOfUllProTobacco = res[20][8]
    score_C2NumberOfMonSalOfUllProTobacco = res[20][9]
    score_C3NumberOfMonSalOfUllProTobacco = res[20][10]
    score_C4NumberOfMonSalOfUllProTobacco = res[20][11]

    T1NumberOfMonSalOfUllProTobacco = res[21][4]  # 销售非法生产的烟草专卖条数参数1
    T2NumberOfMonSalOfUllProTobacco = res[21][5]  # 销售非法生产的烟草专卖条数参数2
    T3NumberOfMonSalOfUllProTobacco = res[21][6]  # 销售非法生产的烟草专卖条数参数3
    score_T1NumberOfMonSalOfUllProTobacco = res[21][8]
    score_T2NumberOfMonSalOfUllProTobacco = res[21][9]
    score_T3NumberOfMonSalOfUllProTobacco = res[21][10]
    score_T4NumberOfMonSalOfUllProTobacco = res[21][11]

    J1NumberOfMonSalOfUllProTobacco = res[22][4]  # 销售非法生产的烟草专卖金额参数1
    J2NumberOfMonSalOfUllProTobacco = res[22][5]  # 销售非法生产的烟草专卖金额参数2
    J3NumberOfMonSalOfUllProTobacco = res[22][6]  # 销售非法生产的烟草专卖金额参数3
    score_J1NumberOfMonSalOfUllProTobacco = res[22][8]
    score_J2NumberOfMonSalOfUllProTobacco = res[22][9]
    score_J3NumberOfMonSalOfUllProTobacco = res[22][10]
    score_J4NumberOfMonSalOfUllProTobacco = res[22][11]

    C1NumberOfTobPermitMail = res[23][4]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数参数1
    C2NumberOfTobPermitMail = res[23][5]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数参数2
    C3NumberOfTobPermitMail = res[23][6]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数参数3
    score_C1NumberOfTobPermitMail = res[23][8]
    score_C2NumberOfTobPermitMail = res[23][9]
    score_C3NumberOfTobPermitMail = res[23][10]
    score_C4NumberOfTobPermitMail = res[23][11]

    T1NumberOfTobPermitMail = res[24][4]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数参数1
    T2NumberOfTobPermitMail = res[24][5]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数参数2
    T3NumberOfTobPermitMail = res[24][6]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数参数3
    score_T1NumberOfTobPermitMail = res[24][8]
    score_T2NumberOfTobPermitMail = res[24][9]
    score_T3NumberOfTobPermitMail = res[24][10]
    score_T4NumberOfTobPermitMail = res[24][11]

    J1NumberOfTobPermitMail = res[25][4]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额参数1
    J2NumberOfTobPermitMail = res[25][5]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额参数2
    J3NumberOfTobPermitMail = res[25][6]  # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额参数3
    score_J1NumberOfTobPermitMail = res[25][8]
    score_J2NumberOfTobPermitMail = res[25][9]
    score_J3NumberOfTobPermitMail = res[25][10]
    score_J4NumberOfTobPermitMail = res[25][11]

    C1NumberOfUnmForCigSold = res[26][4]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数参数1
    C2NumberOfUnmForCigSold = res[26][5]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数参数2
    C3NumberOfUnmForCigSold = res[26][6]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数参数3
    score_C1NumberOfUnmForCigSold = res[26][8]
    score_C2NumberOfUnmForCigSold = res[26][9]
    score_C3NumberOfUnmForCigSold = res[26][10]
    score_C4NumberOfUnmForCigSold = res[26][11]

    T1NumberOfUnmForCigSold = res[27][4]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数参数1
    T2NumberOfUnmForCigSold = res[27][5]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数参数2
    T3NumberOfUnmForCigSold = res[27][6]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数参数3
    score_T1NumberOfUnmForCigSold = res[27][8]
    score_T2NumberOfUnmForCigSold = res[27][9]
    score_T3NumberOfUnmForCigSold = res[27][10]
    score_T4NumberOfUnmForCigSold = res[27][11]

    J1NumberOfUnmForCigSold = res[28][4]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额参数1
    J2NumberOfUnmForCigSold = res[28][5]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额参数2
    J3NumberOfUnmForCigSold = res[28][6]  # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额参数3
    score_J1NumberOfUnmForCigSold = res[28][8]
    score_J2NumberOfUnmForCigSold = res[28][9]
    score_J3NumberOfUnmForCigSold = res[28][10]
    score_J4NumberOfUnmForCigSold = res[28][11]

    C1NumberOfTobMonTraWitTobMonPermit = res[29][4]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数参数1
    C2NumberOfTobMonTraWitTobMonPermit = res[29][5]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数参数2
    C3NumberOfTobMonTraWitTobMonPermit = res[29][6]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数参数3
    score_C1NumberOfTobMonTraWitTobMonPermit = res[29][8]
    score_C2NumberOfTobMonTraWitTobMonPermit = res[29][9]
    score_C3NumberOfTobMonTraWitTobMonPermit = res[29][10]
    score_C4NumberOfTobMonTraWitTobMonPermit = res[29][11]

    T1NumberOfTobMonTraWitTobMonPermit = res[30][4]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数参数1
    T2NumberOfTobMonTraWitTobMonPermit = res[30][5]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数参数2
    T3NumberOfTobMonTraWitTobMonPermit = res[30][6]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数参数3
    score_T1NumberOfTobMonTraWitTobMonPermit = res[30][8]
    score_T2NumberOfTobMonTraWitTobMonPermit = res[30][9]
    score_T3NumberOfTobMonTraWitTobMonPermit = res[30][10]
    score_T4NumberOfTobMonTraWitTobMonPermit = res[30][11]

    J1NumberOfTobMonTraWitTobMonPermit = res[31][4]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额参数1
    J2NumberOfTobMonTraWitTobMonPermit = res[31][5]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额参数2
    J3NumberOfTobMonTraWitTobMonPermit = res[31][6]  # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额参数3
    score_J1NumberOfTobMonTraWitTobMonPermit = res[31][8]
    score_J2NumberOfTobMonTraWitTobMonPermit = res[31][9]
    score_J3NumberOfTobMonTraWitTobMonPermit = res[31][10]
    score_J4NumberOfTobMonTraWitTobMonPermit = res[31][11]

    t1heNumberTwoYears = res[32][4]  # 近两年历史违法次数参数1
    t2heNumberTwoYears = res[32][5]  # 近两年历史违法次数参数2
    t3heNumberTwoYears = res[32][6]  # 近两年历史违法次数参数3
    score_t1heNumberTwoYears = res[32][8]
    score_t2heNumberTwoYears = res[32][9]
    score_t3heNumberTwoYears = res[32][10]
    score_t4heNumberTwoYears = res[32][11]

    C1OutOfProvince = res[33][4]  # 近一年码段外流情况（省内外流）次数参数1
    C2OutOfProvince = res[33][5]  # 近一年码段外流情况（省内外流）次数参数2
    C3OutOfProvince = res[33][6]  # 近一年码段外流情况（省内外流）次数参数3
    score_C1OutOfProvince = res[33][8]
    score_C2OutOfProvince = res[33][9]
    score_C3OutOfProvince = res[33][10]
    score_C4OutOfProvince = res[33][11]

    T1OutOfProvince = res[34][4]  # 近一年码段外流情况（省内外流）条数参数1
    T2OutOfProvince = res[34][5]  # 近一年码段外流情况（省内外流）条数参数2
    T3OutOfProvince = res[34][6]  # 近一年码段外流情况（省内外流）条数参数3
    score_T1OutOfProvince = res[34][8]
    score_T2OutOfProvince = res[34][9]
    score_T3OutOfProvince = res[34][10]
    score_T4OutOfProvince = res[34][11]

    J1OutOfProvince = res[35][4]  # 近一年码段外流情况（省内外流）金额参数1
    J2OutOfProvince = res[35][5]  # 近一年码段外流情况（省内外流）金额参数2
    J3OutOfProvince = res[35][6]  # 近一年码段外流情况（省内外流）金额参数3
    score_J1OutOfProvince = res[35][8]
    score_J2OutOfProvince = res[35][9]
    score_J3OutOfProvince = res[35][10]
    score_J4OutOfProvince = res[35][11]

    C1ProvinceOut = res[36][4]  # 近一年码段外流情况（外流省外）次数参数1
    C2ProvinceOut = res[36][5]  # 近一年码段外流情况（外流省外）次数参数2
    C3ProvinceOut = res[36][6]  # 近一年码段外流情况（外流省外）次数参数3
    score_C1ProvinceOut = res[36][8]
    score_C2ProvinceOut = res[36][9]
    score_C3ProvinceOut = res[36][10]
    score_C4ProvinceOut = res[36][11]

    T1ProvinceOut = res[37][4]  # 近一年码段外流情况（外流省外）条数参数1
    T2ProvinceOut = res[37][5]  # 近一年码段外流情况（外流省外）条数参数2
    T3ProvinceOut = res[37][6]  # 近一年码段外流情况（外流省外）条数参数3
    score_T1ProvinceOut = res[37][8]
    score_T2ProvinceOut = res[37][9]
    score_T3ProvinceOut = res[37][10]
    score_T4ProvinceOut = res[37][11]

    J1ProvinceOut = res[38][4]  # 近一年码段外流情况（外流省外）金额参数1
    J2ProvinceOut = res[38][5]  # 近一年码段外流情况（外流省外）金额参数2
    J3ProvinceOut = res[38][6]  # 近一年码段外流情况（外流省外）金额参数3
    score_J1ProvinceOut = res[38][8]
    score_J2ProvinceOut = res[38][9]
    score_J3ProvinceOut = res[38][10]
    score_J4ProvinceOut = res[38][11]

    # 规则匹配
    score = 0
    sqlStr = "select * from ruledata;"
    cursor.execute(sqlStr)
    res = cursor.fetchall()
    for i in range(len(res)):
        if qt1 == 0:
            if res[i][4] == hostHometownSensitive:
                score += score_hostHometownSensitive
        if qt2 == 0:
            if res[i][5] == other1HometownSensitive:
                score += score_other1HometownSensitive
        if qt3 == 0:
            if res[i][6] == other2HometownSensitive:
                score += score_other2HometownSensitive
        if qt4 == 0:
            if res[i][7] == bigIllegal:
                score += score_bigIllegal
        if qt5 == 0:
            if res[i][8] == downShift:
                score += score_downShift
        if qt6 == 0:
            if res[i][9] == highMonth:
                score += score_highMonth
            if res[i][9] == midMonth:
                score += score_midMonth
            if res[i][9] == lowMonth:
                score += score_lowMonth
        if qt7 == 0:
            if res[i][10] == senDistrict:
                score += score_senDistrict
        if qt8 == 0:
            if res[i][11] == isCriPenalties:
                score += score_isCriPenalties
        if qt9 == 0:
            if res[i][12] == isIllegalWithinThePastSixMonths:
                score += score_isIllegalWithinThePastSixMonths
        if qt10 == 0:
            if res[i][13] == shamSmoking:
                score += score_shamSmoking
        if qt11 == 0:
            if res[i][14] == smugglingCigarettes:
                score += score_smugglingCigarettes
        if qt12 == 0:
            if res[i][15] == feiCigarettes:
                score += score_feiCigarettes
        if qt13 == 0:
            if res[i][16] == logisticsAssociation:
                score += score_logisticsAssociation
        if qt14 == 0:
            if res[i][17] == isLinkedAccount:
                score += score_isLinkedAccount
        # 无证运输烟草专卖品次数
        if qt15 == 0:
            if res[i][18] != 0:
                if C1NumberOfUnlTobMonShipments == 0 and C3NumberOfUnlTobMonShipments == 0:
                    if 0 < res[i][18] <= C2NumberOfUnlTobMonShipments:
                        score += score_C2NumberOfUnlTobMonShipments
                    elif res[i][18] > C2NumberOfUnlTobMonShipments:
                        score += score_C3NumberOfUnlTobMonShipments
                if C1NumberOfUnlTobMonShipments != 0 and C3NumberOfUnlTobMonShipments == 0:
                    if 0 < res[i][18] <= C1NumberOfUnlTobMonShipments:
                        score += score_C1NumberOfUnlTobMonShipments
                    elif C1NumberOfUnlTobMonShipments < res[i][18] <= C2NumberOfUnlTobMonShipments:
                        score += score_C2NumberOfUnlTobMonShipments
                    elif res[i][18] > C2NumberOfUnlTobMonShipments:
                        score += score_C3NumberOfUnlTobMonShipments
                if C1NumberOfUnlTobMonShipments != 0 and C3NumberOfUnlTobMonShipments != 0:
                    if 0 < res[i][18] <= C1NumberOfUnlTobMonShipments:
                        score += score_C1NumberOfUnlTobMonShipments
                    elif C1NumberOfUnlTobMonShipments < res[i][18] <= C2NumberOfUnlTobMonShipments:
                        score += score_C2NumberOfUnlTobMonShipments
                    elif C2NumberOfUnlTobMonShipments < res[i][18] <= C3NumberOfUnlTobMonShipments:
                        score += score_C3NumberOfUnlTobMonShipments
                    elif res[i][18] > C3NumberOfUnlTobMonShipments:
                        score += score_C4NumberOfUnlTobMonShipments
        # 无证运输烟草专卖品条数
        if qt16 == 0:
            if res[i][18] != 0:
                if T1NumberOfUnlTobMonShipments == 0 and T3NumberOfUnlTobMonShipments == 0:
                    if 0 < res[i][19] <= T2NumberOfUnlTobMonShipments:
                        score += score_T2NumberOfUnlTobMonShipments
                    elif res[i][19] > T2NumberOfUnlTobMonShipments:
                        score += score_T3NumberOfUnlTobMonShipments
                if T1NumberOfUnlTobMonShipments != 0 and T3NumberOfUnlTobMonShipments == 0:
                    if 0 < res[i][19] <= T1NumberOfUnlTobMonShipments:
                        score += score_T1NumberOfUnlTobMonShipments
                    elif T1NumberOfUnlTobMonShipments < res[i][19] <= T2NumberOfUnlTobMonShipments:
                        score += score_T2NumberOfUnlTobMonShipments
                    elif res[i][19] > T2NumberOfUnlTobMonShipments:
                        score += score_T3NumberOfUnlTobMonShipments
                if T1NumberOfUnlTobMonShipments != 0 and T3NumberOfUnlTobMonShipments != 0:
                    if 0 < res[i][19] <= T1NumberOfUnlTobMonShipments:
                        score += score_T1NumberOfUnlTobMonShipments
                    elif T1NumberOfUnlTobMonShipments < res[i][19] <= T2NumberOfUnlTobMonShipments:
                        score += score_T2NumberOfUnlTobMonShipments
                    elif T2NumberOfUnlTobMonShipments < res[i][19] <= T3NumberOfUnlTobMonShipments:
                        score += score_T3NumberOfUnlTobMonShipments
                    elif res[i][19] > T3NumberOfUnlTobMonShipments:
                        score += score_T4NumberOfUnlTobMonShipments
        # 无证运输烟草专卖品金额
        if qt17 == 0:
            if res[i][20] != 0:
                if J1NumberOfUnlTobMonShipments == 0 and J3NumberOfUnlTobMonShipments == 0:
                    if 0 < res[i][20] <= J2NumberOfUnlTobMonShipments:
                        score += score_J2NumberOfUnlTobMonShipments
                    elif res[i][20] > J2NumberOfUnlTobMonShipments:
                        score += score_J3NumberOfUnlTobMonShipments
                if J1NumberOfUnlTobMonShipments != 0 and J3NumberOfUnlTobMonShipments == 0:
                    if 0 < res[i][20] <= J1NumberOfUnlTobMonShipments:
                        score += score_J1NumberOfUnlTobMonShipments
                    elif J1NumberOfUnlTobMonShipments < res[i][20] <= J2NumberOfUnlTobMonShipments:
                        score += score_J2NumberOfUnlTobMonShipments
                    elif res[i][20] > J2NumberOfUnlTobMonShipments:
                        score += score_J3NumberOfUnlTobMonShipments
                if J1NumberOfUnlTobMonShipments != 0 and J3NumberOfUnlTobMonShipments != 0:
                    if 0 < res[i][20] <= J1NumberOfUnlTobMonShipments:
                        score += score_J1NumberOfUnlTobMonShipments
                    elif J1NumberOfUnlTobMonShipments < res[i][20] <= J2NumberOfUnlTobMonShipments:
                        score += score_J2NumberOfUnlTobMonShipments
                    elif J2NumberOfUnlTobMonShipments < res[i][20] <= J3NumberOfUnlTobMonShipments:
                        score += score_J3NumberOfUnlTobMonShipments
                    elif res[i][20] > J3NumberOfUnlTobMonShipments:
                        score += score_J4NumberOfUnlTobMonShipments
        # 未在当地进货次数
        if qt18 == 0:
            if res[i][21] != 0:
                if C1NumberOfLocalPurchases == 0 and C3NumberOfLocalPurchases == 0:
                    if 0 < res[i][21] < C2NumberOfLocalPurchases:
                        score += score_C2NumberOfLocalPurchases
                    elif res[i][21] >= C2NumberOfLocalPurchases:
                        score += score_C3NumberOfLocalPurchases
                if C1NumberOfLocalPurchases != 0 and C3NumberOfLocalPurchases == 0:
                    if 0 < res[i][21] < C1NumberOfLocalPurchases:
                        score += score_C1NumberOfLocalPurchases
                    elif C1NumberOfLocalPurchases <= res[i][21] < C2NumberOfLocalPurchases:
                        score += score_C2NumberOfLocalPurchases
                    elif res[i][21] >= C2NumberOfLocalPurchases:
                        score += score_C3NumberOfLocalPurchases
                if C1NumberOfLocalPurchases != 0 and C3NumberOfLocalPurchases != 0:
                    if 0 < res[i][21] < C1NumberOfLocalPurchases:
                        score += score_C1NumberOfLocalPurchases
                    elif C1NumberOfLocalPurchases <= res[i][21] < C2NumberOfLocalPurchases:
                        score += score_C2NumberOfLocalPurchases
                    elif C2NumberOfLocalPurchases <= res[i][21] < C3NumberOfLocalPurchases:
                        score += score_C3NumberOfLocalPurchases
                    elif res[i][21] >= C3NumberOfLocalPurchases:
                        score += score_C4NumberOfLocalPurchases
        # 未在当地进货条数
        if qt19 == 0:
            if res[i][22] != 0:
                if T1NumberOfLocalPurchases == 0 and T3NumberOfLocalPurchases == 0:
                    if 0 < res[i][22] < T2NumberOfLocalPurchases:
                        score += score_T2NumberOfLocalPurchases
                    elif res[i][22] >= T2NumberOfLocalPurchases:
                        score += score_T3NumberOfLocalPurchases
                if T1NumberOfLocalPurchases != 0 and T3NumberOfLocalPurchases == 0:
                    if 0 < res[i][22] < T1NumberOfLocalPurchases:
                        score += score_T1NumberOfLocalPurchases
                    elif T1NumberOfLocalPurchases <= res[i][22] < T2NumberOfLocalPurchases:
                        score += score_T2NumberOfLocalPurchases
                    elif res[i][22] >= T2NumberOfLocalPurchases:
                        score += score_T3NumberOfLocalPurchases
                if T1NumberOfLocalPurchases != 0 and T3NumberOfLocalPurchases != 0:
                    if 0 < res[i][22] < T1NumberOfLocalPurchases:
                        score += score_T1NumberOfLocalPurchases
                    elif T1NumberOfLocalPurchases <= res[i][22] < T2NumberOfLocalPurchases:
                        score += score_T2NumberOfLocalPurchases
                    elif T2NumberOfLocalPurchases <= res[i][22] < T3NumberOfLocalPurchases:
                        score += score_T3NumberOfLocalPurchases
                    elif res[i][22] >= T3NumberOfLocalPurchases:
                        score += score_T4NumberOfLocalPurchases
        # 未在当地进货金额
        if qt20 == 0:
            if res[i][23] != 0:
                if J1NumberOfLocalPurchases == 0 and J3NumberOfLocalPurchases == 0:
                    if 0 < res[i][23] < J2NumberOfLocalPurchases:
                        score += score_J2NumberOfLocalPurchases
                    elif res[i][23] >= J2NumberOfLocalPurchases:
                        score += score_J3NumberOfLocalPurchases
                if J1NumberOfLocalPurchases != 0 and J3NumberOfLocalPurchases == 0:
                    if 0 < res[i][23] < J1NumberOfLocalPurchases:
                        score += score_J1NumberOfLocalPurchases
                    elif J1NumberOfLocalPurchases <= res[i][23] < J2NumberOfLocalPurchases:
                        score += score_J2NumberOfLocalPurchases
                    elif res[i][23] >= J2NumberOfLocalPurchases:
                        score += score_J3NumberOfLocalPurchases
                if J1NumberOfLocalPurchases != 0 and J3NumberOfLocalPurchases != 0:
                    if 0 < res[i][23] < J1NumberOfLocalPurchases:
                        score += score_J1NumberOfLocalPurchases
                    elif J1NumberOfLocalPurchases <= res[i][23] < J2NumberOfLocalPurchases:
                        score += score_J2NumberOfLocalPurchases
                    elif J2NumberOfLocalPurchases <= res[i][23] < J3NumberOfLocalPurchases:
                        score += score_J3NumberOfLocalPurchases
                    elif res[i][23] >= J3NumberOfLocalPurchases:
                        score += score_J4NumberOfLocalPurchases
        # 销售非法生产的烟草专卖次数
        if qt21 == 0:
            if res[i][24] != 0:
                if C1NumberOfMonSalOfUllProTobacco == 0 and C3NumberOfMonSalOfUllProTobacco == 0:
                    if 0 < res[i][24] <= C2NumberOfMonSalOfUllProTobacco:
                        score += score_C2NumberOfMonSalOfUllProTobacco
                    elif res[i][24] > C2NumberOfMonSalOfUllProTobacco:
                        score += score_C3NumberOfMonSalOfUllProTobacco
                if C1NumberOfMonSalOfUllProTobacco != 0 and C3NumberOfMonSalOfUllProTobacco == 0:
                    if 0 < res[i][24] <= C1NumberOfMonSalOfUllProTobacco:
                        score += score_C1NumberOfMonSalOfUllProTobacco
                    elif C1NumberOfMonSalOfUllProTobacco < res[i][24] <= C2NumberOfMonSalOfUllProTobacco:
                        score += score_C2NumberOfMonSalOfUllProTobacco
                    elif res[i][24] > C2NumberOfMonSalOfUllProTobacco:
                        score += score_C3NumberOfMonSalOfUllProTobacco
                if C1NumberOfMonSalOfUllProTobacco != 0 and C3NumberOfMonSalOfUllProTobacco != 0:
                    if 0 < res[i][24] <= C1NumberOfMonSalOfUllProTobacco:
                        score += score_C1NumberOfMonSalOfUllProTobacco
                    elif C1NumberOfMonSalOfUllProTobacco < res[i][24] <= C2NumberOfMonSalOfUllProTobacco:
                        score += score_C2NumberOfMonSalOfUllProTobacco
                    elif C2NumberOfMonSalOfUllProTobacco < res[i][24] <= C3NumberOfMonSalOfUllProTobacco:
                        score += score_C3NumberOfMonSalOfUllProTobacco
                    elif res[i][24] > C3NumberOfMonSalOfUllProTobacco:
                        score += score_C4NumberOfMonSalOfUllProTobacco
        # 销售非法生产的烟草专卖条数
        if qt22 == 0:
            if res[i][25] != 0:
                if T1NumberOfMonSalOfUllProTobacco == 0 and T3NumberOfMonSalOfUllProTobacco == 0:
                    if 0 < res[i][25] <= T2NumberOfMonSalOfUllProTobacco:
                        score += score_T2NumberOfMonSalOfUllProTobacco
                    elif res[i][25] > T2NumberOfMonSalOfUllProTobacco:
                        score += score_T3NumberOfMonSalOfUllProTobacco
                if T1NumberOfMonSalOfUllProTobacco != 0 and T3NumberOfMonSalOfUllProTobacco == 0:
                    if 0 < res[i][25] <= T1NumberOfMonSalOfUllProTobacco:
                        score += score_T1NumberOfMonSalOfUllProTobacco
                    elif T1NumberOfMonSalOfUllProTobacco < res[i][25] <= T2NumberOfMonSalOfUllProTobacco:
                        score += score_T2NumberOfMonSalOfUllProTobacco
                    elif res[i][25] > T2NumberOfMonSalOfUllProTobacco:
                        score += score_T3NumberOfMonSalOfUllProTobacco
                if T1NumberOfMonSalOfUllProTobacco != 0 and T3NumberOfMonSalOfUllProTobacco != 0:
                    if 0 < res[i][25] <= T1NumberOfMonSalOfUllProTobacco:
                        score += score_T1NumberOfMonSalOfUllProTobacco
                    elif T1NumberOfMonSalOfUllProTobacco < res[i][25] <= T2NumberOfMonSalOfUllProTobacco:
                        score += score_T2NumberOfMonSalOfUllProTobacco
                    elif T2NumberOfMonSalOfUllProTobacco < res[i][25] <= T3NumberOfMonSalOfUllProTobacco:
                        score += score_T3NumberOfMonSalOfUllProTobacco
                    elif res[i][25] > T3NumberOfMonSalOfUllProTobacco:
                        score += score_T4NumberOfMonSalOfUllProTobacco
        # 销售非法生产的烟草专卖金额
        if qt23 == 0:
            if res[i][26] != 0:
                if J1NumberOfMonSalOfUllProTobacco == 0 and J3NumberOfMonSalOfUllProTobacco == 0:
                    if 0 < res[i][26] <= J2NumberOfMonSalOfUllProTobacco:
                        score += score_J2NumberOfMonSalOfUllProTobacco
                    elif res[i][26] > J2NumberOfMonSalOfUllProTobacco:
                        score += score_J3NumberOfMonSalOfUllProTobacco
                if J1NumberOfMonSalOfUllProTobacco != 0 and J3NumberOfMonSalOfUllProTobacco == 0:
                    if 0 < res[i][26] <= J1NumberOfMonSalOfUllProTobacco:
                        score += score_J1NumberOfMonSalOfUllProTobacco
                    elif J1NumberOfMonSalOfUllProTobacco < res[i][26] <= J2NumberOfMonSalOfUllProTobacco:
                        score += score_J2NumberOfMonSalOfUllProTobacco
                    elif res[i][26] > J2NumberOfMonSalOfUllProTobacco:
                        score += score_J3NumberOfMonSalOfUllProTobacco
                if J1NumberOfMonSalOfUllProTobacco != 0 and J3NumberOfMonSalOfUllProTobacco != 0:
                    if 0 < res[i][26] <= J1NumberOfMonSalOfUllProTobacco:
                        score += score_J1NumberOfMonSalOfUllProTobacco
                    elif J1NumberOfMonSalOfUllProTobacco < res[i][26] <= J2NumberOfMonSalOfUllProTobacco:
                        score += score_J2NumberOfMonSalOfUllProTobacco
                    elif J2NumberOfMonSalOfUllProTobacco < res[i][26] <= J3NumberOfMonSalOfUllProTobacco:
                        score += score_J3NumberOfMonSalOfUllProTobacco
                    elif res[i][26] > J3NumberOfMonSalOfUllProTobacco:
                        score += score_J4NumberOfMonSalOfUllProTobacco
        # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定次数
        if qt24 == 0:
            if res[i][27] != 0:
                if C1NumberOfTobPermitMail == 0 and C3NumberOfTobPermitMail == 0:
                    if 0 < res[i][27] < C2NumberOfTobPermitMail:
                        score += score_C2NumberOfTobPermitMail
                    elif res[i][27] >= C2NumberOfTobPermitMail:
                        score += score_C3NumberOfTobPermitMail
                if C1NumberOfTobPermitMail != 0 and C3NumberOfTobPermitMail == 0:
                    if 0 < res[i][27] < C1NumberOfTobPermitMail:
                        score += score_C1NumberOfTobPermitMail
                    elif C1NumberOfTobPermitMail <= res[i][27] < C2NumberOfTobPermitMail:
                        score += score_C2NumberOfTobPermitMail
                    elif res[i][27] >= C2NumberOfTobPermitMail:
                        score += score_C3NumberOfTobPermitMail
                if C1NumberOfTobPermitMail != 0 and C3NumberOfTobPermitMail != 0:
                    if 0 < res[i][27] < C1NumberOfTobPermitMail:
                        score += score_C1NumberOfTobPermitMail
                    elif C1NumberOfTobPermitMail <= res[i][27] < C2NumberOfTobPermitMail:
                        score += score_C2NumberOfTobPermitMail
                    elif C2NumberOfTobPermitMail <= res[i][27] < C3NumberOfTobPermitMail:
                        score += score_C3NumberOfTobPermitMail
                    elif res[i][27] >= C3NumberOfTobPermitMail:
                        score += score_C4NumberOfTobPermitMail
        # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定条数
        if qt25 == 0:
            if res[i][28] != 0:
                if T1NumberOfTobPermitMail == 0 and T3NumberOfTobPermitMail == 0:
                    if 0 < res[i][28] < T2NumberOfTobPermitMail:
                        score += score_T2NumberOfTobPermitMail
                    elif res[i][28] >= T2NumberOfTobPermitMail:
                        score += score_T3NumberOfTobPermitMail
                if T1NumberOfTobPermitMail != 0 and T3NumberOfTobPermitMail == 0:
                    if 0 < res[i][28] < T1NumberOfTobPermitMail:
                        score += score_T1NumberOfTobPermitMail
                    elif T1NumberOfTobPermitMail <= res[i][28] < T2NumberOfTobPermitMail:
                        score += score_T2NumberOfTobPermitMail
                    elif res[i][28] >= T2NumberOfTobPermitMail:
                        score += score_T3NumberOfTobPermitMail
                if T1NumberOfTobPermitMail != 0 and T3NumberOfTobPermitMail != 0:
                    if 0 < res[i][28] < T1NumberOfTobPermitMail:
                        score += score_T1NumberOfTobPermitMail
                    elif T1NumberOfTobPermitMail <= res[i][28] < T2NumberOfTobPermitMail:
                        score += score_T2NumberOfTobPermitMail
                    elif T2NumberOfTobPermitMail <= res[i][28] < T3NumberOfTobPermitMail:
                        score += score_T3NumberOfTobPermitMail
                    elif res[i][28] >= T3NumberOfTobPermitMail:
                        score += score_T4NumberOfTobPermitMail
        # 无烟草专卖准运证运输烟草专卖品—邮寄、异地携带烟叶、烟草制品超过有关规定金额
        if qt26 == 0:
            if res[i][29] != 0:
                if J1NumberOfTobPermitMail == 0 and J3NumberOfTobPermitMail == 0:
                    if 0 < res[i][29] <= J2NumberOfTobPermitMail:
                        score += score_J2NumberOfTobPermitMail
                    elif res[i][29] > J2NumberOfTobPermitMail:
                        score += score_J3NumberOfTobPermitMail
                if J1NumberOfTobPermitMail != 0 and J3NumberOfTobPermitMail == 0:
                    if 0 < res[i][29] <= J1NumberOfTobPermitMail:
                        score += score_J1NumberOfTobPermitMail
                    elif J1NumberOfTobPermitMail < res[i][29] <= J2NumberOfTobPermitMail:
                        score += score_J2NumberOfTobPermitMail
                    elif res[i][29] > J2NumberOfTobPermitMail:
                        score += score_J3NumberOfTobPermitMail
                if J1NumberOfTobPermitMail != 0 and J3NumberOfTobPermitMail != 0:
                    if 0 < res[i][29] <= J1NumberOfTobPermitMail:
                        score += score_J1NumberOfTobPermitMail
                    elif J1NumberOfTobPermitMail < res[i][29] <= J2NumberOfTobPermitMail:
                        score += score_J2NumberOfTobPermitMail
                    elif J2NumberOfTobPermitMail < res[i][29] <= J3NumberOfTobPermitMail:
                        score += score_J3NumberOfTobPermitMail
                    elif res[i][29] > J3NumberOfTobPermitMail:
                        score += score_J4NumberOfTobPermitMail
        # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟次数
        if qt27 == 0:
            if res[i][30] != 0:
                if C1NumberOfUnmForCigSold == 0 and C3NumberOfUnmForCigSold == 0:
                    if 0 < res[i][30] < C2NumberOfUnmForCigSold:
                        score += score_C2NumberOfUnmForCigSold
                    elif res[i][30] >= C2NumberOfUnmForCigSold:
                        score += score_C3NumberOfUnmForCigSold
                if C1NumberOfUnmForCigSold != 0 and C3NumberOfUnmForCigSold == 0:
                    if 0 < res[i][30] < C1NumberOfUnmForCigSold:
                        score += score_C1NumberOfUnmForCigSold
                    elif C1NumberOfUnmForCigSold <= res[i][30] < C2NumberOfUnmForCigSold:
                        score += score_C2NumberOfUnmForCigSold
                    elif res[i][30] >= C2NumberOfUnmForCigSold:
                        score += score_C3NumberOfUnmForCigSold
                if C1NumberOfUnmForCigSold != 0 and C3NumberOfUnmForCigSold != 0:
                    if 0 < res[i][30] < C1NumberOfUnmForCigSold:
                        score += score_C1NumberOfUnmForCigSold
                    elif C1NumberOfUnmForCigSold <= res[i][30] < C2NumberOfUnmForCigSold:
                        score += score_C2NumberOfUnmForCigSold
                    elif C2NumberOfUnmForCigSold <= res[i][30] < C3NumberOfUnmForCigSold:
                        score += score_C3NumberOfUnmForCigSold
                    elif res[i][30] >= C3NumberOfUnmForCigSold:
                        score += score_C4NumberOfUnmForCigSold
        # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟条数
        if qt28 == 0:
            if res[i][31] != 0:
                if T1NumberOfUnmForCigSold == 0 and T3NumberOfUnmForCigSold == 0:
                    if 0 < res[i][31] < T2NumberOfUnmForCigSold:
                        score += score_T2NumberOfUnmForCigSold
                    elif res[i][31] >= T2NumberOfUnmForCigSold:
                        score += score_T3NumberOfUnmForCigSold
                if T1NumberOfUnmForCigSold != 0 and T3NumberOfUnmForCigSold == 0:
                    if 0 < res[i][31] < T1NumberOfUnmForCigSold:
                        score += score_T1NumberOfUnmForCigSold
                    elif T1NumberOfUnmForCigSold <= res[i][31] < T2NumberOfUnmForCigSold:
                        score += score_T2NumberOfUnmForCigSold
                    elif res[i][31] >= T2NumberOfUnmForCigSold:
                        score += score_T3NumberOfUnmForCigSold
                if T1NumberOfUnmForCigSold != 0 and T3NumberOfUnmForCigSold != 0:
                    if 0 < res[i][31] < T1NumberOfUnmForCigSold:
                        score += score_T1NumberOfUnmForCigSold
                    elif T1NumberOfUnmForCigSold <= res[i][31] < T2NumberOfUnmForCigSold:
                        score += score_T2NumberOfUnmForCigSold
                    elif T2NumberOfUnmForCigSold <= res[i][31] < T3NumberOfUnmForCigSold:
                        score += score_T3NumberOfUnmForCigSold
                    elif res[i][31] >= T3NumberOfUnmForCigSold:
                        score += score_T4NumberOfUnmForCigSold
        # 销售无标识外国卷烟 或 销售出口倒流国产卷烟 或 销售没收的非法进口卷烟金额
        if qt29 == 0:
            if res[i][32] != 0:
                if J1NumberOfUnmForCigSold == 0 and J3NumberOfUnmForCigSold == 0:
                    if 0 < res[i][32] <= J2NumberOfUnmForCigSold:
                        score += score_J2NumberOfUnmForCigSold
                    elif res[i][32] > J2NumberOfUnmForCigSold:
                        score += score_J3NumberOfUnmForCigSold
                if J1NumberOfUnmForCigSold != 0 and J3NumberOfUnmForCigSold == 0:
                    if 0 < res[i][32] <= J1NumberOfUnmForCigSold:
                        score += score_J1NumberOfUnmForCigSold
                    elif J1NumberOfUnmForCigSold < res[i][32] <= J2NumberOfUnmForCigSold:
                        score += score_J2NumberOfUnmForCigSold
                    elif res[i][32] > J2NumberOfUnmForCigSold:
                        score += score_J3NumberOfUnmForCigSold
                if J1NumberOfUnmForCigSold != 0 and J3NumberOfUnmForCigSold != 0:
                    if 0 < res[i][32] <= J1NumberOfUnmForCigSold:
                        score += score_J1NumberOfUnmForCigSold
                    elif J1NumberOfUnmForCigSold < res[i][32] <= J2NumberOfUnmForCigSold:
                        score += score_J2NumberOfUnmForCigSold
                    elif J2NumberOfUnmForCigSold < res[i][32] <= J3NumberOfUnmForCigSold:
                        score += score_J3NumberOfUnmForCigSold
                    elif res[i][32] > J3NumberOfUnmForCigSold:
                        score += score_J4NumberOfUnmForCigSold
        # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品次数
        if qt30 == 0:
            if res[i][33] != 0:
                if C1NumberOfTobMonTraWitTobMonPermit == 0 and C3NumberOfTobMonTraWitTobMonPermit == 0:
                    if 0 < res[i][33] < C2NumberOfTobMonTraWitTobMonPermit:
                        score += score_C2NumberOfTobMonTraWitTobMonPermit
                    elif res[i][33] >= C2NumberOfTobMonTraWitTobMonPermit:
                        score += score_C3NumberOfTobMonTraWitTobMonPermit
                if C1NumberOfTobMonTraWitTobMonPermit != 0 and C3NumberOfTobMonTraWitTobMonPermit == 0:
                    if 0 < res[i][33] < C1NumberOfTobMonTraWitTobMonPermit:
                        score += score_C1NumberOfTobMonTraWitTobMonPermit
                    elif C1NumberOfTobMonTraWitTobMonPermit <= res[i][33] < C2NumberOfTobMonTraWitTobMonPermit:
                        score += score_C2NumberOfTobMonTraWitTobMonPermit
                    elif res[i][33] >= C2NumberOfTobMonTraWitTobMonPermit:
                        score += score_C3NumberOfTobMonTraWitTobMonPermit
                if C1NumberOfTobMonTraWitTobMonPermit != 0 and C3NumberOfTobMonTraWitTobMonPermit != 0:
                    if 0 < res[i][33] < C1NumberOfTobMonTraWitTobMonPermit:
                        score += score_C1NumberOfTobMonTraWitTobMonPermit
                    elif C1NumberOfTobMonTraWitTobMonPermit <= res[i][33] < C2NumberOfTobMonTraWitTobMonPermit:
                        score += score_C2NumberOfTobMonTraWitTobMonPermit
                    elif C2NumberOfTobMonTraWitTobMonPermit <= res[i][33] < C3NumberOfTobMonTraWitTobMonPermit:
                        score += score_C3NumberOfTobMonTraWitTobMonPermit
                    elif res[i][33] >= C3NumberOfTobMonTraWitTobMonPermit:
                        score += score_C4NumberOfTobMonTraWitTobMonPermit
        # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品条数
        if qt31 == 0:
            if res[i][34] != 0:
                if T1NumberOfTobMonTraWitTobMonPermit == 0 and T3NumberOfTobMonTraWitTobMonPermit == 0:
                    if 0 < res[i][34] < T2NumberOfTobMonTraWitTobMonPermit:
                        score += score_T2NumberOfTobMonTraWitTobMonPermit
                    elif res[i][34] >= T2NumberOfTobMonTraWitTobMonPermit:
                        score += score_T3NumberOfTobMonTraWitTobMonPermit
                if T1NumberOfTobMonTraWitTobMonPermit != 0 and T3NumberOfTobMonTraWitTobMonPermit == 0:
                    if 0 < res[i][34] < T1NumberOfTobMonTraWitTobMonPermit:
                        score += score_T1NumberOfTobMonTraWitTobMonPermit
                    elif T1NumberOfTobMonTraWitTobMonPermit <= res[i][34] < T2NumberOfTobMonTraWitTobMonPermit:
                        score += score_T2NumberOfTobMonTraWitTobMonPermit
                    elif res[i][34] >= T2NumberOfTobMonTraWitTobMonPermit:
                        score += score_T3NumberOfTobMonTraWitTobMonPermit
                if T1NumberOfTobMonTraWitTobMonPermit != 0 and T3NumberOfTobMonTraWitTobMonPermit != 0:
                    if 0 < res[i][34] < T1NumberOfTobMonTraWitTobMonPermit:
                        score += score_T1NumberOfTobMonTraWitTobMonPermit
                    elif T1NumberOfTobMonTraWitTobMonPermit <= res[i][34] < T2NumberOfTobMonTraWitTobMonPermit:
                        score += score_T2NumberOfTobMonTraWitTobMonPermit
                    elif T2NumberOfTobMonTraWitTobMonPermit <= res[i][34] < T3NumberOfTobMonTraWitTobMonPermit:
                        score += score_T3NumberOfTobMonTraWitTobMonPermit
                    elif res[i][34] >= T3NumberOfTobMonTraWitTobMonPermit:
                        score += score_T4NumberOfTobMonTraWitTobMonPermit
        # 无烟草专卖准运证运输烟草专卖品—为无烟草专卖品准运证者承运烟草专卖品金额
        if qt32 == 0:
            if res[i][35] != 0:
                if J1NumberOfTobMonTraWitTobMonPermit == 0 and J3NumberOfTobMonTraWitTobMonPermit == 0:
                    if 0 < res[i][35] <= J2NumberOfTobMonTraWitTobMonPermit:
                        score += score_J2NumberOfTobMonTraWitTobMonPermit
                    elif res[i][35] > J2NumberOfTobMonTraWitTobMonPermit:
                        score += score_J3NumberOfTobMonTraWitTobMonPermit
                if J1NumberOfTobMonTraWitTobMonPermit != 0 and J3NumberOfTobMonTraWitTobMonPermit == 0:
                    if 0 < res[i][35] <= J1NumberOfTobMonTraWitTobMonPermit:
                        score += score_J1NumberOfTobMonTraWitTobMonPermit
                    elif J1NumberOfTobMonTraWitTobMonPermit < res[i][35] <= J2NumberOfTobMonTraWitTobMonPermit:
                        score += score_J2NumberOfTobMonTraWitTobMonPermit
                    elif res[i][35] > J2NumberOfTobMonTraWitTobMonPermit:
                        score += score_J3NumberOfTobMonTraWitTobMonPermit
                if J1NumberOfTobMonTraWitTobMonPermit != 0 and J3NumberOfTobMonTraWitTobMonPermit != 0:
                    if 0 < res[i][35] <= J1NumberOfTobMonTraWitTobMonPermit:
                        score += score_J1NumberOfTobMonTraWitTobMonPermit
                    elif J1NumberOfTobMonTraWitTobMonPermit < res[i][35] <= J2NumberOfTobMonTraWitTobMonPermit:
                        score += score_J2NumberOfTobMonTraWitTobMonPermit
                    elif J2NumberOfTobMonTraWitTobMonPermit < res[i][35] <= J3NumberOfTobMonTraWitTobMonPermit:
                        score += score_J3NumberOfTobMonTraWitTobMonPermit
                    elif res[i][35] > J3NumberOfTobMonTraWitTobMonPermit:
                        score += score_J4NumberOfTobMonTraWitTobMonPermit
        # 近两年历史违法次数
        if qt33 == 0:
            if res[i][36] != 0:
                if t1heNumberTwoYears == 0 and t3heNumberTwoYears == 0:
                    if 0 < res[i][36] < t2heNumberTwoYears:
                        score += score_t2heNumberTwoYears
                    elif res[i][36] >= t2heNumberTwoYears:
                        score += score_t3heNumberTwoYears
                if t1heNumberTwoYears != 0 and t3heNumberTwoYears == 0:
                    if 0 < res[i][36] < t1heNumberTwoYears:
                        score += score_t1heNumberTwoYears
                    elif t1heNumberTwoYears <= res[i][36] < t2heNumberTwoYears:
                        score += score_t2heNumberTwoYears
                    elif res[i][36] >= t2heNumberTwoYears:
                        score += score_t3heNumberTwoYears
                if t1heNumberTwoYears != 0 and t3heNumberTwoYears != 0:
                    if 0 < res[i][36] < t1heNumberTwoYears:
                        score += score_t1heNumberTwoYears
                    elif t1heNumberTwoYears <= res[i][36] < t2heNumberTwoYears:
                        score += score_t2heNumberTwoYears
                    elif t2heNumberTwoYears <= res[i][36] < t3heNumberTwoYears:
                        score += score_t3heNumberTwoYears
                    elif res[i][36] >= T3NumberOfUnmForCigSold:
                        score += score_t4heNumberTwoYears
        # 近一年码段外流情况（省内外流）次数
        if qt34 == 0:
            if res[i][37] != 0:
                if C1OutOfProvince == 0 and C2OutOfProvince == 0:
                    if 0 < res[i][37] < C2OutOfProvince:
                        score += score_C2OutOfProvince
                    elif res[i][37] >= C2OutOfProvince:
                        score += score_C3OutOfProvince
                if C1OutOfProvince != 0 and C2OutOfProvince == 0:
                    if 0 < res[i][37] < C1OutOfProvince:
                        score += score_C1OutOfProvince
                    elif C1OutOfProvince <= res[i][37] < C2OutOfProvince:
                        score += score_C2OutOfProvince
                    elif res[i][37] >= C2OutOfProvince:
                        score += score_C3OutOfProvince
                if C1OutOfProvince != 0 and C3OutOfProvince != 0:
                    if 0 < res[i][37] < C1OutOfProvince:
                        score += score_C1OutOfProvince
                    elif C1OutOfProvince <= res[i][37] < C2OutOfProvince:
                        score += score_C2OutOfProvince
                    elif C2OutOfProvince <= res[i][37] < C3OutOfProvince:
                        score += score_C3OutOfProvince
                    elif res[i][37] >= C3OutOfProvince:
                        score += score_C4OutOfProvince
        # 近一年码段外流情况（省内外流）条数
        if qt35 == 0:
            if res[i][38] != 0:
                if T1OutOfProvince == 0 and T3OutOfProvince == 0:
                    if 0 < res[i][38] < T2OutOfProvince:
                        score += score_T2OutOfProvince
                    elif res[i][38] >= T2OutOfProvince:
                        score += score_T3OutOfProvince
                if T1OutOfProvince != 0 and T3OutOfProvince == 0:
                    if 0 < res[i][38] < T1OutOfProvince:
                        score += score_T1OutOfProvince
                    elif T1OutOfProvince <= res[i][38] < T2OutOfProvince:
                        score += score_T2OutOfProvince
                    elif res[i][38] >= T2OutOfProvince:
                        score += score_T3OutOfProvince
                if T1OutOfProvince != 0 and T3OutOfProvince != 0:
                    if 0 < res[i][38] < T1OutOfProvince:
                        score += score_T1OutOfProvince
                    elif T1OutOfProvince <= res[i][38] < T2OutOfProvince:
                        score += score_T2OutOfProvince
                    elif T2OutOfProvince <= res[i][38] < T3OutOfProvince:
                        score += score_T3OutOfProvince
                    elif res[i][38] >= T3OutOfProvince:
                        score += score_T4OutOfProvince
        # 近一年码段外流情况（省内外流）金额
        if qt36 == 0:
            if res[i][39] != 0:
                if J1OutOfProvince == 0 and J3OutOfProvince == 0:
                    if 0 < res[i][39] < J2OutOfProvince:
                        score += score_J2OutOfProvince
                    elif res[i][39] >= J2OutOfProvince:
                        score += score_J3OutOfProvince
                if J1OutOfProvince != 0 and J3OutOfProvince == 0:
                    if 0 < res[i][39] < J1OutOfProvince:
                        score += score_J1OutOfProvince
                    elif J1OutOfProvince <= res[i][39] < J2OutOfProvince:
                        score += score_J2OutOfProvince
                    elif res[i][39] >= J2OutOfProvince:
                        score += score_J3OutOfProvince
                if J1OutOfProvince != 0 and J3OutOfProvince != 0:
                    if 0 < res[i][39] < J1OutOfProvince:
                        score += score_J1OutOfProvince
                    elif J1OutOfProvince <= res[i][39] < J2OutOfProvince:
                        score += score_J2OutOfProvince
                    elif J2OutOfProvince <= res[i][39] < J3OutOfProvince:
                        score += score_J3OutOfProvince
                    elif res[i][39] >= J3OutOfProvince:
                        score += score_J4OutOfProvince
        # 近一年码段外流情况（外流省外）次数
        if qt37 == 0:
            if res[i][40] != 0:
                if C1ProvinceOut == 0 and C3ProvinceOut == 0:
                    if 0 < res[i][40] < C2ProvinceOut:
                        score += score_C2ProvinceOut
                    elif res[i][40] >= C2ProvinceOut:
                        score += score_C3ProvinceOut
                if C1ProvinceOut != 0 and C3ProvinceOut == 0:
                    if 0 < res[i][40] < C1ProvinceOut:
                        score += score_C1ProvinceOut
                    elif C1ProvinceOut <= res[i][40] < C2ProvinceOut:
                        score += score_C2ProvinceOut
                    elif res[i][40] >= C2ProvinceOut:
                        score += score_C3ProvinceOut
                if C1ProvinceOut != 0 and C3ProvinceOut != 0:
                    if 0 < res[i][40] < C1ProvinceOut:
                        score += score_C1ProvinceOut
                    elif C1ProvinceOut <= res[i][40] < C2ProvinceOut:
                        score += score_C2ProvinceOut
                    elif C2ProvinceOut <= res[i][40] < C3ProvinceOut:
                        score += score_C3ProvinceOut
                    elif res[i][40] >= C3ProvinceOut:
                        score += score_C4ProvinceOut
        # 近一年码段外流情况（外流省外）条数
        if qt38 == 0:
            if res[i][41] != 0:
                if T1ProvinceOut == 0 and T3ProvinceOut == 0:
                    if 0 < res[i][41] < T2ProvinceOut:
                        score += score_T2ProvinceOut
                    elif res[i][41] >= T2ProvinceOut:
                        score += score_T3ProvinceOut
                if T1ProvinceOut != 0 and T3ProvinceOut == 0:
                    if 0 < res[i][41] < T1ProvinceOut:
                        score += score_T1ProvinceOut
                    elif T1ProvinceOut <= res[i][41] < T3ProvinceOut:
                        score += score_T2ProvinceOut
                    elif res[i][41] >= T2ProvinceOut:
                        score += score_T3ProvinceOut
                if T1ProvinceOut != 0 and T3ProvinceOut != 0:
                    if 0 < res[i][41] < T1ProvinceOut:
                        score += score_T1ProvinceOut
                    elif T1ProvinceOut <= res[i][41] < T2ProvinceOut:
                        score += score_T2ProvinceOut
                    elif T2ProvinceOut <= res[i][41] < T3ProvinceOut:
                        score += score_T3ProvinceOut
                    elif res[i][41] >= T3ProvinceOut:
                        score += score_T4ProvinceOut
        # 近一年码段外流情况（外流省外）金额
        if qt39 == 0:
            if res[i][42] != 0:
                if J1ProvinceOut == 0 and J3ProvinceOut == 0:
                    if 0 < res[i][42] < J2ProvinceOut:
                        score += score_J2ProvinceOut
                    elif res[i][42] >= J2ProvinceOut:
                        score += score_J3ProvinceOut
                if J1ProvinceOut != 0 and J3ProvinceOut == 0:
                    if 0 < res[i][42] < J1ProvinceOut:
                        score += score_J1ProvinceOut
                    elif J1ProvinceOut <= res[i][42] < J2ProvinceOut:
                        score += score_J2ProvinceOut
                    elif res[i][42] >= J2ProvinceOut:
                        score += score_J3ProvinceOut
                if J1ProvinceOut != 0 and J3ProvinceOut != 0:
                    if 0 < res[i][42] < J1ProvinceOut:
                        score += score_J1ProvinceOut
                    elif J1ProvinceOut <= res[i][42] < J2ProvinceOut:
                        score += score_J2ProvinceOut
                    elif J2ProvinceOut <= res[i][42] < J3ProvinceOut:
                        score += score_J3ProvinceOut
                    elif res[i][42] >= J3ProvinceOut:
                        score += score_J4ProvinceOut
        sqlStrFour = "update ruledata set score=%s where store_id = %s"
        cursor.execute(sqlStrFour, (score, res[i][3]))
        conn.commit()
        score = 0

    # 对结果进行处理
    sqlFive = "select score from ruledata;"
    cursor.execute(sqlFive)
    res = cursor.fetchall()
    maxScore = res[0][0]
    for i in range(len(res)):
        if res[i][0] > maxScore:
            maxScore = res[i][0]
    sql_warning = "SELECT warning_param1 FROM warning WHERE mode='RULE'"
    cursor.execute(sql_warning)
    rule_param = cursor.fetchone()
    sqlSix = "select store_id,score from ruledata"
    cursor.execute(sqlSix)
    res = cursor.fetchall()
    for i in range(len(res)):
        now_date = datetime.date.today()
        if (res[i][1] / maxScore) > rule_param:
            sqlSeven = "insert into forecast(store_id,forecast_date,mode,result) values(%s,%s,%s,%s)"
            cursor.execute(sqlSeven, (res[i][0], now_date, "RULE", res[i][1] / maxScore))
        conn.commit()
    cursor.close()
    conn.close()


rule_fore()
