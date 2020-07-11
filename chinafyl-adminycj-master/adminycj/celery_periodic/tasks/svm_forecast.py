import pandas as pd
import csv
import pymysql
import os
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.externals import joblib
import datetime


# -----------------svmdata表写入.csv-----------------------------
def JoinDB():
    conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    ##创建游标
    cur = conn.cursor()
    ##执行sql语句
    count = cur.execute(
        'select store_id,whole_illegaltimes,twoyear_illegaltimes,is_halfyear_illegal,maximum_cigar_num,outofprovince_times,\
        maximum_outofprovince_num,is_criminal,format,is_sensitivecircle,is_downgrade,is_sensitive_canton,\
        is_sensitive_nativeplace,purchase_change,required_differ,purchase_price,sensitive_month,is_bigillegal,result from svmdata')
    print('总共有%s条数据' % count)
    # 搜取所有结果
    results = cur.fetchall()
    # 获取表的数据结构字段
    fields = cur.description
    return list(results), list(fields)


# -----------------写入文件-----------------------------
def writer_file(results, fields):
    # 查看文件大小
    # file_size = os.path.getsize('C:/DATA/svmdata.csv')
    # if file_size == 0:
    # 表头
    name = []
    results_list = []
    for i in range(len(fields)):
        name.append(fields[i][0])
    # print(name)
    for i in range(len(results)):
        results_list.append(results[i])
    # 建立DataFrame对象
    file_test = pd.DataFrame(columns=name, data=results_list)
    # 数据写入,不要索引
    file_test.to_csv('svmdata.csv', encoding='utf-8', index=False)


# -------------------预测执行函数------------------------------
def svm_fore():
    db = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
    S = JoinDB()
    results = S[0]
    fields = S[1]
    writer_file(results, fields)
    # 对存入csv的数据预处理得到可以输入模型的x_std
    customer_data = pd.read_csv(r'svmdata.csv', encoding='GB2312')
    df = pd.DataFrame(customer_data, columns=['store_id', 'whole_illegaltimes', 'twoyear_illegaltimes'
        , 'is_halfyear_illegal', 'maximum_cigar_num', 'outofprovince_times', 'maximum_outofprovince_num'
        , 'is_criminal', 'format', 'is_sensitivecircle', 'is_downgrade'
        , 'is_sensitive_canton', 'is_sensitive_nativeplace', 'purchase_change', 'required_differ'
        , 'purchase_price', 'sensitive_month', 'is_bigillegal'])
    storeid = (df.iloc[:, 0]).values
    # print("storeid 在这里")
    # print(len(storeid))
    # print(type(storeid))
    # print(type(storeid.values))
    # df.business_format[df.business_format == 'TOP'] = 1
    # df.business_format[df.business_format == 'MIDDLE'] = 2
    # df.business_format[df.business_format == 'LOW'] = 3
    df = df.reset_index(drop=True)
    newcustomer_data = df.drop(columns=["store_id"], axis=1, inplace=False)
    # print(newcustomer_data.shape)
    scaler = StandardScaler()
    x_std = scaler.fit_transform(newcustomer_data)
    # print(x_std)
    # 调用已经训练好的模型cigar_svm_model得到预测结果并存入svmdata的result中
    cigar_svm_model = joblib.load(r'cigar_svm_model')
    cigar_predict = cigar_svm_model.predict(x_std)
    # print("这里是predict")
    # print(cigar_predict)
    # print(cigar_predict[2])
    # print(type(cigar_predict))
    cursor = db.cursor()
    for count in range(0, len(storeid)):
        # print(count)
        results = cigar_predict[count]
        # print(results)
        storesid = storeid[count]
        # print(storesid)
        sql_2 = "update svmdata set result = '%s' where store_id = '%s';" % (results, storesid)
        try:
            cursor.execute(sql_2)
            db.commit()
        except:
            db.rollback()  # 发生错误后回滚
    # 从svmdata中取store_id和result插入forecast中
    sql_forecast = "SELECT store_id,result FROM svmdata WHERE is_delete=0"
    cursor = db.cursor()
    cursor.execute(sql_forecast)
    bag = cursor.fetchall()
    # print(bag)
    for num in range(0, len(bag)):
        storeid = bag[num][0]
        results = bag[num][1]
        forecastdate = datetime.date.today()
        modes = 'SVM'
        sql_3 = "insert into forecast(store_id,forecast_date,mode,result)values (%s,%s,%s,%s)"
        try:
            if results == 1:
                cursor.execute(sql_3, (storeid, forecastdate, modes, results))
                db.commit()
        except:
            db.rollback()  # 发生错误后回滚
    db.close()  # 关闭数据库

if __name__ == '__main__':
    svm_fore()
