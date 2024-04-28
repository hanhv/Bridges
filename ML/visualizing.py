import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc
import os


def plot_roc_curve(y_true, y_prob, name_classifier='', sampling_method='', output_folder=""):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    roc_auc = auc(fpr, tpr)  # Calculate the AUC-ROC

    plt.plot(fpr, tpr, label='ROC Curve (AUC = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Random Guess')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC curve ({name_classifier}): {sampling_method} data set')
    plt.legend()
    plt.savefig(os.path.join(output_folder, f'roc_curve_{sampling_method}_{name_classifier}.png'))
    plt.show()


def visualize_confusion_matrix(y_true, y_pred, name_classifier='', sampling_method='', output_folder=""):
    # Calculate confusion matrix for test set predictions
    cm = confusion_matrix(y_true, y_pred)

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Label 3', 'Label 4'],
                yticklabels=['Label 3', 'Label 4'])
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title(f'Confusion matrix ({name_classifier}): {sampling_method} data set')
    plt.savefig(os.path.join(output_folder, f'confusion_matrix_{sampling_method}_{name_classifier}.png'))
    plt.show()
