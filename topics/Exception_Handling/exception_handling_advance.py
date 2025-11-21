# exception_handling_advance.py

from helpers.display_utils import *

def main(int_topic_number: int):
    print_heading("Raising Exceptions with `raise`", int_topic_number)
    imp_note_points("""
- The ___raise___ keyword is used to deliberately trigger an exception at a specific point in your code.
- **Why use it?** To signal that an error condition has been met, such as invalid input or a state that your program cannot handle.
- You can raise instances of Python's built-in exception classes or your own custom ones.""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Basic `raise` for Validation
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Basic `raise` for Input Validation")
    display_note("The most common use of `raise` is to reject invalid data passed to a function or method.")
    code1 = '''# A function that raises an error if input is invalid
def check_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError(f"Age '{age}' is invalid, it must be a non-negative integer.")
    print(f"Age '{age}' is Valid")

user1_age, user2_age, user3_age = 19, -20, 'ten'
try:
    print("Checking user1 age", end=": ")
    check_age(user1_age)
    print("Checking user2 age", end=": ")
    check_age(user2_age)
except ValueError as e:
    print(f"Error!! {e}")

try:
    print("Checking user3 age", end=": ")
    check_age(user3_age)
except ValueError as e:
    print(f"Error!! {e}")
#--------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Re-raising an Exception
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Re-raising an Exception")
    display_note("""Sometimes you want to catch an exception, perform an action (like logging),
and then let the exception continue up the call stack. A bare `raise` inside an `except` block does this.""")
    code2 = '''# Catching, logging, and re-raising an error
def process_data(data):
    try:
        result = data / 2  # This might fail if data is not a number
        return result
    except TypeError:
        print("Log: A TypeError occurred while processing data.")
        raise # Re-raise the caught TypeError

try:
    process_data("hello") # if error occur it again caught TypeError
except TypeError as e:
    print(f"Main program caught the re-raised error: {e}")
#--------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Chaining Exceptions with `raise from`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Chaining Exceptions with `raise from`")
    display_note("""`raise NewException from original_exception`
it is used to wrap a low-level error in a more meaningful, high-level exception while preserving the original traceback.""", "tip")
    display_note("This provides better context for debugging.", "example")
    code3 = '''# Wrapping a low-level error in a more descriptive one
def get_user_role(user_id, roles):
    try:
        return roles[user_id]
    except KeyError as e:
        # Wrap the KeyError in a more meaningful ValueError
        raise ValueError(f"Invalid user ID: {user_id}") from e

roles_db = {"admin": "Administrator", "guest": "Guest"}
try:
    get_user_role("tester", roles_db)
except ValueError as e:
    print(f"High-level error: {e}")
    # The original KeyError is available via __cause__
    print(f"Original cause: {e.__cause__}")
#---------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


if __name__ == "__main__":
    main(1)
