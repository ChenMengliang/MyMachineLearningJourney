# -*- coding: UTF-8 -*-
# @Time             : 2019-02-28 10:21
# @Author           : Keith
# @File             : testAttr.py
# @Software         : PyCharm
# @About            : 测试pandas的基本属性和用法

import pandas as pd
import numpy as np

# 1.iloc
data=pd.DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('ABCD'))
print(data)

# 取第0列所有的行
# iloc 传的是index loc 传的是行名或者列名,:表示取这一行或者这一列的所有数据
# print(data.iloc[:,[0]])

# print(data.loc[:,['B']])

row = data.iloc[0,:]
# 求第0行中，值最大的那一列的列名
# print(row.idxmax())
# print(row.argmax())
print(row)
print(row.all())
# print(np.random.uniform(0,1,(1,2)))



