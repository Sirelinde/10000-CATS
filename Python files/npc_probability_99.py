import pandas as pd

# Specify the input and output file names
input_file = "npc_probabilities_abandon_0.csv"
output_file = "final_npc_probabilities.csv"

# Load the CSV into a DataFrame
df = pd.read_csv(input_file)

# Function to check and modify values
def check_value(x):
    if pd.api.types.is_numeric_dtype(type(x)) and x >= 1:
        return 0.99
    else:
        return x

# Apply the function to each column using DataFrame.apply
df = df.apply(lambda col: col.map(check_value) if pd.api.types.is_numeric_dtype(col) else col)

# Save the modified DataFrame to a new CSV file, keeping the same format
df.to_csv(output_file, index=False)

