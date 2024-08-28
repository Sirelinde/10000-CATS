import csv
import random

# Number of days run
days_run = 1 # Should run this code for 1 day but loop it 365 times in the run all accumulate script, then add the data in a cumulative csv. It will become more stable.

# RNG cats abandoned daily to the box or AFCD (data: case study said 379 cats received by AFCD in 2022 *1.04 per day), 151 rehomed (1 every 2.4 days) (39%). 10000 cats KILLED per year = 27-28 per day. More than that are abandoned. AFCD kills 48% cats received, mean at least 20000 cats abandoned)
cats_spawned_to_abandon = {
    "Ethical breeder": 0, # They don't abandon cats
    "Unethical breeder": int(random.random() * (20) + 10) * days_run, # Spawns between 10 to 30 cats
    "Pet shop": 0, # They don't abandon cats
    "SPCA": int(random.random() * (10) + 15) * days_run, # Spawns between 15 to 10 cats
    "LAP": int(random.random() * (10) + 5) * days_run, # Spawns between 5 to 15 cats
    "AFCD" : int(random.random() * (10) + 20) * days_run # Spawns between 20 to 30 cats
}

# Cats that end up in the box in each establishment
cats_in_box = {
    "Ethical breeder": 0, # They don't dump cats
    "Unethical breeder": 0, # All dumped to SPCA, LAP or AFCD
    "Pet shop": 0, # They don't dump cats
    "SPCA": cats_spawned_to_abandon["SPCA"] + int(cats_spawned_to_abandon["Unethical breeder"] * 0.2),
    "LAP": cats_spawned_to_abandon["LAP"] + int(cats_spawned_to_abandon["Unethical breeder"] * 0.05),
    "AFCD" : 2 + cats_spawned_to_abandon["AFCD"] + int(cats_spawned_to_abandon["Unethical breeder"] * 0.75)
}

# Vets euthanising unfit cats (unlikely to be rehomed)
euthanised_cats = {
    "Ethical breeder": 0, # They don't kill cats
    "Unethical breeder": 0, # All dumped to SPCA, LAP or AFCD
    "Pet shop": 0, # They don't kill cats
    "LAP": int(cats_in_box["LAP"] * 0.01), # No kill shelter except in special circumstances
    "SPCA": int(cats_in_box["SPCA"] * 0.1), # Kill cats unlikely to be rehomed
    "AFCD" : int(cats_in_box["AFCD"] * 0.3) # Kill cats unlikely to be rehomed
}

# Minusing unfit cats euthanised immediately after vetting
remaining_cats = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "LAP": cats_in_box["LAP"] - euthanised_cats["LAP"],
    "AFCD": cats_in_box["AFCD"] - euthanised_cats["AFCD"],
    "SPCA": cats_in_box["SPCA"] - euthanised_cats["SPCA"]
}

# Cats deemed vulnerable after vetting
vulnerable_cats = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "AFCD": int(random.random() * remaining_cats["AFCD"]),
    "SPCA": int(random.random() * remaining_cats["SPCA"]),
    "LAP": int(random.random() * remaining_cats["LAP"])
}

# Cats deemed healthy after vetting
healthy_cats = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "AFCD": remaining_cats["AFCD"] - vulnerable_cats["AFCD"],
    "SPCA": remaining_cats["SPCA"] - vulnerable_cats["SPCA"],
    "LAP": remaining_cats["LAP"] - vulnerable_cats["LAP"]
}

# Cats rejected from the shelter (sent to AFCD)
cats_rejected_from_shelter = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "AFCD": 0,
    "SPCA": int(random.random() * vulnerable_cats["SPCA"]), # Prioritise space for vulnerable cats
    "LAP": int(random.random() * healthy_cats["LAP"]) # Prioritise space for cats likely to be rehomed
}

# Cats in AFCD going to each shelter
vulnerable_cats_accepted_from_AFCD = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "AFCD": 0,
    # % of vulnerable cats from AFCD (prioritise saving the vulnerable)
    "LAP": int(0.5 * vulnerable_cats["AFCD"]),
    # % of healthy cats from AFCD (prioritise the likely to rehome)
    "SPCA": int(0.2 * vulnerable_cats["AFCD"])
}

