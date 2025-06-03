import csv
import random

# Number of days run
days_run = 1 # Should run this code for 1 day but loop it 365 times in the run all accumulate script, then add the data in a cumulative csv. It will become more stable.

# INTERACT WITH NPC_ACTIONS.CSV

# Start reading npc_actions.csv
def analyze_npc_actions(filename="npc_actions.csv"):
    # Initialize summary statistics for each establishment in the output later: npc_analysis_flex.csv
    establishments = {
        "Pet shop": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0},
        "SPCA": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0},
        "LAP": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0},
        "Ethical breeder": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0},
        "Unethical breeder": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0},
        "AFCD": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0},
        "Other charities": {"Visited": 0, "Entered": 0, "Bought Cat": 0, "Tried to Adopt Cat": 0, "Adopted Cat": 0, "Bought Stuff": 0, "Donated": 0, "Surrendered Cat": 0, "Cats Sold/Adopted": 0, #"Total Actions": 0,
                     "Total Profit": 0, "Profit from Cats": 0, "Profit from Stuff": 0, "Profit from Donations": 0, "Profit from Supplying": 0, "Unmet Demand": 0, "Total Costs": 0, "Breeding Care Costs": 0, "Restocking Costs": 0, "Total Rent": 0, "Misc Operational Costs": 0,
                     "Cats Spawned to Abandon": 0, "Cats Transferred to Box": 0, "Euthanised after Vetting": 0, 
                     "Remaining Healthy Cats": 0, "Remaining Vulnerable Cats": 0, "Cats Rejected from Shelter": 0, "Cats Claimed from AFCD": 0, "Cats Claimed from SPCA": 0, "Final Cats in Shelter": 0, 
                     "Final Healthy Cats": 0, "Final Vulnerable Cats": 0, "Basic Care Cost": 0, "Vulnerable Care Cost": 0, 
                     "Total Vet Cost": 0, "Basic Checkup Cost": 0, "Vetting Cost": 0, "Euthanasia Cost": 0, "Final Net Income": 0, "Final Net Income Per Place": 0, "Total Cats Killed (everyone)": 0}
    }
    
    # Defining constant multipliers
    MAX_CATS_SOLD_ETHICAL_BREEDER = 4 * days_run # Maximum number of cats that ethical breeders can sell each day (4 cats a litter)
    cat_prices = { # Prices for buying cats
        "Pet shop": 25000,
        "Ethical breeder": 20000,
        "Unethical breeder": 20000
    }
    adoption_fee = { # Adoption fees at shelters
        "SPCA": int(random.random() * (300) + 700), #range between 700 to 1000 to adopt
        "LAP": 1500
    }
    restocking_cost_per_cat = 8000 # Restocking cost for pet shops (pet shop buying from unethical breeders)
    breeding_care_costs = { # Breeding care costs for mother cat (deleted 2 month gestation care divided by litter of 4) + basic care per kitten sold (care 1-2 months after birth)
        "Ethical breeder": 4000,
        "Unethical breeder": 3000
    }

    # Applying constants
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

                # SPCA and LAP cat surrenders
                if row["Abandon cat"] == "Yes" and place in ["SPCA", "LAP"]:
                    establishments[place]["Surrendered Cat"] += 1

                # CAT SPAWNING

                # RNG cats abandoned daily to the box or AFCD
                # DATA:
                # Case study said 379 cats received by AFCD in 2022 = 1.04 per day. 151 rehomed (1 every 2.4 days) (39%).
                # 10000 cats KILLED per year = 27-28 per day. This means more than 10000 are abandoned since not all are killed (some adopted or moved to other charities or stay in the AFCD shelter).
                # AFCD kills 48% cats received, means at least 20000 cats are abandoned per year.
                cats_spawned_to_abandon = {
                    "Ethical breeder": 0, # They don't abandon cats
                    "Unethical breeder": ((establishments["Unethical breeder"]["Bought Cat"] + establishments["Pet shop"]["Bought Cat"]) * int(random.random() * (1) + 1.5) * days_run) - establishments["Pet shop"]["Bought Cat"] - establishments["Unethical breeder"]["Bought Cat"], # Spawns between 1.5 to 2.5 times cats sold to citizens and supplied to pet shop (abandons cats that don't live up to breed standards) (flexible spawning to adjust to market demand)
                    "Pet shop": 0, # They don't abandon cats
                    # Adjust the total number needed to match the data, to relative organisation size
                    "SPCA": int(random.random() * (10) + 10) * days_run, # Spawns between 10 to 20 cats
                    "LAP": int(random.random() * (10) + 5) * days_run, # Spawns between 5 to 15 cats
                    "AFCD": int(random.random() * (10) + 10) * days_run, # Spawns between 10 to 20 cats
                    "Other charities": 0 # They're not the focus of this simulation
                }

                # Cats that end up in the box in each establishment (proportional to organisation size)
                cats_in_box = {
                    "Ethical breeder": 0, # They don't dump cats
                    "Unethical breeder": 0, # Assume all dumped to SPCA, LAP or AFCD
                    "Pet shop": 0, # They don't dump cats (cos it's their merch!?)
                    "SPCA": cats_spawned_to_abandon["SPCA"] + int(cats_spawned_to_abandon["Unethical breeder"] * 0.03) + establishments["SPCA"]["Surrendered Cat"],
                    "LAP": cats_spawned_to_abandon["LAP"] + int(cats_spawned_to_abandon["Unethical breeder"] * 0.12) + establishments["LAP"]["Surrendered Cat"],
                    "AFCD" : cats_spawned_to_abandon["AFCD"] + int(cats_spawned_to_abandon["Unethical breeder"] * 0.85),
                    "Other charities": 0 # They're not the focus of this simulation
                }

                # Vets euthanising unfit cats (severely injured or sick, to be destroyed humanely immediately)
                euthanised_cats = {
                    "Ethical breeder": 0, # They don't kill cats
                    "Unethical breeder": 0, # All dumped to SPCA, LAP or AFCD
                    "Pet shop": 0, # They don't kill cats
                    "LAP": int(cats_in_box["LAP"] * 0.01), # No kill shelter except in special circumstances
                    "SPCA": int(cats_in_box["SPCA"] * 0.1), # Kill cats unlikely to be rehomed (still tries not to)
                    "AFCD" : int(cats_in_box["AFCD"] * 0.3), # Kill cats unlikely to be rehomed (kills them more pragmatically)
                    "Other charities": 0 # They're no kill and not the focus of this simulation
                }

                # Minusing unfit cats euthanised immediately after initial vetting
                remaining_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "LAP": cats_in_box["LAP"] - euthanised_cats["LAP"],
                    "AFCD": cats_in_box["AFCD"] - euthanised_cats["AFCD"],
                    "SPCA": cats_in_box["SPCA"] - euthanised_cats["SPCA"],
                    "Other charities": 0 # They're not the focus of this simulation
                }

                # Cats deemed "vulnerable" after further vetting (deemed "unlikely to be rehomed")
                vulnerable_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": int(random.random() * remaining_cats["AFCD"]),
                    "SPCA": int(random.random() * remaining_cats["SPCA"]),
                    "LAP": int(random.random() * remaining_cats["LAP"]),
                    "Other charities": 0 # They're not the focus of this simulation
                }

                # Cats deemed healthy after vetting ("likely to be rehomed")
                healthy_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": remaining_cats["AFCD"] - vulnerable_cats["AFCD"],
                    "SPCA": remaining_cats["SPCA"] - vulnerable_cats["SPCA"],
                    "LAP": remaining_cats["LAP"] - vulnerable_cats["LAP"],
                    "Other charities": 0 # They're not the focus of this simulation
                }

                # Cats rejected from the shelter (save space for priority cats, send the other cats to other charities)
                cats_rejected_from_shelter = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": 0,
                    "SPCA": int(random.random() * vulnerable_cats["SPCA"]), # Reject vulnerable, prioritise space for healthy cats likely to be rehomed
                    "LAP": int(random.random() * healthy_cats["LAP"]), # Reject healthy, prioritise space for vulnerable cats unlikely to be rehomed
                    "Other charities": 0 # They're not the focus of this simulation
                }

                # Cats accepted from SPCA by LAP and other charities
                vulnerable_cats_accepted_from_SPCA_reject = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": 0,
                    "LAP": int(0.2 * cats_rejected_from_shelter["SPCA"]),
                    "SPCA": 0,
                    "Other charities": int(0.5 * cats_rejected_from_shelter["SPCA"])
                }

                # Cats accepted from LAP by other charities
                healthy_cats_accepted_from_LAP_reject = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": 0,
                    "LAP": 0,
                    "SPCA": 0, # LAP doesn't send cats to SPCA to prevent them from being killed (from case study)
                    "Other charities": cats_rejected_from_shelter["LAP"]
                }

                # Cats from AFCD claimed by each of the shelters (including LAP and SPCA)
                # Vulnerable cats accepted from AFCD
                vulnerable_cats_accepted_from_AFCD = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": 0,
                    "LAP": int(0.1 * vulnerable_cats["AFCD"]), # Higher % of vulnerable cats from AFCD (prioritise saving the vulnerable)
                    "SPCA": int(0.05 * vulnerable_cats["AFCD"]), # Lower % of vulnerable cats from AFCD (prioritise the likely to rehome)
                    "Other charities": int(0.3 * vulnerable_cats["AFCD"])
                }
                # Healthy cats accepted from AFCD
                healthy_cats_accepted_from_AFCD = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": 0,
                    "LAP": int(0 * healthy_cats["AFCD"]), # NO healthy cats from AFCD (prioritise shelter space for saving the vulnerable)
                    "SPCA": int(0.3 * healthy_cats["AFCD"]), # Accepts more healthy cats from AFCD (prioritise the likely to rehome)
                    "Other charities": int(0.5 * healthy_cats["AFCD"])
                }

                # Total cats taken from AFCD
                final_cats_accepted_from_AFCD = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "AFCD": 0,
                    "LAP": vulnerable_cats_accepted_from_AFCD["LAP"] + healthy_cats_accepted_from_AFCD["LAP"],
                    "SPCA": vulnerable_cats_accepted_from_AFCD["SPCA"] + healthy_cats_accepted_from_AFCD["SPCA"],
                    "Other charities": vulnerable_cats_accepted_from_AFCD["Other charities"] + healthy_cats_accepted_from_AFCD["Other charities"]
                }

                # Final vulnerable cats
                total_vulnerable_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "SPCA": vulnerable_cats["SPCA"] + vulnerable_cats_accepted_from_AFCD["SPCA"] - cats_rejected_from_shelter["SPCA"],
                    "LAP": vulnerable_cats["LAP"] + vulnerable_cats_accepted_from_AFCD["LAP"] + vulnerable_cats_accepted_from_SPCA_reject["LAP"], # Doesn't reject vulnerable cats
                    "AFCD": vulnerable_cats["AFCD"] - vulnerable_cats_accepted_from_AFCD["LAP"] - vulnerable_cats_accepted_from_AFCD["SPCA"] - vulnerable_cats_accepted_from_AFCD["Other charities"],
                    "Other charities": vulnerable_cats_accepted_from_SPCA_reject["Other charities"] + vulnerable_cats_accepted_from_AFCD["Other charities"] # There are other sources like abandoned cats, not simulated here.
                }

                # Healthy cats available to be adopted
                adoptable_healthy_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "SPCA": healthy_cats["SPCA"] + healthy_cats_accepted_from_AFCD["SPCA"], # Doesn't reject healthy cats
                    "LAP": healthy_cats["LAP"] + healthy_cats_accepted_from_AFCD["LAP"] - cats_rejected_from_shelter["LAP"],
                    "AFCD": 0, #AFCD doesn't do adoptions
                    "Other charities": healthy_cats_accepted_from_AFCD["Other charities"] + healthy_cats_accepted_from_LAP_reject["LAP"] # There are other sources like abandoned cats, not simulated here.
                }

                ADOPTABLE_CATS = 1000000 # (limit not set to allow ppl to adopt cats that were not received on that day) adoptable_healthy_cats["LAP"]
            
                # Handle SPCA and LAP cat adoptions
                if row["Adopt cat"] == "Yes":
                    establishments[place]["Tried to Adopt Cat"] += 1
                    if row["Adoption approval"] == "Yes" and place in ["SPCA", "LAP"]:
                        if establishments[place]["Adopted Cat"] < ADOPTABLE_CATS:
                            establishments[place]["Adopted Cat"] += 1
                            establishments[place]["Cats Sold/Adopted"] += 1
                            establishments[place]["Profit from Cats"] += adoption_fee[place]
                            #establishments[place]["Final Cats in Shelter"] -= 1
                        else:
                            establishments[place]["Unmet Demand"] += 1

                # Handle SPCA and LAP buying stuff and donations                    
                if row["Buy stuff"] == "Yes":
                    amount_spent = int(random.random() * (80) + 20)
                    establishments[place]["Bought Stuff"] += 1
                    establishments[place]["Profit from Stuff"] += amount_spent

                if row["Donate"] == "Yes":
                    donation_amount = int(random.random() * (999) + 1)
                    establishments[place]["Donated"] += 1
                    establishments[place]["Profit from Donations"] += donation_amount

                # Final healthy cats
                final_healthy_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "SPCA": adoptable_healthy_cats["SPCA"] - int(0.7 * establishments["SPCA"]["Adopted Cat"]), # This models that most healthy cats are available for adoption soon after coming to the shelter, so adoptions are more frequent
                    "LAP": adoptable_healthy_cats["LAP"] - int(0.7 * establishments["LAP"]["Adopted Cat"]), # This models that most healthy cats are available for adoption soon after coming to the shelter, so adoptions are more frequent
                    "AFCD": healthy_cats["AFCD"] - healthy_cats_accepted_from_AFCD["LAP"] - healthy_cats_accepted_from_AFCD["SPCA"] - healthy_cats_accepted_from_AFCD["Other charities"],
                    "Other charities": healthy_cats_accepted_from_AFCD["Other charities"] + healthy_cats_accepted_from_LAP_reject["LAP"] # Adoptions processed by the other charities are not simulated here.
                }

                final_vulnerable_cats = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "SPCA": total_vulnerable_cats["SPCA"] - int(0.3 * establishments["SPCA"]["Adopted Cat"]), # This models that vulnerable cats are available for adoption only after they have healed, so adoptions are less frequent
                    "LAP": total_vulnerable_cats["LAP"] - int(0.3 * establishments["SPCA"]["Adopted Cat"]), # This models that vulnerable cats are available for adoption only after they have healed, so adoptions are less frequent
                    "AFCD": total_vulnerable_cats["AFCD"],
                    "Other charities": total_vulnerable_cats["Other charities"] # Adoptions processed by the other charities are not simulated here.
                }

                # Cats in each shelter FINAL count
                cats_in_shelter = {
                    "Ethical breeder": 0,
                    "Unethical breeder": 0,
                    "Pet shop": 0,
                    "SPCA": final_healthy_cats["SPCA"] + final_vulnerable_cats["SPCA"], # + vulnerable_cats_accepted_from_AFCD["SPCA"] + healthy_cats_accepted_from_AFCD["SPCA"] - cats_rejected_from_shelter["SPCA"],
                    "LAP": final_healthy_cats["LAP"] + final_vulnerable_cats["LAP"], # + vulnerable_cats_accepted_from_AFCD["LAP"] + healthy_cats_accepted_from_AFCD["LAP"] - cats_rejected_from_shelter["LAP"],
                    "AFCD": final_healthy_cats["AFCD"] + final_vulnerable_cats["AFCD"], #remaining_cats["AFCD"] - vulnerable_cats_accepted_from_AFCD["LAP"] - healthy_cats_accepted_from_AFCD["LAP"] - vulnerable_cats_accepted_from_AFCD["SPCA"] - healthy_cats_accepted_from_AFCD["SPCA"] - final_cats_accepted_from_AFCD["Other charities"],
                    "Other charities": vulnerable_cats_accepted_from_SPCA_reject["Other charities"] + healthy_cats_accepted_from_LAP_reject["Other charities"] + final_cats_accepted_from_AFCD["Other charities"]
                }

    # COST CALCULATIONS

    number_of_shops = {
        # Seen as individual operations
        "Pet shop": 200,
        "Ethical breeder": 100,
        "Unethical breeder": 25,
        # Seen as whole organisations
        "SPCA": 1,
        "LAP": 1,
        "AFCD": 1,
        "Other charities": 40 # An estimate based on the list given in the case study that applied for AFCD subvention plus some that I found online. The exact number may be more or less but since other charities are not the focus of this simulation, this is a rough estimate.
    }

    # NOT CAT RELATED COSTS
    # Rent (exempted for ethical breeder because it's their home)
    base_rent = 1000 # For a small shop NOT in the city centre
    total_rent = {
        "Pet shop": base_rent * number_of_shops["Pet shop"] * days_run, # There are 200 pet shops 
        "Ethical breeder": 0, #base_rent * 2 * number_of_shops["Ethical breeder"] * days_run * 0, There are about 100 ethical breeders but rent is negligible cos they operate from their own homes
        "Unethical breeder": (base_rent * 2) * number_of_shops["Unethical breeder"] * days_run, # There are 25 unethical breeders who each own a large breeding farm
        "SPCA": 950 * 10 * days_run, # Used same figure as LAP. There are 10 shelters run by SPCA
        "LAP": 950 * 4 * days_run, # Figure from case study. There are 4 shelters run by LAP, including the cat adoption centre
        "AFCD" : (base_rent / 2) * 4 * days_run, # 4 management centres according to case study, they are government run so rent may be cheaper
        "Other charities": 0 # They're not the focus of this simulation
    }
    # Daily miscellaneous operational costs. A very rough estimate of other costs like utility bills, staff salaries, facility maintenance, insurance, marketing, educational outreach, adminsitration, transportation etc.
    misc_operational_costs = { 
        "Pet shop": 5000 * number_of_shops["Pet shop"] * days_run, # There are 200 pet shops
        "Ethical breeder": 100 * number_of_shops["Ethical breeder"] * days_run, # There are about 100 ethical breeders but operate from their own homes so assume minimal costs
        "Unethical breeder": 3000 * number_of_shops["Unethical breeder"] * days_run, # There are 25 unethical breeders who each occupy a large breeding farm
        "SPCA": 40000 * days_run, # SPCA is a larger organisation than LAP
        "LAP": 8000 * days_run, # Taken from LAP's annual report
        "AFCD" : 40000 * days_run, # Rough estimate close to SPCA since they don't dedicate all their resources to dealing with abandoned animals
        "Other charities": 0 # They're not the focus of this simulation
    }

    # CAT RELATED COSTS
    # Basic cost for taking care of cats
    basic_care_per_cat = 25 # From the case study LAP's data. Extrapolated to all establishments.
    basic_care_cost = {
        "Pet shop": (basic_care_per_cat * 5 * number_of_shops["Pet shop"]) * days_run, # Pet shop pays to care for the stock of 5 cats which is always maintained at the same level, 200 pet shops in total
        "Ethical breeder": (basic_care_per_cat * (365 + 73)) * days_run, # Ethical breeder keeps 365 females. Males min: 73 (1 male should not sire more than 5% of all kittens in a pedigree for genetic diversity)
        "Unethical breeder": (basic_care_per_cat * (375 + 50)) * days_run, # Unethical keeps 375 females. Males are much less thus violates the recommended guidelines for genetic diversity.
        "SPCA": cats_in_shelter["SPCA"] * basic_care_per_cat, # Shelters pay for cats abandoned and cats surrendered
        "LAP": cats_in_shelter["LAP"] * basic_care_per_cat, # Shelters pay for cats abandoned and cats surrendered
        "AFCD": cats_in_shelter["AFCD"] * basic_care_per_cat, # Shelters pay for cats abandoned and cats surrendered
        "Other charities": 0 # They're not the focus of this simulation
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
        "AFCD" : 0, # They only keep cats for 4 days
        "Other charities": 0 # They're not the focus of this simulation
    }
    # AFCD, LAP, SPCA vulnerable cat vet care cost
    vulnerable_care_vet_cost = {
        "Ethical breeder": 0,
        "Unethical breeder": 0,
        "Pet shop": 0,
        "LAP": int((final_vulnerable_cats["LAP"]) * vulnerable_care_fee * days_run / 365 * 6),
        "SPCA": int((final_vulnerable_cats["SPCA"]) * vulnerable_care_fee * days_run / 365 * 6),
        "AFCD": int((final_vulnerable_cats["AFCD"]) * vulnerable_care_fee * days_run / 365 * 6),
        "Other charities": 0 # They're not the focus of this simulation
    } 
    # AFCD, LAP, SPCA cat vetting cost
    vetting_cost = {
        "Ethical breeder": 0,
        "Unethical breeder": 0,
        "Pet shop": 0,
        "SPCA": (cats_in_box["SPCA"]) * vetting_fee,
        "LAP": (cats_in_box["LAP"]) * vetting_fee,
        "AFCD": (cats_in_box["AFCD"]) * vetting_fee,
        "Other charities": 0 # They're not the focus of this simulation
    }
    # Euthanasia costs
    euthanasia_cost = {
        "Ethical breeder": 0,
        "Unethical breeder": 0,
        "Pet shop": 0,
        "LAP": 0, # No kill shelter
        "SPCA": euthanised_cats["SPCA"] * euthanasia_fee,
        "AFCD": euthanised_cats["AFCD"] * euthanasia_fee,
        "Other charities": 0 # They're not the focus of this simulation
    }
    # Total vet fees for each establishment (basic checkup, vulnerable care, vetting, euthanasias)
    total_vet_cost = {
        "Pet shop": basic_checkup_vet_cost["Pet shop"],
        "Ethical breeder": basic_checkup_vet_cost["Ethical breeder"],
        "Unethical breeder": basic_checkup_vet_cost["Unethical breeder"],
        "SPCA": basic_checkup_vet_cost["SPCA"] + vulnerable_care_vet_cost["SPCA"] + vetting_cost["SPCA"] + euthanasia_cost["SPCA"],
        "LAP": basic_checkup_vet_cost["LAP"] + vulnerable_care_vet_cost["LAP"] + vetting_cost["LAP"],
        "AFCD": basic_checkup_vet_cost["AFCD"] + vulnerable_care_vet_cost["AFCD"] + vetting_cost["AFCD"] + euthanasia_cost["AFCD"],
        "Other charities": 0 # They're not the focus of this simulation
    }

    for place, data in establishments.items():
        # Calculate cats for each establishment
        data["Cats Spawned to Abandon"] = cats_spawned_to_abandon[place]
        data["Cats Transferred to Box"] = cats_in_box[place] # + data["Surrendered Cat"]
        data["Euthanised after Vetting"] = euthanised_cats[place]
        data["Remaining Healthy Cats"] = healthy_cats[place]
        data["Remaining Vulnerable Cats"] = vulnerable_cats[place]
        data["Cats Rejected from Shelter"] = cats_rejected_from_shelter[place]
        data["Cats Claimed from AFCD"] = final_cats_accepted_from_AFCD[place]
        data["Cats Claimed from SPCA"] = vulnerable_cats_accepted_from_SPCA_reject[place]
        data["Final Cats in Shelter"] = cats_in_shelter[place]
        data["Final Healthy Cats"] = final_healthy_cats[place]
        data["Final Vulnerable Cats"] = final_vulnerable_cats[place]
        # Calculate total money (profit, cost, net income) for each establishment
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
        # Calculate final killed cats from the whole system. Cats left in AFCD's shelter were mot taken by LAP, SPCA, or any other charity, will be killed in 4 days. This simulation assumes the other charities will come to claim half of the remaining cats.
        data["Total Cats Killed (everyone)"] = cats_in_shelter["AFCD"] + euthanised_cats["AFCD"] + euthanised_cats["LAP"] + euthanised_cats["SPCA"]

    return establishments

