from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Case Conversion and Character check Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------

def main():
    print_heading("String Case Conversion and Character Check")
    print_sub_heading("1) Case Conversion Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    string1 = "Hello, world!"
    display_note("The 'upper()/lower()/title()' method converts all characters in the string to uppercase/lowercase/title case.")
    display_note("The 'casefold()' method is more aggressive than 'lower()' and is used for case-insensitive comparisons, especially for languages with special characters.")
    show_code_with_output('''string1 = "Hello, world!"
print(f"Uppercase of {string1} by 'upper()' method: {string1.upper()}")
print(f"Lowercase of 'Straße' by 'lower()' method: {'Straße'.lower()}")
print(f"Casefolded of 'Straße' by 'casefold()' method: {'Straße'.casefold()}")
print(f"Title case of {string1} by 'title()' method: {string1.title()}")
print(f"Capitalized first letter of 'hello, world.' by 'capitalize()' method: {'hello, world.'.capitalize()}")
print(f"Swapping case of {string1} by 'swapcase()' method: {string1.swapcase()}")'''
,
"Uppercase of '" + string1 + "' by 'upper()' method: " + string1.upper() + "\n" +
"Lowercase of 'Straße' by 'lower()' method: " + 'Straße'.lower() + "\n" +
"Casefolded of 'Straße' by 'casefold()' method: " + 'Straße'.casefold() + "\n" +
"Title case of '" + string1 + "' by 'title()' method: " + string1.title() + "\n" +
"Capitalized first letter of 'hello, world.' by 'capitalize()' method: " + 'hello, world.'.capitalize() + "\n" +
"Swapping case of '" + string1 + "' by 'swapcase()' method: " + string1.swapcase())

    print_sub_heading("2) Character Testing (Boolean Checks)")
    display_note("The 'isalpha()/isdigit()/isalnum()/isspace()/isdecimal()/isnumeric()isupper()/islower()/istitle()/isidentifier()/isprintable()/isascii()' method:")
    display_note("They checks if all characters in the string are alpha/digit/alpha+digit/whitespace/decimal/numerical/uppercase/lowercase/titlecase/valid identifier/printable/ascii characters.")
    show_code_with_output('''string1 = "Hello"
print(f"Checking if all characters in '{string1}' are alphabetic: {string1.isalpha()}")
print(f"Checking if all characters in '12345' are digits: {'12345'.isdigit()}")
print(f"Checking if all characters in 'Hello123' are alphanumeric: {'Hello123'.isalnum()}")
print(f"Checking if all characters in '   \\t\\n' are whitespace: {'   \\t\\n'.isspace()}")
print(f"Checking if all characters in '123.45' are decimal: {'123.45'.isdecimal()}")
print(f"Checking if all characters in '12345' are numeric: {'12345'.isnumeric()}")
print(f"Checking if all characters in {string1} are uppercase: {string1.isupper()}")
print(f"Checking if all characters in {string1} are lowercase: {string1.islower()}")
print(f"Checking if {string1} is in title case: {string1.istitle()}")
print(f"Checking if '{string1}' is a valid identifier: {string1.isidentifier()}")
print(f"Checking if 'Hello123' is a valid identifier: {'Hello123'.isidentifier()}")
print(f"Checking if '{string1}' is printable: {string1.isprintable()}")
print(f"Checking if 'Hello\\nWorld' is printable: {'Hello\\nWorld'.isprintable()}")
print(f"Checking if '{string1}' contains only ASCII characters: {string1.isascii()}")'''
,
"Checking if all characters in '" + string1 + "' are alphabetic: " + str(string1.isalpha()) + "\n" +
"Checking if all characters in '12345' are digits: " + str('12345'.isdigit()) + "\n" +
"Checking if all characters in 'Hello123' are alphanumeric: " + str('Hello123'.isalnum()) + "\n" +
"Checking if all characters in '   \\t\\n' are whitespace: " + str('   \\t\\n'.isspace()) + "\n" +
"Checking if all characters in '123.45' are decimal: " + str('123.45'.isdecimal()) + "\n" +
"Checking if all characters in '12345' are numeric: " + str('12345'.isnumeric()) + "\n" +
"Checking if all characters in " + string1 + " are uppercase: " + str(string1.isupper()) + "\n" +
"Checking if all characters in " + string1 + " are lowercase: " + str(string1.islower()) + "\n" +
"Checking if " + string1 + " is in title case: " + str(string1.istitle()) + "\n" +
"Checking if '" + string1 + "' is a valid identifier: " + str(string1.isidentifier()) + "\n" +
"Checking if 'Hello123' is a valid identifier: " + str('Hello123'.isidentifier()) + "\n" +
"Checking if '" + string1 + "' is printable: " + str(string1.isprintable()) + "\n" +
"Checking if 'Hello\\nWorld' is printable: " + str('Hello\\nWorld'.isprintable()) + "\n" +
"Checking if '" + string1 + "' contains only ASCII characters: " + str(string1.isascii()))
    display_note("These methods return True if the string is empty, as they consider an empty string to be valid for these checks.","WARNING")


