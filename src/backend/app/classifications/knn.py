from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

def stripColumns(dataset, chosenCols, predictCol):
    X = dataset[chosenCols]
    y = dataset[predictCol]

    return X, y

def splitData(X, y, splitData):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=splitData, random_state=1)

    return X_train, X_test, y_train, y_test

def kNeigh(csv, features, target, k, metric, split):
    X, y = stripColumns(csv, features, target)
    X_train, X_test, y_train, y_test = splitData(X, y, split)

    #Add in attribute selection, splitter and/or max_depth in order to optimize

    if metric == 'Manhattan':
    	#P=1 in order to use Manahattan distance
    	classifier = KNeighborsClassifier(n_neighbors=k, p=1)
    else:
    	#P=2 in order to use Euclidean distance
    	classifier = KNeighborsClassifier(n_neighbors=k, p=2)

    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    return metrics.accuracy_score(y_test, y_pred)