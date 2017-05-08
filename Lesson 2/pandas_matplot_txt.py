import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
import os

# The inital set of baby names
names = ['Bob','Jessica','Mary','John','Mel']

# This will ensure the random samples below can be reproduced.
# This means the random samples will always be identical.
random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# The number of births per name for the year 1880
births = [random.randint(low=0,high=1000) for i in range(1000)]

BabyDataSet = list(zip(random_names,births))
#print BabyDataSet[:10]

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df.to_csv('births1880.txt',index=False,header=False)

Location = 'births1880.txt'
df = pd.read_csv(Location, names=['Names','Births'])

#metadata
#print df.info()

#See first five records using head
#print df.head()

#See last five records using tail
#print df.tail()


os.remove(Location)

#df['Names'].unique()
#print(df['Names'].describe())


# Create a groupby object
name = df.groupby('Names')

# Apply the sum function to the groupby object
df = name.sum()

Sorted = df.sort_values(['Births'], ascending=False)
#print Sorted.head(1)

# Create graph
df['Births'].plot.bar()

print("The most popular name")
df.sort_values(by='Births', ascending=False)
plt.show()