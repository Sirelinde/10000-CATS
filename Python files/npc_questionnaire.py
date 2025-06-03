import random
import csv

def generate_npc():
    npc_profile = {
        "Owns a cat": "No",
        "New cat owner (1 year or less)": "N/A",
        "Plans to get a new cat": "No",
        "Cat breed is important": "N/A",
        "Well-informed on animal welfare": "N/A",
        "Monthly income above 20,000 HKD": "Below"
    }

    # Question 1 (Do you own a cat?)
    npc_profile["Owns a cat"] = "Yes" if random.random() < 0.09 else "No"
    
    if npc_profile["Owns a cat"] == "Yes":
        # Question 1.1 (Are you a new cat owner, i.e. had a cat for 1 year or less?)
        npc_profile["New cat owner (1 year or less)"] = "Yes" if random.random() < 0.06 else "No"
    
    # Question 2 (Is cat breed important to you?)
    npc_profile["Cat breed is important"] = "Yes" if random.random() < 0.75 else "No"

    # Question 3 (Are you well-informed on animal welfare and the pet abandonment situation in HK?)
    npc_profile["Well-informed on animal welfare"] = "Yes" if random.random() < 0.30 else "No" # This is the parameter to be changed in the simulation (from 30% to 40%)

    # Question 4 (Do you want/plan to get a new cat?)
    npc_profile["Plans to get a new cat"] = "Yes" if random.random() < 0.25 else "No"
    
    # Question 5 (Is your monthly income above or below 20,000 HKD?)
    npc_profile["Monthly income above 20,000 HKD"] = "Above" if random.random() < 0.50 else "Below"

    return npc_profile

def generate_npcs(n):
    npc_list = []
    for _ in range(n):
        npc_list.append(generate_npc())
    return npc_list

def save_to_csv(npc_list, filename="npc_profiles.csv"):
    keys = npc_list[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(npc_list)

# Number of NPCs to generate
days_run = 1 # Should run this code for 1 day but loop it 365 times in the run_all_accumulate script, then add the data in a cumulative csv. It will become more stable.
num_npcs_per_day = 8000 * days_run # Number based on minimum foot traffic to keep pet shops alive, multiply by 2. Estimate of total people who participate in this system per day.
npcs = generate_npcs(num_npcs_per_day)
save_to_csv(npcs)
