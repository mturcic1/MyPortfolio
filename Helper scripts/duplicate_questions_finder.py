import json
from collections import defaultdict

# Full path to your JSON file
file_path = "your_path"

def find_duplicates(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    question_map = defaultdict(list)

    for key, value in data.items():
        question_text = value.get("question_text")
        if question_text:
            question_map[question_text].append(key)

    duplicates = [ids for ids in question_map.values() if len(ids) > 1]

    return duplicates

duplicate_lists = find_duplicates(file_path)
print(duplicate_lists)
