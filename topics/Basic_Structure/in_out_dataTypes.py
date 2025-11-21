from helpers.display_utils import *

def main(topic_number: int):
    """Display basic data types and input/output in Python using Rich library."""
    print_heading("Basic Data Types and Input/Output/Print in Python", topic_number)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Variables
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Variables in Python")
    display_note("Python is a dynamically typed language, meaning you don't need to declare the type of a variable explicitly.")
    code_snippet1 = '''# Example of variable declaration and assignment
number = 10
string = "Hello, World!"
float_number = 3.14
boolean_value = True
character = 'A'
print("Number:", number, ", Float:", float_number) 
print("String:", string, ", Character:", character) 
print("Boolean:", boolean_value)
'''
    result1 = run_code_snippet(code_snippet1)
    show_code_with_output(code_snippet1, result1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Input Function working
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Example of Input Function")
    print("This code snippet requires user interaction. Please provide input when prompted.")
    display_note("The input function in Python 3 always returns a string, To get a number you need to convert it using int() or float().")
    print("Please provide inputs a number then a string: ")
    code_snippet2 = '''# Example of input function
user_input1 = input("Enter a number: ")
print("\\nUser input number:", user_input1, "and its type is:", type(user_input1))
user_input2 = input("Enter a string: ")
print("\\nUser input string:", user_input2, "and its type is:", type(user_input2))
print("Converting user input to integer and print its value and type")
print("It is also a example of explicit type conversion") 
user_input3 = int(user_input1)
print("User input as integer:", user_input3 , "and its type after conversion is:", type(user_input3)) 
'''
    result2 = run_code_snippet(code_snippet2)
    show_code_with_output(code_snippet2, result2)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Print function working
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Example of print function")
    display_note("""The print function in Python 3 has a default separator of space and end character of newline.
The print function can take optional parameters `sep` and `end` to replace the default values for separator and end character.""")
    code_snippet3 = '''# Example of print function
user_input1 = 10
user_input2 = "Hello"
print("1st print statement", "with default separator and end character.")
print("2nd print statement", "with default separator and end character.")
print("1st print statement", "with custom end ';' and separator ','", end=" ; ", sep=", ") 
print("2nd print statement", "with custom separator ','", sep=": ")
print(f"We can also use f-strings for formatted output:")
print(f"'{user_input1}' is an integer and '{user_input2}' is a string.") 
''' 
    result3 = run_code_snippet(code_snippet3)
    show_code_with_output(code_snippet3, result3)