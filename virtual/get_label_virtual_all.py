import pandas as pd
import ast
import os
from matplotlib import pyplot as plt

from lower_upper_bound import *

# Input file name
folders_list = ["virtual_test"]
# folders_list = ["virtual_A", "virtual_B", "virtual_C", "virtual_D", "virtual_E"]

print("Setting up")
# Directory path for output
directory_out = "label_data"
os.makedirs(directory_out, exist_ok=True)
if folders_list == ["virtual_test"]:
    directory_out_test = "label_data/test_label_data"
    os.makedirs(directory_out_test, exist_ok=True)
    directory_out = directory_out_test

# Label from 1 to 5
max_wirt = 5  # expected
label_dict = {i: [] for i in range(1, max_wirt + 1)}
print("Done setting up")

# Directory path for input
for folder_name in folders_list:
    print("Working on folder ", folder_name)
    directory_in = "virtual_data/" + folder_name + "/"
    for k in range(1, 17):
        input_name = os.path.join(directory_in, f"{folder_name}_{k}.xlsx")
        # Read the Excel file into a DataFrame
        df = pd.read_excel(input_name, header=None)
        # Convert string representation of lists to actual lists
        df[0] = df[0].apply(ast.literal_eval)
        print("done read and now find finding bounds for ", input_name)

        for index, row in df.iterrows():
            gauss_code = row[0]  # Extract Gauss code from the second column
            lower_bound, upper_bound = get_bounds(gauss_code)
            if lower_bound == upper_bound:
                if lower_bound > max_wirt:
                    # expect max bridge number is 5. if not put it here
                    max_wirt = lower_bound
                else:
                    label_dict[lower_bound].append([gauss_code, lower_bound])
            # print(lower_bound, upper_bound, " for ", gauss_code)

# Iterate over label_dict and save each label's data into separate Excel files
for label_num, label_data in label_dict.items():
    # Convert label_data to DataFrame
    label_df = pd.DataFrame(label_data, columns=['Gauss Code', 'Label'])
    # Output file name
    label_output_name = os.path.join(directory_out, f"label_{label_num}.xlsx")
    # Save label_df to an Excel file
    label_df.to_excel(label_output_name, index=False, header=False)

# Plotting
# Convert values to integers
keys = [str(key) for key in label_dict.keys()]
values = [len(lst) for lst in label_dict.values()]

# Plotting
plt.figure(figsize=(8, 6))
bars = plt.bar(keys, values, color='darkblue')
plt.xlabel('Bridge numbers')
plt.ylabel('Number of data points')
plt.title('Labelled data for virtual knots')

# Adding labels above bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(int(bar.get_height())), ha='center', va='bottom')

# Save the plot
plt.savefig(os.path.join(directory_out, 'virtual_bar_chart.png'))

plt.show()

print("Done all and max bridge number is ", max_wirt)
