# custom_exceptions.py

from helpers.display_utils import *

def main(int_topic_number: int):
    print_heading("Custom Exceptions", int_topic_number)
    imp_note_points("""
- Creating custom exceptions makes your code more readable, self-documenting, and easier to debug.
- **Why use them?** To create specific error types that are meaningful to your application's domain
- Example: ___DatabaseError___, ___InvalidAPITokenError___
- **How to create them?** Define a new class that inherits from Python's built-in ___Exception___ class.

- **Review of Common Built-in Exceptions:**
    - __Exception__: The base class for most non-system-exiting exceptions.
    - __AttributeError__: Raised when an attribute reference or assignment fails.
    - __ValueError__: Raised for arguments with the right type but an inappropriate value.
    - __TypeError__: Raised for arguments of the wrong type.
    - __KeyError__: Raised when a dictionary key is not found.
    - __FileNotFoundError__: Raised when a file is requested but doesn’t exist.
- When none of these built-in types precisely describe your error, it's time to create a custom one.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Defining a Simple Custom Exception
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Defining a Simple Custom Exception")
    display_note("The simplest custom exception is an empty class that inherits from `Exception`. Its name alone provides valuable context.")  
    code1 = '''# Define a simple custom exception
class MyAppError(Exception):
    """Base exception for this application."""
    pass

def start_service():
    service_ready = False
    if not service_ready:
        raise MyAppError("The service could not be started.")

try:
    start_service()
except MyAppError as e:
    print(f"Caught a custom application error: {e}")
#------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Creating an Exception Hierarchy
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Creating an Exception Hierarchy")
    display_note("""For complex applications, it's good practice to create a hierarchy of exceptions.
This allows you to catch specific errors or general categories of errors.""", "tip")
    code2 = '''# A base error and specific errors that inherit from it
class MyAppError(Exception):
    """Base exception for this application."""
    pass
                          
class NetworkError(MyAppError):
    """Raised for network-related issues."""
    pass

class DatabaseError(MyAppError):
    """Raised for database-related issues."""
    pass

def connect_to_database():
    # This is a simulation
    raise DatabaseError("Failed to connect: Invalid credentials.")

try:
    connect_to_database()
except DatabaseError as e:
    print(f"Caught a specific database error: {e}")
except NetworkError as e:
    print(f"Caught a specific network error: {e}")
except MyAppError as e: # This would catch any error inheriting from MyAppError
    print(f"Caught a general app error: {e}")
#-------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Adding Attributes to Custom Exceptions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Adding Attributes to Custom Exceptions")
    display_note("""You can add an `__init__` method to your custom exceptions to store extra information about the error, which is incredibly useful for logging and debugging.""")
    code3 = '''# A custom exception that stores extra context
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount_needed):
        self.balance = balance
        self.amount_needed = amount_needed
        self.shortage = amount_needed - balance
        # Create a helpful error message
        message = f"Insufficient funds. Balance is {balance}, but {amount_needed} is needed."
        super().__init__(message) # Call the parent class's __init__

try:
    balance = 100
    withdrawal_amount = 250
    if withdrawal_amount > balance:
        raise InsufficientFundsError(balance, withdrawal_amount)
except InsufficientFundsError as e:
    print(f"Error Message: {e}")
    print(f"Details: You are short by ${e.shortage}.")
#---------------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


if __name__ == "__main__":
    main(1)
