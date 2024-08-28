import subprocess
import pandas as pd
import os

days_run = 30

# Define the script names
scripts = [
    "npc_questionnaire.py",
    "npc_adjustment_raw (backup).py",
    "npc_adjustment_normalise.py",
    "npc_abandon_0.py",
    "npc_final_behaviour.py",
    "shop_tally_cap3.py",
    "npc_type_counter.py"
]

# Paths to accumulate data
npc_analysis_accumulated = "npc_analysis_accumulated.csv"
npc_type_counts_accumulated = "npc_type_counts_accumulated.csv"

# Initialize empty DataFrames to accumulate results
npc_analysis_total = None
npc_type_counts_total = None

# Function to run a script
def run_script(script_name):
    subprocess.run(["python", script_name], check=True)

# Run the scripts 5 times (for testing purposes)
for run in range(days_run):
    print(f"Run {run + 1} of {days_run}")
    for script in scripts:
        run_script(script)
    
    # Read the current run's CSV files
    npc_analysis = pd.read_csv("npc_analysis.csv", index_col=0)
    npc_type_counts = pd.read_csv("npc_type_counts.csv", index_col=0)
    
    # Ensure only numeric data is accumulated
    npc_analysis_numeric = npc_analysis.select_dtypes(include=[float, int])
    npc_type_counts_numeric = npc_type_counts.select_dtypes(include=[float, int])
    
    if npc_analysis_total is None:
        npc_analysis_total = npc_analysis_numeric.copy()
    else:
        npc_analysis_total = npc_analysis_total.add(npc_analysis_numeric, fill_value=0)
    
    if npc_type_counts_total is None:
        npc_type_counts_total = npc_type_counts_numeric.copy()
    else:
        npc_type_counts_total = npc_type_counts_total.add(npc_type_counts_numeric, fill_value=0)

# Save accumulated data to new CSV files
npc_analysis_total.to_csv(npc_analysis_accumulated)
npc_type_counts_total.to_csv(npc_type_counts_accumulated)

print("Simulation complete. Files saved as 'npc_analysis_accumulated.csv' and 'npc_type_counts_accumulated.csv'.")
