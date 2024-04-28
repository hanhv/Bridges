import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from preprocess_data import preprocess_data

# Define data_set
data_paths = ["label_4.xlsx", "label_3.xlsx"]
print("Setting up and preprocessing data")

# Preprocess the data
X, y = preprocess_data(data_paths)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid for GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=5, scoring='accuracy')

# Perform grid search
grid_search.fit(X_train, y_train)

# Get the best model from grid search
best_rf_model = grid_search.best_estimator_

# Get the best hyperparameters
best_hyperparameters = grid_search.best_params_

# Make predictions on the test set
y_pred = best_rf_model.predict(X_test)

# Calculate evaluation metrics
test_accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
auc_score = roc_auc_score(y_test, y_pred)

# Create a DataFrame to store metrics and hyperparameters
data = {
    'Test Accuracy': [test_accuracy],
    'F1 Score (Weighted)': [f1]
}

metrics_df = pd.DataFrame(data)

# Add the best hyperparameters to the DataFrame
for param, value in best_hyperparameters.items():
    metrics_df[param] = value

excel_out = "model_evaluation_results.xlsx"
metrics_df.to_excel(excel_out)

print("Model evaluation results saved to ", excel_out)

print("Done")

