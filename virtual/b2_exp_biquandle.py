import ast
from lower_bound_quandle import *
from lower_upper_bound import *


biquandle = (((1, 3, 4, 2), (3, 1, 2, 4), (2, 4, 3, 1), (4, 2, 1, 3)),
             ((1, 4, 2, 3), (2, 3, 1, 4), (4, 1, 3, 2), (3, 2, 4, 1)))

# Get the length of the subtuple in the first element of the biquandle
biquandle_length = len(biquandle[0][0])

input_name = "exp_biquandles/virtual_upto4.xlsx"
# input_name = "exp_biquandles/virtual_5.xlsx"
excel_out_name = "exp_biquandles/b2_bound_" + input_name.split("/")[-1].split(".")[0] + ".xlsx"
print(excel_out_name)

# Read the Excel file into a DataFrame
df = pd.read_excel(input_name, header=None)
# Convert string representation of lists to actual lists
df[0] = df[0].apply(ast.literal_eval)
print("done read ", input_name)

bound_table = []
for index, row in df.iterrows():
    gauss_code = row[0]  # Extract Gauss code from the second column
    print("working on ", gauss_code)
    lower_bound_v1, upperbound_v1 = get_bounds(gauss_code)

    print("search with biquandle")
    my_length = gbbrcount([gauss_code], biquandle)
    lower_bound_v2 = int(my_length**(1/biquandle_length))
    bound_table.append([gauss_code, lower_bound_v1, upperbound_v1, lower_bound_v2])

# Convert lists to pandas DataFrame
bound_table_df = pd.DataFrame(bound_table, columns=["Gauss Code", "LB v1", "UB v1", "LB v2"])


bound_table_df.to_excel(excel_out_name, index=False)
print("Saved computing bound for v2 bridge to", excel_out_name)