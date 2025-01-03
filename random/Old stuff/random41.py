import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_rows', 20)

# data from sns['diamonds']
'''
diamonds=sns.load_dataset('diamonds')

g=sns.FacetGrid(data=diamonds,col='color',row='clarity',palette='prism',margin_titles=True,hue='color')
g.map_dataframe(sns.histplot,y='price')
g.set_titles('cut material: {col_name}')
g.add_legend()

plt.show()'''


def loaddata(se):
    datasetss = sns.load_dataset(se)
    print(datasetss)


def create_histplot(dataset: str, hue_value: str, y_data: str, set_titles: str):
    datasetss = sns.load_dataset(dataset)

    g = sns.FacetGrid(data=datasetss, col='color', row='clarity', palette='prism', margin_titles=True, hue=hue_value)
    g.map_dataframe(sns.histplot, y=y_data)
    g.set_titles(set_titles)
    g.add_legend()

    plt.show()


# create_histplot('diamonds','color','price','cut material: {col_name}')


x = np.random.random(50) * 100
y = np.random.random(50) * 100
sns.scatterplot(x)
plt.show()
