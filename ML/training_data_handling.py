from over_sample_by_rotation import *
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


# Assume X and y are already defined

# Function to preprocess data
def resample_data(X, y, sampling_method="original"):
    """
    Preprocesses the data and balances the class distribution based on the specified sampling method.

    Parameters:
        X (numpy.ndarray or list): Features.
        y (numpy.ndarray or list): Labels.
        sampling_method (str): Specifies the sampling method to use: "original" for original data,
                               "undersample" for undersampled data, "smote" for SMOTE data, etc.

    Returns:
        tuple: A tuple containing preprocessed features (X) and labels (y).
    """
    if sampling_method == "undersample":
        X, y = undersample_data(X, y)

    if sampling_method == "oversample":
        X, y = oversample_data(X, y)

    if sampling_method == "smote":
        smote = SMOTE(random_state=42)
        X, y = smote.fit_resample(X, y)

    return X, y


def undersample_data(X, y):
    # Create an instance of RandomUnderSampler
    sampler = RandomUnderSampler(random_state=42)

    # Undersample the majority class
    X_resampled, y_resampled = sampler.fit_resample(X, y)

    return X_resampled, y_resampled


def oversample_data(X, y):
    # Separate majority and minority classes
    majority_class_X = X[y == 0]
    minority_class_X = X[y == 1]

    # Calculate the ratio of the majority class size to the minority class size
    ratio = len(majority_class_X) / len(minority_class_X)

    # Determine the oversampling count based on the ratio
    count_rotate = int(np.floor(ratio))

    # Apply cyclic rotations using the custom function
    minority_rotations = cyclic_rotations(minority_class_X, count_rotate)

    # Stack the rotated vectors
    minority_oversampled_X = np.vstack(minority_rotations)

    # Combine minority class rotations with the original minority class
    X_resampled = np.concatenate([majority_class_X, minority_oversampled_X])
    y_resampled = np.concatenate([np.zeros(len(majority_class_X)), np.ones(len(minority_oversampled_X))])

    return X_resampled, y_resampled