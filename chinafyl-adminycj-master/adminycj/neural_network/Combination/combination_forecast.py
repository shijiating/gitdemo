#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from neural_network.BP.BP_version3 import BPNeuralNetwork

start_time = pd.datetime.datetime.now()
def dataReader():
    # 读取数据
    data = pd.read_csv("combination_tain_613.csv", header=0)
    # 均值归一化nomalization
    for i in ['RBF', 'BP', 'LM',  'Result']:
        data[i] = (data[i] - min(data[i])) / (max(data[i]) - min(data[i]))
    return data


# def dataReader_test():
#     # 读取数据
#     data_test = pd.read_csv("data_test_3500.csv", header=0)
#     # 均值归一化nomalization
#     for i in ['NativePlace', 'AdministrativeArea', 'BusinessFormat', 'DownGrade', 'HalfYear', 'Total', 'TwoYear',
#               'ZhongHua', 'LiQun', 'InventoryRatio', 'Sale', 'Month', 'Result']:
#         data_test[i] = (data_test[i] - min(data_test[i])) / (max(data_test[i]) - min(data_test[i]))
#     return data_test

# zscore标准化
# def ZscoreNormalization(x):
#     """Z-score normaliaztion"""
#     x = (x - np.mean(x)) / np.std(x)
#     return x
'''
降维
'''
# pca = PCA(n_components=12)   #降到2维
# pca.fit(data)                  #训练
# newX=pca.fit_transform(data)   #降维后的数据
# # PCA(copy=True, n_components=2, whiten=False)
# print(pca.explained_variance_ratio_)  #输出贡献率
# print("__________newX___________")
# print(newX)                  #输出降维后的数据

nn = BPNeuralNetwork([3,4, 2], 'sigmoid')
data = dataReader()
print('-------data----------')
print(data)
# data_test = dataReader_test()
# print('-------data_test----------')
# print(data_test)
# print(data_test.loc[1,"Result"])
# data_clean = ZscoreNormalization(data)
# data_test_clean = ZscoreNormalization(data_test)
# print('-------data_clean----------')
# print(data_clean)
# print('-------data_test_clean----------')
# print(data_test_clean)
y1 = []  # 训练集
for j in range(500):
    if data.loc[j,"Result"] == 0:
        y1.append(np.array([1, 0]))  # 预测结果最后一列转数组

    elif data.loc[j,"Result"] == 1:
        y1.append(np.array([0, 1]))
y1 = np.array(y1)
# print(y1, '-------y1----------')
print(len(y1))
# y1_test = []  # 测试集
# for j in range(3500):
#     if data_test.loc[j,"Result"] == 0:
#         y1_test.append(np.array([1, 0]))  # 预测结果最后一列转数组
#
#     elif data_test.loc[j,"Result"]== 1:
#         y1_test.append(np.array([0, 1]))
# y1_test = np.array(y1_test)
# print(y1_test, '-------y1_test----------')
# print(len(y1_test))
nn.BPalgorithm(data.iloc[0:500, 0:3], y1, 0.003,500)
# nn.generalize(data_test.iloc[0:3501, 0:12], y1_test)

timespand = pd.datetime.datetime.now() - start_time
print("训练时长为：",timespand)