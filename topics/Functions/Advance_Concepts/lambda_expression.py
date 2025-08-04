from helpers.display_utils import *

def main():
    print_heading("Lambda Expressions and Related Topics in Python")

    imp_note_points("""
**Lambda Expressions:**
- *A lambda expression is a way to create simple, short, anonymous (nameless) functions on the fly using the keyword `lambda`.*
- *Syntax: `lambda arguments: expression`— only a single expression (no statements!)*
- *Lambdas are used especially where a function is needed for a short period, often as arguments to higher-order functions (like `map`, `filter`, `sorted`).* """)

    # -------------------------------------------------------------------------------
    # 1. Lambda Basics: Syntax & Simple Use
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Lambda Expression Syntax & Basics")
    display_note("`lambda` creates a function object just like `def`, but with no name, no return, and only one expression in the body.", "info")
    show_code_with_output("""# Lambda assigned to variable (like any function)
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Immediately invoked lambda (rare)
print((lambda x: x + 1)(10))  # 11
""",
"""
25
7
11
""")

    display_note("Use parentheses when calling a lambda 'directly' because it is anonymous.")
    display_note("Lambdas can be assigned to variables or passed inline as arguments.")

    # -------------------------------------------------------------------------------
    # 2. Lambda vs Regular Functions
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Lambda vs Regular Functions")
    show_code_with_output("""
def add_def(x, y):
    return x + y

add_lambda = lambda x, y: x + y

print(add_def(2, 3))       # 5
print(add_lambda(2, 3))    # 5
"""
,
"""
5
5
""")
    display_note("Lambda functions can't have statements (like assignments or loops) or docstrings, but regular functions can.", "warning")
    display_note("Use def for more complex logic.", "warning", message_continue=True)

    # -------------------------------------------------------------------------------
    # 3. Lambda with map(), filter(), reduce(): Real Use Cases
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Lambda Expressions With map(), filter(), reduce()")
    display_note("The classic use: pass a lambda (as a short 'throwaway' function) into a higher-order function—", "example")
    display_note("no need to define a separate function.", "example", message_continue=True)
    show_code_with_output("""
nums = [1, 2, 3, 4, 5]

# map: apply function to each
doubles = list(map(lambda x: x * 2, nums))
print(doubles)  # [2, 4, 6, 8, 10]

# filter: keep only if function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)    # [2, 4]

# reduce: accumulate result, needs functools
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120
"""
,
"""
[2, 4, 6, 8, 10]
[2, 4]
120
""")

    # -------------------------------------------------------------------------------
    # 4. Lambda in Sorting, Key Functions (sorted, min, max)
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Lambda for Custom Sorting and Key-Functions")
    display_note("You can use a lambda as the `key` argument in functions like `sorted`, `min`, `max` for custom sorting/extracting.", "info")
    show_code_with_output("""
words = ['pear', 'apple', 'banana', 'kiwi']
by_len = sorted(words, key=lambda w: len(w))
print(by_len)  # ['kiwi', 'pear', 'apple', 'banana']

points = [(2, 3), (1, 5), (5, 1)]
by_y = sorted(points, key=lambda t: t[1])
print(by_y)    # [(5, 1), (2, 3), (1, 5)]
"""
,
"""
['kiwi', 'pear', 'apple', 'banana']
[(5, 1), (2, 3), (1, 5)]
""")

    # -------------------------------------------------------------------------------
    # 5. Lambda as Return Value ("Function Factory")
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Lambda Returning Functions (Function Factories)")
    display_note("You can return a lambda (or any function) from a function to create specialized behaviors on demand.", "tip")
    show_code_with_output("""
def power_factory(n):
    return lambda x: x ** n

square = power_factory(2)
cube = power_factory(3)
print(square(4), cube(4))  # 16 64
"""
,
"""
16 64
""")

    # -------------------------------------------------------------------------------
    # 6. Lambda, Closures, and "Late Binding" Gotcha
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Lambda Closures & The 'Late Binding' Trap")
    display_note("Be careful: lambdas (like all closures in Python) capture variables by reference, not value!", "warning")
    show_code_with_output("""
funcs = []
for n in range(3):
    funcs.append(lambda: n)
for f in funcs:
    print(f(), end=' ')  # careful! All print 2 (not 0 1 2)
print()

# The correct way: bind the default at definition time
funcs = []
for n in range(3):
    funcs.append(lambda n=n: n)
for f in funcs:
    print(f(), end=' ')  # prints 0 1 2
print()
"""
,
"""
2 2 2 
0 1 2 
""")

    # -------------------------------------------------------------------------------
    # 7. Limitations and Best Practice
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Limitations & Best Practices")
    imp_note_points("""- Lambdas can only have a single expression — *no* statements (e.g., no assignments, no loops, no try-except).
- Lambdas have no name (their __name__ is '<lambda>'), so they're not as good for debugging or introspection.
- Use lambda for short, simple functions passed as arguments. For anything bigger or used repeatedly, prefer `def`.""")

    # -------------------------------------------------------------------------------
    # 8. Related/Advanced: Lambda with sorted, zip, GUI, and functools
    # -------------------------------------------------------------------------------
    print_sub_heading("8. Advanced/Related Use Cases")
    display_note("Lambda can be handy in GUIs (event callbacks), dataframes (pandas DataFrame.apply), ", "info")
    display_note("and custom iterators, or as a generator expression's key.","info", message_continue=True)
    show_code_with_output("""
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_by_name = sorted(pairs, key=lambda x: x[1])
print(sorted_by_name)  # [(1, 'one'), (3, 'three'), (2, 'two')]

# In Pandas, you'd use df['col'].apply(lambda x: some_transform(x))
"""
,
"""
[(1, 'one'), (3, 'three'), (2, 'two')]
""")

    imp_note_points("""
**Summary:**
- Lambda functions are a core tool for concise, throwaway logic.
- Most useful with `map`, `filter`, `reduce`, `sorted`, and as short callbacks.
- Prefer regular `def` for anything that needs clarity, documentation, or multiple statements.""")

if __name__ == "__main__":
    main()
