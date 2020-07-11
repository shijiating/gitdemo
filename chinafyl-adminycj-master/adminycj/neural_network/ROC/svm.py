#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from time import time
from sklearn.preprocessing import StandardScaler
import datetime

customer_data = pd.read_csv(r'C:\Users\22259\Desktop\data-test200-clean.csv', encoding='GB2312')

#customer_data

customer_data.shape

data = customer_data[
    ['涉烟条数', '涉烟案值', '历史违法总次数', '是否有降级降档', '近半年内是否有违法记录', '是否有刑事处罚', '近两年内违法次数', '码段外流次数', '码段外流条数', '码段外流价值', '周进货增长率',
     '要货-订货', '敏感时间', '是否为敏感籍贯', '是否为敏感行政区', '进货周期内订购卷烟均价与前三个进货周期均价比', 'x0_中', 'x0_低', 'x0_高']].values
feature_name = ['涉烟条数', '涉烟案值', '历史违法总次数', '是否有降级降档', '近半年内是否有违法记录', '是否有刑事处罚', '近两年内违法次数', '码段外流次数', '码段外流条数',
                '码段外流价值', '周进货增长率', '要货-订货', '敏感时间', '是否为敏感籍贯', '是否为敏感行政区', '进货周期内订购卷烟均价与前三个进货周期均价比', 'x0_中', 'x0_低',
                'x0_高']
target = customer_data['结果'].values
species = ['守法户', '违法户']

np.unique(target)  # 数据量非常大的时候可以使用此代码查看标签有几种分类

plt.scatter(data[:, 0], data[:, 1], c=target)
plt.show()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(data, target, test_size=0.3, random_state=420)

Kernel = ["linear", "rbf", "sigmoid"]

for kernel in Kernel:
    time0 = time()
    clf = SVC(kernel=kernel
              , gamma="auto"
              , degree=1
              , cache_size=5000
              ).fit(Xtrain, Ytrain)
    print("The accuracy under kernel %s is %f" % (kernel, clf.score(Xtest, Ytest)))

time()

import pandas as pd

customer_data.describe([0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]).T
X = StandardScaler().fit_transform(customer_data)
standardData = pd.DataFrame(X)
standardData.describe([0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]).T

Xtrain, Xtest, Ytrain, Ytest = train_test_split(data, target, test_size=0.3, random_state=420)

Kernel = ["linear", "rbf", "sigmoid"]

for kernel in Kernel:
    time0 = time()
    clf = SVC(kernel=kernel
              , gamma="auto"
              , degree=1
              , cache_size=5000
              ).fit(Xtrain, Ytrain)
    print("The accuracy under kernel %s is %f" % (kernel, clf.score(Xtest, Ytest)))
