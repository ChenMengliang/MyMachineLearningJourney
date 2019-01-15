# -*- coding: UTF-8 -*-
# @Time             : 2019-01-15 11:29
# @Author           : Keith
# @File             : test1.py
# @Software         : PyCharm
# @About            : numpy 几种属性测试

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)

# 纬度
print('number fo dimension:', array.ndim)

# 行数和列数
print('shape:', array.shape)

# 元素个数
print('size:', array.size)
