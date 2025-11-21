# modules_and_packages.py

from helpers.display_utils import *
import os

def main(topic_number: int):
    print_heading("Modules in Python", topic_number)
    imp_note_points("""
- **Module:** Any Python file ***(.py)*** is a module. It's the simplest way to organize code into logical units.
- **Package:** A directory that contains multiple modules and a special ***'__init__.py'*** file. It allows you to structure a complex application's modules in a directory hierarchy.
- **Purpose:** They help in organizing code, promoting reusability, and preventing naming conflicts in large projects.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Modules
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Understanding Modules")
    imp_note_points("""A module is a single ___.py___ file containing functions, classes, and variables.  
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
    
    #----------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Creating and Importing a Module")
    display_note("You use the `import` keyword to access the code from another module.")
    code1 = '''# sample code
import os

# Write the module code and create a module
module_file = os.path.join("tests/output_dump", "example_module2.py")
module_code = """
def shout(text):
    print("Original text:", text)
    print("Text after convering it to uppercase:", text.upper() + "!")
"""
with open(module_file, "w") as f:
    f.write(module_code)

# File: example_module2.py
import tests.output_dump.example_module2
tests.output_dump.example_module2.shout("hello world")
#------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    #----------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3) Using an Alias with `as`")
    display_note("You can rename a module during import, which is useful for avoiding name conflicts or shortening long module names.")
    code3 = '''# File: example_module2.py remains the same.
import tests.output_dump.example_module2 as text_convert
text_convert.shout("aliases are cool") 
#-------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #----------------------------------------------------------------------------------------------------------------
    print_sub_heading("4) The `from...import` Statement")
    display_note("This allows you to import specific functions or classes directly into the current namespace, so you don't have to prefix them with the module name.")
    code2 = '''# File: example_module2.py remains the same.
from tests.output_dump.example_module2 import shout
# No need for 'example_module.' prefix now 
shout("this is convenient")
#---------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    #-----------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5) The `__name__` Special Variable")
    display_note("Every module has a special variable `__name__`. When the module is run directly, `__name__` is set to `'__main__'`, When it's imported, `__name__` is set to the module's filename.")
    display_note("This allows you to write code that only runs when the file is executed as a script, not when it's imported.", "tip")
    code4 = '''# File: example_module2.py  
import os 

# adding __name__ to example2.py file
add_main = """                       
if __name__ == "__main__":
    print("This module is being run directly.")
    shout("testing")
"""
module_file = os.path.join("tests/output_dump", "example_module2.py")
with open(module_file, "a") as f:
    f.write(add_main)

# This will now also run if example_module2.py is executed directly
# Running directly
print("running example_module.py directly i.e. without importing......")
import subprocess
result = subprocess.run(["python", "tests/output_dump/example_module2.py"], capture_output=True, text=True)
print(result.stdout)

# Now running by importing, Notice the test block from example_module.py, it does NOT run.
import tests.output_dump.example_module2
print("Importing example_module and then running")
tests.output_dump.example_module2.shout("imported")
#------------------------------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

if __name__ == "__main__":
    main(1)

