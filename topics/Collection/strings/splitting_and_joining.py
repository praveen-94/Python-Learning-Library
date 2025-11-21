from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Splitting and joining Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main(topic_number: int):
    print_heading("String Splitting & Joining Methods Demo", topic_number)
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Splitting Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("The 'split(sep[, maxsplit]])/rsplit([sep[, maxsplit]])' method: ")
    display_note("""The 'split()' method takes two optional arguments:
'sep' (separator) and 'maxsplit' (maximum number of splits) and splits the string into a list of substrings
If the separator is not found, split() returns a list containing the entire original string as a single element.""")
    display_note("split() returns list, not string","WARNING")
    code1 = '''# sample code
string = "Hello, World! Welcome to Python."
print("Enter string is:", string)
print(f"Splitting this string by default whitespace separator: {string.split()}")
print(f"Splitting this string by default whitespace separator with maxsplit=2: {string.split(maxsplit=2)}")
print(f"Splitting this string by '!' separator: {string.split('!')}")
#-----------------------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("The 'partition(separator)/rpartition(separator)' method:",True)                  
    display_note("""These method splits the string into a tuple of three parts: (before separator, separator, after separator
If the separator is not found, it returns a tuple with the original string as the 1st element and two empty strings as the 2nd and 3rd elements.""")
    code2 = '''# sample code
string = "Hello, World! Welcome to Python."
print(f"Partitioning '{string}' by '!' separator: {string.partition('!')}")
#--------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    print_small_sub_heading("The 'splitlines(keepends)' method:",True)
    display_note("""The 'splitlines(keepends)' method splits the string into a list of lines, removing line breaks.
If 'keepends' is True, the line breaks are included in the resulting list.""")
    code3 = ''' # sample code
multiline_string = "Hello!\\nWelcome to Python.\\nWorld."
print(f"Splitting multiline string into lines: {multiline_string.splitlines()}")
print(f"Splitting multiline string into lines with keepends True: {multiline_string.splitlines(True)}")
#------------------------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Joining Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("The 'join(iterable)' method:",True)
    display_note("The 'join(iterable)' method joins the list of strings into a single string using the specified delimiter.")
    display_note("join() method can only be used with a list of strings, not with a list of other data types like integers or floats.","WARNING")
    code4 = '''# sample code
str_list =  ['Hello', 'World', 'Python']
print(f"Joining list of strings {str_list} with space as delimiter: {' '.join(str_list)}")
print(f"Joining list of strings {str_list} with comma as delimiter: {', '.join(str_list)}")
#------------------------------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)
