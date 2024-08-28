import os
print("Current Working Directory:", os.getcwd())

import subprocess

# List of script files to run in sequence
scripts = ["npc_questionnaire.py", "npc_adjustment_raw.py", "npc_adjustment_normalise.py", "npc_abandon_0.py", "npc_final_behaviour.py", "shop_tally_cap3.py", "npc_type_counter.py"]

for script in scripts:
    subprocess.run(["python", script], check=True)

