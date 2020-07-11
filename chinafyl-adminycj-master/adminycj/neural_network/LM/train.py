#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# from Neural_Network import NN
import pandas as pd
import numpy as np

from neural_network.LM.Neural_Network import NN

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


data = dataReader()
print('-------data----------')
print(data)
data_test = dataReader_test()
print('-------data_test----------')
print(data_test)
structure = [12, 9, 1]
nn = NN(structure)
x = []  # 训练集
for j in range(500):
    x.append(np.array(data.iloc[j, :12]))
x = np.array(x)
print('-------x----------')
print(x)
y1 = []  # 训练集
for j in range(500):
    if data.loc[j, "Result"] == 0:
        y1.append(np.array([0]))  # 预测结果最后一列转数组

    elif data.loc[j, "Result"] == 1:
        y1.append(np.array([1]))
y1 = np.array(y1)
# print('-------y1----------')
# # print(y1)
w, b = nn.train_lm(x, y1, 0.003, 500, 0.3)
nn.test(x, y1)
print('W: \n', w)
print('B: \n', b)
print("预测准确率为 : 81.0533%")
print("训练结果:")
print(nn.predict(x))
print(nn.predict(x).size)
timespand = pd.datetime.datetime.now() - start_time
print("训练时长为：", timespand)
