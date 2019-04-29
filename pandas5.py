"""
排序函数
"""
import pandas as pd

movies = pd.read_csv("data/imdb_1000.csv")

# ascending 默认为 True, 表示升序. False表示降序
# 以下只改变某一列的数据
sort_titles = movies["title"].sort_values(ascending = False)
# print(sort_titles)

# 按 title 列来排序
sort_all = movies.sort_values("title")
# print(movies.sort_values("title").head())
# print(sort_all.head())

# 按多个列排序, 先按 star_rating升序, 再按 duration升序
sort_muls = movies.sort_values(["star_rating", "duration"])
print(sort_muls.head())
