"""
如何筛选多个条件
"""
import pandas as pd

movies = pd.read_csv("data/imdb_1000.csv")

# 查出时长 >= 200, 并且是戏剧的电影
x = movies[(200 <= movies.duration) & ("Drama" == movies.genre)]
# print(x)

# 查出戏剧, 动作, 犯罪的电影
x = movies[("Drama" == movies.genre) | ("Action" == movies.genre) | ("Crime" == movies.genre)]
# 简化写法
x = movies[movies["genre"].isin(["Drama", "Action", "Crime"])]
print(x)