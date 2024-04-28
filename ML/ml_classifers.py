import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from preprocess_data import preprocess_data
import os
import numpy as np

# data_set = "data_test"
data_set = "data_classical"

data_folder = "data/" + data_set + "/"
data_paths = [data_folder + filename for filename in ["label_4.xlsx", "label_3.xlsx"]]

print("Setting up and preprocess data")


def train_and_evaluate_classifier(classifier_model, features_train, features_test, labels_train, labels_test):
    classifier_model.fit(features_train, labels_train)
    train_acc = classifier_model.score(features_train, labels_train)
    test_acc = classifier_model.score(features_test, labels_test)
    predictions = classifier_model.predict(features_test)
    f1score_weighted = f1_score(labels_test, predictions, average='weighted')
    return train_acc, test_acc, f1score_weighted


# List of classifiers to evaluate
classifiers = {
    "Random Forest": RandomForestClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Extra Trees": ExtraTreesClassifier(),
    "Logistic Regression default": LogisticRegression(),
    "Logistic Regression": LogisticRegression(max_iter=10000),
    "Stochastic Gradient Descent": SGDClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "XGBoost": XGBClassifier(),
    "Gaussian Naive Bayes": GaussianNB(),
    "Neural Network default": MLPClassifier(),
    "Neural Network": MLPClassifier(max_iter=500, hidden_layer_sizes=(100, 100, 100)),
    "Support Vector Machine": SVC(),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

# Dictionary to store results
results_dict = {}

X, y = preprocess_data(data_paths)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for name_classifier, classifier in classifiers.items():
    print("Working on ", name_classifier)

    train_accuracy, test_accuracy, f1score, = train_and_evaluate_classifier(classifier, X_train, X_test, y_train, y_test)

    print("Done ",
          name_classifier, "\nTraining accuracy:", train_accuracy,
          "\nTest accuracy:", test_accuracy,
          "\nF1-score: ", f1score,
          "\n-------------\n-------------")

    results_dict.setdefault(name_classifier, {
        "Train Accuracy": train_accuracy,
        "Test Accuracy": test_accuracy,
        "F1 Score": f1score
    })
# Convert results dictionary to DataFrame
results_df = pd.DataFrame.from_dict(results_dict, orient='index')

# Reset index and rename the first column to "Model"
results_df.reset_index(inplace=True)
results_df.rename(columns={'index': 'Model'}, inplace=True)

# Define the folder to save the Excel file
output_folder_path = "output_ML/"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Save the Excel file in the "output_ML" folder
output_file_path = os.path.join(output_folder_path, "classifier_results.xlsx")
results_df.to_excel(output_file_path, index=False)  # Set index=False to exclude row numbers
