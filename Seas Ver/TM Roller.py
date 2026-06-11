import random
import os
import json
from pathlib import Path

script_dir = Path(__file__).parent #Fetching the folder the script lives in...

storage = script_dir / "Moves" #... and loading the moves directory.

#Pulling the provided TM list, recognizing pipes as the delimiter.
with open(script_dir / "TMs.txt") as f: #Open the TMs file...
    mon_tms = [move.strip() for move in f.read().split("|")] #...and populate the list mon_tms from the file.

#Loading every JSON file from the moves directory into a list.
moves = [] #Said list.
for filename in os.listdir(storage):  #Honestly I never messed with json files before, so I'm not all that sure if this is correct. But it works.
    if filename.endswith(".json"): #If the filename ends in .json...
        with open(os.path.join(storage, filename), encoding="utf-8") as f: #...fetch the filename...
            moves.append(json.load(f)) #...and append the filename to list moves.

max_power = int(input("Max TM power: ")) #Power cap input.

mode = input("Roll or list eligible moves? (r/l): ").strip().lower() #Mode selection, r for random roll, or l for list.

eligible = [m for m in moves #The filtering
            if m["name"] in mon_tms #If move name is in the TM list...
            and (m.get("power", 0) == 0 or m.get("power", 0) <= max_power)] #...and the power from the json is 0, or equal or lesser than the provided max power, load the result into list 'eligible'.

if mode == "l": #List mode, lists all eligible TMs for the provided TM power.
    print(f"\n{len(eligible)} eligible moves:\n")
    for m in sorted(eligible, key=lambda m: m["name"]): #For each value in list 'eligible'.
        power = m.get("power", 0) #If there's no power in the move's json, set it as 0.
        power_str = f"  [Power {power}]" if power > 0 else "  [Status]" #If move power is greater than 0, list the move power, otherwise say that its a status move.
        print(f"  {m['name']} ({m['type']} - {m['category']}){power_str}") #Printing the name, type, category, and power of the move.
else: #Roll mode, does what it says on the tin, rolls a random eligible TM.
    result = random.choice(eligible) #Roll a random value from list 'eligible'.

    #Output
    print(f"\n{result['name']}")
    print(f"{result.get('description', '')}")
    print(f"Type: {result['type']} - {result['category']}")
    print(f"Target: {result.get('target', '?')}")
    if result.get('power', 0) > 0:  #If a move's power greater 0 (i.e. not a status move)...
        print(f"Damage Dice: {result['damage']} + {result['power']}") #... output the damage dice line. This is so status moves don't print the Damage Dice line.
    print(f"Accuracy Dice: {result['accuracy']} + Rank")
    print(f"Effect: {result.get('effect', 'No effect listed')}")
