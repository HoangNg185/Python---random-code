import random
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Job Applied part 2.xlsx', sheet_name=1)
df=df[:10]
print(df.to_string())
X=df[['cpp','ei']]

y=df['total income tax deducted is report in T4 split line 22. The amount of total tax is the same, they will adjust at the end of the year.']
regr=linear_model.LinearRegression()
regr.fit(X.values,y)

print(regr.predict([[5000,500]]))

plt.show()