# Healthy cats accepted from AFCD
healthy_cats_accepted_from_AFCD = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "AFCD": 0,
    # % of vulnerable cats from AFCD (prioritise saving the vulnerable)
    "LAP": int(0.2 * healthy_cats["AFCD"]),
    # % of healthy cats from AFCD (prioritise the likely to rehome)
    "SPCA": int(0.5 * healthy_cats["AFCD"])
}

# Total cats taken from AFCD
final_cats_accepted_from_AFCD = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "AFCD": 0,
    "LAP": vulnerable_cats_accepted_from_AFCD["LAP"] + healthy_cats_accepted_from_AFCD["LAP"],
    "SPCA": vulnerable_cats_accepted_from_AFCD["SPCA"] + healthy_cats_accepted_from_AFCD["SPCA"]
}

# Final vulnerable cats
final_vulnerable_cats = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "SPCA": vulnerable_cats["SPCA"] + vulnerable_cats_accepted_from_AFCD["SPCA"] - cats_rejected_from_shelter["SPCA"],
    "LAP": vulnerable_cats["LAP"] + vulnerable_cats_accepted_from_AFCD["LAP"],
    "AFCD": vulnerable_cats["AFCD"] - vulnerable_cats_accepted_from_AFCD["LAP"] - vulnerable_cats_accepted_from_AFCD["SPCA"] + cats_rejected_from_shelter["SPCA"]
}

# Final healthy cats
final_healthy_cats = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "SPCA": healthy_cats["SPCA"] + healthy_cats_accepted_from_AFCD["SPCA"],
    "LAP": healthy_cats["LAP"] + healthy_cats_accepted_from_AFCD["LAP"] - cats_rejected_from_shelter["LAP"],
    "AFCD": healthy_cats["AFCD"] - healthy_cats_accepted_from_AFCD["LAP"] - healthy_cats_accepted_from_AFCD["SPCA"] + cats_rejected_from_shelter["LAP"]
}

# Cats in each shelter
cats_in_shelter = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "SPCA": final_healthy_cats["SPCA"] + final_vulnerable_cats["SPCA"] + vulnerable_cats_accepted_from_AFCD["SPCA"] + healthy_cats_accepted_from_AFCD["SPCA"] - cats_rejected_from_shelter["SPCA"],
    "LAP": final_healthy_cats["LAP"] + final_vulnerable_cats["LAP"] + vulnerable_cats_accepted_from_AFCD["LAP"] + healthy_cats_accepted_from_AFCD["LAP"] - cats_rejected_from_shelter["LAP"],
    "AFCD": remaining_cats["AFCD"] - vulnerable_cats_accepted_from_AFCD["LAP"] - healthy_cats_accepted_from_AFCD["LAP"] - vulnerable_cats_accepted_from_AFCD["SPCA"] - healthy_cats_accepted_from_AFCD["SPCA"] + cats_rejected_from_shelter["SPCA"] + cats_rejected_from_shelter["LAP"]
}

number_of_shops = {
    # Seen as individual operations
    "Pet shop": 200,
    "Ethical breeder": 100,
    "Unethical breeder": 25,
    # Seen as whole organisations
    "SPCA": 1,
    "LAP": 1,
    "AFCD": 1
}

# Basic cost for taking care of cats
basic_care_per_cat = 25 # From the case study LAP's data
basic_care_cost = {
    "Pet shop": (basic_care_per_cat * 5 * number_of_shops["Pet shop"]) * days_run, # Pet shop pays to care for the stock of 5 cats which is always maintained at the same level, 200 pet shops in total
    "Ethical breeder": (basic_care_per_cat * (365 + 50)) * days_run, # Ethical breeder keeps 365 females. Males are much less.
    "Unethical breeder": (basic_care_per_cat * (375 + 50)) * days_run, # Unethical keeps 375 females. Males are much less.
    "SPCA": cats_in_shelter["SPCA"] * basic_care_per_cat, # Shelters pay for cats abandoned and cats surrendered
    "LAP": cats_in_shelter["LAP"] * basic_care_per_cat, # Shelters pay for cats abandoned and cats surrendered
    "AFCD": cats_in_shelter["AFCD"] * basic_care_per_cat # Shelters pay for cats abandoned and cats surrendered
}

