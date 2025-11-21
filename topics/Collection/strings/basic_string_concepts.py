from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Basic Concept Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main(topic_number: int):
    notes_points = """
- String is a collection of characters (alphabets, digits, symbols).
- String is 'immutable', meaning once created, it cannot be changed.            
- To change a string, you must create a new string.                            
- Strings can be created using single quotes, double quotes, or triple quotes. 
- Strings can be concatenated using the + operator.
- Strings can be repeated using the * operator.                                
- Strings can be indexed and sliced.                                           
- Strings can be formatted using f-strings, format() method, or % operator.    
"""
    print_heading("String and string collections details", topic_number)
    imp_note_points(notes_points)
    
    #------------------------------------------------------
    print_sub_heading("Example of string creation")
    code1 = """# String creation
String1 = "Hello, world!"
print(f"String1 is: {String1}")
#----------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)
    
    #------------------------------------------------------
    print_sub_heading("Example of taking user input for a string")
    code2 = '''# Taking user input
string2 = input("Enter a string....... ")
print("\\nEnter String is:", string2)
#---------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    #------------------------------------------------------
    print_sub_heading("Example of string concatenation")
    code3 = '''# String concatenation
string1 = "Hello, World!"
string2 = "Welcome to Python!"
concatenated_string = string1 + " " + string2
print(f"String1 is: {string1}")
print(f"String2 is: {string2}")
print(f"Concatenated String of 'string1' and 'string2' is: {concatenated_string}")
#--------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)
    
    #------------------------------------------------------
    print_sub_heading("Example of string repetition")
    code4 = '''# String repetition
string1 = "Hello, World! "
repeated_string = string1 * 2
print(f"Repeated String of '{string1}' two times: {repeated_string}")
#---------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    #------------------------------------------------------
    print_sub_heading("Example of string indexing and slicing")
    display_note("""String indexing starts from 0, and negative indexing starts from the end of the string (-1 is the last character).
String slicing can also be done with a step value, like string[start:end:step].
For example, string[::2] will return every second character of the string.""")
    code5 = '''# slicing
string1 = "Hello, world!"
print(f"First character of '{string1}': {string1[0]}")
print(f"Last character of '{string1}': {string1[-1]}")
print(f"Substring of '{string1}' from index 0 to 4: {string1[0:5]}")
print(f"Substring of '{string1}' from index 7 to end: {string1[7:]}")
print(f"Substring of '{string1}' with step 2: {string1[::2]}")
print(f"Reverse of '{string1}': {string1[::-1]}")
#---------------------------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    #------------------------------------------------------
    print_sub_heading("len() method:")
    display_note("The 'len()' method returns the length of the string, which is the number of characters in it.")
    code6 = '''# len() method
string1 = "Hello, world!"
print(f"Length of '{string1}' is: {len(string1)}")
#---------------------------------------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)
