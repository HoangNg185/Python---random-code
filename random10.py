import pandas as pd

# Read the first Excel file into a DataFrame
df1 = pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\KCC Customer and Orders DB.xlsx', sheet_name='Flat File')

# Read the second Excel file into another DataFrame
df2 = pd.read_excel('modified_orders.xlsx')

# Perform comparison operations between the DataFrames
# For example, you can check if the DataFrames are equal
if df1.equals(df2):
    print("The two Excel files are equal.")
else:
    print("The two Excel files are not equal.")

# You can also perform more specific comparisons, such as checking for differences in specific columns
# For example, check if the values in column 'A' are equal between the two DataFrames
if (df1['OrderDate'] == df2['OrderDate']).all():
    print("Column 'A' is equal between the two Excel files.")
else:
    print("Column 'A' is not equal between the two Excel files.")
