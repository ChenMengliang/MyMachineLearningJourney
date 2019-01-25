# -*- coding: UTF-8 -*-
# @Time             : 2019-01-24 10:20
# @Author           : Keith
# @File             : test.py
# @Software         : PyCharm
# @About            : 用Tensorflow计算a=(b+c)∗(c+2)
import tensorflow as tf


const = tf.constant(2.0, name='const')
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, dtype=tf.float32, name='c')

d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
a = tf.multiply(d, e, name='a')

# 1.定义init operation
init_op = tf.global_variables_initializer()

# session
with tf.Session() as sess:
#     # 2. 运行init operation
    sess.run(init_op)
#     # 计算
    a_out = sess.run(a)
    print("Variable a is {}".format(a_out))
