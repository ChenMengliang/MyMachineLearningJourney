# -*- coding: UTF-8 -*-
# @Time             : 2019-01-15 16:00
# @Author           : Keith
# @File             : compute.py
# @Software         : PyCharm
# @About            : numpy基础运算

import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)

#矩阵减法 对应元素相减
c = a - b
print(c)
#乘方运算
c = b**2
print(c)

print(b<3)

#矩阵乘法 对应元素相乘
a = np.array([[1,0],[0,1]])
b = np.arange(4).reshape(2,2)

c = a*b
print(c)
#一行*一列
c = a.dot(b)
# c = np.dot(a,b) 等同上面的写法
print(c)

#sum min max
a = np.random.random((2,4))
print(a.sum())
print(a.min())
print(a.max())

#axis==0 按列求和，axis=1按行求和
print("sum=",np.sum(a,axis=0))
print("sum=",np.sum(a,axis=1))