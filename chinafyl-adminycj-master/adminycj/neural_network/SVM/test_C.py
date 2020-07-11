import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from time import time
import datetime

customer_data = pd.read_csv(r'D:\桌面文件移动\实验室\烟草局\烟草违规预测\后台\neural_network\SVM\svm_model\data-train-1200+400-lowclean.csv', encoding='GB2312')

data=customer_data[['涉烟条数','历史违法总次数','是否有降级降档','近半年内是否有违法记录','是否有刑事处罚','近两年内违法次数','码段外流次数','码段外流条数','销售增长率','周进货增长率','存销比','是否为敏感籍贯','是否为敏感行政区','进货周期内订购卷烟均价与前三个进货周期均价比','经营业态_中','经营业态_低','经营业态_高','敏感时间_中','敏感时间_低','敏感时间_高']].values
feature_name=['涉烟条数','历史违法总次数','是否有降级降档','近半年内是否有违法记录','是否有刑事处罚','近两年内违法次数','码段外流次数','码段外流条数','销售增长率','周进货增长率','存销比','是否为敏感籍贯','是否为敏感行政区','进货周期内订购卷烟均价与前三个进货周期均价比','经营业态_中','经营业态_低','经营业态_高','敏感时间_中','敏感时间_低','敏感时间_高']
target=customer_data['结果'].values
species=['守法户','违法户']
np.unique(target)  # 数据量非常大的时候可以使用此代码查看标签有几种分类

Xtrain, Xtest, Ytrain, Ytest = train_test_split(data, target, test_size=0.2, random_state=420)

score = []
C_range = np.linspace(0.01, 10, 50)
for i in C_range:
    clf = SVC(kernel="rbf", C=i, gamma=0.18507465086393204, cache_size=5000).fit(Xtrain, Ytrain)
    score.append(clf.score(Xtest, Ytest))

print(max(score), C_range[score.index(max(score))])
plt.plot(C_range, score)
plt.show()