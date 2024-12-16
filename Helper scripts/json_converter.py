# this converts txt to json
import json

# Input and output file paths
input_file_path = "your_path"  
output_file_path = "your_path"      

with open(input_file_path, "r", encoding="utf-8") as infile:
    content = infile.read()


content = '{"questions": ' + content + '}'


try:
    data = json.loads(content)  # Convert to JSON object
    with open(output_file_path, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    print(f"The file has been successfully converted to JSON and saved to {output_file_path}.")
except json.JSONDecodeError as e:
    error_position = e.pos  # The position of the error in the string
    print(f"JSONDecodeError: {e.msg}")
    print(f"Error occurred at position: {error_position}")
    print(f"Context around the error:\n{content[error_position:error_position+100]}")  # Show 100 chars after the error
