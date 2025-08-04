from helpers.display_utils import *

def main():
    print_heading("Chaining Decorators in Python (Deep Dive)")

    imp_note_points("""
**Chaining Decorators:**  
*Applying multiple decorators to a function or method. Allows you to wrap a function with several layers of behavior (logging, timing, validation, etc.)*  
- *They’re applied from the closest to the function outward.*  
- *The order matters: `@d1`, then `@d2` means `f = d1(d2(f))`!*  
- *Used for building complex, reusable compositions elegantly.*  
""")

    # -------------------------------------------------------------------------------
    # 1. Basic Chaining: Two Decorators
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Basic Example: Two Decorators")
    display_note("Decorators are applied from bottom upward. The one closest to the function is innermost (wraps first).", "info")
    show_code_with_output('''# Two Decorators
def deco_one(func):
    def wrapper(*args, **kwargs):
        print("deco_one: before")
        result = func(*args, **kwargs)
        print("deco_one: after")
        return result
    return wrapper

def deco_two(func):
    def wrapper(*args, **kwargs):
        print("deco_two: before")
        result = func(*args, **kwargs)
        print("deco_two: after")
        return result
    return wrapper

@deco_one
@deco_two
def greet():
    print("Hello!")

greet()
'''
,
'''deco_one: before
deco_two: before
Hello!
deco_two: after
deco_one: after'''
    )
    display_note("First, `deco_two` wraps `greet()`, then `deco_one` wraps that result. Innermost to outermost: greet → deco_two → deco_one.", "tip")

    # -------------------------------------------------------------------------------
    # 2. Chaining with Arguments, Return Values, and Execution Order
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Chaining Decorators (with Args/Return, Order Demo)")
    display_note("Each decorator receives the function returned by the next one below it.", "warning")
    display_note("All wrappers typically pass through *args/**kwargs, and can also manipulate output.", "warning", message_continue=True)
    show_code_with_output('''# With Args/Return, Order Demo
def star(func):
    def wrapper(*args, **kwargs):
        print("*****")
        return func(*args, **kwargs)
    return wrapper

def plus(func):
    def wrapper(*args, **kwargs):
        print("+++++")
        result = func(*args, **kwargs)
        print("+++++")
        return result
    return wrapper

def dash(func):
    def wrapper(*args, **kwargs):
        print("-----")
        result = func(*args, **kwargs)
        print("-----")
        return result
    return wrapper

@star
@plus
@dash
def message(msg):
    print(msg)

message("Decorators chain!")
'''
,
'''*****
+++++
-----
Decorators chain!
-----
+++++'''
    )
    display_note("Order: @dash (innermost), then @plus, then @star (outermost). So output is: star → plus → dash → [function body] → dash → plus → star.", "example")

    # -------------------------------------------------------------------------------
    # 3. Chaining with Parameterized (Args) Decorators
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Chaining Parameterized Decorators")
    display_note("Even decorators with their own arguments (parameterized) can be chained, but each must add another level of function nesting.", "info")
    show_code_with_output('''# Chaining with Parameterized (Args) Decorators
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

def surround(char):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(char * 10)
            func(*args, **kwargs)
            print(char * 10)
        return wrapper
    return decorator

@repeat(3)
@surround("#")
def hello():
    print("Hi!")

hello()
'''
,
'''Run 1:
##########
Hi!
##########
Run 2:
##########
Hi!
##########
Run 3:
##########
Hi!
##########'''
    )

    # -------------------------------------------------------------------------------
    # 4. Practical: Logging, Timing, and Validation Together
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Real World: Logging, Timing, Checking in a Chain")
    show_code_with_output('''import time
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        t1 = time.time()
        print(f"[TIME] {func.__name__} took {t1-t0:.4f}s")
        return res
    return wrapper

def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x < 0:
            raise ValueError("Must be non-negative")
        return func(x)
    return wrapper

@log
@timer
@validate_positive
def factorial(x):
    time.sleep(0.1)
    return 1 if x==0 else x*factorial(x-1)

print(factorial(4))
'''
,
'''[LOG] Calling factorial
[TIME] factorial took 0.4050s
24'''
    )

    imp_note_points("""**Key Insights:**  
- Decorators always apply inside–out, top to bottom.  
- Good design: each decorator should call and return the next layer, never break the chain.  
- Use @functools.wraps on wrappers to keep function meta-info for all chains!
- Complex behaviors can be built up via composition, not inheritance.""")

if __name__ == "__main__":
    main()
