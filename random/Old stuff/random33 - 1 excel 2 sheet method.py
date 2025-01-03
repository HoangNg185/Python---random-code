import pandas as pd

df = pd.read_excel('Data manipulation.xlsx', sheet_name='Company Note')
df['Notes'] = str()
for index in df.index:
    print(type(df.loc[index, '% Gross Sale']))
    df.loc[index, 'Notes'] = df.loc[index, '% Gross Sale'] * 100
df.to_excel('Data manipulation.xlsx', index=False)

'''import pandas as pd

# Read the Excel file
file_path = "path/to/your/excel/file.xlsx"
with pd.ExcelFile(file_path) as xls:
    # Read the sheets
    df_sheet1 = pd.read_excel(xls, sheet_name='Sheet1')
    df_sheet2 = pd.read_excel(xls, sheet_name='Sheet2')

# Modify data in df_sheet2 here
# For example, let's say you want to update a value in the DataFrame:
# df_sheet2.at[0, 'Column_Name'] = new_value

# Write back to the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df_sheet1.to_excel(writer, index=False, sheet_name='Sheet1')  # Write sheet1 unchanged
    df_sheet2.to_excel(writer, index=False, sheet_name='Sheet2')  # Write modified sheet2
'''
