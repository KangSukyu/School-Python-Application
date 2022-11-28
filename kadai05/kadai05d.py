import pandas as pd
data = pd.read_csv("kadai05\shift_202210.csv")

scores_df = pd.DataFrame(data=data)
scores_judge = scores_df == "〇"
print("出勤日数")
print(scores_judge.drop(columns=scores_judge.columns[[0, 1]]).sum())