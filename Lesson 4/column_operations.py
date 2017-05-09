import pandas as pd

# Our small data set
d = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe
df = pd.DataFrame(d)
#print df

# Lets change the name of the column
df.columns = ['Rev']

# Lets add a column
df['NewCol'] = 5

# Lets modify our new column
df['NewCol'] = df['NewCol'] + 1

# We can delete columns
del df['NewCol']

# Lets add a couple of columns
df['test'] = 3
df['col'] = df['Rev']

# If we wanted, we could change the name of the index
i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i

#print df.loc['a']
# df.loc[inclusive:inclusive]
# print df.loc['a':'d']

# df.iloc[inclusive:exclusive]
# Note: .iloc is strictly integer position based.
#print df.iloc[0:3]

#We can also select using the column name.
#print df['Rev']
#print df[['Rev', 'test']]

# df.ix[rows,columns]
#print df.ix[0:3,'Rev']
#print df.ix[5:,'col']
#print df.ix[:3,['col', 'test']]

# Select top N number of records (default = 5)
#print df.head()

# Select bottom N number of records (default = 5)
#print df.tail()
