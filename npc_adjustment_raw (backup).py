import csv

# Baseline probabilities for exposure to each place
baseline_probabilities_visit = {
    "Pet shop": 0.75,
    "SPCA": 0.04,
    "LAP": 0.01,
    "Ethical breeder": 0.10,
    "Unethical breeder": 0.10
}

# Baseline probabilities for engaging after exposure
baseline_probabilities_enter = {
    "Pet shop": 0.60,
    "SPCA": 0.10,
    "LAP": 0.10,
    "Ethical breeder": 0.15,
    "Unethical breeder": 0.15
}

# Baseline probabilities for actions after deciding to engage
baseline_probabilities_actions = {
    "Abandon cat": 0.00,
    "Adopt cat": 0.06,
    "Adoption approval": 0.50,
    "Buy cat": 0.13,
    "Buy stuff": 0.30,
    "Donate": 0.20
}

def adjust_probabilities(npc):
    visit_probabilities = baseline_probabilities_visit.copy()
    enter_probabilities = baseline_probabilities_enter.copy()
    action_probabilities = baseline_probabilities_actions.copy()

    # Adjustments based on whether they own a cat
    if npc.get("Owns a cat") == "Yes":
        action_probabilities["Abandon cat"] += 0.05
        action_probabilities["Adoption approval"] += 0.20
        action_probabilities["Donate"] += 0.20
        action_probabilities["Buy stuff"] += 0.20
        for key in enter_probabilities:
            enter_probabilities[key] += 0.10

        # Further adjustments for new or experienced cat owners
        if npc.get("New cat owner (1 year or less)") == "Yes":
            action_probabilities["Abandon cat"] += 0.55 # Immediately bumped up to 60% to match case study saying 60% cats abandoned within the first 6 months
        else:  # Experienced owner
            action_probabilities["Adoption approval"] += 0.20
            action_probabilities["Donate"] += 0.10
    else:  # Does not own a cat
        action_probabilities["Adoption approval"] -= 0.10
        action_probabilities["Buy stuff"] -= 0.10
        action_probabilities["Donate"] -= 0.10

        for key in enter_probabilities:
            enter_probabilities[key] -= 0.05

    # Adjustments based on whether they plan to get a new cat
    if npc.get("Plans to get a new cat") == "Yes":
        action_probabilities["Adopt cat"] += 0.10
        action_probabilities["Buy cat"] += 0.10
        for key in enter_probabilities:
            enter_probabilities[key] += 0.20
        
        if npc.get("Owns a cat") == "Yes":
            action_probabilities["Abandon cat"] -= 0.01

        if npc.get("Cat breed is important") == "Yes":
            visit_probabilities["Ethical breeder"] += 0.10
            visit_probabilities["Unethical breeder"] += 0.10
            visit_probabilities["Pet shop"] += 0.10
            visit_probabilities["SPCA"] -= 0.01
            visit_probabilities["LAP"] -= 0.01
        else:  # Breed is not important
            visit_probabilities["LAP"] += 0.05
            visit_probabilities["SPCA"] += 0.05
            visit_probabilities["Ethical breeder"] -= 0.05
            visit_probabilities["Unethical breeder"] -= 0.05
    else:  # Does not plan to get a new cat
        action_probabilities["Adopt cat"] -= 0.40
        action_probabilities["Buy cat"] -= 0.40
        for key in enter_probabilities:
            enter_probabilities[key] -= 0.10

    # Adjustments based on whether they are well-informed on the pet abandonment situation in HK
    if npc.get("Well-informed on animal welfare") == "Yes":
        if npc.get("New cat owner (1 year or less)") == "No":
            action_probabilities["Abandon cat"] -= 0.02
        else: # New cat owner
            action_probabilities["Abandon cat"] -= 0.20
        action_probabilities["Donate"] += 0.10
        action_probabilities["Adoption approval"] += 0.10
        action_probabilities["Buy cat"] -= 0.20
        visit_probabilities["SPCA"] += 0.25
        visit_probabilities["LAP"] += 0.25
        visit_probabilities["Ethical breeder"] += 0.10
        visit_probabilities["Pet shop"] -= 0.30
        visit_probabilities["Unethical breeder"] -= 0.30
        for key in ["Ethical breeder", "Unethical breeder", "Pet shop"]:
            enter_probabilities[key] -= 0.20
    else:  # Not well-informed on animal welfare
        action_probabilities["Donate"] -= 0.10
        action_probabilities["Adopt cat"] -= 0.10
        action_probabilities["Adoption approval"] -= 0.10
        if npc.get("New cat owner (1 year or less)") == "No":
            action_probabilities["Abandon cat"] += 0.05
        else: #New cat owner
            action_probabilities["Abandon cat"] += 0.20

    # Adjustments based on monthly income
    if npc.get("Monthly income above 20,000 HKD") == "Above":
        action_probabilities["Adoption approval"] += 0.10
        action_probabilities["Buy cat"] += 0.05
        action_probabilities["Adopt cat"] += 0.05
        action_probabilities["Buy stuff"] += 0.10
        action_probabilities["Donate"] += 0.10
        visit_probabilities["Ethical breeder"] += 0.05
        visit_probabilities["Pet shop"] += 0.05
        visit_probabilities["LAP"] -= 0.05
        visit_probabilities["SPCA"] -= 0.05
        for key in enter_probabilities:
            enter_probabilities[key] += 0.10
    else:  # Below 20,000 HKD
        action_probabilities["Adoption approval"] -= 0.10
        action_probabilities["Abandon cat"] += 0.05
        action_probabilities["Buy cat"] -= 0.15
        action_probabilities["Adopt cat"] -= 0.15
        action_probabilities["Donate"] -= 0.10
        visit_probabilities["Unethical breeder"] += 0.05
        visit_probabilities["Ethical breeder"] -= 0.15
        visit_probabilities["SPCA"] += 0.05
        visit_probabilities["LAP"] += 0.05
        for key in enter_probabilities:
            enter_probabilities[key] -= 0.05

    return visit_probabilities, enter_probabilities, action_probabilities

# Read NPC profiles from the CSV file
def read_npc_profiles(filename="npc_profiles.csv"):
    npc_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            npc_list.append(row)
    return npc_list

# Adjust probabilities for all NPCs and save the results
def adjust_npc_probabilities(npc_list, output_filename="adjusted_npc_probabilities.csv"):
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = (
            list(baseline_probabilities_visit.keys()) +
            ["Enter " + place for place in baseline_probabilities_enter.keys()] +
            list(baseline_probabilities_actions.keys())
        )
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for npc in npc_list:
            visit_probs, enter_probs, action_probs = adjust_probabilities(npc)
            combined_probs = {
                **visit_probs,
                **{"Enter " + k: v for k, v in enter_probs.items()},
                **action_probs
            }
            writer.writerow(combined_probs)

# Main function to run the adjustments
def main():
    npc_list = read_npc_profiles()
    adjust_npc_probabilities(npc_list)

# Execute the main function
if __name__ == "__main__":
    main()
