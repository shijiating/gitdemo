import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from time import time
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib


customer_test_data = pd.read_csv(r'C:\DATA\data-test-300+100-englow(test).csv', encoding='GB2312')
customer_test_result=pd.read_csv(r'C:\DATA\svm_test_result.csv', encoding='GB2312')
cigar_svm_model=joblib.load(r'C:\Users\Administrator\Desktop\yutong\后台\后台\neural_network\SVM\svm_model\cigar_svm_model')


target=customer_test_result['result'].values
cigar400_predict=cigar_svm_model.predict(customer_test_data)
print(cigar400_predict)
print("模型在测试集上的表现: %s" % cigar_svm_model.score(customer_test_data,target))


