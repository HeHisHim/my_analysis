"""
删除某些列
"""

import pandas as pd

ufo = pd.read_csv("data/ufo.csv")

# axis = 0 or 1, 0 表示操作行, 1 表示操作列. 当为0时, 第一个参数需传入一个list表示需要删除的行
# inplace 是否就地操作, 不返回, 默认为False. 当为False时, 表示不修改原数据. 为True时, 修改原数据

ufo.drop("Colors Reported", axis = 1, inplace = True)

print(ufo.head())