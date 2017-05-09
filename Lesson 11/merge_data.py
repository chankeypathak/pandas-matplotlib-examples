import pandas as pd
import matplotlib.pyplot as plt
import os

# Create DataFrame
d = {'Channel':[1], 'Number':[255]}
df = pd.DataFrame(d)

# Create 3 excel files
# Export to Excel

df.to_excel('test1.xlsx', sheet_name = 'test1', index = False)
df.to_excel('test2.xlsx', sheet_name = 'test2', index = False)
df.to_excel('test3.xlsx', sheet_name = 'test3', index = False)
print('Done')

# Place all three Excel files into a DataFrame
# List to hold file names
FileNames = []

os.chdir(r".")

# Find any file that ends with ".xlsx"
for files in os.listdir("."):
    if files.endswith(".xlsx"):
        FileNames.append(files)

print FileNames

# Create a function to process all of the excel files

def GetFile(fnombre):
    # Path to excel file
    # Your path will be different, please modify the path below.
    location = r'' + fnombre

    # Parse the excel file
    # 0 = first sheet
    df = pd.read_excel(location, 0)

    # Tag record to file name
    df['File'] = fnombre

    # Make the "File" column the index of the df
    return df.set_index(['File'])

# Go through each file name, create a dataframe, and add it to a list
# i.e. df_list = [df, df, df]
# Create a list of dataframes
df_list = [GetFile(fname) for fname in FileNames]
print df_list

# Combine all of the dataframes into one
big_df = pd.concat(df_list)
print big_df

# Plot it!
big_df['Channel'].plot.bar()
plt.show()
