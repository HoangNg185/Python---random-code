import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

df = pd.read_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\stores_sales_forecasting.csv',
                 encoding='latin1')

data1 = df.loc[df['Sub-Category'].isin(['Chairs', 'Furnishing'])]
data2 = df['Postal Code'].describe()
data3 = df['Region'].unique()
data4 = df['Customer Name'].value_counts()
data4_1 = df.loc[(df['Customer Name'] == 'Claire Gute')]
data5 = df['Sales'].mean()
data5_1 = df['Sales'].map(lambda s: s - data5)
data6 = df['Country'] + ' - ' + df['State']

df['new'] = df['Row ID']
# set up Datas
newnew = df
newnew['Postal Code'] = newnew['Postal Code'].astype(object)
newnew['Discount'] = newnew['Discount'].astype(object)
newnew['Ship Date'] = pd.to_datetime(newnew['Ship Date'])
newnew['Order Date'] = pd.to_datetime(newnew['Order Date'])
newnew['Profit'] = newnew['Profit'].astype(str)

# Interpret Datas
for i in newnew.index:
    if newnew.loc[i, 'Discount'] > 0:
        newnew.loc[i, 'Profit'] = '(' + newnew.loc[i, 'Profit'] + ')'
    else:
        newnew.loc[i, 'Profit'] = newnew.loc[i, 'Profit']

    if newnew.loc[i, 'Segment'] == 'Consumer':
        newnew.loc[i, 'Segment'] = 'C'
    else:
        newnew.loc[i, 'Segment'] = 'others'
    newnew.loc[i, 'Product Name'] = newnew.loc[i, 'Product Name'][:10:1]
    newnew.loc[i, 'Order ID'] = newnew.loc[i, 'Order ID'][-6:]
    newnew.loc[i, 'City'] = newnew.loc[i, 'City'] + '-' + newnew.loc[i, 'State'] + '-' + newnew.loc[
        i, 'Region'] + '-' + str(newnew.loc[i, 'Postal Code'])
    newnew.loc[i, 'Customer Name'] = newnew.loc[i, 'Customer Name'] + '-' + newnew.loc[i, 'Segment']
    newnew.loc[i, 'Shipping time'] = newnew.loc[i, 'Ship Date'] - newnew.loc[i, 'Order Date']
newnew['Profit'] = newnew['Profit'].astype(object)
newnew['Order ID'] = newnew['Order ID'].astype('int64')

'''newnew['Order Date']=pd.to_datetime(df['Order Date'])
newnew['Ship Date']=pd.to_datetime(df['Ship Date'])'''

# Cleaning, Rename, Drop
newnew = newnew.rename(columns={'Row ID': 'ID', 'City': 'Order from'})
newnew = newnew.drop(
    columns=['new', 'Ship Mode', 'Customer ID', 'Sub-Category', 'Quantity', 'State', 'Region', 'Segment', 'Postal Code',
             'Product ID', 'Ship Date', 'Order Date', 'Discount'])

print(newnew)
# print(newnew.dtypes)


# export to excel
# newnew.to_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\asd1.xlsx')

'''df['Sales']=sorted(df['Sales'])
print(df['Sales'][0:3])
ypoints=np.array(df['Sales'])
plt.plot(ypoints)
plt.show()'''

#
