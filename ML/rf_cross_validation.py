from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from preprocess_data import preprocess_data
import pandas as pd
import numpy as np
import os

# data_set = "data_test"
data_set = "data_classical"

print("Setting up and preprocess data")
data_folder = "data/" + data_set + "/"
data_paths = [data_folder + filename for filename in ["label_4.xlsx", "label_3.xlsx"]]

X, y = preprocess_data(data_paths)

# Instantiate Random Forest classifier
rf_classifier = RandomForestClassifier()

# Specify the number of folds for cross-validation
num_folds = 10

# Create StratifiedKFold object for stratified cross-validation
stratified_kfold = StratifiedKFold(n_splits=num_folds, shuffle=True, random_state=42)

# Perform cross-validation and get scores for accuracy, F1-score, and ROC AUC
accuracy_scores = cross_val_score(rf_classifier, X, y, cv=stratified_kfold, scoring='accuracy')
f1_scores = cross_val_score(rf_classifier, X, y, cv=stratified_kfold, scoring='f1_weighted')
roc_auc_scores = cross_val_score(rf_classifier, X, y, cv=stratified_kfold, scoring='roc_auc')

accuracy_mean = accuracy_scores.mean()
f1_mean = f1_scores.mean()
roc_auc_mean = roc_auc_scores.mean()

accuracy_std = np.std(accuracy_scores)
f1_std = np.std(f1_scores)
roc_auc_std = np.std(roc_auc_scores)

# Print the mean scores and standard deviations for accuracy, F1-score, and ROC AUC
print("Mean Accuracy: {:.4f} ± {:.4f}".format(accuracy_mean, accuracy_std))
print("Mean F1-score: {:.4f} ± {:.4f}".format(f1_mean, f1_std))
print("Mean ROC AUC: {:.4f} ± {:.4f}".format(roc_auc_mean, roc_auc_std))

# Create a DataFrame to store the mean scores
mean_scores_df = pd.DataFrame({
    'Metric': ['Accuracy', 'F1-score', 'ROC AUC'],
    'Mean Score': [accuracy_mean, f1_mean, roc_auc_mean],
    'Std Deviation': [accuracy_std, f1_std, roc_auc_std]
})

# Define the folder to save the Excel file
output_folder_path = "output_ML/"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Save the Excel file in the "output_ML" folder
excel_file_path = os.path.join(output_folder_path, "rf_mean_scores.xlsx")

# Export the DataFrame to an Excel file
mean_scores_df.to_excel(excel_file_path, index=False)

print("Mean scores saved to:", excel_file_path)