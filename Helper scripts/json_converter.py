import json

# Input and output file paths
input_file_path = "D:\\questions_collection_fixed.txt"  # Path to the cleaned file
output_file_path = "D:\\questions_collection2.json"      # Path for the JSON output file

# Read the corrected file content
with open(input_file_path, "r", encoding="utf-8") as infile:
    content = infile.read()

# Wrap the content with a JSON object if necessary
content = '{"questions": ' + content + '}'

# Attempt to parse the content as JSON
try:
    data = json.loads(content)  # Convert to JSON object
    # Write the JSON object to the output file
    with open(output_file_path, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    print(f"The file has been successfully converted to JSON and saved to {output_file_path}.")
except json.JSONDecodeError as e:
    # Debugging: Print the error and problematic section
    error_position = e.pos  # The position of the error in the string
    print(f"JSONDecodeError: {e.msg}")
    print(f"Error occurred at position: {error_position}")
    print(f"Context around the error:\n{content[error_position:error_position+100]}")  # Show 100 chars after the error
