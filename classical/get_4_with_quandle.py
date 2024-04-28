import pandas as pd
import os
from lower_bound_quandle import *

# Directory path for input
directory_in = "exp_quandles/"
# file_name = "unknown_3or4.xlsx"
file_name = "test_only_quandle.xlsx"

directory_out = directory_in + "after_quandles/"
if not os.path.exists(directory_out):
    os.makedirs(directory_out)


input_name = directory_in + file_name

quandle = ((1, 3, 2), (3, 2, 1), (2, 1, 3))
# Read the Excel file
df = pd.read_excel(input_name, header=None)

count_new_known = 0
new_known = []
still_unknown = []

for index, row in df.iterrows():
    gauss_code_str = row[0]
    gauss_code = eval(gauss_code_str)
    print("working on ", gauss_code)
    my_length = use_favorite_quandle(gauss_code, quandle)
    print("my length ", my_length)
    the_upper_bound = int(row[1])

    if my_length == 3 ** the_upper_bound:
        count_new_known += 1
        new_known.append([gauss_code, the_upper_bound])
    else:
        still_unknown.append([gauss_code, the_upper_bound])

if count_new_known >= 1:
    # NEW
    # Convert lists to DataFrame
    df_new_known = pd.DataFrame(new_known, columns=["Gauss Code", "Upper Bound"])
    # Save DataFrames to Excel files
    excel_new4 = directory_out + "new4.xlsx"
    df_new_known.to_excel(excel_new4, index=False, header=False)
    print("Saved new label 4")

    # Still unknown
    # Convert lists to DataFrame
    df_still_unknown = pd.DataFrame(still_unknown, columns=["Gauss Code", "Upper Bound"])
    # Save DataFrames to Excel files
    excel_still_unknown = directory_out + "still_unknown.xlsx"
    df_still_unknown.to_excel(excel_still_unknown, index=False, header=False)
    print("Saved the still unknown")
else:
    print("No new found")

