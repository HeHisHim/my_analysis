"""
改变pandas数据列的数据类型
"""
import pandas as pd

drinks = pd.read_csv("data/drinks.csv")

"""
country                          object
beer_servings                     int64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object
"""

# 在加载数据的时候改变列的数据类型
drinks = pd.read_csv("data/drinks.csv", dtype = {"beer_servings": "float64"})

# 将 beer_servings 从int64 改成 float64
drinks["beer_servings"] = drinks["beer_servings"].astype("float64")

orders = pd.read_csv("data/chipotle.tsv", sep = "\t")
# 将 item_price字符串行 转换成 数字供计算用 (先剔除 $ 符号, 再转换成 float)
x = orders["item_price"].str.replace("$", "").astype("float64")
print(x.mean()) #  -- 7.464335785374297