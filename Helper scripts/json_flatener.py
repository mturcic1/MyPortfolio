import json

# Input and output file paths
input_file_path = "your_path"  
output_file_path = "your_path"  

with open(input_file_path, "r", encoding="utf-8") as infile:
    data = json.load(infile)

flattened_questions = {}
for question in data["questions"]["questions"]:
    question_id = question.pop("question_id")  # Extract the question ID as the key
    flattened_questions[question_id] = question

with open(output_file_path, "w", encoding="utf-8") as outfile:
    json.dump(flattened_questions, outfile, indent=4, ensure_ascii=False)

print(f"Flattened JSON has been saved to {output_file_path}.")
