# Bridge Numbers

## 1. Classical Knots:

- Filtering to get knots with exact bridge numbers (file `classical_filtering.py`).
- Using `lower_bound_quandle` to find more 4-bridge knots if needed.

Labelled data for classical knots are saved in `classical/data_classical`.

## 2. Virtual Knots:

Note: In contrast with classical knots, for virtual knots, the two versions of bridge numbers differ. In what follows, we work with version 1 bridge numbers. Version 2 bridge numbers are treated in Section 4.
- Obtaining virtual knots (file `get_virtual.py`): removing `k, -k \in {1,...,16}` from 16-crossing actual knots from files `A` to `E`.
- Obtaining labels (file `get_label_virtual_all.py`): computing lower and upper bounds using `calc_wirt.py` and `sym_hm.py`. 
In the function `calc_wirt_info`, a modification has been made to the variable `n`. Originally, it was set to 2, but it has been changed to 1. Below is the updated version of the function:

```python
def calc_wirt_info(knot_dict):
    n = 1  # Setting n = 1 instead of 2 as in the original file
    # Rest of the function implementation goes here
```

- Obtaining unknown data with bounded bridge numbers (file `b1_find_bounds.py`): using `lower_bound_quandle` to search for a better lower bound for the bridge number.

Labelled data for virtual knots are saved in `virtual/label_data`.
Virtual knots with bounded bridge numbers are saved in `virtual/unknown`.

## 3. Machine Learning:

Experimenting with machine learning to classify classical knots with 3 or 4 bridges.

- Imbalanced data (majority `0 := label 3`, minority `1 := label 4`).

- Model selection with the original data (file `ml_classifers.py`): NN, RF, KNN, SVM, etc. Output: `classifier_results.xlsx`.

- RF:
  - n-fold cross-validation for n=10 (file `rf_cross_validation.py`). Output: `rf_mean_scores.xlsx`.
  - with and without under/oversampling, oversampling by both rotation and SMOTE (file `rf_sampling.py`). Output: `rf_with_sampling_methods.xlsx`.
  - tuning: grid search (file `rf_tune.py`). Output: `rf_grid_search_results.xlsx`.

## 4. Biquandles:
Computing lower bounds for version 2 bridge number for virtual knots up to 5 real crossings using the biquandle method (file `virtual/b2_exp_biquandle.py`). Output: `virtual/exp_biquandle`.

## Acknowledgments

- https://github.com/pommevilla/calc_wirt/tree/master
- https://github.com/ThisSentenceIsALie/Wirt_Hm/tree/main/Wirt_Hm_Suite_Python
- Ho-Nelson: https://arxiv.org/pdf/math/0412417.pdf