# Vet fees per cat
basic_checkup_fee = 500 # Usual care involves vet visits every 4 months (3 days a year), 6 months (2 days a year) for unethical breeders
vulnerable_care_fee = 1400 # Average of 800 and 2000 from case study. Special care involves vet visits every 2 months (6 days a year)
vetting_fee = 500 # Every cat that that goes into the box has to be vetted for fit vs unfit (a basic checkup)
euthanasia_fee = 500 # For cats killed

# Regular checkups for all cats
basic_checkup_vet_cost = {
    # Pet shops usually stock no more than 5 cats, there are 200 pet shops in HK
    "Pet shop": int((basic_checkup_fee * 5 * number_of_shops["Pet shop"]) * days_run / 365 * 3),
    # 365F & 50M cats. 365F required to sustain the market demand of 3000 kittens a year (bred 1-2 times a year, average litter of 4)
    "Ethical breeder": int((basic_checkup_fee * (365 + 50)) * days_run / 365 * 3),
    # 375 & 50M cats. 375F required to sustain the market demand of 7000 kittens a year (bred 5 times a year, average litter of 4)
    "Unethical breeder": int((basic_checkup_fee * (375 + 50)) * days_run / 365 * 2),
    "SPCA": int(basic_checkup_fee * cats_in_shelter["SPCA"] / 365 * 3),
    "LAP": int(basic_checkup_fee * cats_in_shelter["LAP"] / 365 * 3),
    "AFCD" : 0 # They only keep cats for 4 days
}

# AFCD, LAP, SPCA vulnerable cat care cost
vulnerable_care_vet_cost = {
    "Ethical breeder": 0,
    "Unethical breeder": 0,
    "Pet shop": 0,
    "LAP": int((vulnerable_cats["LAP"] + vulnerable_cats_accepted_from_AFCD["LAP"]) * vulnerable_care_fee * days_run / 365 * 6),
    "SPCA": int((vulnerable_cats["SPCA"] + vulnerable_cats_accepted_from_AFCD["SPCA"]) * vulnerable_care_fee * days_run / 365 * 6),
    "AFCD": int((vulnerable_cats["AFCD"] - vulnerable_cats_accepted_from_AFCD["SPCA"] - vulnerable_cats_accepted_from_AFCD["LAP"]) * vulnerable_care_fee * days_run / 365 * 6)
}

# Prices for buying cats
cat_prices = {
    "Pet shop": 25000,
    "Ethical breeder": 20000,
    "Unethical breeder": 20000
}

# Adoption fees
adoption_fee = {
    "SPCA": 1500,
    "LAP": 1500
}

# Maximum number of cats that ethical breeders can sell each day (4 cats a litter)
MAX_CATS_SOLD_ETHICAL_BREEDER = 4 * days_run

# Restocking cost for pet shops (pet shop buying from unethical breeders)
restocking_cost_per_cat = 8000

# Cost multipliers for rent (exempted for ethical breeder because it's their home)
base_rent = 1000 # For a small shop NOT in the city centre
total_rent = {
    "Pet shop": base_rent * number_of_shops["Pet shop"] * days_run, # There are 200 pet shops 
    "Ethical breeder": 0, #base_rent * 2 * number_of_shops["Ethical breeder"] * days_run * 0, There are about 100 ethical breeders but rent is negligible cos they operate from their own homes
    "Unethical breeder": (base_rent * 2) * number_of_shops["Unethical breeder"] * days_run, # There are 25 unethical breeders who each own a large breeding farm
    "SPCA": 950 * 10 * days_run, # Used same figure as LAP. There are 10 shelters run by SPCA
    "LAP": 950 * 4 * days_run, # Figure from case study. There are 4 shelters run by LAP, including the cat adoption centre
    "AFCD" : (base_rent / 2) * 4 * days_run # 4 management centres according to case study, they are government run so rent may be cheaper
}

