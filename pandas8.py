import pandas as pd

drinks = pd.read_csv("data/drinks.csv")

# 删除行 删除第 0 行, axis = 0 表示操作的是行
filter_drinks = drinks.drop(0, axis = 0)

# 删除列 删除continent列, axis = 1 表示操作的是列
filter_drinks = drinks.drop("continent", axis = 1)

# axis = 0表示操作行, 类似从上到下压缩数据
summary_drinks = drinks.mean(axis = 0)

# axis = 1表示操作列, 类似从左到右压缩数据
summary_drinks = drinks.mean(axis = 1)

# print(summary_drinks)
# print(filter_drinks.head())