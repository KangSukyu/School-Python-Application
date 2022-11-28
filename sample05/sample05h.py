import pandas as pd
scores = [
    [82, 67, 71, 91, 98], 
    [80, 98, 99, 60, 87],
    [97, 100, 100, 98, 96],
    [73, 60, 62, 77, 64]
    ]
names = ["青山", "伊藤", "江川", "大森"]
subjects = ["国語","数字","料理","社会","英語"]
scores_df = pd.DataFrame(data=scores, index=names, columns=subjects)
scores_judge = scores_df["数字"] >= 70 
print(scores_judge)