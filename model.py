import pandas as pd
import warnings
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings("ignore")
data = pd.read_csv('train.csv')
# store the feature matrix (X) and response vector (y)
X = data[data.columns[:-1]]
y = data[data.columns[-1]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DT', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
models.append(('MLP', MLPClassifier()))
# evaluate each model in turn
seed=7
scoring = 'accuracy'
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    
    
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))
#model=[[0.994489796   , 0.5 ,   0.024183673  ,  0   , 0.25  ,  0.4  ,  0.5   , 0.3  ,  0 ,   0 ,   0  ,  0   , 0  ,  0  ,  0  ,  0 ,   0.2 ,   0.2  ,  0   , 0.166666667  ,  0 ,   0  ,  0  ,  0   , 0   , 0  ,  0 ,   0 ,   0.1  ,  0  ,  0.1  ,  0   , 0.1 ,   0  ,  0  ,  0   , 0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0   , 0   , 0 ,   0 ,   0  ,  0   , 0 ,   0,    0 ,   0 ,   0   , 0  ,  0.1  ,  0 ,   0  ,  0.1 ,   0  ,  0  ,  0 ,   0   , 0  ,  0.1 ,   0 ,   0.166666667 ,   0,    0.1 ,   0  ,  0 ,   0  ,  0 ,   0.2 ,   0 ,   0  ,  0  ,  0  ,  0   , 0 ,   0.05 ,   0  ,  0  ,  0.1499925 ,   0 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0.081247969]]
#pred=knn.predict(model)
#print(pred)

lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
y_pred = lda.predict(X_test)
print("lda model accuracy:", metrics.accuracy_score(y_test, y_pred))

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print("lr model accuracy:", metrics.accuracy_score(y_test, y_pred))

cart = DecisionTreeClassifier()
cart.fit(X_train, y_train)
y_pred = cart.predict(X_test)
print("dt model accuracy:", metrics.accuracy_score(y_test, y_pred))

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("gnb model accuracy:", metrics.accuracy_score(y_test, y_pred))

svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
print("svc model accuracy:", metrics.accuracy_score(y_test, y_pred))

mlp = MLPClassifier()
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)
print("mlp model accuracy:", metrics.accuracy_score(y_test, y_pred))