import json
import re

# File path to the JSON file
file_path = r""

# Function to sort keys by separating numeric and string parts
def alphanum_key(key):
    # Split the key into parts: strings and numbers
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', key)]

# Function to reorder JSON keys alphabetically and numerically
def reorder_json_keys(json_data):
    return dict(sorted(json_data.items(), key=lambda item: alphanum_key(item[0])))

# Load the JSON data from the file
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Reorder the JSON data
reordered_data = reorder_json_keys(data)

# Save the reordered data back to the file
output_file = r""
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(reordered_data, f, indent=4, ensure_ascii=False)

print(f"Reordered JSON data has been saved to {output_file}.")
