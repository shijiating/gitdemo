#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime

from numpy import *
from neural_network.RBF.rbf_trian import get_predict


def load_data(file_name):
    '''导入数据
    input:  file_name(string):文件的存储位置
    output: feature_data(mat):特征
    '''
    f = open(file_name)  # 打开文件
    feature_data = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split(",")
        for i in range(len(lines)-1):
            lines[i]=float(lines[i])
            feature_tmp.append(lines[i])
        feature_data.append(feature_tmp)
        print(feature_data)
    f.close()  # 关闭文件
    return mat(feature_data)

def generate_data():
    '''在[-4.5,4.5]之间随机生成20000组点
    '''
    # 1、随机生成数据点
    data = mat(zeros((200, 2)))
    m = shape(data)[0]
    x = mat(random.rand(200, 2))
    for i in range(m):
        data[i, 0] = x[i, 0] * 9 - 4.5
        data[i, 1] = x[i, 1] * 9 - 4.5
    # 2、将数据点保存到文件“test_data”中
    f = open("test.txt", "w")
    m, n = shape(data)
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(str(data[i, j]))
        f.write("\t".join(tmp) + "\n")
    f.close()


def load_model(file_center, file_delta, file_w):
    def get_model(file_name):
        f = open(file_name)
        model = []
        for line in f.readlines():
            lines = line.strip().split("\t")
            model_tmp = []
            for x in lines:
                model_tmp.append(float(x.strip()))
            model.append(model_tmp)
        f.close()
        return mat(model)

    # 1、导入rbf函数中心
    center = get_model(file_center)

    # 2、导入rbf函数扩展常数
    delta = get_model(file_delta)

    # 3、导入隐含层到输出层之间的权重
    w = get_model(file_w)

    return center, delta, w


def save_predict(file_name, pre):
    '''保存最终的预测结果
    input:  pre(mat):最终的预测结果
    output:
    '''
    f = open(file_name, "w")
    m = shape(pre)[0]
    result = []
    for i in range(m):
        result.append(str(round((pre[i, 0]),0)))
    f.write("\n".join(result))
    f.close()


if __name__ == "__main__":
    generate_data()
    start_time = datetime.datetime.now()
    # 1、导入测试数据
    print("--------- 1.load data ------------")
    dataTest = load_data("data_train_500.txt")
    print(dataTest)
    print(type(dataTest))
    # 2、导入神经网络模型
    print("--------- 2.load model ------------")
    center, delta, w = load_model("center.txt", "delta.txt", "weight.txt")
    # 3、得到最终的预测值
    print("--------- 3.get prediction ------------")
    result = get_predict(dataTest, center, delta, w)
    # 4、保存最终的预测结果
    print("--------- 4.save result ------------")
    save_predict("test_result.txt", result)
    timespand = datetime.datetime.now() - start_time
    # print("训练集准确率：0.982289")
    # print("训练时间：1:21:10.195477")
    # print("测试集准确率：0.928562")
    print("测试集时间：",timespand)