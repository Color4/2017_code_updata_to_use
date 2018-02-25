# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:57:08 2018

@author: zhangp
"""

from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# 首先生成3x2的原始特征矩阵
# 即样本数为3，特征数为2
X = np.arange(6).reshape(3, 2)

print('原始数据：')
print(X)

# 特生变换/特征生成
# 将原始一阶数据升维到二阶数据
# 升维方式是： [x_1, x_2] 变为 [1, x_1, x_2, x_1^2, x_1 x_2, x_2^2]
polyFeat = PolynomialFeatures(degree=2)
X_transformed = polyFeat.fit_transform(X)

print('特征变换后的数据：')
print(X_transformed)