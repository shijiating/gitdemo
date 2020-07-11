# -*-coding:utf-8-*-
import datetime
import sys
# import cur as cur
import pymysql

# 打开数据库连接
# from celery_periodic import app

sys.setrecursionlimit(1000)


# @app.task
def store_query():
    conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    conn.ping(reconnect=True)
    # 使用cursor()方法创建一个x游标对象
    cursor = conn.cursor()

    # 从store表获取store_id、is_downgrade、business_format、is_sensitivecircle、is_bigillegal
    sql_store = "SELECT id,is_downgrade,business_format,circle,person_id,is_bigillegal FROM store WHERE is_delete=0"

    # 从case表获取store_id，whole_illegaltimes、twoyear_illegaltimes、is_halfyear_illegal、is_criminal、
    sql_case = "SELECT case_date,is_criminal FROM `case` WHERE store_id=%s"
    sql_case_date = "SELECT case_date FROM `case` WHERE store_id=%s AND case_date BETWEEN %s AND %s"

    # 从法人表查敏感籍贯
    sql_person = "SELECT census_register FROM personinfo WHERE id=%s AND is_delete=0"

    # 从经营业态表查询经营液态是否敏感
    sql_bf = "select degree from businessformat where business_format=%s and is_delete=0"

    # 从商圈表查询商圈是否敏感
    sql_cc = "SELECT is_sensitive FROM circle WHERE is_delete=0 AND store_circle_name =%s"

    # 从monthtable表查询当前月份敏感等级sensitive_month(123表示低中高危)
    sql_month = "SELECT degree FROM monthtable WHERE month=%s AND is_delete=0"

    # 从进货purchase表查询purchase_week、required_count、average_price。进货增长率purchase_change、要货量-进货量required_differ、平均进货单价增长率purchase_price
    sql_purchase = """SELECT purchase_date,purchase_week,required_count,average_price FROM purchase WHERE store_id=%s
    AND purchase_date BETWEEN %s AND %s"""
    sql_purchase_lastweek = """SELECT purchase_date,purchase_week,average_price FROM purchase WHERE store_id=%s
    AND purchase_date BETWEEN %s AND %s"""

    # 插入前清空bpdata表中所有记录
    sql_delete = "DELETE FROM bpdata"

    # 插入基础数据和违法数据
    sql_insert = """INSERT INTO bpdata(store_id,is_downgrade,format,is_sensitivecircle,is_bigillegal,is_sensitive_canton,
    whole_illegaltimes,twoyear_illegaltimes,is_halfyear_illegal,is_criminal,required_differ,purchase_change,purchase_price,
    sensitive_month)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    # 异常处理
    # try:
    cursor.execute(sql_delete)
    conn.commit()
    # 执行SQL语句
    cursor.execute(sql_store)
    # 提交事务到数据库执行
    results = cursor.fetchall()
    # print("results",results.count())
    # 月份敏感度
    now_date = datetime.date.today()
    cursor.execute(sql_month, (now_date.month))
    degree = cursor.fetchone()
    sensitive_month = degree[0]
    # 计算各时间变量
    two_years_ago = now_date - datetime.timedelta(days=730)
    half_year_ago = now_date - datetime.timedelta(days=183)
    a_week_ago = now_date - datetime.timedelta(days=8)
    two_weeks_ago = now_date - datetime.timedelta(days=15)
    # 循环零售户
    for row in results:
        # 取出基础指标数据
        store_id = row[0]
        # 是否降级降档判断
        downgrade = row[1]
        if downgrade is None:
            is_downgrade = 0
        else:
            is_downgrade = downgrade
        # 经营业态判断
        business_format = row[2]
        if business_format is None:
            status = 1
        else:
            cursor.execute(sql_bf, business_format)
            format = (cursor.fetchone())[0]
            if format is None:
                status = 1
            elif format == 'TOP':
                status = 3
            elif format == 'MIDDLE':
                status = 2
            else:
                status = 1
        # 商圈判断
        circle = row[3]
        # print(circle)
        if circle is None:
            is_sensitive_circle = 0
        else:
            cursor.execute(sql_cc, circle)
            circle1 = (cursor.fetchone())[0]
            # if circle1 is None:
            #     is_sensitive_circle = 0
            # else:
            is_sensitive_circle = circle1
        person_id = row[4]
        is_bigillegal = row[5]
        # 查该零售户法人信息（敏感籍贯）
        cursor.execute(sql_person, person_id)
        cantons = cursor.fetchone()
        if cantons:
            for i in cantons:
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
        # 查该零售户违法数据
        cursor.execute(sql_case, store_id)
        cases = cursor.fetchall()
        # 历年违法次数
        whole_illegaltimes = len(cases)
        if whole_illegaltimes == 0:
            is_criminal = 0
            twoyear_illegaltimes = 0
            is_halfyear_illegal = 0
        else:
            # 查近两年内违法次数以及半年内是否违法
            for case in cases:
                case_date = case[0]
                is_criminal = case[1]
            twoyear_illegaltimes = cursor.execute(sql_case_date, (store_id, two_years_ago, now_date))
            halfyear_illegal = cursor.execute(sql_case_date, (store_id, half_year_ago, now_date))
            if halfyear_illegal > 0:
                is_halfyear_illegal = 1
            else:
                is_halfyear_illegal = 0
        # 查该户营销指标数据
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
        # 查进货记录
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
        # 执行数据插入语句
        cursor.execute(sql_insert, (
            store_id, is_downgrade, status, is_sensitive_circle, is_bigillegal, is_sensitive_canton,
            whole_illegaltimes, twoyear_illegaltimes, is_halfyear_illegal, is_criminal, required_differ,
            purchase_change, purchase_price, sensitive_month))
        conn.commit()
    # except Exception as e:
    #     conn.rollback()  # 事务回滚
    #     print('事务处理失败', e)
    # else:
    #     conn.commit()  # 事务提交
    #     print('事务处理成功', cursor.rowcount)
    # # 关闭数据库连接
    conn.close()


if __name__ == '__main__':
    store_query()
