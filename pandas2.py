import pandas as pd

ufo = pd.read_csv("data/ufo.csv")

print(ufo.shape) # 18241行, 5列

print(type(ufo)) # -- <class 'pandas.core.frame.DataFrame'>

# 可以直接调用 [ key ] 来取对应的列数据, 也可以使用 .key来获取
theCity = ufo["City"] # ufo.City
print(type(theCity)) # -- <class 'pandas.core.series.Series'>

# 可自定义列名
# 列之间的连接可以像字符串一样拼接
ufo["Location"] = ufo["City"] + " - " + ufo["State"]

# print(type(ufo["Location"])) # -- <class 'pandas.core.series.Series'>

print(ufo.shape) # 18241行, 6列

print(ufo.head())