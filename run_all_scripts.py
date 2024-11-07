import os
print("Current Working Directory:", os.getcwd())

import subprocess

# List of script files to run in sequence
scripts = ["npc_questionnaire.py",
    "npc_adjustment_raw (backup).py",
    "npc_adjustment_normalise.py",
    "npc_abandon_0.py",
    "npc_probability_99.py",
    "npc_final_behaviour.py",
    "shop_tally_flex_spawn.py",
    "afcd_4_day_death_watch.py",
    "npc_type_counter.py"]

for script in scripts:
    subprocess.run(["python", script], check=True)

