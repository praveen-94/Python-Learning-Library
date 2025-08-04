from helpers.display_utils import *

def main():
    print_heading("functools Module in Python")

    imp_note_points("""
**functools:**  
*A powerful standard library module for higher-order functions and decorators.*  
*Key use: Enable, simplify, and optimize function wrapping, caching, partial evaluation, and more.*  

**Most useful functionalities:**  
- Caching/memoization with @lru_cache (and @cache in Python 3.9+)  
- Preserving function metadata in decorators with @wraps  
- Partial function application with partial()  
- Reducing iterables with reduce()  
- Enforcing total comparison ordering with @total_ordering  
    """)

    # -------------------------------------------------------------------------------
    # 1. functools.lru_cache / functools.cache
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Caching Results: @lru_cache and @cache")
    display_note("Caches function results for given arguments (keyed by input), speeding up repeated calls, ", "tip")
    display_note("great for recursion or expensive computations.", "tip", message_continue=True)
    show_code_with_output('''
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 55
'''
,
'''55''')

    display_note("Since Python 3.9, you can also use @cache for unlimited-size caching.", "example")

    # -------------------------------------------------------------------------------
    # 2. functools.wraps
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Preserving Metadata: @wraps")
    display_note("Ensures that decorated functions keep their original name, docstring, and signature, crucial for debug and documentation.", "warning")
    show_code_with_output('''
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    "Says hello"
    print("Hello!")

print(greet.__name__)
print(greet.__doc__)
'''
,
'''greet
Says hello''')

    # -------------------------------------------------------------------------------
    # 3. functools.partial
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Creating Partial Functions: partial()")
    display_note("Creates a new version of a function with some arguments pre-filled.", "info")
    display_note("Great for callbacks or functional programming patterns.", "info")
    show_code_with_output('''
from functools import partial
                          
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("Printing square of numbers from 1 to 5:")
for i in range(6):
    print(square(i), end=", ")

print("\n\nPrinting cube of 2, 6, 9: ")
print(cube(2), end=", ")   # 125
print(cube(6), end=", ")   # 125
print(cube(9)) 
'''
,
'''Printing square of numbers from 1 to 5:
0, 1, 4, 9, 16, 25,

Printing cube of 2, 6, 9:
8, 216, 729''')

    # -------------------------------------------------------------------------------
    # 4. functools.reduce
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Reducing Iterables: reduce()")
    display_note("Reduces an iterable to a single value by successively applying a binary function. ")
    display_note("Typical use: sum, product, or combining items accumulatively.", message_continue=True)
    display_note("Syntax: `reduce(func, iterable[, initial]`")
    imp_note_points('''WORKFLOW
Input List: [1, 2, 3, 4, 5]  
Step-by-step Execution of: reduce(add, [1, 2, 3, 4, 5])                               
`┌──────┐                                                       `  
`│Start │─────→  1, 2,     3,     4,     5                      `  
`└──────┘        ┬  ┬      ┬      ┬      ┬                      `  
`               a│  │b     │      │      │                      `  
`                ↓  ↓      │      │      │                      `  
`            add(1, 2)→ 3  │      │      │                      `  
`                       ┬  │      │      │                      `  
`                      a│  │b     │      │                      `  
`                       ↓  ↓      │      │                      `  
`                   add(3, 3)→ 6  │      │                      `  
`                              ┬  │      │                      `  
`                             a│  │b     │                      `  
`                              ↓  ↓      |                      `  
`                          add(6, 4)→ 10 │                      `  
`                                     ┬  │                      `  
`                                    a│  │b                     `  
`                                     ↓  ↓             ┌──────┐ `  
`                                add(10, 5)→ 15 ──────→│ End  │ `  
`                                                      └──────┘ `  
''')
    show_code_with_output('''from functools import reduce
from functools import reduce

nums = [1, 2, 3, 4]

def sum(a, b):
    return a+b
                          
list_sum1 = reduce(sum, nums)
list_sum2 = reduce(sum, nums, 10)  # taking initial value 10
list_product = reduce(lambda x, y: x * y, nums) # we can also use lambda
print(f"sum of list {nums} using reduce(): {list_sum1}")
print(f"sum of list {nums} using reduce() with initial value 10: {list_sum2}")
print(f"product of list {nums} using reduce(): {list_product}")
'''
,
'''
sum of list [1, 2, 3, 4] using reduce(): 10
sum of list [1, 2, 3, 4] using reduce() with initial value 10: 20
product of list [1, 2, 3, 4] using reduce(): 24
''')

    # -------------------------------------------------------------------------------
    # 5. functools.total_ordering
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Automatic Ordering: @total_ordering")
    display_note("@total_ordering auto-generates the rest of rich comparison methods (`__le__`, `__gt__`, etc.) ")
    display_note("if just `__eq__` and one other are defined; reduces boilerplate for sortable classes.", message_continue=True)
    show_code_with_output('''from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

    def __lt__(self, other):
        

a = Student('Alice', 1)
b = Student('Bob', 3)
print(a < b)     # True
print(a >= b)    # False (auto-generated)
'''
,
'''
True
False
''')

    # -------------------------------------------------------------------------------
    # 6. Bonus: functools.singledispatch
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Generic Functions: @singledispatch")
    display_note("@singledispatch turns a function into a generic function ")
    display_note("that dispatches to registered implementations depending on the type of the first argument.", message_continue=True)
    show_code_with_output('''
from functools import singledispatch

@singledispatch
def fun(arg):
    print("default", arg)

@fun.register(int)
def _(arg):
    print("int", arg)

@fun.register(str)
def _(arg):
    print("str", arg)

fun(10)
fun("hello")
fun([1,2,3])
'''
,
'''
int 10
str hello
default [1, 2, 3]
''')

    imp_note_points("""
**Summary of functools:**  
- Use for advanced decorator writing, caching, generic functions, partial application, and custom ordering.
- Most decorators (wraps, lru_cache, cache, singledispatch, total_ordering) are highly practical and widely used in Pythonic code.
    """)

if __name__ == "__main__":
    main()
