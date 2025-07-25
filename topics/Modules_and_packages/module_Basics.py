# modules_and_packages.py

from helpers.display_utils import *

def main():
    print_heading("Modules in Python")
    imp_note_points("""
- **Module:** Any Python file (`.py`) is a module. It's the simplest way to organize code into logical units.
- **Package:** A directory that contains multiple modules and a special `__init__.py` file. It allows you to structure a complex application's modules in a directory hierarchy.
- **Purpose:** They help in organizing code, promoting reusability, and preventing naming conflicts in large projects.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Modules
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Understanding Modules")
    display_note("A module is a single `.py` file containing functions, classes, and variables. Let's imagine we have the following file structure:", "example")
    display_note("""
project/
├── main.py
└── string_utils.py
    """, "info")

    print_sub_heading("2) Creating and Importing a Module")
    display_note("You use the `import` keyword to access the code from another module.")
    show_code_with_output('''# File: string_utils.py
# This module contains string utility functions.
def shout(text):
    return text.upper() + "!"

# File: main.py
import string_utils

message = string_utils.shout("hello world") 
print(message)'''
,
"HELLO WORLD!")

    print_sub_heading("3) The `from...import` Statement")
    display_note("This allows you to import specific functions or classes directly into the current namespace, so you don't have to prefix them with the module name.")
    show_code_with_output('''# File: string_utils.py remains the same.
# File: main.py
from string_utils import shout

# No need for 'string_utils.' prefix now 
message = shout("this is convenient")
print(message)'''
,
"THIS IS CONVENIENT!")

    print_sub_heading("4) Using an Alias with `as`")
    display_note("You can rename a module during import, which is useful for avoiding name conflicts or shortening long module names.")
    show_code_with_output('''# File: string_utils.py remains the same.
# File: main.py
import string_utils as su

message = su.shout("aliases are cool") 
print(message)'''
,
"ALIASES ARE COOL!")

    print_sub_heading("5) The `__name__` Special Variable")
    display_note("Every module has a special variable `__name__`. When the module is run directly, `__name__` is set to `'__main__'`. When it's imported, `__name__` is set to the module's filename.")
    display_note("This allows you to write code that only runs when the file is executed as a script, not when it's imported.", "tip")
    show_code_with_output('''# File: string_utils.py
def shout(text):
    return text.upper() + "!"

# This block will only run if string_utils.py is executed directly
if __name__ == "__main__":
    print("This module is being run directly.")
    print(shout("testing"))

# --- Output when running 'python string_utils.py' ---'''
,
'''This module is being run directly.
TESTING!''')

    show_code_with_output('''# File: main.py
import string_utils

print("Importing string_utils from main.py")
print(string_utils.shout("imported"))

# --- Output when running 'python main.py' ---
# Notice the test block from string_utils.py does NOT run.'''
,
'''Importing string_utils from main.py
IMPORTED!''')
    

if __name__ == "__main__":
    main()

