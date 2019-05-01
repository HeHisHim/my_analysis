"""
groupby
"""

import pandas as pd

drinks = pd.read_csv("data/drinks.csv")
groupbyDrink = drinks.groupby("continent")
# print(type(groupbyDrink)) # -- <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# 获取每个州的啤酒平均供应量
drinkDatas = groupbyDrink["beer_servings"].mean()

# 获取每个州的啤酒供应量最大值
drinkDatas = groupbyDrink["beer_servings"].max()

# 获取每个州的啤酒供应量最小值
drinkDatas = groupbyDrink["beer_servings"].min()

# 获取每个州的啤酒供应量计数
drinkDatas = groupbyDrink["beer_servings"].count()

# 同时获取多个聚合数据
drinkDatas = groupbyDrink["beer_servings"].agg(["count", "max", "min", "mean"])
print(drinkDatas)