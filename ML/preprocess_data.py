import pandas as pd
import numpy as np


def preprocess_data(data):
    """
    Preprocesses the data from Excel files and prepares it for training.

    Parameters:
        data (list): A list containing paths to two Excel files containing the data for two labels.

    Returns:
        tuple: A tuple containing preprocessed features (X) and labels (y).
    """

    # Read the data from the Excel files
    label4_data = pd.read_excel(data[0], engine="openpyxl", header=None)
    label3_data = pd.read_excel(data[1], engine="openpyxl", header=None)

    # Extract Gauss codes from the second column
    label4_features = label4_data.iloc[:, 0].apply(eval).tolist()  # For label 4
    label3_features = label3_data.iloc[:, 0].apply(eval).tolist()  # For label 3

    # Combine features and labels
    X = label4_features + label3_features
    y = [1] * len(label4_features) + [0] * len(label3_features)

    # Convert lists of lists to numpy arrays
    X = np.array(X)
    y = np.array(y)

    return X, y
