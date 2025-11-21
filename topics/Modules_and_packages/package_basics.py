# modules_and_packages.py

from helpers.display_utils import *
import shutil
import os
import sys

def main(topic_number: int):
    print_heading("Packages in Python", topic_number)
    imp_note_points("""
- **Module:** Any Python file ___(.py)___ is a module. It's the simplest way to organize code into logical units.
- **Package:** A directory that contains multiple modules and a special ***__init__.py*** file. It allows you to structure a complex application's modules in a directory hierarchy.
- **Purpose:** They help in organizing code, promoting reusability, and preventing naming conflicts in large projects.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Packages
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Understanding Packages")
    imp_note_points("""A package is a way to structure Python’s module namespace by using 'dotted module names'.  
Let's take a look to more complex file structure, our project structure:  

***pyCodeNotes/***  
***├── .venv/                # Virtual environment (excluded from Git)***  
***├── helpers/              # Reusable helper functions***  
***├── tests/                # Manual test scripts (optional)***  
***│   ├── output_dump/***              
***│   │   ├── example_module.py    # Example module for testing, created during script execution***  
***│   │   ├── sample_test_package/ # Example package for testing, created during script execution***  
***│   │   │    ├── __init__.py***  
***│   │   │    └── sub_example_module.py***  
***│   │   └── ...***               
***│   └── ...***   
***├── topics/               # Topic-wise Python scripts***  
***│   ├── Basic_Structure/***   
***│   ├── Functions/***  
***│   ├── File_Handling/***  
***│   ├── Modules_and_packages/***                   
***│   └── ...***  
***├── main.py               # entry point of project***  
***├── progress.md           # Markdown progress tracking***  
***├── requirements.txt      # Installed dependencies (if any)***  
***├── .gitignore            # Files/folders to ignore in version control***   
***|── README.md             # Project overview and instructions***  
***└── topics.json           # Contains name of topic, subtopic.. and their modules***  
    """, "Example")
    
    #-------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Importing from a Package")
    display_note("You use dot notation to navigate the package hierarchy.")
    code1 = '''# sample code
import os

# Step 1: Create package and module structure in helpers
# 'tests/output_dump' package is already there, so no need to create it

# Step 2: Write the module code
module_code = """
def sum_numbers(*args):
    return f" sum of numbers {args} is: {sum(args)}"
"""
module_file = os.path.join("tests/output_dump", "example_module1.py")
with open(module_file, "w") as f:
    f.write(module_code)

# Step 3: import the module
from tests.output_dump import example_module1

# Step 4: Use the function
print("Result:")
print(example_module1.sum_numbers(100, 25))
print(example_module1.sum_numbers(50, 75, 25))

#------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3) Importing from a Sub-package")
    code2 = '''# sample code
import os

# Step 1: Create package, subpackage and module structure
# 'tests/output_dump' package is already there, so no need to create it
# creating 'sample_test_package' subpackage
os.makedirs("tests/output_dump/sample_test_package", exist_ok=True)

# Step 2: Write the module code
module_code = """
def product_numbers(*args):
    product = 1
    for n in args:
        product *= n
    return f"Product of numbers {args} is: {product}"
"""
module_file = os.path.join("tests/output_dump/sample_test_package", "sub_example_module.py")
with open(module_file, "w") as f:
    f.write(module_code)


# File: sub_example_module.py
from tests.output_dump.sample_test_package import sub_example_module

result1 = sub_example_module.product_numbers(2, 4)
result2 = sub_example_module.product_numbers(2, 4, 6)

print("Result:")
print(result1)
print(result2)
#---------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)
 
    #----------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4) The Role of `__init__.py`")
    display_note("__init__.py file is also used to initialize the package and can contain package-level docstrings or code.")
    display_note("""`__init__.py` file is essential. 
It can be empty, but it tell Python that the directory should be treated as a package.""", "warning")
    display_note("""`__init__.py` can also be used to make imports more convenient,
You can import modules at the package level to expose them to the user.""", "tip")
    display_note("Let's add `tests/output_dump/sample_test_package/__init__.py` file to simplify our imports.", "example")
    code3 = '''# sample code
import os 

# By adding __init__.py file), 'product_numbers' is available directly from the 'sub_example_module' package.
module_file = os.path.join("tests/output_dump/sample_test_package", "__init__.py")
with open(module_file, "w") as f:
    f.write("")

# File: sub_example_module.py
# Now we can import 'product_numbers' directly from 'sub_example_module'
from tests.output_dump.sample_test_package.sub_example_module import product_numbers

result = product_numbers(100, 25)
print(f"Simplified import result: {result}")
#------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

if __name__ == "__main__":
    main(1)