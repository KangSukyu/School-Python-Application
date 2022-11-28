import pandas as pd
import random
import matplotlib.pyplot as plt
data = pd.read_csv("kadai05\kokusei_pop_2015.csv",encoding= "utf-8-sig", usecols=[7,8], header=1)

plt.rcParams['font.family'] = "MS Gothic"

nums1 = []
nums2 = []

is_First = True
for row in data:
    # if is_First:
    #     xtext = row[0]
    #     ytext = row[1]
    #     is_First = False
    # else:
        nums1.append(int(row[0]))
        nums2.append(int(row[1]))

s1 = pd.Series(nums1)
s2 = pd.Series(nums2)

res = s1.corr(s2)
text = f"相関係数：{res}"
plt.text(0,10, text)

text = f"名都道府県における男女別人口の散布図（２０１５年）"
plt.text(1,10.5, text)

plt.xlabel("男性人口")
plt.ylabel("女性人口")
plt.scatter(nums1, nums2)
plt.show()