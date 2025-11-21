from helpers.display_utils import *

def main(topic_number: int):
    print_heading("functools Module in Python", topic_number)

    imp_note_points("""
**functools:**  
*A powerful standard library module for higher-order functions and decorators.*  
*Key use: Enable, simplify, and optimize function wrapping, caching, partial evaluation, and more.*  

**Most useful functionalities:**  
- Caching/memoization with @lru_cache (and @cache in Python 3.9+)  
- Preserving function metadata in decorators with @wraps  
- Partial function application with partial()  
- Reducing iterables with reduce()  
- Enforcing total comparison ordering with @total_ordering""")

    # -------------------------------------------------------------------------------
    # 1. functools.lru_cache / functools.cache
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Caching Results: @lru_cache and @cache")
    display_note("Caches function results for given arguments (keyed by input), speeding up repeated calls, great for recursion or expensive computations.", "tip")
    display_note("Since Python 3.9, you can also use @cache for unlimited-size caching.", "example")
    code1 ='''
import time
from functools import lru_cache

# Without caching
def fib_plain(n):
    if n < 2:
        return n
    return fib_plain(n - 1) + fib_plain(n - 2)

# With caching
@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

# Measure plain
start = time.time()
fib_plain(40)
plain_time = time.time() - start

# Measure cached
start = time.time()
fib_cached(40)
cached_time = time.time() - start

print(f"Time taken by plain factorial function:  {plain_time:.6f} seconds")
print(f"Time taken by cached factorial function: {cached_time:.6f} seconds")
#---------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -------------------------------------------------------------------------------
    # 2. functools.wraps
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Preserving Metadata: @wraps")
    display_note("Ensures that decorated functions keep their original name, docstring, and signature, crucial for debug and documentation.", "warning")
    code2 ='''
from functools import wraps

def my_decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@my_decorator1
def greet1():
    "Says hello"
    print("Hello!")

@my_decorator2
def greet2():
    "Says hello"
    print("Hello!")

print("function greet1() details:")
print(greet1.__name__)
print(greet1.__doc__)

print("\\nfunction greet2() details:")
print(greet2.__name__)
print(greet2.__doc__)
#----------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -------------------------------------------------------------------------------
    # 3. functools.partial
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Creating Partial Functions: partial()")
    display_note("""Creates a new version of a function with some arguments pre-filled.
Great for callbacks or functional programming patterns.""", "info")
    code3 ='''
from functools import partial
                          
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("Printing square of numbers from 1 to 5:", end=" ")
for i in range(6):
    print(square(i), end=", ")

print("\\nPrinting cube of 2, 6, 9:", end=" ")
print(cube(2), end=", ")   # 8
print(cube(6), end=", ")   # 216
print(cube(9)) 
#--------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------
    # 4. functools.reduce
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Reducing Iterables: reduce()")
    display_note("""Reduces an iterable to a single value by successively applying a binary function. Typical use: sum, product, or combining items accumulatively.
Syntax: `reduce(func, iterable[, initial]`""")
    imp_note_points('''WORKFLOW
Input List: [1, 2, 3, 4, 5]  
Step-by-step Execution of: reduce(add, [1, 2, 3, 4, 5])                               
***........................................................................  
:   ┌──────┐                                                           :  
:   │Start │─────→  1, 2,     3,     4,     5                          :  
:   └──────┘                                                           :  
:                   ┬  ┬      ┬      ┬      ┬                          :  
:                  a│  │b     │      │      │                          :  
:                   ↓  ↓      │      │      │                          :  
:               add(1, 2)→ 3  │      │      │                          :  
:                          ┬  │      │      │                          :  
:                         a│  │b     │      │                          :  
:                          ↓  ↓      │      │                          :  
:                      add(3, 3)→ 6  │      │                          :  
:                                 ┬  │      │                          :  
:                                a│  │b     │                          :  
:                                 ↓  ↓      │                          :  
:                             add(6, 4)→ 10 │                          :  
:                                        ┬  │                          :  
:                                       a│  │b                         :  
:                                        ↓  ↓             ┌──────┐     :  
:                                   add(10, 5)→ 15 ──────→│ End  │     :  
:                                                         └──────┘     :  
........................................................................***  ''')
    code4 ='''
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
#------------------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -------------------------------------------------------------------------------
    # 5. functools.total_ordering
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Automatic Ordering: @total_ordering")
    display_note("@total_ordering auto-generates the rest of rich comparison methods (`__le__`, `__gt__`, etc.), if just `__eq__` and one other are defined; reduces boilerplate for sortable classes.")
    code5 ='''
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

    def __lt__(self, other):
        return self.roll < other.roll

a = Student('Alice', 1)
b = Student('Bob', 3)
print(f"a < b: {a < b}")     # True
print(f"a >= b: {a >= b}")   # False (auto-generated)
#----------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -------------------------------------------------------------------------------
    # 6. Bonus: functools.singledispatch
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Generic Functions: @singledispatch")
    display_note("@singledispatch turns a function into a generic function that dispatches to registered implementations depending on the type of the first argument.")
    code6 ='''
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
#---------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    imp_note_points("""
**Summary of functools:**  
- Use for advanced decorator writing, caching, generic functions, partial application, and custom ordering.
- Most decorators (wraps, lru_cache, cache, singledispatch, total_ordering) are highly practical and widely used in Pythonic code.""")

if __name__ == "__main__":
    main(1)
