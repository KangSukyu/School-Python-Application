import pandas as pd
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
water = [
    43.5, 88.5, 173.0, 156.0, 99.5,
    168.5, 310.0, 382.5, 222.5, 199.5, 93.0, 116.0
    ]
score_series = pd.Series(data=water, index=month)
score_desc = score_series.describe()
print(score_desc)