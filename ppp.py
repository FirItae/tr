import pandas as pd
data = pd.DataFrame([[0, 1, 1], [1, 0, 0], [1, 1, pd.NA]], columns=['A', 'B', 'C'])
print(data)