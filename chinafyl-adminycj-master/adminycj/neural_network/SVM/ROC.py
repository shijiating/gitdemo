# import pandas as pd
# import numpy as np
# from scipy import interp
# import matplotlib.pyplot as plt
#
# from sklearn import svm, datasets
# from sklearn.metrics import roc_curve, auc
# from sklearn.model_selection import StratifiedKFold
#
# ###############################################################################
# # Data IO and generation,导入iris数据，做数据准备
# customer_data = pd.read_csv(r'D:\桌面文件移动\实验室\烟草局\烟草违规预测\后台\neural_network\SVM\svm_model\data-train-1200+400-englowclean.csv', encoding='GB2312')
#
# # import some data to play with
# data=customer_data[['cigar_num','cigar_num','illegal_total','reduce_rank'
#                     ,'illegal_halfyear','criminal_penalty','illegal_twoyear'
#                     ,'flowout_total','flowout_num','sales_growth','stock_growth'
#                     ,'sales_ratio','sensitice_hometown','sensitive_canton'
#                     ,'averagePrice_ratio','bussiness_mid','bussiness_low'
#                     ,'bussiness_high','sensivetime_mid','sensivetime_low'
#                     ,'sensivetime_high']].values
# feature_name=['cigar_num','cigar_num','illegal_total','reduce_rank'
#               ,'illegal_halfyear','criminal_penalty','illegal_twoyear'
#               ,'flowout_total','flowout_num','sales_growth','stock_growth'
#               ,'sales_ratio','sensitice_hometown','sensitive_canton'
#               ,'averagePrice_ratio','bussiness_mid','bussiness_low'
#               ,'bussiness_high','sensivetime_mid','sensivetime_low'
#               ,'sensivetime_high']
# target=customer_data['result'].values
# species=['legal','illegal']
#
# # X = iris.data
# # y = iris.target
# # X, y = X[y != 2], y[y != 2]
# # n_samples, n_features = X.shape
#
# # Add noisy features
# random_state = np.random.RandomState(0)
# # X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
# customer_data = np.c_[customer_data]
# ###############################################################################
# # Classification and ROC analysis
# # 分类，做ROC分析
#
# # Run classifier with cross-validation and plot ROC curves
# # 使用6折交叉验证，并且画ROC曲线
# cv = StratifiedKFold(n_splits=10)
# classifier = svm.SVC(kernel='rbf', probability=True,
#                      random_state=random_state)
#
# # mean_tpr = 0.0
# # mean_fpr = np.linspace(0, 1, 100)
# # all_tpr = []
#
# tprs = []
# aucs = []
# mean_fpr = np.linspace(0, 1, 100)
#
# i = 0
# for train, test in cv.split(customer_data, target):
#     # 通过训练数据，使用svm线性核建立模型，并对测试集进行测试，求出预测得分
#     probas_ = classifier.fit(customer_data[train], target[train]).predict_proba(customer_data[test])
#     # Compute ROC curve and area the curve
#     # 通过roc_curve()函数，求出fpr和tpr，以及阈值
#     fpr, tpr, thresholds = roc_curve(target[test], probas_[:, 1])
#     tprs.append(interp(mean_fpr, fpr, tpr))
#     tprs[-1][0] = 0.0
#     roc_auc = auc(fpr, tpr)
#     aucs.append(roc_auc)
#     # 画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数能计算出来
#     plt.plot(fpr, tpr, lw=1, alpha=0.3, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
#     i += 1
#
# # 画对角线
# plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Luck', alpha=.8)
#
# mean_tpr = np.mean(tprs, axis=0)  # 在mean_fpr100个点，每个点处插值插值多次取平均
# mean_tpr[-1] = 1.0  # 坐标最后一个点为（1,1）
# mean_auc = auc(mean_fpr, mean_tpr)  # 计算平均AUC值
# # 画平均ROC曲线
#
# std_auc = np.std(aucs, axis=0)
# plt.plot(mean_fpr, mean_tpr, color='b',
#          label=r'Mean ROC (area = %0.2f)' % mean_auc, lw=2, alpha=.8)
#
# std_tpr = np.std(tprs, axis=0)
# tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
# tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
# plt.fill_between(mean_tpr, tprs_lower, tprs_upper, color='gray', alpha=.2,
#                  label=r'$\pm$ 1 std. dev.')
#
# plt.xlim([-0.05, 1.05])
# plt.ylim([-0.05, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc="lower right")
# plt.show()

# coding:utf-8
print(__doc__)

import numpy as np
from scipy import interp
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold

###############################################################################
# Data IO and generation,导入iris数据，做数据准备

# import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target
X, y = X[y != 2], y[y != 2]
n_samples, n_features = X.shape

# Add noisy features
random_state = np.random.RandomState(0)
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]

###############################################################################
# Classification and ROC analysis
# 分类，做ROC分析

# Run classifier with cross-validation and plot ROC curves
# 使用6折交叉验证，并且画ROC曲线
cv = StratifiedKFold(n_splits=6)
classifier = svm.SVC(kernel='linear', probability=True,
                     random_state=random_state)

# mean_tpr = 0.0
# mean_fpr = np.linspace(0, 1, 100)
# all_tpr = []

tprs = []
aucs = []
mean_fpr = np.linspace(0, 1, 100)

i = 0
for train, test in cv.split(X, y):
    # 通过训练数据，使用svm线性核建立模型，并对测试集进行测试，求出预测得分
    probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test])
    # Compute ROC curve and area the curve
    # 通过roc_curve()函数，求出fpr和tpr，以及阈值
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    tprs.append(interp(mean_fpr, fpr, tpr))
    tprs[-1][0] = 0.0
    roc_auc = auc(fpr, tpr)
    aucs.append(roc_auc)
    # 画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数能计算出来
    plt.plot(fpr, tpr, lw=1, alpha=0.3, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
    i += 1

# 画对角线
plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Luck', alpha=.8)

mean_tpr = np.mean(tprs, axis=0)  # 在mean_fpr100个点，每个点处插值插值多次取平均
mean_tpr[-1] = 1.0  # 坐标最后一个点为（1,1）
mean_auc = auc(mean_fpr, mean_tpr)  # 计算平均AUC值
# 画平均ROC曲线

std_auc = np.std(aucs, axis=0)
plt.plot(mean_fpr, mean_tpr, color='b',
         label=r'Mean ROC (area = %0.2f)' % mean_auc, lw=2, alpha=.8)

std_tpr = np.std(tprs, axis=0)
tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
plt.fill_between(mean_tpr, tprs_lower, tprs_upper, color='gray', alpha=.2,
                 label=r'$\pm$ 1 std. dev.')

plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

