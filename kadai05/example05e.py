import pandas as pd
import random
import matplotlib.pyplot as plt
data = pd.read_csv("kadai05\kokusei_pop_2015.csv")

plt.rcParams['font.family'] = "MS Gothic"

nums1 = []
nums2 = []
for _ in range(50):
    nums1.append(random.uniform(0,10))
    nums2.append(random.uniform(0,10))

s1 = pd.Series(nums1)
s2 = pd.Series(nums2)

res = s1.corr(s2)
text = f"相関係数：{res}"
plt.text(0,10.5, text)

plt.scatter(nums1, nums2)
plt.show()