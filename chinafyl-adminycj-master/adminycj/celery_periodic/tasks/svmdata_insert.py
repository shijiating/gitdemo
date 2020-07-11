# -*-coding:utf-8-*-
import datetime
# import cur as cur
import pymysql


# 打开数据库连接
# from celery_periodic import app


# @app.task
def store_query():
    conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    conn.ping(reconnect=True)
    # 使用cursor()方法创建一个x游标对象
    cursor = conn.cursor()

    # 从store表获取store_id、is_downgrade、business_format、is_sensitivecircle、is_bigillegal、administrative
    sql_store = "SELECT id,is_downgrade,business_format,circle,person_id,is_bigillegal,administrative FROM store WHERE is_delete='0'"

    # 从case表获取store_id，whole_illegaltimes、twoyear_illegaltimes、is_halfyear_illegal、is_criminal、
    sql_case = "SELECT case_date,is_criminal FROM `case` WHERE store_id=%s"
    sql_case_date = "SELECT case_date FROM `case` WHERE store_id=%s AND case_date BETWEEN %s AND %s"

    # 从法人表查敏感籍贯
    sql_person = "SELECT census_register FROM personinfo WHERE id=%s AND is_delete='0'"

    # 从monthtable表查询当前月份敏感等级sensitive_month(123表示低中高危)
    sql_month = "SELECT degree FROM monthtable WHERE month=%s AND is_delete='0'"

    # 从进货purchase表查询purchase_week、required_count、average_price。进货增长率purchase_change、要货量-进货量required_differ、平均进货单价增长率purchase_price
    sql_purchase = """SELECT purchase_date,purchase_week,required_count,average_price FROM purchase WHERE store_id=%s
    AND purchase_date BETWEEN %s AND %s"""
    sql_purchase_lastweek = """SELECT purchase_date,purchase_week,average_price FROM purchase WHERE store_id=%s
    AND purchase_date BETWEEN %s AND %s"""

    # 插入前清空bpdata表中所有记录
    sql_delete = "DELETE FROM svmdata"
    # 插入基础数据和违法数据
    sql_insert = """INSERT INTO svmdata(store_id,is_downgrade,format,is_sensitivecircle,is_bigillegal,is_sensitive_canton,
    whole_illegaltimes,twoyear_illegaltimes,is_halfyear_illegal,is_criminal,required_differ,purchase_change,purchase_price,
    sensitive_month,maximum_cigar_num,outofprovince_times,maximum_outofprovince_num,is_sensitive_nativeplace)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    #   ,%s
    # 查询码段外流次数
    sql_6 = "select count(out_date)as outofprovince_times from codesegment where store_id=%s"

    # 查询码段外流最大条数
    sql_7 = "select max(out_count)as maximum_outofprovince_num from codesegment where store_id=%s"

    # 查询最大案件条数
    sql_8 = "SELECT max(count)as maximum_cigar_num FROM `case` WHERE store_id=%s"

    # 异常处理
    # try:
    cursor.execute(sql_delete)
    conn.commit()
    # 执行SQL语句
    cursor.execute(sql_store)
    # 提交事务到数据库执行
    results = cursor.fetchall()
    now_date = datetime.date.today()
    cursor.execute(sql_month, (now_date.month))
    degree = cursor.fetchone()
    sensitive_month = degree[0]
    print('sensitive_month:', sensitive_month)
    two_years_ago = now_date - datetime.timedelta(days=730)
    print(two_years_ago)
    half_year_ago = now_date - datetime.timedelta(days=183)
    print(half_year_ago)
    a_week_ago = now_date - datetime.timedelta(days=8)
    print('a_week_ago', a_week_ago)
    two_weeks_ago = now_date - datetime.timedelta(days=15)
    print('two_week_ago', two_weeks_ago)
    for row in results:
        # print(row)
        store_id = row[0]
        downgrade = row[1]
        if downgrade is None:
            is_downgrade = 0
        else:
            is_downgrade = downgrade
            # real_business_format = str(row[2])
        real_business_format = row[2]
        if real_business_format is None:
            status = 1
        else:
            sql_bf = "select degree from businessformat where business_format=%s and is_delete='0'"
            cursor.execute(sql_bf, real_business_format)
            business_format = (cursor.fetchone())[0]
        if business_format is None:
            status = 1
        elif business_format == 'TOP':
            status = 3
        elif business_format == 'MIDDLE':
            status = 2
        else:
            status = 1
        # print(status)
        real_circle = row[3]
        # print(real_circle)
        if real_circle is None:
            is_sensitive_circle = 0
        else:
            sql_cc = "SELECT is_sensitive FROM circle WHERE is_delete='0' AND store_circle_name =%s"
            cursor.execute(sql_cc, real_circle)
            circle = (cursor.fetchone())[0]
            is_sensitive_circle = circle
        person_id = row[4]
        is_bigillegal = row[5]
        administrative = row[6]
        sql_admin = "SELECT is_cantonsensitivity FROM canton WHERE is_delete='0' AND canton =%s"
        cursor.execute(sql_admin, administrative)
        is_administrative = (cursor.fetchone())[0]
        print(is_administrative)

        cursor.execute(sql_person, (person_id))
        cantons = cursor.fetchone()
        # print(cantons)
        if cantons:
            for i in cantons:
                # print(i)
                if i is None:
                    is_sensitive_canton = 0
                else:
                    canton = ''.join(i)
                    if "余干" in canton or "温岭" in canton or "临海" in canton:
                        is_sensitive_canton = 1
                    else:
                        is_sensitive_canton = 0
        else:
            is_sensitive_canton = 0
        cursor.execute(sql_case, (store_id))
        cases = cursor.fetchall()
        whole_illegaltimes = len(cases)
        if whole_illegaltimes == 0:
            is_criminal = 0
            twoyear_illegaltimes = 0
            is_halfyear_illegal = 0
        else:
            # print(whole_illegaltimes)
            for case in cases:
                case_date = case[0]
                is_criminal = case[1]
            twoyear_illegaltimes = cursor.execute(sql_case_date, (store_id, two_years_ago, now_date))
            halfyear_illegal = cursor.execute(sql_case_date, (store_id, half_year_ago, now_date))
            if halfyear_illegal > 0:
                is_halfyear_illegal = 1
            else:
                is_halfyear_illegal = 0
        cursor.execute(sql_6, (store_id))
        out_count = cursor.fetchall()
        for outnum in out_count:
            if outnum != (None,):
                outofprovince_times = outnum[0]
            else:
                outofprovince_times = 0
        # print('outofprovince_times', outofprovince_times)

        cursor.execute(sql_7, (store_id))
        max_outcount = cursor.fetchall()
        # for outcount in max_outcount:
        # print("最大外流条数在这里")
        # print(max_outcount[0])
        if max_outcount[0] != (None,):
            maximum_outofprovince_num = max_outcount[0]
        else:
            maximum_outofprovince_num = 0
        # print('maximum_outofprovince_num', maximum_outofprovince_num)

        cursor.execute(sql_8, (store_id))
        max_count = cursor.fetchall()
        # for outcount in max_outcount:
        # print("最大案件条数在这里")
        # print(max_count[0])
        if max_count[0] != (None,):
            maximum_cigar_num = max_count[0]
        else:
            maximum_cigar_num = 0
        # print('maximum_cigar_num', maximum_cigar_num)
        cursor.execute(sql_purchase, (store_id, a_week_ago, now_date))
        purchase = cursor.fetchall()
        if purchase:
            for p in purchase:
                purchase_date = p[0]
                purchase_week = float(p[1])
                required_count = p[2]
                average_price = float(p[3])
                required_differ = abs(required_count - purchase_week)
        else:
            purchase_week = 0
            required_count = 0
            average_price = 0
            required_differ = 0
        cursor.execute(sql_purchase_lastweek, (store_id, two_weeks_ago, a_week_ago))
        purchase_lastweek = cursor.fetchall()
        if purchase_lastweek:
            for pl in purchase_lastweek:
                purchase_date_l = pl[0]
                purchase_week_l = float(pl[1])
                average_price_l = float(pl[2])
        else:
            purchase_week_l = 0
            average_price_l = 0
        if purchase_week_l == 0:
            purchase_change = 0
        else:
            purchase_change = round(((purchase_week - purchase_week_l) / purchase_week_l), 2)

        if average_price_l == 0:
            purchase_price = 0
        else:
            purchase_price = round(((average_price - average_price_l) / average_price_l), 2)
        cursor.execute(sql_insert, (
            store_id, is_downgrade, status, is_sensitive_circle, is_bigillegal, is_sensitive_canton,
            whole_illegaltimes, twoyear_illegaltimes, is_halfyear_illegal, is_criminal, required_differ,
            purchase_change, purchase_price, sensitive_month, maximum_cigar_num, outofprovince_times,
            maximum_outofprovince_num, is_administrative))
        conn.commit()
        #
    # except Exception as e:
    #     conn.rollback()  # 事务回滚
    #     print('事务处理失败', e)

    # conn.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)
    # 关闭数据库连接
    conn.close()


store_query()
