import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix, roc_curve, auc

def plot_roc_curve(y_test, y_proba):
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    plt.plot(fpr, tpr, label=f'AUC = {auc(fpr, tpr):.2f}')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()
