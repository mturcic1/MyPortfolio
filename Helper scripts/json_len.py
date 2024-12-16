import json

# Full path to your JSON file
file_path = "D:/cleaned_eng_survival_of_the_strongest.json"


def count_questions(file_path):
    # Load the JSON data
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Count the number of questions
    total_questions = len(data)

    # Print the count
    print(f"Total number of questions: {total_questions}")

# Run the script
count_questions(file_path)