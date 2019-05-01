import pandas as pd

orders = pd.read_csv("data/chipotle.tsv", sep = "\t")
# 将 item_name列的数据全部转换为大写字母
upperOrder = orders["item_name"].str.upper()

# item_name列的数据是否包含 chicken 单词
containOrder = orders["item_name"].str.contains("Chicken")

# 保留含有 Chicken 的数据
filterOrder = orders[containOrder]

# 剔除 choice_description 数据的左右方括号
choiceData = orders["choice_description"].str.replace("[", "").str.replace("]", "")

print(choiceData.head())