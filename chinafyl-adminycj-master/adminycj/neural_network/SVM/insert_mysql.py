import numpy as np
import pymysql
import datetime

prediction = np.array([])

mysql_server = 'localhost'
name = 'root'
password = '123456'
mysql_db = 'ycj'
db = pymysql.connect(mysql_server, name, password, mysql_db)

x = np.array([0, 0, 0, 1, 1, 0, 1, 1, 0, 1])
print(type(x)) #这里是ndarray的类型
# for item in x.flat:
#     item


    # cursor.execute("insert into forecast(result) values(%s)", int(item))
    #
    # db.commit()
