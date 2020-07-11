# -*-coding:utf-8-*-
import sys

sys.path.append("/root/adminycj")

import datetime
import pymysql
# 打开数据库连接
from numpy import mat
# from celery_periodic import app
from neural_network.RBF.rbf_test import load_model
from neural_network.RBF.rbf_trian import get_predict


# @app.task
def bp_fore():
    conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    conn.ping(reconnect=True)
    # 使用cursor()方法创建一个x游标对象
    cursor = conn.cursor()

    # 查询输入指标数据
    sql_forecast = """SELECT store_id,is_downgrade,format,is_sensitivecircle,is_bigillegal,is_sensitive_canton,
      whole_illegaltimes,twoyear_illegaltimes,is_halfyear_illegal,is_criminal,required_differ,purchase_change,purchase_price,
      sensitive_month FROM bpdata"""
    sql_result = "UPDATE bpdata SET bp_result = %s WHERE store_id = %s"
    sql_warning = "SELECT warning_param1 FROM warning WHERE mode='BP'"

    # 插入forecast预测表a
    sql_insert = "INSERT INTO forecast(store_id,forecast_date,mode,result) VALUES (%s,%s,'BP',%s)"

    # 异常处理
    try:
        cursor.execute(sql_forecast)
        datas = cursor.fetchall()
        store_id_list = []
        data_list = []
        now_date = datetime.date.today()
        cursor.execute(sql_warning)
        bp_param = cursor.fetchone()
        for i in datas:
            store_id_list.append(i[0])
            data_list.append(i[1:14])
        data = mat(data_list)
        center, delta, w = load_model("center.txt", "delta.txt", "weight.txt")
        bp_result = get_predict(data, center, delta, w)
        for i in range(len(store_id_list)):
            cursor.execute(sql_result, (float(bp_result[i]), store_id_list[i]))
            conn.commit()
            # 如果预测结果大于设定参数，插入预测表
            if float(bp_result[i] > bp_param):
                fore_result = 1
                cursor.execute(sql_insert, (store_id_list[i], now_date, fore_result))
                conn.commit()
        print('事务处理成功', cursor.rowcount)
        conn.commit()
    except Exception as e:
        conn.rollback()  # 事务回滚
        print('事务处理失败', e)

    # 关闭数据库连接
    conn.close()


if __name__ == '__main__':
    bp_fore()