# Daily miscellaneous operational costs. A very rough estimate of other costs like utility bills, staff salaries, facility maintenance, insurance, marketing, educational outreach, adminsitration, transportation etc.
misc_operational_costs = { 
    "Pet shop": 5000 * number_of_shops["Pet shop"] * days_run, # There are 200 pet shops
    "Ethical breeder": 100 * number_of_shops["Ethical breeder"] * days_run, # There are about 100 ethical breeders but operate from their own homes so assume minimal costs
    "Unethical breeder": 3000 * number_of_shops["Unethical breeder"] * days_run, # There are 25 unethical breeders who each occupy a large breeding farm
    "SPCA": 40000 * days_run, # SPCA is a larger organisation than LAP
    "LAP": 20000 * days_run, # LAP is smaller than SPCA
    "AFCD" : 40000 * days_run # Rough estimate close to SPCA since they don't dedicate all their resources to dealing with abandoned animals
}

# Breeding care costs for mother cat (deleted 2 month gestation care divided by litter of 4) + basic care per kitten sold (care 1-2 months after birth)
breeding_care_costs = {
    "Ethical breeder": 4000,
    "Unethical breeder": 3000
}

def analyze_npc_actions(filename="npc_actions.csv"):
    # Initialize summary statistics for each establishment
    establishments = {
        "Pet shop": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Abandoned Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": cats_spawned_to_abandon["Pet shop"], "Cats Transferred to Box": cats_in_box["Pet shop"], "Euthanised after Vetting": euthanised_cats["Pet shop"], 
                     "Remaining Healthy Cats": healthy_cats["Pet shop"], "Remaining Vulnerable Cats": vulnerable_cats["Pet shop"], "Cats Rejected from Shelter": cats_rejected_from_shelter["Pet shop"], "Final Cats in Shelter": cats_in_shelter["Pet shop"], 
                     "Final Healthy Cats": final_healthy_cats["Pet shop"], "Final Vulnerable Cats": final_vulnerable_cats["Pet shop"], "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed": 0},
        "SPCA": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Abandoned Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": cats_spawned_to_abandon["SPCA"], "Cats Transferred to Box": cats_in_box["SPCA"], "Euthanised after Vetting": euthanised_cats["SPCA"], 
                     "Remaining Healthy Cats": healthy_cats["SPCA"], "Remaining Vulnerable Cats": vulnerable_cats["SPCA"], "Cats Rejected from Shelter": cats_rejected_from_shelter["SPCA"], "Final Cats in Shelter": cats_in_shelter["SPCA"], 
                     "Final Healthy Cats": final_healthy_cats["SPCA"], "Final Vulnerable Cats": final_vulnerable_cats["SPCA"], "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed": 0},
        "LAP": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Abandoned Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": cats_spawned_to_abandon["LAP"], "Cats Transferred to Box": cats_in_box["LAP"], "Euthanised after Vetting": euthanised_cats["LAP"], 
                     "Remaining Healthy Cats": healthy_cats["LAP"], "Remaining Vulnerable Cats": vulnerable_cats["LAP"], "Cats Rejected from Shelter": cats_rejected_from_shelter["LAP"], "Final Cats in Shelter": cats_in_shelter["LAP"], 
                     "Final Healthy Cats": final_healthy_cats["LAP"], "Final Vulnerable Cats": final_vulnerable_cats["LAP"], "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed": 0},
        "Ethical breeder": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Abandoned Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": cats_spawned_to_abandon["Ethical breeder"], "Cats Transferred to Box": cats_in_box["Ethical breeder"], "Euthanised after Vetting": euthanised_cats["Ethical breeder"], 
                     "Remaining Healthy Cats": healthy_cats["Ethical breeder"], "Remaining Vulnerable Cats": vulnerable_cats["Ethical breeder"], "Cats Rejected from Shelter": cats_rejected_from_shelter["Ethical breeder"], "Final Cats in Shelter": cats_in_shelter["Ethical breeder"], 
                     "Final Healthy Cats": final_healthy_cats["Ethical breeder"], "Final Vulnerable Cats": final_vulnerable_cats["Ethical breeder"], "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed": 0},
        "Unethical breeder": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Abandoned Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": cats_spawned_to_abandon["Unethical breeder"], "Cats Transferred to Box": cats_in_box["Unethical breeder"], "Euthanised after Vetting": euthanised_cats["Unethical breeder"], 
                     "Remaining Healthy Cats": healthy_cats["Unethical breeder"], "Remaining Vulnerable Cats": vulnerable_cats["Unethical breeder"], "Cats Rejected from Shelter": cats_rejected_from_shelter["Unethical breeder"], "Final Cats in Shelter": cats_in_shelter["Unethical breeder"], 
                     "Final Healthy Cats": final_healthy_cats["Unethical breeder"], "Final Vulnerable Cats": final_vulnerable_cats["Unethical breeder"], "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed": 0},
        "AFCD": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Abandoned Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": cats_spawned_to_abandon["AFCD"], "Cats Transferred to Box": cats_in_box["AFCD"], "Euthanised after Vetting": euthanised_cats["AFCD"], 
                     "Remaining Healthy Cats": healthy_cats["AFCD"], "Remaining Vulnerable Cats": vulnerable_cats["AFCD"], "Cats Rejected from Shelter": cats_rejected_from_shelter["AFCD"], "Final Cats in Shelter": cats_in_shelter["AFCD"], 
                     "Final Healthy Cats": final_healthy_cats["AFCD"], "Final Vulnerable Cats": final_vulnerable_cats["AFCD"], "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed": 0}
    }

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            place = row["Visit"]
            establishments[place]["Visited"] += 1
            
            if row["Enter"] == "Yes":
                establishments[place]["Entered"] += 1

                # Handle pet shop and breeders
                if row["Buy cat"] == "Yes" and place in ["Pet shop", "Ethical breeder", "Unethical breeder"]:
                    if place == "Ethical breeder":
                        if establishments[place]["Bought Cat"] < MAX_CATS_SOLD_ETHICAL_BREEDER:
                            establishments[place]["Bought Cat"] += 1
                            establishments[place]["Cats Sold/Adopted"] += 1
                            establishments[place]["Profit from Cats"] += cat_prices[place]
                            establishments[place]["Breeding Care Costs"] += breeding_care_costs["Ethical breeder"]
                        else:
                            establishments[place]["Unmet Demand"] += 1
                    elif place == "Pet shop":
                        establishments[place]["Bought Cat"] += 1
                        establishments[place]["Cats Sold/Adopted"] += 1
                        establishments[place]["Profit from Cats"] += cat_prices[place]
                        establishments[place]["Restocking Costs"] += restocking_cost_per_cat
                        establishments["Unethical breeder"]["Breeding Care Costs"] += breeding_care_costs["Unethical breeder"]
                        establishments["Unethical breeder"]["Profit from Supplying"] += restocking_cost_per_cat  
                    elif place == "Unethical breeder":
                        establishments[place]["Bought Cat"] += 1
                        establishments[place]["Cats Sold/Adopted"] += 1
                        establishments[place]["Profit from Cats"] += cat_prices[place]
                        establishments[place]["Breeding Care Costs"] += breeding_care_costs["Unethical breeder"]
                                        
                # Handle SPCA and LAP
                if row["Adopt cat"] == "Yes":
                    establishments[place]["Tried to Adopt Cat"] += 1
                    if row["Adoption approval"] == "Yes" and place in ["SPCA", "LAP"]:
                        establishments[place]["Adopted Cat"] += 1
                        establishments[place]["Cats Sold/Adopted"] += 1
                        establishments[place]["Profit from Cats"] += adoption_fee[place]
                        establishments[place]["Final Cats in Shelter"] -= 1

                if row["Abandon cat"] == "Yes" and place in ["SPCA", "LAP"]:
                    establishments[place]["Abandoned Cat"] += 1
                    establishments[place]["Cats Transferred to Box"] += 1

                if row["Buy stuff"] == "Yes":
                    amount_spent = int(row["Amount spent on stuff"])
                    establishments[place]["Bought Stuff"] += 1
                    establishments[place]["Profit from Stuff"] += amount_spent

                if row["Donate"] == "Yes":
                    donation_amount = int(row["Donation amount"])
                    establishments[place]["Donated"] += 1
                    establishments[place]["Profit from Donations"] += donation_amount

                #Count the total number of actions
                #establishments[place]["Total Actions"] += (
                #    establishments[place]["Bought Cat"] +
                #    establishments[place]["Tried to Adopt Cat"] +
                #    establishments[place]["Adopted Cat"] +
                #    establishments[place]["Bought Stuff"] +
                #    establishments[place]["Donated"] +
                #    establishments[place]["Abandoned Cat"]
                #)
    
    # AFCD, LAP, SPCA cat vetting cost
    vetting_cost = {
        "Ethical breeder": 0,
        "Unethical breeder": 0,
        "Pet shop": 0,
        "SPCA": establishments["SPCA"]["Cats Transferred to Box"] * vetting_fee,
        "LAP": establishments["LAP"]["Cats Transferred to Box"] * vetting_fee,
        "AFCD": cats_in_box["AFCD"] * vetting_fee
    }

    # Euthanasia costs
    euthanasia_cost = {
        "Ethical breeder": 0,
        "Unethical breeder": 0,
        "Pet shop": 0,
        "LAP": 0, # No kill shelter
        "SPCA": euthanised_cats["SPCA"] * euthanasia_fee,
        "AFCD": euthanised_cats["AFCD"] * euthanasia_fee
    }

    # Total vet fees for each establishment (basic checkup, vulnerable care, vetting, euthanasias)
    total_vet_cost = {
        "Pet shop": basic_checkup_vet_cost["Pet shop"],
        "Ethical breeder": basic_checkup_vet_cost["Ethical breeder"],
        "Unethical breeder": basic_checkup_vet_cost["Unethical breeder"],
        "SPCA": basic_checkup_vet_cost["SPCA"] + vulnerable_care_vet_cost["SPCA"] + vetting_cost["SPCA"] + euthanasia_cost["SPCA"],
        "LAP": basic_checkup_vet_cost["LAP"] + vulnerable_care_vet_cost["LAP"] + vetting_cost["LAP"],
        "AFCD": basic_checkup_vet_cost["AFCD"] + vulnerable_care_vet_cost["AFCD"] + vetting_cost["AFCD"] + euthanasia_cost["AFCD"]
    }

    # Calculate total costs for each establishment
    for place, data in establishments.items():
        data["Total Rent"] = total_rent[place]
        data["Misc Operational Costs"] = misc_operational_costs[place]
        data["Basic Care Cost"] = basic_care_cost[place]
        data["Basic Checkup Cost"] = basic_checkup_vet_cost[place]
        data["Vulnerable Care Cost"] = vulnerable_care_vet_cost[place]
        data["Vetting Cost"] = vetting_cost[place]
        data["Euthanasia Cost"] = euthanasia_cost[place]
        data["Total Vet Cost"] = total_vet_cost[place]
        data["Total Costs"] = data["Total Rent"] + data["Misc Operational Costs"] + data["Breeding Care Costs"] + data["Restocking Costs"] + data["Basic Care Cost"] + data["Total Vet Cost"]
        data["Total Profit"] = data["Profit from Cats"] + data["Profit from Stuff"] + data["Profit from Donations"] + data["Profit from Supplying"]
        data["Final Net Income"] = data["Total Profit"] - data["Total Costs"]
        data["Final Net Income Per Place"] = data["Final Net Income"] / number_of_shops[place]
        data["Total Cats Killed"] = cats_in_shelter["AFCD"] + euthanised_cats["AFCD"] + euthanised_cats["LAP"] + euthanised_cats["SPCA"]

    return establishments

