from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Basic Concept Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    notes_points = """
- String is a collection of characters (alphabets, digits, symbols).
- String is `immutable`, meaning once created, it cannot be changed.            
- To change a string, you must create a new string.                            
- Strings can be created using single quotes, double quotes, or triple quotes. 
- Strings can be concatenated using the + operator.
- Strings can be repeated using the * operator.                                
- Strings can be indexed and sliced.                                           
- Strings can be formatted using f-strings, format() method, or % operator.    
"""
    print_heading("String","String and string collections details")
    imp_note_points(notes_points)

    print_sub_heading("Example of string creation")
    string1 = "Hello, world!"
    show_code_with_output("string1 = 'Hello, World!'",string1)

    print_sub_heading("Example of taking user input for a string")
    string2 = input("  Enter a string: ")
    show_code_with_output('string2 = input("Enter a string: )"\nprint("Enter String is:", string2)") ','Enter String is: ' + string2)
    print("Enter String is:", string2)

    print_sub_heading("Example of string concatenation")
    concatenated_string = string1 + " " + string2
    inStr = 'concatenated_string = string1 + " " + string2\nprint(f"Concatenated String of \'{string}\' and \'{string2}\' is: {concatenated_string}'
    Outstr = "Concatenated String of '" + string1 + "' and '" + string2 + "' is: " + concatenated_string
    show_code_with_output(inStr,Outstr)

    print_sub_heading("Example of string repetition")
    repeated_string = string1 * 2
    show_code_with_output('repeated_string = string1 * 2\nprint(f"Repeated String of \'{string1}\' two times: {repeated_string}")',"Repeated String of '" + string1 + "' two times: '" + repeated_string)

    print_sub_heading("Example of string indexing and slicing")
    display_note("String indexing starts from 0, and negative indexing starts from the end of the string (-1 is the last character).")
    display_note("String slicing can also be done with a step value, like string[start:end:step].")
    display_note("For example, string[::2] will return every second character of the string.")
    show_code_with_output('''string1 = "Hello, world!"
print(f"First character of '{string1}': {string1[0]}")
print(f"Last character of '{string1}': {string1[-1]}")
print(f"Substring of '{string1}' from index 0 to 4: {string1[0:5]}")
print(f"Substring of '{string1}' from index 7 to end: {string1[7:]}")
print(f"Substring of '{string1}' with step 2: {string1[::2]}")
print(f"Reverse of '{string1}': {string1[::-1]}")'''
,
"First character of '" + string1 + "': " + string1[0] + "\n" +
"Last character of '" + string1 + "': " + string1[-1] + "\n" +
"Substring of '" + string1 +  "' from index 0 to 4: " + string1[0:5] + "\n" +
"Substring of '" + string1 + "' from index 7 to end: " + string1[7:] + "\n" + 
"Substring of '" + string1 + "' with step 2: " + string1[::2] + "\n" +
"Reverse of '" + string1 + "': " + string1[::-1])

    print_sub_heading("len() method:")
    display_note("The 'len()' method returns the length of the string, which is the number of characters in it.")
    show_code_with_output('''print(f"Length of '{string1}' is: {len(string1)}"''',"Length of '" + string1 + "' is: " + str(len(string1)))

