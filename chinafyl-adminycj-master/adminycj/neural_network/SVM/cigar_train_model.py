import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from time import time
import datetime
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

customer_data = pd.read_csv(r'C:\DATA\data-train-1200+400-englow(train).csv', encoding='GB2312')
customer_train_result=pd.read_csv(r'C:\DATA\svm_train_result.csv', encoding='GB2312')
# , index_col=0

data=customer_data[['maximum_cigar_num','whole_illegaltimes','twoyear_illegaltimes'
                          ,'is_halfyear_illegal','outofprovince_times','maximum_outofprovince_num'
                          ,'is_criminal','business_format','is_sensitivecircle','is_downgrade'
                          ,'is_sensitive_canton','is_sensitive_nativeplace','purchase_change','required_differ'
                          ,'purchase_price','sensitive_month','is_bigillegal']].values

feature_name=['maximum_cigar_num','whole_illegaltimes','twoyear_illegaltimes'
                          ,'is_halfyear_illegal','outofprovince_times','maximum_outofprovince_num'
                          ,'is_criminal','business_format','is_sensitivecircle','is_downgrade'
                          ,'is_sensitive_canton','is_sensitive_nativeplace','purchase_change','required_differ'
                          ,'purchase_price','sensitive_month','is_bigillegal']
print(customer_data.shape)
target=customer_train_result['result'].values
species=['legal','illegal']

clf=SVC(kernel="rbf"
        ,gamma="auto"
        ,cache_size=5000
        ,C=0.2136607510970837
        ).fit(customer_data,target)

cigar_svm_model = r'C:\Users\Administrator\Desktop\yutong\后台\后台\neural_network\SVM\svm_model\cigar_svm_model.pkl'

joblib.dump(clf,"cigar_svm_model")
print("训练完成了")
print("训练集测试评分: % s" % clf.score(data,target))

# time0=time()
# gamma_range = gamma_range=np.logspace(0,0.5,100)
# C_range = np.linspace(0.01,10,50)
#
# param_grid=dict(gamma=gamma_range,C=C_range)
#
# cv=StratifiedShuffleSplit(n_splits=10,test_size=0.1)
# grid=GridSearchCV(SVC(kernel="rbf",cache_size=5000),param_grid=param_grid,cv=cv)
#
# grid.fit(customer_data,target)
#
# print("C与gamma最佳参数取值组合为： %s 可达到的效果为： %0.5f" % (grid.best_params_,grid.best_score_))
# print(datetime.datetime.utcfromtimestamp(time()-time0).strftime("%M:%S:%f"))




#
# print("C与gamma最佳参数取值组合为： {'C':0.2136607510970837,'gamma':0.18706721979366404} 可达到的效果为： 0.78650")
# print("26:33:878916")