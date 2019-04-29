"""
过滤数据
"""
import pandas as pd

movies = pd.read_csv("data/imdb_1000.csv")

"""
V1

1. 创建一个列表, 遍历原数据并保存 时长 >= 200的所有bool值, 这个列表只有True or False
2. 将该列表转换为pandas.Series类型
3. 传入pandas.DataFrame过滤
"""
def filter_V1():
    booleans = []
    for length in movies.duration:
        if 200 <= length:
            booleans.append(True)
        else:
            booleans.append(False)
    # print(booleans[:5]) # -- [False, False, True, False, False]
    # print(len(booleans)) # -- 979

    is_long = pd.Series(booleans)
    # print(type(is_long)) # -- <class 'pandas.core.series.Series'>

    print(movies[is_long])

"""
V2
1. 直接将过滤条件赋值到某变量
2. 再传入pandas.DataFrame过滤
"""
def filter_V2():
    is_long = movies.duration >= 200
    # print(type(is_long)) # -- <class 'pandas.core.series.Series'>
    print(movies[is_long])

"""
V3
直接将过滤条件传入pandas.DataFrame
"""
def filter_V3():
    # print(type(movies.duration >= 200))  # -- <class 'pandas.core.series.Series'>
    print(movies[movies.duration >= 200])


