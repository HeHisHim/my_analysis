"""
修改 表头名称 的几种方式
"""
import pandas as pd

ufo = pd.read_csv("data/ufo.csv")
# print(ufo.columns) # -- Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')

# 1. rename
# ufo.rename(columns = {"Colors Reported": "Colors_Reported", "Shape Reported": "Shape_Reported"}, inplace = True)

# 2. ufo.columns = [...]
ufo_cols = ["city", "Colors_Reported", "Shape_Reported", "State", "Time"]
# ufo.columns = ufo_cols

# 3. read_csv(name = xxx, header = 0)
# ufo = pd.read_csv("data/ufo.csv", names = ufo_cols, header = 0)

# 4. table.columns.str.replace(old, new)
ufo.columns = ufo.columns.str.replace(" ", "_")

print(ufo.head())
# print(ufo.columns) # -- Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')
