import json
import random
import os
import glob

# 1. Setup the folder path
folder_path = os.path.expanduser("/home/photon/Documents/code/hadeeth_project")
# We look for all .json files in that folder
json_files = glob.glob(os.path.join(folder_path, "*.json"))

all_hadiths = []

# 2. Loop through each file and extract the English text
for file_path in json_files:
    filename = os.path.basename(file_path) # e.g., "nawawi40.json"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            # These specific files store Hadiths inside a "hadiths" list
            if "hadiths" in data:
                for item in data["hadiths"]:
                    # We specifically want the English text
                    if "english" in item and "text" in item["english"]:
                        english_text = item["english"]["text"]
                        # Clean up the text (remove extra newlines if needed)
                        english_text = english_text.strip()

                        if english_text:
                            # Add tuple: (The Text, The Filename)
                            all_hadiths.append((english_text, filename))

    except Exception as e:
        pass # Skip files that are broken or don't match

# 3. Pick Random and Print
if all_hadiths:
    # Pick one random entry
    text, source_file = random.choice(all_hadiths)

    # Print ONLY the English text followed by the source file
    print(f"{source_file.replace('40.json', '').upper()}\n{text}\n")
else:
    print("No Hadiths found. Make sure your JSON files are in ~/hadith_project")