# PREPARE THE ACCUMULATED OUTPUT CSV

def save_analysis(analysis, filename="npc_analysis_flex.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            "Establishment", "Visited", "Entered", "Bought Cat", "Tried to Adopt Cat", "Adopted Cat", "Bought Stuff", "Donated", "Surrendered Cat",
            "Cats Sold/Adopted", "Total Profit", "Profit from Cats", "Profit from Stuff", "Profit from Donations", "Profit from Supplying", "Unmet Demand",
            "Total Costs", "Breeding Care Costs", "Restocking Costs", "Total Rent", "Misc Operational Costs", "Basic Care Cost", "Total Vet Cost", 
            "Cats Spawned to Abandon", "Cats Transferred to Box", "Euthanised after Vetting", "Remaining Healthy Cats", "Remaining Vulnerable Cats", 
            "Cats Rejected from Shelter", "Cats Claimed from AFCD", "Cats Claimed from SPCA", "Final Cats in Shelter", "Final Healthy Cats", "Final Vulnerable Cats",
            "Basic Checkup Cost", "Vulnerable Care Cost", "Vetting Cost", "Euthanasia Cost", "Final Net Income", "Final Net Income Per Place", "Total Cats Killed (everyone)"
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
                "Surrendered Cat": data.get("Surrendered Cat", 0),
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
                "Cats Claimed from AFCD": data.get("Cats Claimed from AFCD", 0),
                "Cats Claimed from SPCA": data.get("Cats Claimed from SPCA", 0),
                "Final Cats in Shelter": data.get("Final Cats in Shelter", 0),
                "Final Healthy Cats": data.get("Final Healthy Cats", 0),
                "Final Vulnerable Cats": data.get("Final Vulnerable Cats", 0),
                "Basic Checkup Cost": data.get("Basic Checkup Cost", 0),
                "Vulnerable Care Cost": data.get("Vulnerable Care Cost", 0),
                "Vetting Cost": data.get("Vetting Cost", 0),
                "Euthanasia Cost": data.get("Euthanasia Cost", 0),
                "Final Net Income": data.get("Final Net Income", 0),
                "Final Net Income Per Place": data.get("Final Net Income Per Place", 0),
                "Total Cats Killed (everyone)": data.get("Total Cats Killed (everyone)", 0)
            }
            writer.writerow(row)

def main():
    analysis = analyze_npc_actions()
    save_analysis(analysis)

if __name__ == "__main__":
    main()
