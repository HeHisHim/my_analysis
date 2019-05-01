import pandas as pd

movies = pd.read_csv("data/imdb_1000.csv")

# 对 genre数据简要的描述
genreDatas = movies["genre"].describe()

# 对 genre数据种类的计数
genreDatas = movies["genre"].value_counts()

# 计算种类所占百分比
genreDatas = movies["genre"].value_counts(normalize = True)

print(genreDatas)