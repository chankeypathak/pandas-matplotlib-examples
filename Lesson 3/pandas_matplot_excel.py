import numpy.random as np
import pandas as pd
import matplotlib.pyplot as plt

# set seed
np.seed(111)


# Function to generate test data
def CreateDataSet(Number=1):
    Output = []

    for i in range(Number):
        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        # Status pool
        status = [1, 2, 3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']

        # Make a random list of states
        random_states = [states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output

dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])

# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)

# Location of file
Location = 'Lesson3.xlsx'

# Parse a specific sheet
df = pd.read_excel(Location, 0, index_col='StatusDate')

# Clean State Column, convert to upper case
df['State'] = df.State.apply(lambda x: x.upper())

# Only grab where Status == 1
mask = df['Status'] == 1
df = df[mask]

# Convert NJ to NY
mask = df.State == 'NJ'
df['State'][mask] = 'NY'

df['CustomerCount'].plot(figsize=(15,5));
#plt.show()

sortdf = df[df['State']=='NY'].sort_index(axis=0)
#print sortdf.head(10)

# Group by State and StatusDate
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
#print Daily.head()

del Daily['Status']
#print Daily.head()

# What is the index of the dataframe
#print Daily.index

# Select the State index
#print Daily.index.levels[0]

# Select the StatusDate index
#print Daily.index.levels[1]

#Daily.loc['FL'].plot()
#Daily.loc['GA'].plot()
#Daily.loc['NY'].plot()
#Daily.loc['TX'].plot();
#plt.show()

# Calculate Outliers
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])

# Remove Outliers
Daily = Daily[Daily['Outlier'] == False]
#print Daily.head()

# Combine all markets

# Get the max customer count by Date
ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount'] # rename column

# Group by Year and Month
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])

# What is the max customer count per Year and Month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
#print ALL.head()

# Create the BHAG (Big Hairy Annual Goal) dataframe
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])
#print BHAG

# Combine the BHAG and the ALL data set
combined = pd.concat([ALL,BHAG], axis=0)
combined = combined.sort_index(axis=0)
#print combined.tail()

fig, axes = plt.subplots(figsize=(12, 7))

combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best')
#plt.show()

# Group by Year and then get the max value per year
Year = combined.groupby(lambda x: x.year).max()
#print Year

# Add a column representing the percent change per year
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
#print Year

#forecast
#print (1 + Year.ix[2012,'YR_PCT_Change']) * Year.ix[2012,'Max']

# First Graph
ALL['Max'].plot(figsize=(10, 5));
plt.title('ALL Markets')

# Last four Graphs
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
fig.subplots_adjust(hspace=1.0) ## Create space between plots

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,1])
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,0])
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,1])

# Add titles
axes[0,0].set_title('Florida')
axes[0,1].set_title('Georgia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East');
plt.show()