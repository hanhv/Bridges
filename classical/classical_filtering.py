import pandas as pd
import os
from lower_bound_quandle import *
from visualize import *

# input_name = ["all_data_A.xlsx", "all_data_B.xlsx", "all_data_C.xlsx", "all_data_D.xlsx", "all_data_E.xlsx"]
input_name = ["all_data_test.xlsx"]
# Define input parameters
num_crossing = 16
directory = "../data_original/"

print("Setting up")

# Directory path for output
directory_out = "data_classical/"
if not os.path.exists(directory_out):
    os.makedirs(directory_out)

# Subdirectory name
subdirectory_name = "classical_test_only"
subdirectory_test_only_filter = os.path.join(directory_out, subdirectory_name)
# Creating the subdirectory if it doesn't exist
if not os.path.exists(subdirectory_test_only_filter):
    os.makedirs(subdirectory_test_only_filter)

if input_name == ["all_data_test.xlsx"]:
    directory_out = subdirectory_test_only_filter

print("Done setting up")

list_2 = []

list_3 = []
list_4 = []

list_unknown_4 = []

list_5 = []
list_unknown_5 = []

quandle = ((1, 3, 2), (3, 2, 1), (2, 1, 3))
count_new_known_4 = 0

for file in input_name:
    file_name = os.path.join(directory, file)
    print("working on: ", file_name)

    # Read the data from the Excel file
    data = pd.read_excel(file_name, engine="openpyxl", header=0)
    print("done read and now filtering")

    # Check row by row
    for index, row in data.iterrows():
        gauss_code_str = row.iloc[1]
        gauss_code = eval(gauss_code_str)
        if num_crossing in gauss_code:
            wirt = int(row.iloc[2])
            if wirt == 2:
                list_2.append([gauss_code, wirt])
            if wirt == 3:
                list_3.append([gauss_code, wirt])
            if wirt == 4:
                exact = int(row.iloc[3])
                if exact == 1:
                    list_4.append([gauss_code, wirt])
                if exact == 0:
                    my_length = use_favorite_quandle(gauss_code, quandle)
                    if my_length == 3 ** wirt:
                        count_new_known_4 += 1
                        list_4.append([gauss_code, wirt])
                    else:
                        list_unknown_4.append([gauss_code, wirt])
            if wirt == 5:
                exact = int(row.iloc[3])
                if exact == 1:
                    list_5.append([gauss_code, wirt])
                if exact == 0:
                    list_unknown_5.append([gauss_code, wirt])

# Output file names
df_label2 = pd.DataFrame(list_2, columns=["Gauss Code", "Wirt"])
df_label3 = pd.DataFrame(list_3, columns=["Gauss Code", "Wirt"])
df_label4 = pd.DataFrame(list_4, columns=["Gauss Code", "Wirt"])
df_label5 = pd.DataFrame(list_5, columns=["Gauss Code", "Wirt"])

df_unknown_4 = pd.DataFrame(list_unknown_4, columns=["Gauss Code", "Wirt"])
df_unknown_5 = pd.DataFrame(list_unknown_5, columns=["Gauss Code", "Wirt"])

excel_label2 = os.path.join(directory_out, "label_2.xlsx")
excel_label3 = os.path.join(directory_out, "label_3.xlsx")
excel_label4 = os.path.join(directory_out, "label_4.xlsx")
excel_label5 = os.path.join(directory_out, "label_5.xlsx")

excel_unknown_4 = os.path.join(directory_out, "unknown_3or4.xlsx")
excel_unknown_5 = os.path.join(directory_out, "unknown_up_to_5.xlsx")

# Save DataFrames to Excel files
df_label2.to_excel(excel_label2, index=False, header=False)
df_label3.to_excel(excel_label3, index=False, header=False)
df_label4.to_excel(excel_label4, index=False, header=False)
df_label5.to_excel(excel_label5, index=False, header=False)

df_unknown_4.to_excel(excel_unknown_4, index=False, header=False)
df_unknown_5.to_excel(excel_unknown_5, index=False, header=False)

print("Saved excel files of all labels")

visualize_classical(directory_out, list_2, list_3, list_4, list_5, list_unknown_4, list_unknown_5)

print("Number of new gauss codes with label 4 using quandles: ", count_new_known_4, "\nDone all")