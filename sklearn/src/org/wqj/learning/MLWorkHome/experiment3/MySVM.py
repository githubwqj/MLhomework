# coding=utf-8
from sklearn import svm
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
import os

data = []
labels = []

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("sklearn\\") + len("sklearn\\")]
dataPath = rootPath + "Input/MLWorkHome/experiment3/data.txt"
# 读取身高体重数据集
with open(dataPath) as ifile:
    for line in ifile:
        tokens = line.strip().split(' ')
        # data列表存储身高体重数据
        data.append([float(tk) for tk in tokens[:-1]])
        # label列表存储此人被定义为胖还是瘦
        labels.append(tokens[-1])
# x: 以array形式存储身高体重构成的坐标
x = np.array(data)
# labels: 将label列表array化
labels = np.array(labels)
y = np.zeros(labels.shape)

# y：存储0,1化的体重标签，值为0说明此人被定义为瘦，值为1说明此人定义为胖
y[labels == 'fat'] = 1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.0)

# 建立画布（可以不用关心具体的实现过程）
h = .02
x_min, x_max = x_train[:, 0].min() - 0.1, x_train[:, 0].max() + 0.1
y_min, y_max = x_train[:, 1].min() - 1, x_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# 绘图名称
titles = ['LinearSVC (linear kernel)',
          'SVC with polynomial kernel',
          'SVC with RBF kernel',
          'SVC with Sigmoid kernel']
# 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'
# 建立模型并拟合数据
# 核函数为线性函数
clf_linear = svm.SVC(kernel='linear').fit(x, y)
# 核函数为多项式函数
clf_poly = svm.SVC(kernel='poly',degree=2).fit(x, y)
# 核函数为径向基函数
clf_rbf = svm.SVC(kernel='rbf').fit(x, y)
# 核函数为Sigmoid函数
clf_sigmoid = svm.SVC(kernel='sigmoid').fit(x, y)

for i, clf in enumerate((clf_linear, clf_poly, clf_rbf, clf_sigmoid)):
    answer = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # 设置位置和大小
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    # 将数据点绘制在坐标图上
    z = answer.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)

    plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=plt.cm.Paired)
    plt.xlabel('Height(m)')
    plt.ylabel('Weight(kg)')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()
