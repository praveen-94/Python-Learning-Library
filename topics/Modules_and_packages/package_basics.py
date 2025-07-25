# modules_and_packages.py

from helpers.display_utils import *

def main():
    print_heading("Packages in Python")
    imp_note_points("""
- **Module:** Any Python file (`.py`) is a module. It's the simplest way to organize code into logical units.
- **Package:** A directory that contains multiple modules and a special `__init__.py` file. It allows you to structure a complex application's modules in a directory hierarchy.
- **Purpose:** They help in organizing code, promoting reusability, and preventing naming conflicts in large projects.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Packages
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Understanding Packages")
    display_note("A package is a way to structure Python’s module namespace by using 'dotted module names'. Let's imagine a more complex file structure:", "example")
    display_note("""
project/
├── main.py
└── my_app/
    ├── __init__.py
    ├── math_ops.py
    └── text_ops/
        ├── __init__.py
        └── formatting.py
    """, "info")
    display_note("The `__init__.py` files are essential. They can be empty, but they tell Python that the directory should be treated as a package.", "warning")

    print_sub_heading("2) Importing from a Package")
    display_note("You use dot notation to navigate the package hierarchy.")
    show_code_with_output('''# File: my_app/math_ops.py
def add(a, b):
    return a + b

# File: main.py
from my_app import math_ops

result = math_ops.add(10, 5)
print(f"Result: {result}")'''
,
"Result: 15")

    print_sub_heading("3) Importing from a Sub-package")
    show_code_with_output('''# File: my_app/text_ops/formatting.py
def stylish_title(text):
    return f"--- {text.title()} ---"

# File: main.py
from my_app.text_ops import formatting

title = formatting.stylish_title("my awesome title")
print(title)'''
,
"--- My Awesome Title ---")

    print_sub_heading("4) The Role of `__init__.py`")
    display_note("`__init__.py` can also be used to make imports more convenient. You can import modules at the package level to expose them to the user.", "tip")
    display_note("Let's modify `my_app/__init__.py` to simplify our imports.")
    show_code_with_output('''# File: my_app/__init__.py
# By adding this line, 'add' is available directly from the 'my_app' package.
from .math_ops import add

# File: main.py
# Now we can import 'add' directly from 'my_app'
from my_app import add

result = add(100, 25)
print(f"Simplified import result: {result}")''',
"Simplified import result: 125")


if __name__ == "__main__":
    main()