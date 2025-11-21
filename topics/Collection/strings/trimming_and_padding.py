from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Trimming and Padding Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main(topic_number: int):
    print_heading("Trimming and Padding Methods:", topic_number)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) String Trimming Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("The 'strip([chars]), lstrip([chars]), rstrip([chars])' method: ")
    display_note("""strip([chars]): Removes leading and trailing whitespace characters from the string.
lstrip([chars]): Removes whitespace characters from the beginning(left side) 
rstrip([chars]): Removes whitespace characters from the end(right side)
All 3 methods remove whitespace characters (by default), but we can also specify characters to remove by passing them as an argument.
All 3 methods remove characters, not substrings.""")
    display_note("'strip('lo')' will remove all 'l' and 'o' characters from both ends of the string, not just the substring 'lo'.","Example")
    code1 = '''# sample code
wstring = '  $$Hello World!!!'
print(f"Stripped whitespace of '{wstring}' string by 'strip()' method: {wstring.strip()}")
print(f"Stripped '$$' from '{wstring}' string by 'lstrip()' method: {(wstring.lstrip()).lstrip('$')}")
print(f"Stripped '!!!' from end of '{wstring}' string by 'rstrip('!')' method: {wstring.rstrip('!')}")
#------------------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("The 'removeprefix(prefix)/removesuffix(suffix)' methods:",True)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    display_note("""these methods are used to remove a specified prefix or suffix from the string.
If the prefix/suffix is not found or not pass, it returns the original string unchanged.""")
    display_note("The 'removeprefix()' and 'removesuffix()' methods are available only in Python 3.9 and later versions.","WARNING")
    code2 = '''# sample code
string1 = "Hello, world!" 
print(f"Removing prefix 'Hello' from '{string1}' string: '{string1.removeprefix('Hello')}'")
print(f"Removing suffix 'World!' from '{string1}' string: '{string1.removesuffix('World!')}'")
#-------------------------------------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)
 
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) String Padding Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("The 'center(width[, fillchar]), ljust(width[, fillchar]), rjust(width[, fillchar])' methods:",True)
    display_note("""These methods are used to Center/left-align/right-align string with padding, with specified characters to a given width.
The 'zfill(width)' method pads the string with zeros on the left side to make it a specified width.
The 'center()/ljust()/rjust()' methods can also take a fill character as an optional argument, If not provided, it defaults to space.""")
    code3 = '''# sample code
string1 = "Hello, world!" 
print(f"Centering '{string1}' string to width 30 with '-' fill character: '{string1.center(30, '-')}'")
print(f"Left-aligning '{string1}' string to width 30 with '-' fill character: '{string1.ljust(30, '-')}'")
print(f"Right-aligning '{string1}' string to width 30 with '-' fill character: '{string1.rjust(30, '-')}'")
print(f"Zero-filling '{string1}' string to width 30: '{string1.zfill(30)}'")
#-----------------------------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)