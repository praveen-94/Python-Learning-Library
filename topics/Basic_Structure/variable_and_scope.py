from helpers.display_utils import *

def main():
    print_heading("Basic Variable Concepts" )

    #Basic Variable Concepts -----------------------------
    print_sub_heading("0) Understanding Variables in Python")
    display_note("A variable is a named container used to store data. ")
    display_note("You can assign different types of values to variables without declaring their type explicitly.", message_continue=True)
    display_note("Python is dynamically typed — the type is inferred from the value.")
    show_code_with_output('''# Variable assignment
x = 10
name = "Alice"

# Reassigning variable
x = 20

# Printing variable values
print(f"x = {x}")
print(f"name = {name}")
''',
"x = 20\nname = Alice")

    # Variable Scope Examples -----------------------------
    print_sub_heading("1) Local Scope")
    display_note("A variable declared inside a function is in local scope and only accessible within that function.")
    show_code_with_output('''# Local Scope
def local_example():
    message = "Hello from local scope"
    print(message)

local_example()
# print(message)  # Would raise NameError if uncommented'''
,
"Hello from local scope")

    # ------------------------------------------------------------------------

    print_sub_heading("2) Global Scope")
    display_note("A variable declared outside any function is in global scope and can be accessed inside functions.")
    display_note("You can read global variables inside a function without declaring them as global.")
    show_code_with_output('''# Global Scope
message = "Hello from global scope"
                          
def global_example():
    print(message)  # Accessing global variable

global_example()'''
,
"Hello from global scope")

    # ------------------------------------------------------------------------

    print_sub_heading("3) Modifying Global Variable from Inside Function")
    display_note("To modify a global variable inside a function, you must declare it using the `global` keyword.")
    display_note("Without `global`, a new local variable would be created inside the function.")
    show_code_with_output('''# Modifying Global Variable from Inside Function
count = 0

def modify_global():
    global count
    count += 1
    print(f"Inside function, count = {count}")

modify_global()
print(f"Outside function, count = {count}")'''
,
"Inside function, count = 1\nOutside function, count = 1")

    # ------------------------------------------------------------------------

    print_sub_heading("4) Enclosing (Nonlocal) Scope")
    display_note("Variables in an enclosing (nonlocal) scope are accessible in nested functions.")
    display_note("Use `nonlocal` to modify variables from the outer (but non-global) scope inside a nested function.")
    show_code_with_output('''# Enclosing (Nonlocal) Scope
def outer():
    msg = "original"
    def inner():
        nonlocal msg
        msg = "modified by inner"
    inner()
    print(f"Message after inner call: {msg}")

outer()'''
,
"Message after inner call: modified by inner")

    # ------------------------------------------------------------------------

    print_sub_heading("5) LEGB Rule Summary")
    display_note("LEGB = Local → Enclosing → Global → Built-in — the order in which Python resolves variable names.")
    display_note("This example demonstrates all levels, but only 'local' is used when defined inside the function.")
    show_code_with_output('''
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Prints 'local'
    inner()

outer()'''
,
"local")
