from helpers.display_utils import *
    
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print_heading("Example of Functions")
    imp_note_points('''IMPORTANT POINTS
- Functions in Python are defined using the `def` keyword, and they can take parameters and return values.
- Functions help organize code into reusable blocks.
- we can pass argumnet to function by two ways, pass by value and pass by reference.
- In Python, all arguments are passed by reference, but immutable types (like integers, strings, tuple) behave like pass by value.'''
    )

    # 1) Function without parameters and return value
    print_sub_heading("1) Function without parameters and return value")
    show_code_with_output('''# a simple function
def greet():
    print("Hello, World!")
greet()  # Calling the function''' 
,
"Hello, World!"
    )

    # 2) Function with parameters and return value
    print_sub_heading("2) Function with parameters and return value")
    input_a, input_b = 10, 20 #input("Enter first and second number separated by space to add: ").split()
    show_code_with_output('''# function with parameters
def add(a, b):
    return a + b

input_a, input_b = 10, 20                    
result = add(int(input_a), int(input_b)) 
print(f"The sum of {input_a} and {input_b} is: {result}")'''
,
"The sum of " + str(input_a) +  " and " + str(input_b) + " is: " + str(input_a+input_b)
    )

    # 3) Function with default parameters
    print_sub_heading("3) Function with default parameters")
    display_note("Default parameters allow you to call a function without explicitly passing all arguments.")
    display_note("In this ex, if no name is provided to `greet_user()`, it uses the default value 'Guest'.", "example")
    show_code_with_output('''# function with default parameter
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

print("Calling greet_user() with default parameter", end=": ")
greet_user()
print("Calling greet_user() with custom 'Alice' parameter", end=": ") 
greet_user("Alice")'''
,
"Calling greet_user() with default parameter: Hello, Guest!\nCalling greet_user() with custom 'Alice' parameter: Hello, Alice!"
    )

    # 4) Function with variable-length arguments
    print_sub_heading("4) Function with variable-length arguments")
    display_note("The `*args` syntax allows a function to accept any number of positional arguments.")
    display_note("In this ex, user input is split into a list and unpacked using `*args` during the function call.","example")
    show_code_with_output('''# function with variable length arguments
def sum_numbers(*args):
    sum=0
    for number in args:
        sum+=number
    print("Sum of numbers", args, "is:", sum)
print("Calling print_numbers() with variable-length arguments:") 
sum_numbers(12,34)
sum_numbers(1,2,3,4) 
sum_numbers(2,4,6,8,10,12)'''
,
"Calling print_numbers() with variable-length arguments:" + "\n" +
"Sum of numbers (12, 34) is: 46" + "\n" +
"Sum of numbers (1, 2, 3, 4) is: 10" + "\n" +
"Sum of numbers (2, 4, 6, 8, 10, 12) is: 42"
    )

    # 5) function with keyword arguments
    print_sub_heading("5) Function with keyword arguments")
    display_note("Keyword arguments allow you to pass arguments to a function using the parameter names explicitly.")
    display_note("This improves readability and allows parameters to be passed in any order.")
    show_code_with_output('''# function with keyword arguments
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

print("Calling print_info() with keyword arguments:")
print_info(name="Alice", age=30, city="New York")  # Using keyword arguments
print_info(age=30, name="Alice", city="New York")  # Using keyword arguments but different order '''
,
"Calling print_info() with keyword arguments:\nName: Alice, Age: 30, City: New York\nName: Alice, Age: 30, City: New York"
    )

    # 6) function with *kwarg
    print_sub_heading("6) Function with *kwargs")
    display_note("Using **kwargs allows a function to accept any number of keyword arguments as a dictionary.")
    display_note("You can iterate through the dictionary using a for loop to access both keys and values.")
    display_note("This provides flexibility when passing dynamic named data to functions.")
    show_code_with_output('''# function with *kwarg
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=", ")
    print()

print("Calling print_details() with keyword arguments:")
print_details(name="Alice", age=30, city="New York", occupation="Engineer")
print_details(name="Bob", age=25, city="Los Angeles", occupation="Designer", hobby="Photography") '''
,
"""Calling print_details() with keyword arguments:
name: Alice, age: 30, city: New York, occupation: Engineer, 
name: Bob, age: 25, city: Los Angeles, occupation: Designer, hobby: Photography, """
    )

    # 7) Lambda function
    print_sub_heading("7) Lambda function")
    display_note("Lambda functions are anonymous functions defined using the `lambda` keyword.")
    display_note("They are typically used for short, throwaway functions without formally defining them using `def`.")
    show_code_with_output('''# Lambda function
square = lambda x: x * x
print("Calling lambda function to calculate square of 5:") 
print(f"The square of 5 is: {square(5)}")'''
,
"Calling lambda function to calculate square of 5:\nThe square of 5 is: 25"
    )

    # 8) function with annotations
    print_sub_heading("8) Function with annotations")
    display_note("Function annotations are a way to attach metadata (like expected types) to function parameters and return values.")
    display_note("These annotations do not enforce type checking at runtime— they're mainly used for documentation, IDE support, ")
    display_note("and static analysis tools.", message_continue=True)
    show_code_with_output('''# function with annotations
def multiply(a: int, b: int) -> int:
    return a * b

print("Calling multiply() function with annotations:") 
result = multiply(3, 4)
print(f"The result of multiplication is: {result}")'''
,
"Calling multiply() function with annotations:\nThe result of multiplication is: 12"
    )

    # 9) Recursive function
    print_sub_heading("9) Recursive function")
    display_note("A recursive function is one that calls itself to solve a smaller subproblem.")
    display_note("The factorial of a number `n` is calculated as `n * (n-1) * (n-2) * ... * 1`.")
    display_note("Always include a base case (`n == 0 or 1`) to prevent infinite recursion.")
    show_code_with_output('''# Recursive function
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Calling factorial() function with recursion:") 
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")'''
,
"Calling factorial() function with recursion:\nThe factorial of 5 is: 120"
    )

    # 10) Function with docstring
    print_sub_heading("10) Function with docstring")
    display_note("The docstring is a multi-line string that describes the function's purpose, parameters, and return value.")
    display_note("Docstrings are used to document how a function should be used. They can be accessed at runtime using the `__doc__` attribute.")
    show_code_with_output('''Function with docstring
def power(base, exponent):
    """
    _______________________________________________________
    | Calculate the power of a number.                    |
    |                                                     |
    | Parameters:                                         |
    | base (int): The base number.                        |
    | exponent (int): The exponent to raise the base to.  |
    |                                                     |
    | Returns:                                            | 
    | int: The result of base raised to the exponent.     |
    |_____________________________________________________|
    """
    return base ** exponent

print("Calling power() function with docstring", end=": ")
print(power(2, 3))  # Output: 8

print("Docstring of power function:", power.__doc__)'''
,
"""Calling power() function with docstring: 8
Docstring of power function: 
    _______________________________________________________
    | Calculate the power of a number.                    |
    |                                                     |
    | Parameters:                                         |
    | base (int): The base number.                        |
    | exponent (int): The exponent to raise the base to.  |
    |                                                     |
    | Returns:                                            |
    | int: The result of base raised to the exponent.     |
    |_____________________________________________________|"""
    )