def save_analysis(analysis, filename="npc_analysis.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            "Establishment", "Visited", "Entered", "Bought Cat", "Tried to Adopt Cat", "Adopted Cat", "Bought Stuff", "Donated", "Abandoned Cat", #"Total Actions",
            "Cats Sold/Adopted", "Total Profit", "Profit from Cats", "Profit from Stuff", "Profit from Donations", "Profit from Supplying", "Unmet Demand",
            "Total Costs", "Breeding Care Costs", "Restocking Costs", "Total Rent", "Misc Operational Costs", "Basic Care Cost", "Total Vet Cost", 
            "Cats Spawned to Abandon", "Cats Transferred to Box", "Euthanised after Vetting", "Remaining Healthy Cats", "Remaining Vulnerable Cats", 
            "Cats Rejected from Shelter", "Final Cats in Shelter", "Final Healthy Cats", "Final Vulnerable Cats",
            "Basic Checkup Cost", "Vulnerable Care Cost", "Vetting Cost", "Euthanasia Cost", "Final Net Income", "Final Net Income Per Place", "Total Cats Killed"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for place, data in analysis.items():
            row = {
                "Establishment": place,
                "Visited": data.get("Visited", 0),
                "Entered": data.get("Entered", 0),
                "Bought Cat": data.get("Bought Cat", 0),
                "Tried to Adopt Cat": data.get("Tried to Adopt Cat", 0),
                "Adopted Cat": data.get("Adopted Cat", 0),
                "Bought Stuff": data.get("Bought Stuff", 0),
                "Donated": data.get("Donated", 0),
                "Abandoned Cat": data.get("Abandoned Cat", 0),
                #"Total Actions": data.get("Total Actions", 0),
                "Cats Sold/Adopted": data.get("Cats Sold/Adopted", 0),
                "Total Profit": data.get("Total Profit", 0),
                "Profit from Cats": data.get("Profit from Cats", 0),
                "Profit from Stuff": data.get("Profit from Stuff", 0),
                "Profit from Donations": data.get("Profit from Donations", 0),
                "Profit from Supplying": data.get("Profit from Supplying", 0),
                "Unmet Demand": data.get("Unmet Demand", 0),
                "Total Costs": data.get("Total Costs", 0),
                "Breeding Care Costs": data.get("Breeding Care Costs", 0),
                "Restocking Costs": data.get("Restocking Costs", 0),
                "Total Rent": data.get("Total Rent", 0),
                "Misc Operational Costs": data.get("Misc Operational Costs", 0),
                "Basic Care Cost": data.get("Basic Care Cost", 0),
                "Total Vet Cost": data.get("Total Vet Cost", 0),
                "Cats Spawned to Abandon": data.get("Cats Spawned to Abandon", 0),
                "Cats Transferred to Box": data.get("Cats Transferred to Box", 0),
                "Euthanised after Vetting": data.get("Euthanised after Vetting", 0),
                "Remaining Healthy Cats": data.get("Remaining Healthy Cats", 0),
                "Remaining Vulnerable Cats": data.get("Remaining Vulnerable Cats", 0),
                "Cats Rejected from Shelter": data.get("Cats Rejected from Shelter", 0),
                "Final Cats in Shelter": data.get("Final Cats in Shelter", 0),
                "Final Healthy Cats": data.get("Final Healthy Cats", 0),
                "Final Vulnerable Cats": data.get("Final Vulnerable Cats", 0),
                "Basic Checkup Cost": data.get("Basic Checkup Cost", 0),
                "Vulnerable Care Cost": data.get("Vulnerable Care Cost", 0),
                "Vetting Cost": data.get("Vetting Cost", 0),
                "Euthanasia Cost": data.get("Euthanasia Cost", 0),
                "Final Net Income": data.get("Final Net Income", 0),
                "Final Net Income Per Place": data.get("Final Net Income Per Place", 0),
                "Total Cats Killed": data.get("Total Cats Killed", 0)
            }
            writer.writerow(row)

def main():
    analysis = analyze_npc_actions()
    save_analysis(analysis)

if __name__ == "__main__":
    main()