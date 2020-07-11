import pymysql
from api.views.base import get_this_monday


def store_query():
    conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    # conn.ping(reconnect=True)
    # 使用cursor()方法创建一个x游标对象
    cursor = conn.cursor()

    # 查询规则预警参数
    sql_warning = "SELECT warning_param1,warning_param2,warning_param3 FROM warning WHERE mode='RULE'"

    # 查询规则预测结果高中低危零售户
    sql_rule = "SELECT store_id,result FROM forecast WHERE mode='RULE' AND forecast_date=%s AND result>=%s"

    # 查询bp预测违法零售户
    sql_bp = "SELECT store_id FROM forecast WHERE mode='BP'AND forecast_date=%s"

    # 查询svm预测违法零售户
    sql_svm = "SELECT store_id FROM forecast WHERE mode='SVM'AND forecast_date=%s"

    # 查询station_id
    sql_station_id = "SELECT station_id FROM department WHERE id=%s"

    # 查询department_id
    sql_department_id = "SELECT department_id FROM store WHERE id=%s"

    # 插入规则和综合模型的预测高中低结果
    sql_insert = "INSERT INTO forecast_store(forecast_store_id,forecast_mode,forecast_result,department_id,station_id,forecast_date) VALUES (%s,%s,%s,%s,%s,%s) "

    # 规则预警参数
    cursor.execute(sql_warning)
    warning_params = cursor.fetchone()
    param1 = warning_params[0]
    param2 = warning_params[1]
    param3 = warning_params[2]

    # 规则预测结果高中低危零售户
    this_monday = get_this_monday()
    cursor.execute(sql_rule, (this_monday, param1))
    rule_list = cursor.fetchall()

    # 定义元祖列表方便后面整行数据插入
    top_rule = []
    middle_rule = []
    low_rule = []
    # 定义零售户id高中低列表方便综合模型判断
    t_rule = []
    m_rule = []
    l_rule = []

    for ru in rule_list:
        store_id = ru[0]
        rule_result = float(ru[1])

        cursor.execute(sql_department_id, store_id)
        department_id = cursor.fetchone()[0]

        cursor.execute(sql_station_id, department_id)
        station_id = cursor.fetchone()[0]

        if rule_result >= param3:
            top_rule.append(
                (store_id, 'rule', 'TOP', department_id, station_id, this_monday))
            t_rule.append(store_id)
        elif rule_result > param2:
            middle_rule.append((store_id, 'rule', 'MIDDLE', department_id, station_id, this_monday))
            m_rule.append(store_id)
        else:
            low_rule.append((store_id, 'rule', 'LOW', department_id, station_id, this_monday))
            l_rule.append(store_id)
    print("top_rule", top_rule)
    print("middle_rule", middle_rule)
    print("low_rule", low_rule)

    # bp预测违法零售户
    cursor.execute(sql_bp, this_monday)
    bp_list = cursor.fetchall()
    bp_fore = []
    for b in bp_list:
        bp_fore.append(b[0])
    print("bp_fore", bp_fore)

    # svm预测违法零售户
    cursor.execute(sql_svm, this_monday)
    svm_list = cursor.fetchall()
    svm_fore = []
    for s in svm_list:
        svm_fore.append(s[0])
    print("svm_fore", svm_fore)

    # 综合模型预测结果
    top_all = []
    middle_all = []
    low_all = []
    for r in t_rule:
        cursor.execute(sql_department_id, r)
        department_id = cursor.fetchone()[0]
        cursor.execute(sql_station_id, department_id)
        station_id = cursor.fetchone()[0]
        if r not in bp_fore and r not in svm_fore:
            middle_all.append((r, 'comprehensive', 'MIDDLE', department_id, station_id, this_monday))
        else:
            top_all.append((r, 'comprehensive', 'TOP', department_id, station_id, this_monday))
    for m in m_rule:
        cursor.execute(sql_department_id, m)
        department_id = cursor.fetchone()[0]
        cursor.execute(sql_station_id, department_id)
        station_id = cursor.fetchone()[0]
        if m not in bp_fore and m not in svm_fore:
            low_all.append((m, 'comprehensive', 'LOW', department_id, station_id, this_monday))
        else:
            middle_all.append((m, 'comprehensive', 'MIDDLE', department_id, station_id, this_monday))
    for l in l_rule:
        cursor.execute(sql_department_id, l)
        department_id = cursor.fetchone()[0]
        cursor.execute(sql_station_id, department_id)
        station_id = cursor.fetchone()[0]
        low_all.append((l, 'comprehensive', 'LOW', department_id, station_id, this_monday))
    print("top_all", top_all)
    print("middle_all", middle_all)
    print("low_all", low_all)

    # 插入预测结果
    cursor.executemany(sql_insert, top_rule)
    cursor.executemany(sql_insert, middle_rule)
    cursor.executemany(sql_insert, low_rule)
    cursor.executemany(sql_insert, top_all)
    cursor.executemany(sql_insert, middle_all)
    cursor.executemany(sql_insert, low_all)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    store_query()
