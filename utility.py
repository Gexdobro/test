import pandas as pd

_data = {
    'a': [1,2,3],
    'b': [4,5,6]
}

df = pd.DataFrame(_data)

print(df.head())