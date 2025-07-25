# custom_exceptions.py

from helpers.display_utils import *

def main():
    print_heading("Custom Exceptions")
    imp_note_points("""
- Creating custom exceptions makes your code more readable, self-documenting, and easier to debug.
- **Why use them?** To create specific error types that are meaningful to your application's domain 
- Example: `DatabaseError`, `InvalidAPITokenError`
- **How to create them?** Define a new class that inherits from Python's built-in `Exception` class.

- **Review of Common Built-in Exceptions:**
    - `Exception`: The base class for most non-system-exiting exceptions.
    - `AttributeError`: Raised when an attribute reference or assignment fails.
    - `ValueError`: Raised for arguments with the right type but an inappropriate value.
    - `TypeError`: Raised for arguments of the wrong type.
    - `KeyError`: Raised when a dictionary key is not found.
    - `FileNotFoundError`: Raised when a file is requested but doesn’t exist.
- When none of these built-in types precisely describe your error, it's time to create a custom one.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Defining a Simple Custom Exception
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Defining a Simple Custom Exception")
    display_note("The simplest custom exception is an empty class that inherits from `Exception`. Its name alone provides valuable context.")  
    show_code_with_output('''# Define a simple custom exception
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
    print(f"Caught a custom application error: {e}")'''
,
"Caught a custom application error: The service could not be started.")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Creating an Exception Hierarchy
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Creating an Exception Hierarchy")
    display_note("For complex applications, it's good practice to create a hierarchy of exceptions.","tip")
    display_note("This allows you to catch specific errors or general categories of errors.", "tip", message_continue=True)
    show_code_with_output('''# A base error and specific errors that inherit from it
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
    print(f"Caught a general app error: {e}")'''
,
"Caught a specific database error: Failed to connect: Invalid credentials.")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Adding Attributes to Custom Exceptions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Adding Attributes to Custom Exceptions")
    display_note("You can add an `__init__` method to your custom exceptions to store extra information about the error,")
    display_note("which is incredibly useful for logging and debugging.",message_continue=True)
    show_code_with_output('''# A custom exception that stores extra context
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
    print(f"Details: You are short by ${e.shortage}.")'''
,
'''Error Message: Insufficient funds. Balance is 100, but 250 is needed.
Details: You are short by $150.''')


if __name__ == "__main__":
    main()
