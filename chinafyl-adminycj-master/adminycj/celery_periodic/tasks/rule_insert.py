from datetime import datetime
from typing import Any, Union
import pymysql
import datetime
# 数据库连接
from pymysql.cursors import Cursor

conn = pymysql.connect('localhost', 'ycj', '@Ycj2020', 'ycj0527')
cursor = conn.cursor()

# 往预测规则表里插入规则
sql = "insert into predictrule(id,created_at,is_delete,rule_name,parameter1,parameter2,parameter3,parameter4,score1," \
      "score2,score3,score4,describe_rule, modifydate) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = ((1, create_time, 0, 'person_nativeplace', None, None, None, 1, 2, 0, None, None, None, None),
        (2, create_time, 0, 'person01_nativeplace', None, None, None, 1, 1, 0, None, None, None, None),
        (3, create_time, 0, 'person02_nativeplace', None, None, None, 1, 1, 0, None, None, None, None),
        (4, create_time, 0, 'is_bigillegal', None, None, None, 1, 5, 0, None, None, None, None),
        (5, create_time, 0, 'is_downgrade', None, None, None, 1, 2, 0, None, None, None, None),
        (6, create_time, 0, 'month', 3, 2, 1, None, 5, 3, 1, None, None, None),
        (7, create_time, 0, 'canton_id', None, None, None, 1, 2, 0, None, None, None, None),
        (8, create_time, 0, 'is_criminal', None, None, None, 1, 10, 0, None, None, None, None),
        (9, create_time, 0, 'is_illegal', None, None, None, 1, 10, 0, None, None, None, None),
        (10, create_time, 0, 'cigar_property_jia', None, None, None, 1, 3, 0, None, None, None, None),
        (11, create_time, 0, 'cigar_property_zou', None, None, None, 1, 3, 0, None, None, None, None),
        (12, create_time, 0, 'cigar_property_fei', None, None, None, 1, 3, 0, None, None, None, None),
        (13, create_time, 0, 'logistics', None, None, None, 1, 5, 0, None, None, None, None),
        (14, create_time, 0, 'car', None, None, None, 1, 5, 0, None, None, None, None),
        (15, create_time, 0, 'unlicensed_transport_times', 0, 2, 0, 0, 0, 4, 6, None, None, None),
        (16, create_time, 0, 'unlicensed_transport_num', 0, 50, 0, 0, 0, 3, 5, None, None, None),
        (17, create_time, 0, 'unlicensed_transport_price', 0, 10000, 0, 0, 0, 2, 4, None, None, None),
        (18, create_time, 0, 'purchase_illegcigar_times', 0, 3, 0, 0, 0, 4, 6, None, None, None),
        (19, create_time, 0, 'purchase_illegcigar_num', 0, 50, 0, 0, 0, 3, 5, None, None, None),
        (20, create_time, 0, 'purchase_illegcigar_price', 0, 10000, 0, 0, 0, 3, 5, None, None, None),
        (21, create_time, 0, 'sell_illegcigar_times', 0, 2, 0, 0, 0, 3, 5, None, None, None),
        (22, create_time, 0, 'sell_illegcigar_num', 0, 50, 0, 0, 0, 2, 4, None, None, None),
        (23, create_time, 0, 'sell_illegcigar_price', 0, 10000, 0, 0, 0, 2, 4, None, None, None),
        (24, create_time, 0, 'over_postcigar_times', 0, 3, 0, 0, 0, 3, 5, None, None, None),
        (25, create_time, 0, 'over_postcigar_num', 0, 50, 0, 0, 0, 2, 4, None, None, None),
        (26, create_time, 0, 'over_postcigar_price', 0, 10000, 0, 0, 0, 2, 4, None, None, None),
        (27, create_time, 0, 'sell_abroadcigar_times', 0, 3, 0, 0, 0, 3, 5, None, None, None),
        (28, create_time, 0, 'sell_abroadcigar_num', 0, 50, 0, 0, 0, 2, 4, None, None, None),
        (29, create_time, 0, 'sell_abroadcigar_price', 0, 10000, 0, 0, 0, 2, 4, None, None, None),
        (30, create_time, 0, 'helpothers_transport_times', 0, 3, 0, 0, 0, 3, 5, None, None, None),
        (31, create_time, 0, 'helpothers_transport_num', 0, 3, 0, 0, 0, 2, 4, None, None, None),
        (32, create_time, 0, 'helpothers_transport_price', 0, 50, 0, 0, 0, 2, 4, None, None, None),
        (33, create_time, 0, 'twoyear_illegaltimes', 0, 10000, 0, 0, 0, 5, 8, None, None, None),
        (34, create_time, 0, 'in_province_times', 0, 3, 0, 0, 0, 2, 4, None, None, None),
        (35, create_time, 0, 'in_province_num', 0, 50, 0, 0, 0, 2, 4, None, None, None),
        (36, create_time, 0, 'in_province_price', 0, 10000, 0, 0, 0, 2, 4, None, None, None),
        (37, create_time, 0, 'out_of_province_times', 0, 3, 0, 0, 0, 3, 5, None, None, None),
        (38, create_time, 0, 'out_of_province_num', 0, 50, 0, 0, 0, 3, 5, None, None, None),
        (39, create_time, 0, 'out_of_province_price', 0, 10000, 0, 0, 0, 3, 5, None, None, None))
cursor.executemany(sql, data)
conn.commit()
