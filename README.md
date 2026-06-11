# Description
Quick and dirty Python script for listing and randomly rolling TMs for PokeRole discord servers using the [All-Knowing Magikarp/pokerole-discord-bot](https://github.com/Jacudibu/pokerole-discord-bot) Discord bot. Primarily made for personal use and to share with the communities of servers I am in. Obviously requires Python.
The scripts are public domain under the Unlicense license.
## Move info data provenance
As with All-Knowing Magikarp, base move data comes from [Pokerole-Data](https://github.com/Pokerole-Software-Development/Pokerole-Data), which Magikarp then converts into its own schema, and then overrides moves with its data from [pokerole-custom-data](https://github.com/Jacudibu/pokerole-custom-data).  I have written my own converter script to convert the Pokerole-Data JSON files to Magikarp's expected schema, and then replaced the JSON files with those from pokerole-custom-data's base overrides, and then again from the server-specific overrides.
Note: Some of pokerole-custom-data is outdated and does not include up-to-date overrides within the Discord bot, e.g. Will-O-Wisp. pokerole-custom-data also includes typos within the files names of a handful of files, such as Acid Spray being `Acid Srpy.json` and Round being `Round,json`. Both have been manually corrected.

# Usage
## Providing a TM list
In a server with All-Knowing Magikarp, enter `/learns pokemon:(name of Pokemon)` and click on ` Show All Learnable Moves` to retrieve the Pokemon's TM list. Copy the moves list, delete the contents of `TMs.txt` (of which contains the TMs list for Cinderace out of the box) and paste it in, don't forget to save the file.
## Running the script
Download this repo. Navigate to the directory containing `TM Roller.py` in your terminal (Command Prompt/PowerShell/Konsole/whatever), and type `py "TM Roller.py"`
First it will ask for your desired max move power, enter a number. It will then ask if you want to roll a random move equal or lesser than the provided move power, or to simply list them. Type `r` to roll, or `l` to list. Rolling will roll a random move, and output the full block, and the script closes. Listing will list all eligible moves, only displaying their name, type, and power before closing.