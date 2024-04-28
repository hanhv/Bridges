import pandas as pd
import ast
import os

directory = "../data_original/"

# Input file name
file = "test"
# file = "E"

print("Setting up")
# Directory path for output
os.makedirs("virtual_data", exist_ok=True)
directory_out = "virtual_data/virtual_" + file + "/"
# Create the directory if it doesn't exist
os.makedirs(directory_out, exist_ok=True)

# Read the Excel file into a DataFrame
input_name = os.path.join(directory, "all_data_" + file + ".xlsx")
df = pd.read_excel(input_name)

print("Done setting up")

for k in range(1, 17):
    print("removing ", k)
    # Filter rows containing "16" in the second column
    df_filtered = df[df.iloc[:, 1].astype(str).str.contains('16')]

    # Convert string representation of lists to actual lists and remove "k" and "-k"
    df_filtered.iloc[:, 1] = df_filtered.iloc[:, 1].apply(lambda x: [i for i in ast.literal_eval(x) if abs(i) != k])

    # Output file name
    output_name = os.path.join(directory_out, f"virtual_{file}_{k}.xlsx")

    # Save only the second column to a new Excel file
    df_filtered.iloc[:, 1].to_excel(output_name, index=False, header=False)

print("Done generating virtual")