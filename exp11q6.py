# 6.WAP to create and work with a Pandas Series.

import pandas as pd
# Create a Series
data = [10, 20, 30]
labels = ['a', 'b', 'c']
series = pd.Series(data, index=labels)
print("Pandas Series:")
print(series)
# Access data using label
print("Value at label 'b':", series['b'])
