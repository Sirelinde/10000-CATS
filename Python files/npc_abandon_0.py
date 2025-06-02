import csv

def set_abandon_cat_to_zero(original_filename="npc_profiles.csv", input_filename="normalised_npc_probabilities.csv", output_filename="npc_probabilities_abandon_0.csv"):
    # Load the ownership data from the original CSV file using row number as the identifier
    ownership_data = []
    with open(original_filename, newline='') as orig_file:
        reader = csv.DictReader(orig_file)
        for row in reader:
            ownership_data.append(row.get("Owns a cat"))

    # Process the adjusted probabilities file and correct the abandon cat probabilities
    with open(input_filename, newline='') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, row in enumerate(reader):
            # Check if the NPC does not own a cat based on the row number
            if i < len(ownership_data) and ownership_data[i] == "No":
                # Set "Abandon cat" probability to 0
                row["Abandon cat"] = 0.0

            writer.writerow(row)

# Execute the adjustment process
if __name__ == "__main__":
    set_abandon_cat_to_zero()
