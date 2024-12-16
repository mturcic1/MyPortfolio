import json
from collections import defaultdict

# Full path to your JSON file
file_path = "D:/cleaned_eng_survival_of_the_strongest.json"

def find_duplicates(file_path):
    # Load the JSON data
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Dictionary to map question_text to their question IDs
    question_map = defaultdict(list)

    # Populate the dictionary with question_text
    for key, value in data.items():
        question_text = value.get("question_text")
        if question_text:
            question_map[question_text].append(key)

    # Create a list of lists for duplicates
    duplicates = [ids for ids in question_map.values() if len(ids) > 1]

    return duplicates

# Run the script and print the result
duplicate_lists = find_duplicates(file_path)
print(duplicate_lists)
