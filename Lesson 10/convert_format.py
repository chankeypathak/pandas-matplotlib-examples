import pandas as pd
# Create DataFrame
d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['Number'])

# Export to Excel
df.to_excel('Lesson10.xlsx', sheet_name = 'testing', index = False)

# From Excel to DataFrame
location = r'Lesson10.xlsx'

# Parse the excel file
df = pd.read_excel(location, 0)

# From DataFrame to JSON
df.to_json('Lesson10.json')

# From JSON to DataFrame
jsonloc = r'Lesson10.json'

# read json file
df2 = pd.read_json(jsonloc)
