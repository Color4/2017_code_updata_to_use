import tensorflow as tf
import numpy as np
a = tf.constant([1.0, 2.0], name = 'a')
b = tf.constant([2.0, 3.0], name = 'b')
init=tf.global_variables_initializer()
result = tf.add(a,b,name = 'add')
print(result)

print(a.graph is tf.get_default_graph())

print('two_seeion')
init=tf.global_variables_initializer()
g1 = tf.Graph()
with g1.as_default():
    v = tf.get_variable('v', initializer = tf.zeros_initializer(),shape = [1])

g2 = tf.Graph()
with g2.as_default():
    v = tf.get_variable('v', initializer = tf.ones_initializer(),shape = [1])

init=tf.global_variables_initializer()
with tf.Session(graph = g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('',reuse = True):
        print(sess.run(tf.get_variable('v')))

with tf.Session(graph = g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('',reuse = True):
        print(sess.run(tf.get_variable('v')))

import tensorflow as tf
a=tf.constant(10)
print(a)
x=tf.Variable(tf.ones([3,3]))
y=tf.Variable(tf.zeros([3,3]))
init=tf.global_variables_initializer()
result = tf.add(x,y,name = 'add')
print(result)


print('three session')

x = np.array([[1,1,1],[1,-8,1],[1,1,1]])
w = tf.Variable(initial_value = x)
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(w))

x = tf.placeholder(tf.float32, [None, 784])

x = 3
y = 2
z = x + y
print(z)

print('four session')

a = tf.Variable(3)
b = tf.Variable(4)
z = tf.add(a,b)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(z))

print('five session')

word = tf.constant('hello world')
with tf.Session() as sess:
    print(sess.run(word))


a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)
with tf.Session() as sess:
    print('a + b =', sess.run(add, feed_dict = {a:2, b:3}))
    print('a * b =', sess.run(mul, feed_dict = {a:2, b:3}))

a = tf.Variable(tf.ones([3,2]))
b = tf.Variable(tf.ones([2,3]))
product = tf.matmul(5*a,4*b)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(product))


print('second_paper')

import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


print(mnist.train.images.shape)
print(mnist.train.labels.shape)
print(mnist.validation.images.shape)
print(mnist.validation.labels.shape)
print(mnist.test.images.shape)
print(mnist.test.labels.shape)

#import tensorflow.contrib.learn.python.learn.datasets.base as base
from tensorflow.contrib.learn.python.learn.datasets import base
iris_data,iris_label = base.load_iris()
house_data,house_label = base.load_boston()

print(iris_data.shape)
print(house_data.shape)

from tensorflow.python.keras._impl.keras.datasets import cifar10
cifar10.load_data()
image, lables = cifar10.distorted_inputs()
print(images)
print(lables)









































