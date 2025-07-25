from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Miscellaneous Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print_heading("Other String Miscellaneous Methods Demo")
    print_sub_heading("1) Encoding & Translation Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("The 'encode()' method converts a string into bytes using a specified encoding. Default is 'utf-8'.")
    display_note("The 'maketrans()' method creates a translation table for use with 'translate()'.")
    display_note("The 'translate()' method returns a string where each character is mapped using the translation table.")
    show_code_with_output('''trans_table = str.maketrans('ae', '12')
print(f"Encoded version of 'hello' using 'encode()' method: {'hello'.encode()}")
print(f"Translation table using 'maketrans()': {trans_table}")
print(f"Translated string of 'apple' using 'translate()': {'apple'.translate(trans_table)}")'''
,
"Encoded version of 'hello' using 'encode()' method: " + str('hello'.encode()) + "\n" +
"Translation table using 'maketrans()': " + str(str.maketrans('ae', '12')) + "\n" +
"Translated string of 'apple' using 'translate()': " + str('apple'.translate(str.maketrans('ae', '12'))))

    print_sub_heading("2) Formatting Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("The 'format()' method allows inserting values into placeholders defined by curly braces {}.")
    display_note("The 'format_map()' method is similar to 'format()', but takes a dictionary directly instead of unpacked arguments.")
    show_code_with_output('''print("Using 'format()' to insert values: {}".format("Hello, World!"))
print("Formatted string with multiple values: {} + {} = {}".format(2, 3, 2+3))
                          
info = {'name': 'Alice', 'age': 25}
print("Formatted string using 'format_map()': {name} is {age} years old.".format_map(info))'''
,
"Using 'format()' to insert values: Hello, World!\n" +
"Formatted string with multiple values: 2 + 3 = 5\n" +
"Formatted string using 'format_map()': Alice is 25 years old.")

    print_sub_heading("3) expandtabs() Method")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("The 'expandtabs()' method replaces tab characters '\\t' with spaces. Default is 8 spaces per tab.")
    show_code_with_output('''tabbed_string = "Name\tAge\tCountry"\nprint(f"Original tabbed string: {tabbed_string}")\nprint(f"Expanded version using 'expandtabs(4)': {tabbed_string.expandtabs(4)}")''',
                           "Original tabbed string: Name\tAge\tCountry\n" + "Expanded version using 'expandtabs(4)': Name    Age     Country")