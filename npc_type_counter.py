import csv
from collections import defaultdict

def generate_profile_sentence(row):
    # Generate a descriptive sentence based on the row values
    sentence_parts = []
    
    if row["Owns a cat"] == "Yes":
        sentence_parts.append("Owns a cat")
        if row["New cat owner (1 year or less)"] == "Yes":
            sentence_parts.append("is a new cat owner")
        else:
            sentence_parts.append("is an experienced cat owner")
    else:
        sentence_parts.append("Does not own a cat")
        if row["Plans to get a new cat"] == "Yes":
            sentence_parts.append("plans to get a new cat")
        else:
            sentence_parts.append("does not plan to get a new cat")
    
    if row["Cat breed is important"] == "Yes":
        sentence_parts.append("cares about the cat breed")
    else:
        sentence_parts.append("does not care about the cat breed")
    
    if row["Well-informed on animal welfare"] == "Yes":
        sentence_parts.append("is well-informed on animal welfare")
    else:
        sentence_parts.append("is not well-informed on animal welfare")
    
    if row["Monthly income above 30,000 HKD"] == "Above":
        sentence_parts.append("has a monthly income above 30,000 HKD")
    else:
        sentence_parts.append("has a monthly income below 30,000 HKD")
    
    return ", ".join(sentence_parts)

def count_npc_types(filename="npc_profiles.csv", output_filename="npc_type_counts.csv"):
    # Initialize a dictionary to hold the counts of each type of NPC
    type_counts = defaultdict(int)

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Generate the profile sentence for this NPC
            profile_sentence = generate_profile_sentence(row)
            
            # Use the sentence as the key to count NPC types
            type_counts[profile_sentence] += 1

    # Write the counts to an output CSV file
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["NPC Profile", "Count"])
        
        for profile_sentence, count in type_counts.items():
            writer.writerow([profile_sentence, count])

# Execute the counting process
if __name__ == "__main__":
    count_npc_types()
