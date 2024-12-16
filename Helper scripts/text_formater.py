
input_file_path = "your path"  
output_file_path = "your path"   

with open(input_file_path, "r", encoding="utf-8") as infile:
    content = infile.read()

corrected_content = content.replace("]\n}\n{\n  \"questions\": [", ",")

corrected_content = corrected_content.replace("}\n  ,\n  {", "},{")

with open(output_file_path, "w", encoding="utf-8") as outfile:
    outfile.write(corrected_content)

print(f"The problematic sequences have been replaced and saved to {output_file_path}.")
