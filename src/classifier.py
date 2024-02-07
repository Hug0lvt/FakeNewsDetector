from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier

def logistic_regression(X_train, y_train, X_test):
    logistic = LogisticRegression(max_iter = 100000)
    logistic.fit(X_train,y_train)

    return logistic.predict(X_test)

def decision_tree(X_train, y_train, X_test):
    decisionTree = DecisionTreeClassifier()
    decisionTree = decisionTree.fit(X_train,y_train)

    return decisionTree.predict(X_test)

def knn_classifier(X_train, y_train, X_test):
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    return knn.predict(X_test)

def sgd_classifier(X_train, y_train, X_test):
    sgd = SGDClassifier(loss="hinge", penalty="l2")
    sgd.fit(X_train, y_train)

    return sgd.predict(X_test)
