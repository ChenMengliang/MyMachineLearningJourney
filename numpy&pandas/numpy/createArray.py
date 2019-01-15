# -*- coding: UTF-8 -*-
# @Time             : 2019-01-15 14:16
# @Author           : Keith
# @File             : createArray.py
# @Software         : PyCharm
# @About            : numpy 创建array测试

import numpy as np


a = np.array([2,23,4])
print(a)

a = np.array([2,23,4],dtype=np.float32)
print(a)

a = np.array([[2,3,4],[4,5,6]])
print(a)

a = np.zeros((3,4))
print(a)

print(np.ones((3,4),dtype=np.int))

#arange create continuous array
a = np.arange(10,20,2)

print(a)
#reshape 改变数据形状
a = np.arange(12).reshape((3,4))
print(a)

#linspace 创建线段型数据
a = np.linspace(1,10,20)#开始端1 结束端10,分割成20个数据段，生成线段
print(a)

a = a.reshape((5,4))
print(a)