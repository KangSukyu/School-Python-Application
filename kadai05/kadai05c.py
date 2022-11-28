import pandas as pd
import random
# data = []
# for i in range(100):
#     data = random.randint(1,6)

data = [random.randint(1, 6) for i in range(10000)] 

score_series = pd.Series(data=data)
score_desc = score_series.describe()
print(score_desc)