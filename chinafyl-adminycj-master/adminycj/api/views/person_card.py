# 把需要用到的库一股脑import进来
import importlib, sys

importlib.reload(sys)
import time
import requests
from lxml import etree
from openpyxl.workbook import Workbook
from bs4 import BeautifulSoup
import random


#该模块会根据所要访问的网站的协议类型自动的选择合适的ip

#随机选择列表中的字典，直到匹配上可以使用的ip


time1 = time.time()  # 定义个时间，为了后面可以记录一下代码执行的时长
import pandas as pd

# 先将存有身份证号码信息的txt文件读取进来
df = pd.read_csv(r"C:\Users\Administrator\Desktop\demo.txt", sep='\t', header=None, dtype=str, na_filter=False)

# 定义接下来存储身份证号码、性别、生日、户籍地信息的4个list
idcard = []
sex1 = []
birthday1 = []
address1 = []

# 看一下读取进来的一共有多少个身份证号码
length = len(df)
print(length)

# 通过循环，依次将每个身份证号码对应的信息获取
for i in range(0, length):


    # 多一个try，防止某个号码出差自己中止代码执行
    try:
        procxy = [
            {'http': 'HTTP://121.52.208.200:808',
             'https': 'HTTPS://111.177.106.231:9999'
             },
            {'http': 'HTTP://180.119.68.10:9999',
             'https': 'HTTPS://123.169.34.240:4366'
             }
        ]
        http = random.choice(procxy)
        # 查看身份证查询网页的网址，发现规律，按照规律组成url
        url = "https://qq.ip138.com/idsearch/index.asp?userid=" + df.iloc[i, 0] + "&action=idcard"
        print(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        }
        # 解析网页
        time.sleep(random.random() * 3)
        res = requests.get(url, timeout=500, proxies=http,headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')

        # 将网页中需要的信息所有在的模块切出来
        mainpart = soup.select('div[class="bd"] table tbody tr')
        print(mainpart)
        # 将信息取出并存入list中
        if len(mainpart) > 4:
            sex = mainpart[1].text.split('性别')[1]
            birthday = mainpart[2].text.split('出生日期')[1]
            address = mainpart[4].text.split('发证地')[1]

            idcard.append(df.iloc[i, 0])
            sex1.append(sex)
            birthday1.append(birthday)
            address1.append(address)
            print(idcard)
            print(sex1)
            print(birthday1)
            print(address1)
        else:
            continue
    except Exception as e:
        print(Exception, ":", e)

# 打包数据
data = pd.DataFrame({'idcard': idcard, 'sex': sex1, 'birthday': birthday1, 'address': address1})
print("data",data)

# 将数据输出成一个excel文件
#pd.DataFrame.to_excel(data, r"C:\Users\Administrator\Desktop\person_card1.xlsx", header=True, encoding='gbk',
#                      index=False)

time2 = time.time()
print(u'ok,结束!')
print(u'总共耗时：' + str(time2 - time1) + 's')
