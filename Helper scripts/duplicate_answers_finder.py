import json
from collections import defaultdict

file_path = "file_path"

def group_by_correct_answer_texts(file_path):

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

    grouped_questions = [texts for texts in correct_answer_map.values() if len(texts) > 1]

    return grouped_questions

def save_and_print_groups(groups, output_path="correct_answer_question_texts.json"):
  
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(groups, file, indent=4)
    print("Groups of question_texts with the same correct_answer:")
    for group in groups:
        print(group)

groups = group_by_correct_answer_texts(file_path)


save_and_print_groups(groups)
