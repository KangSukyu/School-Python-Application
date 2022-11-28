import pandas as pd

data = pd.read_csv("kadai05\sangiin_tokyo.csv",index_col=0)
x = data.mean(axis="index")
y = data.max(axis="index")
z = data.min(axis="index")

print("平均投票率："  + str(x["投票率（％）"]))
print("最高投票率："  + str(y["投票率（％）"]))
print("最低投票率："  + str(z["投票率（％）"]))
