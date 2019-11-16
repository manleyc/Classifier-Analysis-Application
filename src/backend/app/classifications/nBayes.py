from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

def stripColumns(dataset, chosenCols, predictCol):
    X = dataset[chosenCols]
    y = dataset[predictCol]

    return X, y

def splitData(X, y, splitData):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=splitData, random_state=1)

    return X_train, X_test, y_train, y_test

def nbayes(csv, features, target, split):
    X, y = stripColumns(csv, features, target)

    X_train, X_test, y_train, y_test = splitData(X, y, split)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    return metrics.accuracy_score(y_test, y_pred)







