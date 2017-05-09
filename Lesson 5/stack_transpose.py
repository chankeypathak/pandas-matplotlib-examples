import pandas as pd

# Our small data set
d = {'one':[1,1],'two':[2,2]}
i = ['a','b']

# Create dataframe
df = pd.DataFrame(data = d, index = i)

# Bring the columns and place them in the index
stack = df.stack()
print stack

unstack = df.unstack()
print unstack

transpose = df.T
print transpose
