import json
from collections import defaultdict

# Read the text file and parse it as JSON
def read_and_parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return json.loads(content)

# Count the number of questions per country
def count_questions(data):
    question_counts = defaultdict(int)

    for key in data.keys():
        # Extract the country part (string part before the numeric part)
        country_name = ''.join([char for char in key if not char.isdigit()])
        question_counts[country_name] += 1

    return question_counts

# Main execution
if __name__ == "__main__":
    # Path to your text file
    file_path = r"insert_file_path_here" 

    try:
        data = read_and_parse_file(file_path)
        question_counts = count_questions(data)

        print("Number of questions for each country:")
        for country, count in question_counts.items():
            if count < 100:
                print(f"{country}: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")