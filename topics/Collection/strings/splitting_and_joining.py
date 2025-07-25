from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Splitting and joining Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print_heading("String Splitting & Joining Methods Demo")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Splitting Methods")
    print_small_sub_heading("The 'split(sep[, maxsplit]])/rsplit([sep[, maxsplit]])' method: ")
    display_note("The 'split()' method takes two optional arguments: 'sep' (separator) and 'maxsplit' (maximum number of splits) and splits the string into a list of substrings")
    display_note("If the separator is not found, split() returns a list containing the entire original string as a single element.")
    display_note("split() returns list, not string","WARNING")
    string3 = "Hello, World! Welcome to Python."
    show_code_with_output('''string3 = "Hello, World! Welcome to Python."
print(f"Splitting '{string3}' by default whitespace separator: {string3.split()}")
print(f"Splitting '{string3}' by default whitespace separator with maxsplit=2: {string3.split(maxsplit=2)}")
print(f"Splitting '{string3}' by '!' separator: {string3.split(',')}")'''
,
"Splitting '" + string3 + "' by default whitespace separator: " + str(string3.split()) + "\n" +
"Splitting '" + string3 + "' by default whitespace separator with maxsplit=2: " + str(string3.split(maxsplit=2)) + "\n" +
"Splitting '" + string3 + "' by '!' separator: " + str(string3.split(',')))
    
    print_small_sub_heading("The 'partition(separator)/rpartition(separator)' method:",True)                  
    display_note("These method splits the string into a tuple of three parts: (before separator, separator, after separator).")
    display_note("If the separator is not found, it returns a tuple with the original string as the first element and two empty strings as the second and third elements.")
    show_code_with_output('''print(f"Partitioning '{string3}' by '!' separator: {string3.partition('!')}")''', "Partitioning '" + string3 + "' by '!' separator: " + str(string3.partition('!')))

    print_small_sub_heading("The 'splitlines(keepends)' method:",True)
    display_note("The 'splitlines(keepends)' method splits the string into a list of lines, removing line breaks.")
    display_note("If 'keepends' is True, the line breaks are included in the resulting list.")
    multiline_string = "Hello, World!\nWelcome to Python.\nThis is a multiline string."
    show_code_with_output('''multiline_string = "Hello, World!\\nWelcome to Python.\\nThis is a multiline string."
print(f"Splitting multiline string into lines: {multiline_string.splitlines()}")
print(f"Splitting multiline string into lines with keepends True: {multiline_string.splitlines(True)}")'''
,
"Splitting multiline string into lines: " + str(multiline_string.splitlines()) + "\n" +
"Splitting multiline string into lines with keepends True: " + str(multiline_string.splitlines(True)))
    
    print_sub_heading("2) Joining Methods")
    print_small_sub_heading("The 'join(iterable)' method:",True)
    display_note("The 'join(iterable)' method joins the list of strings into a single string using the specified delimiter.")
    display_note("The 'join()' method can only be used with a list of strings, not with a list of other data types like integers or floats.","WARNING")
    show_code_with_output('''print(f"Joining list of strings {['Hello', 'World', 'Python']} with space as delimiter: {' '.join(['Hello', 'World', 'Python'])}")\nprint(f"Joining list of strings {['Hello', 'World', 'Python']} with comma as delimiter: {', '.join(['Hello', 'World', 'Python'])}")''',
    "Joining list of strings ['Hello', 'World', 'Python'] with space as delimiter: " + ' '.join(['Hello', 'World', 'Python']) + "\n" + "Joining list of strings ['Hello', 'World', 'Python'] with comma as delimiter: " + ', '.join(['Hello', 'World', 'Python']))
