import pandas as pd
import ast
import os
from lower_upper_bound import *
from lower_bound_quandle import *

# Input file name
folder_name = "virtual_A"
# folder_name = "virtual_test"
k = '3'

quandle = ((1, 3, 2), (3, 2, 1), (2, 1, 3))
count_useful = 0

unknown = []
new = []

# too many unknown data so I do it separately

print("setting up")
# Directory path for input
directory_in = "virtual_data/" + folder_name + "/"
input_name = directory_in + folder_name + "_" + k + ".xlsx"

# Directory path for input
directory_out = "unknown/"
os.makedirs(directory_out, exist_ok=True)

# Read the Excel file into a DataFrame
df = pd.read_excel(input_name, header=None)
# Convert string representation of lists to actual lists
df[0] = df[0].apply(ast.literal_eval)
print("done read ", input_name)

for index, row in df.iterrows():
    gauss_code = row[0]  # Extract Gauss code from the second column
    lower_bound_1, upper_bound = get_bounds(gauss_code)

    if lower_bound_1 < upper_bound:
        my_length = use_favorite_quandle(gauss_code, quandle)
        lower_bound_2 = int(my_length**(1/3))
        # as our quandle is of size 3
        best_lower_bound = max(lower_bound_1, lower_bound_2)

        if lower_bound_2 == upper_bound:
            new.append([gauss_code, lower_bound_2])
        else:
            unknown.append([gauss_code, best_lower_bound, upper_bound])

        if lower_bound_2 > lower_bound_1:
            print("lb2", lower_bound_2, "lb1", lower_bound_1)
            count_useful += 1

# Convert unknown to DataFrame
unknown_df = pd.DataFrame(unknown, columns=['Gauss Code', 'Lower Bound', 'Upper Bound'])
# Save unknown_df to an Excel file
output_name_unknown = directory_out + "unknown_best_v1_bound_from_" + folder_name + "_" + k + ".xlsx"
unknown_df.to_excel(output_name_unknown, index=False)

# Convert unknown to DataFrame
new_df = pd.DataFrame(new, columns=['Gauss Code', 'Label'])
# Save unknown_df to an Excel file
output_name_new = directory_out + "new_known_from_" + folder_name + "_" + k + ".xlsx"
new_df.to_excel(output_name_new, index=False, header=False)

print("new ", len(new), "\nbound with quandle ", count_useful, "\nDone.")