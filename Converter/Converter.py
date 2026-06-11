import json
import os
from pathlib import Path

script_dir = Path(__file__).parent #Fetching the folder the script lives in...
input_folder = script_dir / "Moves" #...and pointing to the Moves subfolder for input...
output_folder = script_dir / "Output" #...and the Output subfolder for converted files.
output_folder.mkdir(exist_ok=True) #It is okay if the output folder already exists, do not raise an error if it does.

for filename in os.listdir(input_folder): #Loading the PokeRole-Data .json files
    if filename.endswith(".json"): #If the file ends with .json...
        with open(input_folder / filename, encoding="utf-8") as f: # ...open it with UTF-8 encoding...
            raw = json.load(f) #and load the keys into list raw.
        
        converted = {
            "name": raw["Name"],
            "type": raw["Type"],
            "power": raw["Power"],
            "damage": raw["Damage1"],
            "accuracy": raw["Accuracy1"],
            "target": raw["Target"],
            "effect": raw["Effect"],
            "description": raw["Description"],
            "category": raw["Category"]
        }
        
        with open(output_folder / filename, "w", encoding="utf-8") as f: #Writing the files with the converted schema into the output folder with UTF-8
            json.dump(converted, f, indent=4, ensure_ascii=False) #ensure_ascii=false prevents e-acutes from being escaped.
