import preprocessing
import classifier
import analysis

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

if __name__ == '__main__':
    print("Start learning...")

    X_train, X_test, y_train, y_test = preprocessing.process()
    print("\nPre-processing... OK")

    print("\nTraining models...")
    
    y_pred_knn, knn = classifier.knn_classifier(X_train, y_train, X_test)
    print("Knn... OK")

    y_pred_dt = classifier.decision_tree(X_train, y_train, X_test)
    print("DecisionTree... OK")

    y_pred_logistic_reg = classifier.logistic_regression(X_train, y_train, X_test)
    print("Logistic Regression... OK")

    y_pred_sgd = classifier.sgd_classifier(X_train, y_train, X_test)
    print("SGD... OK")

    print("\nMetrics calculations...")
    
    print("\n--------------Knn metrics---------------")
    knn_accuracy, knn_conf_matrix, knn_class_report = analysis.metrics(y_test, y_pred_knn)
    print(f'Accuracy: {knn_accuracy}')
    print(f'Confusion Matrix:\n{knn_conf_matrix}')
    print(f'Classification Report:\n{knn_class_report}')

    analysis.confusion_matrix_view(knn_conf_matrix, knn.classes_)
    analysis.roc_curve_view(y_test, y_pred_knn)
    analysis.learning_curve_view(knn, X_train, y_train, 10)
