import pandas as pd
scores = [
    [82, 67, 71, 91, 98], 
    [80, 98, 99, 60, 87],
    [97, 100, 100, 98, 96],
    [73, 60, 62, 77, 64]
    ]
scores_df = pd.DataFrame(data=scores)
print(scores_df)