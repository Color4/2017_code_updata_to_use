import tensorflow as tf

matrix1 = tf.constant([[3.,2.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1,matrix2)
sess = tf.Session()
with tf.Session() as sess:
    result = sess.run([product])
    print(result)
