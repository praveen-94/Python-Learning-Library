from helpers.display_utils import *

def main():
    print_heading("Decorators in Python")
    
    imp_note_points("""
**Decorator:**  
*A function that takes another function as an arg, adds some functionality to it without changing the original function's code,*  
*and then returns the enhanced function.*  
*It is possible because in python functions are treated as object, and we can pass an object as argument in function.*  
*so we can pass a function to another function as an argument.*  

**Common and Practical Use Cases**  
*`Logging:`*  
    - *Automatically print a message when a function starts and ends, or log its arguments and return value.*  
    - *This is incredibly useful for debugging.*  
*`Timing/Performance:`*  
    - *Create a decorator that measures how long a function takes to execute.*  
    - *You can wrap any function with it to find performance bottlenecks in your code.*  
*`Authentication/Authorization:`*  
    - *In web frameworks (like Flask or Django), decorators are used to*  
    - *Check if a user is logged in before allowing them to access a specific page or function (e.g., @login_required).*  
*`Caching/Memoization:`*  
    - *For functions that perform expensive calculations, a decorator can store the result for a given set of inputs.*  
    - *If the function is called again with the same inputs, the decorator returns the cached result instead of re-running.*  
*`Data Validation:`*  
    - *A decorator can check the arguments passed to a function*  
    - *to ensure they are of the correct type or within a valid range before the function's logic is executed.*  
         
**Anatomy and Working Process of Decorator Function**  
*To work correctly, a decorator function generally has three parts:*  
_`The Outer Function:`_  
_- This is the decorator itself. It takes one argument: the function to be decorated (func)._  
_`The Inner "Wrapper" Function:`_  
_- Inside the decorator, you define another function (often called wrapper)._  
_- This is the function that contains the new functionality and also calls the original function._  
_- To be able to decorate any function, this wrapper must accept *args and **kwargs._  
_`The Return Statement:`_  
_- The outer decorator function returns the inner wrapper function._  
                
- _When you apply a decorator using @decorator_name above a function definition, Python executes this as:_  
_function = decorator_name(function)_  
- _At this moment, the outer function runs once, receiving the original function as its argument (func)._  
- _The outer function defines and returns the wrapper function object but does not execute it yet._  
- _The name of the original function is now bound to this returned wrapper function._  
- _When you call the decorated function, you are actually calling the wrapper._  
- _Inside the wrapper:_  
 -_You can place any custom code you want to execute before calling the original function._  
 -_Then you call the original function (func(*args, **kwargs)) with all its original arguments._  
 -_You can also add code to run after the original function finishes._  
 -_Finally, the wrapper returns the result of the original function call._  
- _This process effectively "wraps" the original function inside new behavior without modifying its code._""")
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Basic Function Decorator (Function Wrapping)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Basic Function Decorator")
    display_note("Decorators add code to a function before and/or after it runs, without changing that function's source code.", "info")
    show_code_with_output('''# basic Example 
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()'''
,
'''Before the function runs
Hello, World!
After the function runs''')

    display_note("`@my_decorator` is just syntactic sugar for: `greet = my_decorator(greet)`.", "tip")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Decorators With Arguments (`*args, **kwargs`)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Writing Universal Decorators (Handling Arguments)")
    display_note("To decorate any function (regardless of arguments), always use `*args` and `**kwargs`.", "warning")
    show_code_with_output('''# Handling Arguments
def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"\nCalling {func.__name__}...")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

@universal_decorator
def add(*args: int):
    sum=0
    for number in args:
        sum+=number
    print("Sum of numbers", args, "is:", sum)

@universal_decorator
def multiply(a: int,b: int):
    print(f"The multiply of {a} and {b} is {a * b}")
                          
add(5,6)
add(4,5,5,6)
multiply(2,6)'''
,
'''
Calling add...
Sum of numbers (5, 6) is: 11
Done!

Calling add...
Sum of numbers (4, 5, 5, 6) is: 20
Done!

Calling multiply...
The multiply of 2 and 6 is 12
Done!
''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Real-World Use Case: Timing a Function
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Real-World Example: Timing a Function")
    display_note("Decorators are perfect for code you want to apply to many functions, like timing or logging.", "example")
    show_code_with_output('''import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time elapsed: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Function complete.")

slow_function()'''
,
'''Function complete.
Time elapsed: 1.0000 seconds''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Parameterized Decorator (Decorator With Arguments)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Parameterized Decorator")
    display_note("Parameterized decorators are decorators that take their own arguments. They need an extra layer of function nesting.", "tip")
    show_code_with_output('''# Parameterized Decorator
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def wave(name):
    print(f"👋 Hello, {name}!")

wave("Alice")'''
,
'''👋 Hello, Alice!
👋 Hello, Alice!
👋 Hello, Alice!''')

if __name__ == "__main__":
    main()

    