# Input and output file paths
input_file_path = "D:\\survival_of_the_smartest_eng.txt"  # Update to your actual file path
output_file_path = "D:\\questions_collection_fixed.txt"   # Update to your desired output path

# Read the existing content of the file
with open(input_file_path, "r", encoding="utf-8") as infile:
    content = infile.read()

# Replace the problematic sequence with a comma
corrected_content = content.replace("]\n}\n{\n  \"questions\": [", ",")

# Ensure proper connection between JSON objects
corrected_content = corrected_content.replace("}\n  ,\n  {", "},{")

# Write the corrected content back to the file
with open(output_file_path, "w", encoding="utf-8") as outfile:
    outfile.write(corrected_content)

print(f"The problematic sequences have been replaced and saved to {output_file_path}.")
