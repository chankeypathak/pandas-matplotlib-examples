import pandas as pd
# Our small data set
d = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}

# Create dataframe
df = pd.DataFrame(d)

# Create group object
one = df.groupby('letter')

# Apply sum function
print one.sum()

letterone = df.groupby(['letter','one']).sum()
print letterone

letterone = df.groupby(['letter','one'], as_index=False).sum()
print letterone
