# json_file_handling.py

from helpers.display_utils import *
import json
import os

def main():
    print_heading("Handling JSON Files")
    imp_note_points("""
- JSON (JavaScript Object Notation) is a lightweight, human-readable format for data interchange. It is the standard for web APIs.
- Python's built-in `json` module provides the tools to work with JSON data.
- **Serialization (or Encoding):** 
    The process of converting a Python object (like a dictionary or list) into a JSON string. The main function for this is `json.dump()`.
- **Deserialization (or Decoding):** 
    The process of converting a JSON string back into a Python object. The main function for this is `json.load()`.
""")

    # Define the filename for our examples
    json_filename = 'user_data.json'

    # Create a sample data structure
    user_data = {
        "userId": 101,
        "username": "alice_g",
        "isActive": True,
        "courses": ["History", "Computer Science"],
        "profile": {
            "age": 30,
            "city": "New York"
        }
    }

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Writing to a JSON File (`json.dump`)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Writing to a JSON File (`json.dump`)")
    display_note("`json.dump(data, file_object)` serializes a Python object and writes it to a file.")
    display_note("The `indent` parameter is optional but highly recommended for creating human-readable files.", "tip")
    
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, indent=4)
        
    show_code_with_output('''# Show the code
import json

json_filename = 'user_data.json'

# Create a sample data structure
user_data = {
    "userId": 101,
    "username": "alice_g",
    "isActive": True,
    "courses": ["History", "Computer Science"],
    "profile": {
        "age": 30,
        "city": "New York"
    }
}
# A Python dictionary
user_data = {json.dumps(user_data, indent=4)}

# Open a file in write mode and dump the data into it
with open('{json_filename}', 'w', encoding='utf-8') as f:
    # Use indent=4 for pretty-printing
    json.dump(user_data, f, indent=4)

print("'{json_filename}' created successfully.")
'''
, f"'{json_filename}' created successfully.")

    display_note("The content of `user_data.json` would now be:")
    # Read the file to display its actual content
    with open(json_filename, 'r', encoding='utf-8') as f:
        file_content = f.read()
    console.print(Syntax(file_content, "json", theme="monokai", background_color="#272822"))


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Reading from a JSON File (`json.load`)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Reading from a JSON File (`json.load`)")
    display_note("`json.load(file_object)` deserializes a JSON file, parsing it back into a Python object (usually a dictionary).")

    # Execute the read operation ---
    with open(json_filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)

    show_code_with_output('''import json
                          
json_filename = 'user_data.json'

# Open the JSON file in read mode
with open('{json_filename}', 'r', encoding='utf-8') as f:
    data_from_file = json.load(f)

# The data is now a Python dictionary
print(f"Username: {{data_from_file['username']}}")
print(f"Is Active: {{data_from_file['isActive']}}")
print(f"First Course: {{data_from_file['courses'][0]}}")
''',
f'''Username: {loaded_data['username']}
Is Active: {loaded_data['isActive']}
First Course: {loaded_data['courses'][0]}''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. `dump` vs `dumps` and `load` vs `loads`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. `dump` vs `dumps` and `load` vs `loads`")
    display_note("The `s` stands for 'string'. These versions work with strings in memory instead of file objects.")
    
    print_small_sub_heading("a) `json.dumps()`: Object to String")
    display_note("Converts a Python object into a JSON formatted string in memory.")
    json_string = json.dumps(user_data, indent=4)
    show_code_with_output('''# Convert a dictionary to a JSON string
json_string = json.dumps(user_data, indent=4)
print(json_string)''',
json_string)

    print_small_sub_heading("b) `json.loads()`: String to Object")
    display_note("Parses a JSON formatted string from memory into a Python object.")
    new_data = json.loads(json_string)
    show_code_with_output('''# Parse a JSON string back into a Python object
reloaded_data = json.loads(json_string)
# It is now a dictionary again
print(f"Type of reloaded data: {type(reloaded_data)}")
print(f"User's city: {reloaded_data['profile']['city']}")''',
f'''Type of reloaded data: {type(new_data)}
User's city: {new_data['profile']['city']}''')

    # Clean up the created file
    if os.path.exists(json_filename):
        os.remove(json_filename)


if __name__ == "__main__":
    main()

