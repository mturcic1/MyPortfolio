import json

# Input and output file paths
input_file_path = "D:\\eng_survival_of_the_strongest.json"  # Path to your input JSON file
output_file_path = "D:\\flattened_questions.json"  # Path for the output JSON file

# Read the JSON file
with open(input_file_path, "r", encoding="utf-8") as infile:
    data = json.load(infile)

# Flatten the questions
flattened_questions = {}
for question in data["questions"]["questions"]:
    question_id = question.pop("question_id")  # Extract the question ID as the key
    flattened_questions[question_id] = question

# Save the flattened JSON
with open(output_file_path, "w", encoding="utf-8") as outfile:
    json.dump(flattened_questions, outfile, indent=4, ensure_ascii=False)

print(f"Flattened JSON has been saved to {output_file_path}.")
