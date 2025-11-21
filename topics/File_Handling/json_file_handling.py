# json_file_handling.py

from helpers.display_utils import *
import json
import os

def main(topic_number: int):
    print_heading("Handling JSON Files", topic_number)
    imp_note_points("""
- JSON (JavaScript Object Notation) is a lightweight, human-readable format for data interchange. It is the standard for web APIs.
- Python's built-in ___json___ module provides the tools to work with JSON data.
- **Serialization (or Encoding):** 
    The process of converting a Python object (like a dictionary or list) into a JSON string. The main function for this is ___json.dump()___.
- **Deserialization (or Decoding):** 
    The process of converting a JSON string back into a Python object. The main function for this is ___json.load()___.""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Writing to a JSON File (`json.dump`)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Writing to a JSON File (`json.dump`)")
    display_note("`json.dump(data, file_object)` serializes a Python object and writes it to a file.")
    display_note("The `indent` parameter is optional but highly recommended for creating human-readable files.", "tip")
    json_filename = 'user_data.json'
    code1 = '''# Show the code
import json

json_filename = 'tests/output_dump/user_data.json'

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

# Open a file in write mode and dump the data into it
with open(json_filename, 'w', encoding='utf-8') as f:
    # Use indent=4 for pretty-printing
    json.dump(user_data, f, indent=4)

print(f"'{json_filename}' created successfully.")
#----------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Reading from a JSON File (`json.load`)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Reading from a JSON File (`json.load`)")
    display_note("`json.load(file_object)` deserializes a JSON file, parsing it back into a Python object (usually a dictionary).")
    code2 = '''
import json
                          
json_filename = 'tests/output_dump/user_data.json'

# Open the JSON file in read mode
with open(json_filename, 'r', encoding='utf-8') as f:
    data_from_file = json.load(f)

# The data is now a Python dictionary
print(f"Username: {data_from_file['username']}")
print(f"Is Active: {data_from_file['isActive']}")
print(f"First Course: {data_from_file['courses'][0]}")
#-------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. `dump` vs `dumps` and `load` vs `loads`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. `dump` vs `dumps` and `load` vs `loads`")
    display_note("The `s` stands for 'string'. These versions work with strings in memory instead of file objects.")
    
    print_small_sub_heading("a) `json.dumps()`: Object to String")
    display_note("Converts a Python object into a JSON formatted string in memory.")
    code3 = '''# Convert a dictionary to a JSON string
import json

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

json_string = json.dumps(user_data, indent=4)
print(json_string)
#---------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    print_small_sub_heading("b) `json.loads()`: String to Object")
    display_note("Parses a JSON formatted string from memory into a Python object.")
    code4 = '''# Parse a JSON string back into a Python object
import json

json_string = """
{   "userId": 101,
    "username": "alice_g",
    "isActive": true,
    "courses": ["History", "Computer Science"],
    "profile": {
        "age": 30,
        "city": "New York"
    }
}
"""
reloaded_data = json.loads(json_string)
# It is now a dictionary again
print(f"Type of reloaded data: {type(reloaded_data)}")
print(f"User's city: {reloaded_data['profile']['city']}")
#---------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)


if __name__ == "__main__":
    main(1)

