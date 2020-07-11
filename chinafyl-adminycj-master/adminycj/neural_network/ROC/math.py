import matplotlib.pyplot as plt
# from keras.utils import to_categorical
# from sklearn import metrics
import numpy as np
from sklearn.metrics import roc_curve, auc  # 计算roc和auc


def acu_curve(y1, prob1, y2, prob2, y3, prob3):
    """
    画图
    :param y: 标准值们
    :param prob: 每个预测值对应的阳性概率
    :return:
    """
    # y真实prob预测
    fpr1, tpr1, threshold1 = roc_curve(y1, prob1, pos_label=1)  # 计算真阳性率和假阳性率, pos_label=2 是指在y中标签为2的是标准阳性标签，其余值是阴性
    print(fpr1)
    roc_auc1 = auc(fpr1, tpr1)  # 计算auc的值
    fpr2, tpr2, threshold2 = roc_curve(y2, prob2, pos_label=1)  # 计算真阳性率和假阳性率, pos_label=2 是指在y中标签为2的是标准阳性标签，其余值是阴性
    print(fpr2)
    roc_auc2 = auc(fpr2, tpr2)  # 计算auc的值
    fpr3, tpr3, threshold3 = roc_curve(y3, prob3, pos_label=1)  # 计算真阳性率和假阳性率, pos_label=2 是指在y中标签为2的是标准阳性标签，其余值是阴性
    print(fpr3)
    roc_auc3 = auc(fpr3, tpr3)  # 计算auc的值
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr1, tpr1, color='red',
             lw=lw, label='ROC curve (area = %0.3f)' % roc_auc1)  # 假正率为横坐标，真正率为纵坐标做曲线
    plt.plot(fpr2, tpr2, color='blue',
             lw=lw, label='ROC curve (area = %0.3f)' % roc_auc2)  # 假正率为横坐标，真正率为纵坐标做曲线
    plt.plot(fpr3, tpr3, color='green',
             lw=lw, label='ROC curve (area = %0.3f)' % roc_auc3)  # 假正率为横坐标，真正率为纵坐标做曲线

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.title('BP LM RBF _ROC', fontsize=20)
    plt.legend(loc="lower right", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()


# def direct_show(fpr, tpr):
#     roc_auc = auc(fpr, tpr)  # 计算auc的值
#
#     plt.figure()
#     lw = 2
#     plt.figure(figsize=(10, 10))
#     plt.plot(fpr, tpr, color='darkorange',
#              lw=lw, label='ROC curve (area = %0.3f)' % roc_auc)  # 假正率为横坐标，真正率为纵坐标做曲线
#     plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
#     plt.xlabel('False Positive Rate')
#     plt.ylabel('True Positive Rate')
#     plt.title('AUC')
#     plt.legend(loc="lower right")
#
#     plt.show()


if __name__ == '__main__':
    # y = np.array([1, 1, 2, 2])
    # scores = np.array([0.1, 0.4, 0.35, 0.8])
    # acu_curve(y, scores)

    data = np.loadtxt("./222.csv", delimiter=",", skiprows=0)
    tp_data = data.transpose()
    # acu_curve(tp_data[1], tp_data[0])
    acu_curve(tp_data[1], tp_data[0],tp_data[3], tp_data[2],tp_data[5], tp_data[4])

# DIRECT
# fprs = np.array([47/157, 41/157, 33/157, 30/157])
# tprs = np.array([34/52, 36/52, 37/52, 38/52])
# direct_show(fprs, tprs)
