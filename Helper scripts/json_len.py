import json

# Full path to your JSON file
file_path = "your_path"


def count_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    total_questions = len(data)

    print(f"Total number of questions: {total_questions}")


count_questions(file_path)
