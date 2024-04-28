import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from preprocess_data import preprocess_data
from training_data_handling import *
from visualizing import *

# data_set = "data_test"
data_set = "data_classical"

data_folder = "data/" + data_set + "/"
data_paths = [data_folder + filename for filename in ["label_4.xlsx", "label_3.xlsx"]]

print("Setting up and preprocess data")

results = []

models = {
    "Random Forest": RandomForestClassifier(n_estimators=1000, random_state=42)
}

# Define the desired sampling methods
sampling_methods = ["original", "undersample", "smote", "oversample"]
X, y = preprocess_data(data_paths)

# Separate data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Done preprocess data")

# Resample the data for each sampling method
for sampling_method in sampling_methods:
    print("Train and evaluate models using", sampling_method)
    X_train_resampled, y_train_resampled = resample_data(X_train, y_train, sampling_method=sampling_method)

    for name_classifier, model in models.items():
        model.fit(X_train_resampled, y_train_resampled)
        train_accuracy = accuracy_score(y_train, model.predict(X_train))
        y_pred = model.predict(X_test)
        test_accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')

        # Append results to the list
        results.append({
            'Sampling Method': sampling_method,
            'Classifier': name_classifier,
            'Train Accuracy': train_accuracy,
            'Test Accuracy': test_accuracy,
            'F1 Score': f1
        })


# Convert results to DataFrame
results_df = pd.DataFrame(results)


# Define the folder to save the Excel file
output_folder_path = "output_ML/"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

excel_file_path = os.path.join(output_folder_path, "rf_with_sampling_methods.xlsx")
results_df.to_excel(excel_file_path, index=False)

print("Done")
