'''array11=numpy.random.normal(170,10,250)
array22=numpy.random.normal(50,20,250)
array11.sort()
array22.sort()
slope, intercept, r, p, std_err = stats.linregress(array11, array22)
def linerline(array11):
    return slope * array11 + intercept
drawlinerline=list(map(linerline,array11))
print(drawlinerline)
plt.scatter(array11,array22)
plt.plot(array11,drawlinerline)
plt.show()'''

# polygression line
'''x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)
print(mymodel(17))
print(r2_score(y,mymodel(x)))
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()'''

# multiple Regression
'''from sklearn import linear_model

df=pd.read_csv('data3.csv')
X=df[['Weight','Volume']]
y=df['CO2']

regr=linear_model.LinearRegression()
regr.fit(X.values,y)

predicted_CO2=regr.predict([[2300,1300]])
print(predicted_CO2)
print(regr.coef_)
print(regr.predict([[3300,1300]]))

X1=df['Weight']
X2=df['Volume']
plt.plot(X2,y)
plt.plot(X1,y)
plt.show()'''

# Scale: z = (x - u) / s
'''from sklearn import linear_model
from sklearn.preprocessing import StandardScaler #this is important as we do not use regularly

scale = StandardScaler() #assgin alias/ memory location for easy use. You can assign any name as you like
df=pd.read_csv('data3.csv')
X=df[['Weight','Volume']]
y=df['CO2']

scaledX=scale.fit_transform(X)
regr=linear_model.LinearRegression()
regr.fit(scaledX,y)
scaled=scale.transform([[2300,1.3],[2400,1.5]])

predict_CO2=regr.predict([scaled[1]])
print(predict_CO2)'''
# print(scaledX)


# testing: take a portion of the data, reconsider if r2_score is good (1) or bad (0)
'''numpy.random.seed(2)
x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100) / x

train_x=x[:80] #Take index of x from 0 to 80. simply take some 'points' and put it on the graph
train_y=y[:80]
test_x=x[80:]
test_y=y[80:]

mymodel= numpy.poly1d(numpy.polyfit(train_x,train_y,4))
myline=numpy.linspace(0,6,100)

print(r2_score(train_y,mymodel(train_x)))
print(mymodel(5))
plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()'''

# Desicion tree
'''from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
df=pd.read_csv('data3decision.csv')
#print(df)
d= {'UK':0,'USA':1,'N':2}
df['Nationality']=df['Nationality'].map(d) #amazing way to reassign name by using PANDAS!

d={'YES':1,'NO':0}
df['Go']=df['Go'].map(d)

print(df)

X=df[['Age','Experience','Rank','Nationality']]
y=df['Go']

dtree=DecisionTreeClassifier()
dtree=dtree.fit(X, y)
if dtree.predict([[40,10,6,1]])==1:
    print('lets go')
else:
    print('nah')
print(dtree.predict([[40,10,7,1]]))
tree.plot_tree(dtree, feature_names=['Age', 'Experience', 'Rank', 'Nationality'])
plt.show()'''

# Matrix
'''from sklearn import metrics

actual= numpy.random.binomial(1,.9,size=1000)
predicted=numpy.random.binomial(1,0.9,size=1000)

meeeeee_confusion_matric = metrics.confusion_matrix(actual,predicted)
cm_display= metrics.ConfusionMatrixDisplay(confusion_matrix=meeeeee_confusion_matric, display_labels=[False,True])
cm_display.plot()
#plt.show()
#False Negative (Top-Left Quadrant)
#False Positive (Top-Right Quadrant)
#True Negative (Bottom-Left Quadrant)
#True Positive (Bottom-Right Quadrant)

#some 5 data analizations: Accuracy, Precision, Sensitivity (Recall), Specificity, F-score

Accuracy= metrics.accuracy_score(actual,predicted)
Precision= metrics.precision_score(actual,predicted)
Sensitivity_recall=metrics.recall_score(actual,predicted,pos_label=1) #for Sensitivity_recall, pos_lebel is default = 1. we do not need to include it)
Specificity=metrics.recall_score(actual,predicted,pos_label=0)
F1_score=metrics.f1_score(actual,predicted)
print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})'''

# Hierarchical Clustering
'''from scipy.cluster.hierarchy import dendrogram, linkage
import sys
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

link_data = linkage(data, method='ward',metric='euclidean')
dendrogram(link_data)

plt.show()
#still have somemore, but I feel like it has no use at the moment
'''
