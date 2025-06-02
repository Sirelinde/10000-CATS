import csv
import random

# Use pre-adjusted probabilities to determine final behaviour
def determine_actions(npc_data):
    place_visited = weighted_choice({place: float(npc_data[place]) for place in ["Pet shop", "SPCA", "LAP", "Ethical breeder", "Unethical breeder"]})
    enter_place = random.random() < float(npc_data[f"Enter {place_visited}"])

    if not enter_place:
        return {"Visit": place_visited, "Enter": "No"}

    actions = {"Visit": place_visited, "Enter": "Yes"}

    if place_visited in ["SPCA", "LAP"]:
        actions["Abandon cat"] = "Yes" if random.random() < float(npc_data["Abandon cat"]) else "No"
        actions["Adopt cat"] = "Yes" if random.random() < (float(npc_data["Adopt cat"]) * 1) else "No" # Constant for model adjustment

        if actions["Adopt cat"] == "Yes":
            actions["Adoption approval"] = "Yes" if random.random() < (float(npc_data["Adoption approval"]) * 1) else "No" # Constant for model adjustment
        else:
            actions["Adoption approval"] = "N/A"

        actions["Donate"] = "Yes" if random.random() < float(npc_data["Donate"]) else "No"
        if actions["Donate"] == "Yes":
            actions["Donation amount"] = random.randint(1, 1000) # Data from case study
        else:
            actions["Donation amount"] = 0
    else:
        actions["Abandon cat"] = "N/A"
        actions["Adopt cat"] = "N/A"
        actions["Adoption approval"] = "N/A"
        actions["Donate"] = "N/A"
        actions["Donation amount"] = 0

    if place_visited in ["Ethical breeder", "Unethical breeder"]:
        actions["Buy cat"] = "Yes" if random.random() < float(npc_data["Buy cat"]) else "No"
    elif place_visited in ["Pet shop"]:
        actions["Buy cat"] = "Yes" if random.random() < (float(npc_data["Buy cat"]) / 4) else "No" # Model adjustment, people in shelters are more likely to go there with intention to adopt than people at pet shops with intention to buy (e.g. browsers) (to match ratio in case study)
    else:
        actions["Buy cat"] = "N/A"

    if place_visited in ["SPCA", "LAP"]:
        actions["Buy stuff"] = "Yes" if random.random() < float(npc_data["Buy stuff"]) else "No"
        if actions["Buy stuff"] == "Yes":
            actions["Amount spent on stuff"] = random.randint(20, 100) # Data from case study
        else:
            actions["Amount spent on stuff"] = 0
    elif place_visited in ["Pet shop"]:
        actions["Buy stuff"] = "Yes" if random.random() < (float(npc_data["Buy stuff"]) * 1) else "No" # Constant for future model adjustment, expected conversion rate 40-60% (web research)
        if actions["Buy stuff"] == "Yes":
            actions["Amount spent on stuff"] = random.randint(20, 1000) # Data from friends and family
        else:
            actions["Amount spent on stuff"] = 0
    else:
        actions["Buy stuff"] = "N/A"
        actions["Amount spent on stuff"] = 0

    return actions

def weighted_choice(weights):
    total = sum(weights.values())
    r = random.uniform(0, total)
    upto = 0
    for key, weight in weights.items():
        if upto + weight >= r:
            return key
        upto += weight

def read_npc_probabilities(filename="final_npc_probabilities.csv"):
    actions_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            actions = determine_actions(row)
            actions_list.append(actions)
    return actions_list

def save_npc_actions(actions_list, output_filename="npc_actions.csv"):
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ["Visit", "Enter", "Abandon cat", "Adopt cat", "Adoption approval", "Buy cat", "Buy stuff", "Amount spent on stuff", "Donate", "Donation amount"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for actions in actions_list:
            writer.writerow(actions)

def main():
    npc_actions = read_npc_probabilities()
    save_npc_actions(npc_actions)

if __name__ == "__main__":
    main()
