import numpy as np


def cyclic_rotations(X, count_rotate=4):
    """
    Generates all possible cyclic rotations for each vector in X.

    Parameters:
        X (numpy.ndarray): Features.
        count_rotate (int): Maximum number of rotations for each vector. Default is 4.

    Returns:
        list: A list containing lists of all possible cyclic rotations for each vector in X.
    """
    rotations = []

    for vec in X:
        if len(vec) <= 1:
            rotations.append([vec])
        else:
            vec_rotations = [np.roll(vec, i) for i in range(min(count_rotate, len(vec)))]
            rotations.append(vec_rotations)

    return rotations


# # # Example usage:
# # X_example = np.array([[1, 2], [4, 5]])
# X_example = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8]])
# rotations = cyclic_rotations(X_example, count_rotate=4)
# print(rotations)
