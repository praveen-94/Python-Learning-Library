# exception_handling_basics.py

from helpers.display_utils import *

def main():
    print_heading("Exception Handling in Python")
    imp_note_points("""
- An exception is an event that occurs during program execution that disrupts the normal flow of instructions.
- Python uses `try`, `except`, `else`, and `finally` blocks to handle these errors gracefully, preventing the program from crashing.
- Handling exceptions allows you to respond to errors in a controlled and predictable way, making your code more robust.
- **Common Built-in Exceptions:**
    - `Exception`: The base class for most non-system-exiting exceptions.
    - `AttributeError`: Raised when an attribute reference or assignment fails.
    - `ImportError`: Raised when an `import` statement has trouble trying to load a module.
    - `IndexError`: Raised when a sequence subscript is out of range.
    - `KeyError`: Raised when a dictionary key is not found.
    - `TypeError`: Raised when an operation or function is applied to an object of inappropriate type.
    - `ValueError`: Raised when an operation gets an argument of the right type but an inappropriate value.
    - `ZeroDivisionError`: Raised when the second argument of a division or modulo operation is zero.
    - `FileNotFoundError`: Raised when a file or directory is requested but doesn’t exist.
""")
    num1 = 10
    num2 = 5
    num3 = 0
    num4 = 'two'
    num5 = '2'

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Basic `try...except` Block (Catch-All)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Basic `try...except` Block (General Catch-All)")
    display_note("The simplest form. The `try` block runs code, and if *any* error occurs, the bare `except` block catches it.")
    display_note("Generally bad practice because it can hide unexpected errors and make debugging difficult. It's better to be specific!", "warning")
    show_code_with_output('''# A bare except block that catches all errors.
try:
    num1 = 10
    num2 = 5
    num3 = 0
    print(f"Dividing {num1} by {num2}", end=': ')
    result1 = num1 / num2
    print(result1)
    print(f"Dividing {num1} by {num3}", end=': ')
    result2 = num1 / num3
    print(result2)
except:
    print("An unknown error occurred. It could be anything!")'''
,
"Dividing 10 by 5: 2.0" + "\n" +
"Dividing 10 by 0: An unknown error occurred. It could be anything!")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Handling Specific Exceptions and Chaining
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Handling Specific Exceptions and Chaining")
    display_note("A better approach is to chain `except` blocks to handle different, specific errors. execute the first one that matches.")
    display_note("Using `as e` allows you to capture the exception object, which contains details about the error.", "tip")        
    show_code_with_output('''# This handles two different errors specifically.
num1 = 10
num2 = 5
num3 = 0
num4 = 'two'
try:
    print(f"Dividing {num1} by {num2}", end=': ')
    result1 = num1 / num2
    print(result1)
    print(f"Dividing {num1} by {num3}", end=': ')
    result2 = num1 / num3
    print(result2)
except ZeroDivisionError as e:
    print(f"Handled a ZeroDivisionError, Error details: {e}")

try:
    print(f"Dividing {num1} by {num4}", end=': ')
    result3 = num1 / num4
    print(result3)
except TypeError as e:
    print(f"Handled a TypeError, Error details: {e}")
except ZeroDivisionError as e:
    print(f"Handled a ZeroDivisionError, Error details: {e}")
# default except block, should be last, if not present error are not match to above error not caught
except: 
    print("Some other error occured")'''
,
"Dividing 10 by 5: 2.0\n" +
"Dividing 10 by 0: Handled a ZeroDivisionError, Error details: division by zero\n" +
"Dividing 10 by two: Handled a TypeError, Error details: unsupported operand type(s) for /: 'int' and 'str'")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Grouping Multiple Exceptions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Grouping Multiple Exceptions")
    display_note("If the handling logic is the same for multiple error types, you can group them in a single `except` block using a tuple.")
    show_code_with_output('''# You can group exceptions in a tuple
num4 = 'two'
num5 = '2'
try:
    print(f"Converting string {num5} to int: ", int(num5))
    print(f"Converting string {num4} to int: ", int(num4))
except (ValueError, TypeError, KeyError) as e:
    print(f"A handled error occurred: {e}")'''
,
"Converting string 2 to int:  2\n" +
"A handled error occurred: invalid literal for int() with base 10: 'two'")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. The `else` Block
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. The `else` Block")
    display_note("The `else` block executes only if **no exceptions** are raised in the `try` block.")
    display_note("This is useful for code that should only run if the 'try' part was successful.")
    show_code_with_output('''# Demonstrating the else block
num1 = 10
num2 = 5
num3 = 0
try:
    result = num1 / num2
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is {result}")
    print("Success! The 'else' block has executed.", end='\n\n')

try:
    result = num1 / num3
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred, due to that else block was not executed: {e}")
else:
    print(f"Result is {result}")
    print("Success! The 'else' block has executed.")'''
,
"Result is 2.0\n" +
"Success! The 'else' block has executed.\n\n" +
"An error occurred, due to that else block was not executed: division by zero")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 5. The `finally` Block
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5. The `finally` Block")
    display_note("The `finally` block executes **no matter what**, whether an exception was raised or not.")
    display_note("It is essential for cleanup actions like closing a file or releasing a resource.")
    show_code_with_output('''# Demonstrating the finally block
num1 = 10
num4 = 'two'
try:
    print(f"Dividing {num1} by {num4}", end=': ')
    result3 = num1 / num4
    print(result3)
except TypeError as e:
    print(f"Handled a TypeError, Error details: {e}")
except ZeroDivisionError as e:
    print(f"Handled a ZeroDivisionError, Error details: {e}")
except:
    print("Some other error occured")
finally:
    print("Inside finally block which always execute, Cleanup is complete.")'''
,
"Dividing 10 by two: Handled a TypeError, Error details: unsupported operand type(s) for /: 'int' and 'str'\n" +
"Inside finally block which always execute, Cleanup is complete.")


if __name__ == "__main__":
    main()
