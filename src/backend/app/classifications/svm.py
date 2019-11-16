from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import train_test_split

def stripColumns(dataset, chosenCols, predictCol):
    X = dataset[chosenCols]
    y = dataset[predictCol]

    return X, y

def splitData(X, y, splitData):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=splitData, random_state=1)

    return X_train, X_test, y_train, y_test

def svm(csv, features, target, split):
    X, y = stripColumns(csv, features, target)
    X_train, X_test, y_train, y_test = splitData(X, y, split)

    classifier = SVC()
    
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    return metrics.accuracy_score(y_test, y_pred)
