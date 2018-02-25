# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:18:31 2017

@author: zhangp
"""

import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam

# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# X shape (60,000 28x28), y shape (10,000, )
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train)
# data pre-processing
X_train = X_train.reshape(-1, 1,28, 28)/255.
X_test = X_test.reshape(-1, 1,28, 28)/255.

print(X_train)


X_batch = X_train[1: 3, :, 1:3]
print('++++++++++++++++++++++++++++++++')
print(X_batch)