#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from neural_network.BP.BP_version3 import BPNeuralNetwork

start_time = pd.datetime.datetime.now()
def dataReader():
    # 读取数据
    data = pd.read_csv("data_train_500.csv", header=0)
    # 均值归一化nomalization
    for i in ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3',
              'C1', 'C2', 'C3', 'D1', 'Result']:
        data[i] = (data[i] - min(data[i])) / (max(data[i]) - min(data[i]))
    return data


def dataReader_test():
    # 读取数据
    data_test = pd.read_csv("data_test_200.csv", header=0)
    # 均值归一化nomalization
    for i in ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3',
              'C1', 'C2', 'C3', 'D1', 'Result']:
        data_test[i] = (data_test[i] - min(data_test[i])) / (max(data_test[i]) - min(data_test[i]))
    return data_test

nn = BPNeuralNetwork([12,9, 2], 'sigmoid')
data = dataReader()
print('-------data----------')
print(data)
data_test = dataReader_test()
print('-------data_test----------')
print(data_test)

y1 = []  # 训练集
for j in range(500):
    if data.loc[j,"Result"] == 0:
        y1.append(np.array([1, 0]))  # 预测结果最后一列转数组

    elif data.loc[j,"Result"] == 1:
        y1.append(np.array([0, 1]))
y1 = np.array(y1)
# print(y1, '-------y1----------')
# print(len(y1))
y1_test = []  # 测试集
for j in range(209):
    if data_test.loc[j,"Result"] ==0:
        y1_test.append(np.array([1, 0]))  # 预测结果最后一列转数组

    elif data_test.loc[j,"Result"]==1:
        y1_test.append(np.array([0, 1]))
y1_test = np.array(y1_test)
# print(y1_test, '-------y1_test----------')
# print(len(y1_test))
nn.BPalgorithm(data.iloc[0:500, 0:12], y1, 0.003,500)
timespand = pd.datetime.datetime.now() - start_time
print("训练时长为：",timespand)