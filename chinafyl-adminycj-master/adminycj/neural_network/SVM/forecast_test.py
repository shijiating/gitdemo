import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from time import time
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib


customer_test_data = pd.read_csv(r'svmdata.csv', encoding='GB2312')

cigar_svm_model=joblib.load(r'cigar_svm_model')



cigar_predict=cigar_svm_model.predict(customer_test_data)
print(cigar_predict)
