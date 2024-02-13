import preprocessing
import run

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':

    print("Start learning...")
    X_train, X_test, y_train, y_test = preprocessing.process()
    print("\nPre-processing... OK")

    #run.run_knn(X_train, y_train, X_test, y_test)
    #run.run_decision_tree(X_train, y_train, X_test, y_test)
    #run.run_logistic_regression(X_train, y_train, X_test, y_test)
    #run.run_stochastic_gradient_descent(X_train, y_train, X_test, y_test)