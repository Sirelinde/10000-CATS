import csv

# Baseline probabilities for each place visit
baseline_probabilities_visit = {
    "Pet shop": 0.75,
    "SPCA": 0.04,
    "LAP": 0.01,
    "Ethical breeder": 0.10,
    "Unethical breeder": 0.10
}

# Baseline probabilities for entering a shop after visiting
baseline_probabilities_enter = {
    "Pet shop": 0.50,
    "SPCA": 0.10,
    "LAP": 0.10,
    "Ethical breeder": 0.10,
    "Unethical breeder": 0.10
}

# Baseline probabilities for actions
baseline_probabilities_actions = {
    "Abandon cat": 0.00,
    "Adopt cat": 0.10,
    "Adoption approval": 0.50,
    "Buy cat": 0.10,
    "Buy stuff": 0.50,
    "Donate": 0.50
}

def normalize_and_adjust_probabilities(visit_probs):
    # Normalize the probabilities to sum to 1
    total_prob = sum(visit_probs.values())
    if total_prob > 0:
        visit_probs = {k: v / total_prob for k, v in visit_probs.items()}
    
    # Sort the probabilities by value (ascending order)
    sorted_probs = sorted(visit_probs.items(), key=lambda item: item[1])

    # Adjust any probabilities that are 0 or negative
    for i, (key, value) in enumerate(sorted_probs):
        if value <= 0:
            deficit = 0.01 - value
            sorted_probs[i] = (key, 0.01)

            # Redistribute the deficit
            for j in range(i+1, len(sorted_probs)):
                donor_key, donor_value = sorted_probs[j]
                if donor_value > 0.01:
                    transfer_amount = min(deficit, donor_value - 0.01)
                    sorted_probs[j] = (donor_key, donor_value - transfer_amount)
                    deficit -= transfer_amount
                if deficit <= 0:
                    break

    # Ensure the probabilities sum to 1 after adjustment
    total_adjusted_prob = sum([prob for _, prob in sorted_probs])
    if total_adjusted_prob > 0:
        sorted_probs = [(key, prob / total_adjusted_prob) for key, prob in sorted_probs]

    return dict(sorted_probs)

def adjust_probabilities_without_normalization(probabilities):
    """ Adjust probabilities by setting any negative or zero values to 0.01 without normalization. """
    adjusted_probs = {}
    for key, value in probabilities.items():
        if value <= 0:
            adjusted_probs[key] = 0.01
        else:
            adjusted_probs[key] = value
    return adjusted_probs

def correct_small_values(probabilities):
    """ Correct small floating-point values close to zero. """
    corrected_probabilities = {}
    for key, value in probabilities.items():
        if abs(value) < 1e-10:
            corrected_probabilities[key] = 0.0
        else:
            corrected_probabilities[key] = value
    return corrected_probabilities

def process_csv(input_filename="adjusted_npc_probabilities.csv", output_filename="normalised_npc_probabilities.csv"):
    with open(input_filename, newline='') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Extract visiting probabilities
            visit_probs = {key: float(value) for key, value in row.items() if key in baseline_probabilities_visit.keys()}
            
            # Normalize and adjust visiting probabilities
            adjusted_visit_probs = normalize_and_adjust_probabilities(visit_probs)
            
            # Correct small floating-point values for visiting probabilities
            visit_probs_corrected = correct_small_values(adjusted_visit_probs)
            
            # Extract and adjust entering and action probabilities (without normalizing)
            enter_probs = {key: float(value) for key, value in row.items() if key.startswith("Enter ")}
            action_probs = {key: float(value) for key, value in row.items() if key in baseline_probabilities_actions.keys()}
            
            enter_probs_corrected = adjust_probabilities_without_normalization(enter_probs)
            action_probs_corrected = adjust_probabilities_without_normalization(action_probs)
            
            # Update the row with adjusted probabilities
            for key in visit_probs_corrected.keys():
                row[key] = visit_probs_corrected[key]
            for key in enter_probs_corrected.keys():
                row[key] = enter_probs_corrected[key]
            for key in action_probs_corrected.keys():
                row[key] = action_probs_corrected[key]

            writer.writerow(row)

# Execute the normalization and adjustment process
if __name__ == "__main__":
    process_csv(output_filename="normalised_npc_probabilities.csv")
