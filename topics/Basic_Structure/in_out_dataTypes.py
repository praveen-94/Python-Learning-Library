from helpers.display_utils import *

def main():
    """Display basic data types and input/output in Python using Rich library."""
    print_heading("Basic Data Types and Input/Output/Print in Python")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Variables
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Variables in Python")
    display_note("Python is a dynamically typed language, meaning you don't need to declare the type of a variable explicitly.")
    show_code_with_output('''# Example of variable declaration and assignment
number = 10
string = "Hello, World!"
float_number = 3.14
boolean_value = True
character = 'A'
print("Number:",number, ", String:", string, ", Float:", float_number,", Boolean:", boolean_value, ", Character:", character) '''
,
"Number: 10 , String: Hello, World! , Float: 3.14, Boolean: True , Character: A"
    )

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Input Function working
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Example of Input Function")
    display_note("The input function in Python 3 always returns a string, To get a number you need to convert it using int() or float().")
    show_code_with_output('''# Example of input function
user_input1 = input("Enter a number: ")
user_input2 = input("Enter a string: ")
print("User input number:", user_input1, "and its type is:", type(user_input1))
print("User input string:", user_input2, "and its type is:", type(user_input2))
print("Converting user input to integer and print its value and type, it is also a example of explicit type conversion") 
user_input1 = int(user_input1)
print("User input as integer:", user_input1 , "and its type after conversion is:", type(user_input1))'''
,
"User input number: 5 and its type is: <class 'str'>\n"
"User input string: Hello and its type is: <class 'str'>\n"
"Converting user input to integer and print its value and type, it is also a example of explicit type conversion\n"
"User input as integer: 5 and its type after conversion is: <class 'int'>"
    )

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Print function working
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Example of print function")
    display_note("The print function in Python 3 has a default separator of space and end character of newline.")
    display_note("The print function can take optional parameters `sep` and `end` to change the default separator and end character.")
    show_code_with_output('''# Example of print function
print("1st print statement", "with default separator and end character.")
print("2nd print statement", "with default separator and end character.")
print("1st print statement", "with custom end '|' and separator ':'", end=" | ", sep=": ") 
print("2nd print statement", "with custom end '|' and separator ':'", end=" | ", sep=": ")
print(f"We can also use f-strings for formatted output: {user_input1} is an integer and {user_input2} is a string.") ''',
"1st print statement with default separator and end character.\n"
"2nd print statement with default separator and end character.\n"
"1st print statement: with custom end '|' and separator ':' | 2nd print statement: with custom end '|' and separator ':' |\n"
"We can also use f-strings for formatted output: 5 is an integer and Hello is a string."
)