"""
read_csv
"""

import pandas as pd

# .tsv文件以 \t 为分隔符, 所以在调用 read_csv时, 要传参 sep = "\t"
others = pd.read_csv("data/chipotle.tsv", sep = "\t")
# 取前n行, 默认 n = 5
others = others.head(7)
print(others)