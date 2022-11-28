import pandas as pd
scores = [90, 70, 60, 80, 100, 40, 70, 60, 70, 80]
names = [
    "青山", "伊藤", "江川", "大森", "加藤",
    "佐藤", "鈴木", "高樫", "中田", "山本"
    ]
score_series = pd.Series(data=scores, index=names)
score_desc = score_series.describe()
print(score_desc)