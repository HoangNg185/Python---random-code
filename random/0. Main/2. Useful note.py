# Note 1
'''import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
df=pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\Student_performance_data _.xlsx',sheet_name='Sheet1')
print(df.columns)
columns=['StudentID', 'Age', 'Gender', 'Ethnicity', 'ParentalEducation',
       'StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport',
       'Extracurricular', 'Sports', 'Music', 'Volunteering', 'GPA',
       'GradeClass']
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

x_axis='Age'
y_axis='StudyTimeWeekly'
stats=df.groupby(x_axis)[y_axis].std()
sns.displot(data=df,x=x_axis,weights=y_axis, bins=len(df['Age'].unique()))
plt.plot(stats.index,stats.values)

#--------------------------------------------------------------------------------------------------------------------------
plt.xlabel('')
plt.ylabel('Sum of weelly study hour')
formatter_x = FuncFormatter(lambda x, pos: f'{int(x):.2f}')
formatter_y = FuncFormatter(lambda x, pos: f'{int(x):.2f}')
plt.gca().xaxis.set_major_formatter(formatter_x)
plt.gca().yaxis.set_major_formatter(formatter_y)
plt.grid(True)
plt.tight_layout()
plt.show()
'''

# Note 2
'''import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

import os
for a,b,c in os.walk('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle'):
    for i in c:
        #print(os.path.join(a,i))
        pass
pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',10)

df =pd.read_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\Nuclear Energy\\world_nuclear_energy_generation.csv')
columns=['Entity', 'Year', 'electricity_from_nuclear_twh',
       'share_of_electricity_pct']
desc=df.describe()
df=df.fillna(0,inplace=True)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
x_axix='Year'
y_axis='share_of_electricity_pct'
plots_kind = ['line','bar','barh','hist','box','kde','density','area']

fig,axes = plt.subplots(3,3,figsize=(15,12))
axes=axes.flatten()
for ax, plot_kind in zip(axes, plots_kind):
    print(ax, plot_kind)
    desc.plot(kind=plot_kind,title=f'{plot_kind} plot',ax=ax)


#plot_kind='line'
#desc.plot(kind=plot_kind,title=f'{plot_kind} plot')
#plt.scatter(df[x_axix],df[y_axis])
#---------------------------------------------------------------------------------------------------------------------
plt.grid(True)
plt.tight_layout()
plt.show()
sns.pairplot(df)
'''
