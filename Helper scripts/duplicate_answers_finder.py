import json
from collections import defaultdict

# Full path to your JSON file
file_path = "D:/cleaned_eng_survival_of_the_strongest.json"

def group_by_correct_answer_texts(file_path):
    # Load the JSON data
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Dictionary to map correct_answer to their question_texts
    correct_answer_map = defaultdict(list)

    # Populate the dictionary with correct_answer
    for value in data.values():
        correct_answer = value.get("correct_answer")
        question_text = value.get("question_text")
        if correct_answer and question_text:
            correct_answer_map[correct_answer].append(question_text)

    # Create a list of lists for groups with the same correct_answer
    grouped_questions = [texts for texts in correct_answer_map.values() if len(texts) > 1]

    return grouped_questions

def save_and_print_groups(groups, output_path="correct_answer_question_texts.json"):
    # Save the grouped lists to a JSON file
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(groups, file, indent=4)

    # Print the groups
    print("Groups of question_texts with the same correct_answer:")
    for group in groups:
        print(group)

# Step 1: Group question_texts by correct_answer
groups = group_by_correct_answer_texts(file_path)

# Step 2: Save and print the groups
save_and_print_groups(groups)
