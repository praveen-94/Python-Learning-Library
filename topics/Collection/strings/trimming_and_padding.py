from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Trimming and Padding Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print_heading("Trimming and Padding Methods:")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    string1 = "Hello, world!"
    print_sub_heading("1) String Trimming Methods")
    print_small_sub_heading("The 'strip([chars]), lstrip([chars]), rstrip([chars])' method: ")
    display_note("Removes leading and trailing/from the beginning(left side) or end(right side) whitespace characters from the string.")
    display_note("it removes whitespace characters (by default), but we can also specify characters to remove by passing them as an argument.")
    display_note("All 3 methods remove characters, not substrings.")
    display_note("'strip('lo')' will remove all 'l' and 'o' characters from both ends of the string, not just the substring 'lo'.","Example")
    wstring = '  $$Hello World!!!'
    show_code_with_output('''wstring = '  $$Hello World!!!'
print(f"Stripped whitespace of '{wstring}' string by 'strip()' method: {wstring.strip()}")
print(f"Stripped '$$' from begginning of '{wstring}' string by 'lstrip('$')' method: {(wstring.lstrip()).lstrip('$')}")
print(f"Stripped '!!!' from end of '{wstring}' string by 'rstrip('!')' method: {wstring.rstrip('!')}")'''
,
"Stripped whitespace of '" + wstring + "' string by 'strip()' method: "  + wstring.strip() + "\n" +
"Stripped '$$' from begginning of '" + wstring + "' string by 'lstrip('$')' method: " + (wstring.lstrip()).lstrip("$") + "\n" +
"Stripped '!!!' from end of '" + wstring + "' string by 'rstrip('!')' method: " + wstring.rstrip('!'))
    
    print_small_sub_heading("The 'removeprefix(prefix)/removesuffix(suffix)' methods are used to remove a specified prefix or suffix from the string.",True)
    display_note("If the prefix/suffix is not found or not pass, it returns the original string unchanged.")
    display_note("The 'removeprefix()' and 'removesuffix()' methods are available only in Python 3.9 and later versions.","WARNING")
    show_code_with_output('''string1 = "Hello, world!" 
print(f"Removing prefix 'Hello' from '{string1}' string by 'removeprefix()' method: '{string1.removeprefix('Hello')}'")
print(f"Removing suffix 'World!' from '{string1}' string by 'removesuffix()' method: '{string1.removesuffix('World!')}'")'''
,
"Removing prefix 'Hello' from '" + string1  + "' string by 'removeprefix()' method: " + string1.removeprefix('Hello') + "\n" +
"Removing suffix 'world!' from '" + string1 + "' string by 'removesuffix()' method: " + string1.removesuffix('world!'))                  
    
    print_sub_heading("2) String Padding Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("The 'center(width[, fillchar]), ljust(width[, fillchar]), rjust(width[, fillchar])' methods:",True)
    display_note("These methods are used to Center/left-align/right-align string with padding, with specified characters to a given width.")
    display_note("The 'zfill(width)' method pads the string with zeros on the left side to make it a specified width.")
    display_note("The 'center()/ljust()/rjust()' methods can also take a fill character as an optional argument.")
    display_note("If not provided, it defaults to space.","NOTE", message_continue=True)
    show_code_with_output('''string1 = "Hello, world!" 
print(f"Centering '{string1}' string to width 30 with '-' fill character: '{string1.center(30, '-')}'")
print(f"Left-aligning '{string1}' string to width 30 with '-' fill character: '{string1.ljust(30, '-')}'")
print(f"Right-aligning '{string1}' string to width 30 with '-' fill character: '{string1.rjust(30, '-')}'")
print(f"Zero-filling '{string1}' string to width 30: '{string1.zfill(30)}'")'''
,
"Centering '" + string1 + "' string to width 30 with '-' fill character: " + string1.center(30, '-') + "\n" +
"Left-aligning '" + string1 + "' string to width 30 with '-' fill character: " + string1.ljust(30, '-') + "\n" +
"Right-aligning '" + string1 + "' string to width 30 with '-' fill character: " + string1.rjust(30, '-') + "\n" +
"Zero-filling '" + string1 + "' string to width 30: " + string1.zfill(30))