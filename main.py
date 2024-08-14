import chardet

with open('data.json', 'rb') as file:
    result = chardet.detect(file.read())
    current_encoding = result['encoding']

# Convert the file to UTF-8
with open('data.json', 'r', encoding=current_encoding) as source_file:
    content = source_file.read()

# Create a new UTF-8 file (or change the encofing as per your need)
with open('data_utf8.json', 'w', encoding='utf-8') as target_file:
    target_file.write(content)
