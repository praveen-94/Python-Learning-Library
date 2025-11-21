from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Case Conversion and Character check Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------

def main(topic_number: int):
    print_heading("String Case Conversion and Character Check", topic_number)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Character Testing (Boolean Checks)")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    string_methods_info = [
        ["Method", "Description (Return True if)", "Use Cases"],
        ["isalpha", "All characters are A–Z, a–z", "Validate names, tags, or labels"],
        ["isdigit", "All characters are digits (0–9)", "Verify numeric-only inputs like PINs or counters"],
        ["isalnum", "All characters are letters or digits", "Filter valid usernames, filenames, or identifiers"],
        ["isdecimal", "All characters are base-10 digits", "Validate decimal-only numeric strings)"],
        ["isupper", "All characters are uppercase", "Enforce formatting rules, detect emphasis in logs"],
        ["islower", "All characters are lowercase", "Validate lowercase-only inputs(e.g. config keys)"],
        ["istitle", "Each word starts with upper followed by lowercase", "Format validation for titles or headings"],
        ["isspace", "All characters are whitespace (\" \", \\t, \\n, etc.)", "Detect blank or formatting-only strings"],
        ["isascii", "All characters are within ASCII range (0–127)", "Ensure compatibility across non-Unicode systems"],
        ["isidentifier", "If string is a valid Python identifier", "Validate variable names or dynamic identifiers"],
        ["isnumeric", "All characters are numeric (including Unicode numerals)", "Broader numeric validation, including internationalized inputs"],
        ["isprintable", "All characters are printable (No control characters like \\n, \\t)", "Sanitize output for logs, UI, or CLI tools"]
    ]  
    render_2d_table(string_methods_info, title="  Table of All String Character Testing Methods", inner_border=True)
    display_note("All these methods return True if the string is empty (they treat empty string to be valid for these checks).","WARNING")
    code1 = '''# Sample Code
print(f"Checking if all characters in 'Hello' are alphabetic: {'Hello'.isalpha()}")
print(f"Checking if all characters in 'Hello2025' are digits: {'Hello2025'.isdigit()}")
print(f"Checking if all characters in 'Hello_' are alphanumeric: {'Hello_'.isalnum()}")
print(f"Checking if all characters in '2025' are alphanumeric: {'2025'.isalnum()}")
print(f"Checking if all characters in 'Hello' are whitespace: {'Hello'.isspace()}")
print(f"Checking if all characters in '2025.08' are decimal: {'2025.08'.isdecimal()}")
print(f"Checking if all characters in '2025' are numeric: {'2025'.isnumeric()}")
print(f"Checking if all characters in 'Hello' are uppercase: {'Hello'.isupper()}")
print(f"Checking if all characters in 'hello' are lowercase: {'Hello'.islower()}")
print(f"Checking if 'Hello' is in title case: {'Hello'.istitle()}")
print(f"Checking if 'Hello' is a valid identifier: {'Hello'.isidentifier()}")
print(f"Checking if '123Hello' is a valid identifier: {'123Hello'.isidentifier()}")
whiteSpaceString = "   \\t\\n"
nextLinestring = 'Hello\\nWorld'
print(f"Checking if all characters in whiteSpaceString are whitespace: {whiteSpaceString.isspace()}")
print(f"Checking if nextLinestring is printable: {nextLinestring.isprintable()}")
print(f"Checking if 'Hello' is printable: {'Hello'.isprintable()}")
print(f"Checking if 'Hello' contains only ASCII characters: {'Hello'.isascii()}")
#--------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Case Conversion Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("""The 'upper()/lower()/title()' method converts all characters in the string to uppercase/lowercase/title case.
The 'casefold()' method is more aggressive than 'lower()' and is used for case-insensitive comparisons, especially for languages with special characters.""")
    code2 = '''string1 = "Hello, world!"
print(f"Uppercase of {string1} by 'upper()' method: {string1.upper()}")
print(f"Lowercase of 'Straße' by 'lower()' method: {'Straße'.lower()}")
print(f"Casefolded of 'Straße' by 'casefold()' method: {'Straße'.casefold()}")
print(f"Title case of {string1} by 'title()' method: {string1.title()}")
print(f"Capitalized first letter of 'hello, world.' by 'capitalize()' method: {'hello, world.'.capitalize()}")
print(f"Swapping case of {string1} by 'swapcase()' method: {string1.swapcase()}")
#---------------------------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

