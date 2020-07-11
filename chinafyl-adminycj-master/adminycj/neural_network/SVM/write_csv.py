import pandas as pd
import csv
import pymysql
import os

def JoinDB():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='ycj')
    ##创建游标
    cur = conn.cursor()
    ##执行sql语句
    count = cur.execute('select whole_illegaltimes,twoyear_illegaltimes,is_halfyear_illegal,maximum_cigar_num,outofprovince_times,maximum_outofprovince_num,is_criminal,business_format,is_sensitivecircle,is_downgrade,is_sensitive_canton,is_sensitive_nativeplace,purchase_change,sell_change,sales_ratio,sensitive_time from svmdata')
    print('总共有%s条数据' % count)
    # 搜取所有结果
    results = cur.fetchall()
    # 获取表的数据结构字段
    fields = cur.description
    return list(results), list(fields)


S = JoinDB()
# print(S[0][i])
# print(S[1][i][0])
results = S[0]
fields = S[1]
print(results)
print(fields)


# print(fields[0][0])
# print(results)
# #写入文件
def writer_file(results, fields):
    ##查看文件大小
    # file_size = os.path.getsize('C:/DATA/svmdata.csv')
    # if file_size == 0:
        ##表头

        name = []
        results_list = []
        for i in range(len(fields)):
            name.append(fields[i][0])
        print(name)
        for i in range(len(results)):
            results_list.append(results[i])
        ##建立DataFrame对象
        file_test = pd.DataFrame(columns=name, data=results_list)
        ##数据写入,不要索引
        file_test.to_csv('svmdata.csv', encoding='utf-8', index=False)
    # else:
    #     with open('C:/DATA/svmdata.csv', 'a+', newline='') as file_test:
    #         ##追加到文件后面
    #         writer = csv.writer(file_test)
    #         ##写文件
    #         writer.writerows(results)

writer_file(results,fields)