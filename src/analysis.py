#from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay, roc_curve, auc, RocCurveDisplay
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
import numpy as np

def metrics(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    return accuracy, conf_matrix, class_report

def confusion_matrix_view(confusion_matrix, knn_classes):
    cmap = plt.cm.Blues
    disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=knn_classes)
    disp.plot(cmap=cmap)
    plt.show()

def roc_curve_view(y_test, y_pred):
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)
    display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='estimator')
    display.plot()
    plt.show()

def learning_curve_view(classifier, X_train, y_train, learning_reps):
    print('Training in progress, wait please...')
    train_sizes, train_scores, test_scores = learning_curve(classifier, X_train, y_train, cv=learning_reps, scoring='accuracy', n_jobs=-1)

    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)

    plt.plot(train_sizes, train_scores_mean, label='Train')
    plt.plot(train_sizes, test_scores_mean, label='Validation')
    plt.xlabel("Training set size")
    plt.ylabel('Score')
    plt.title('Learning curve')
    plt.legend()
    plt.show()