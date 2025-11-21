from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Basic Variable Concepts", topic_number)

    #Basic Variable Concepts -----------------------------
    print_sub_heading("Understanding Variables in Python")
    display_note("""A variable is a named container used to store data, You can assign different types of values to variables without declaring their type explicitly.
Python is dynamically typed — the type is inferred from the value.""")
    code1 = '''# Variable assignment
x = 10
name = "Alice"

# Reassigning variable
x = 20

# Printing variable values 
print(f"x = {x}")
print(f"name = {name}")
'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # Variable Scope Examples ---------------------------------------------------------------
    # Local Scope ----------------------------------------------------------
    print_sub_heading("1) Local Scope")
    display_note("A variable declared inside a function is in local scope and only accessible within that function.")
    code2 = '''# Local Scope
def local_example():
    message = "Hello from local scope"
    print(message)

local_example()
# print(message)  # Would raise NameError if uncommented 
#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # Global Scope ----------------------------------------------------------
    print_sub_heading("2) Global Scope")
    display_note("""A variable declared outside any function is in global scope and can be accessed inside functions.
You can read global variables inside a function without declaring them as global.""")
    code3 ='''# Global Scope
message = "Hello from global scope"
                          
def global_example():
    print(message)  # Accessing global variable 

global_example()
'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #-------------------------------------------------------------------------
    print_sub_heading("3) Modifying Global Variable from Inside Function")
    display_note("""To modify a global variable inside a function, you must declare it using the `global` keyword.
Without `global`, a new local variable would be created inside the function.""")
    code4 = '''# Modifying Global Variable from Inside Function
count = 0

def modify_global():
    global count
    count += 1
    print(f"Inside function, count = {count}") 

modify_global()
print(f"Outside function, count = {count}")
'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # ------------------------------------------------------------------------
    print_sub_heading("4) Enclosing (Nonlocal) Scope")
    display_note("""Variables in an enclosing (nonlocal) scope are accessible in nested functions.
Use `nonlocal` to modify variables from the outer (but non-global) scope inside a nested function.""")
    code5 = '''# Enclosing (Nonlocal) Scope
def outer():
    msg = "original"
    def inner():
        nonlocal msg
        msg = "modified by inner"
    inner()
    print(f"Message after inner call: {msg}") 

outer()
'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # ------------------------------------------------------------------------
    print_sub_heading("5) LEGB Rule Summary")
    display_note("""LEGB = Local → Enclosing → Global → Built-in — the order in which Python resolves variable names.
This example demonstrates all levels, but only 'local' is used when defined inside the function.""")
    code6 = '''
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Prints 'local' 
    inner()

outer()
'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)