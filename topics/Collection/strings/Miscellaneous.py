from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Miscellaneous Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main(topic_number: int):
    print_heading("Other String Miscellaneous Methods Demo", topic_number)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Encoding & Translation Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("""The 'encode()' method converts a string into bytes using a specified encoding. Default is 'utf-8'.
The 'maketrans()' method creates a translation table for use with 'translate()'.
The 'translate()' method returns a string where each character is mapped using the translation table.""")
    code1 = '''# sample code
trans_table = str.maketrans('ae', '12')
print(f"Encoded version of 'hello' using 'encode()' method: {'hello'.encode()}")
print(f"Translation table using 'maketrans()': {trans_table}")
print(f"Translated string of 'apple' using 'translate()': {'apple'.translate(trans_table)}")
#-------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Formatting Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("""The 'format()' method allows inserting values into placeholders defined by curly braces {}.
The 'format_map()' method is similar to 'format()', but takes a dictionary directly instead of unpacked arguments.""")
    code2 = '''# sample code
print("Using 'format()' to insert values: {}".format("Hello, World!"))
print("Formatted string with multiple values: {} + {} = {}".format(2, 3, 2+3))
                          
info = {'name': 'Alice', 'age': 25}
print("Formatted string using 'format_map()': {name} is {age} years old.".format_map(info))
#------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    #------------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3) expandtabs() Method")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("The 'expandtabs()' method replaces tab characters '\\t' with spaces. Default is 8 spaces per tab.")
    code3 = '''# sample code
tabbed_string = "Name\tAge\tCountry"
print(f"Original tabbed string: {tabbed_string}")
print(f"Expanded version using 'expandtabs(4)': {tabbed_string.expandtabs(4)}")
#------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)