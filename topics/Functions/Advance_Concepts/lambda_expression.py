from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Lambda Expressions and Related Topics in Python", topic_number)

    imp_note_points("""
**Lambda Expressions:**
- It is a way to create simple, short, anonymous (nameless) functions on the fly using the keyword ___lambda___.
- Syntax: ___lambda arguments: expression___— only a single expression (no statements!)
- Lambdas are used especially where a function is needed for a short period, often as arguments to higher-order functions___(like map, filter, sorted)___. 

**Summary:**
- Lambda functions are a core tool for concise, throwaway logic.
- Most useful with ___map, filter, reduce, sorted___, and as short callbacks.
- Prefer regular ___def___ for anything that needs clarity, documentation, or multiple statements.
    
**Limitations & Best Practices**
- Lambdas can only have a single expression— *no* statements (e.g., no assignments, no loops, no try-except).
- Lambdas have no name (their __name__ is 'lambda'), so they're not as good for debugging or introspection.
- Use lambda for short, simple functions passed as arguments. For anything bigger or used repeatedly, prefer ___def___.""")

    # -------------------------------------------------------------------------------
    # 1. Lambda Basics: Syntax & Simple Use
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Lambda Expression Syntax & Basics")
    display_note("""Use parentheses when calling a lambda 'directly' because it is anonymous.
Lambdas can be assigned to variables or passed inline as arguments.""")
    display_note("`lambda` creates a function object just like `def`, but with no name, no return, and only one expression in the body.", "info")
    code1 = """# Lambda assigned to variable (like any function)
square = lambda x: x ** 2
print(f"Square of 5 by lambda function: {square(5)}")  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"Sum of 3 and 4 by lambda function: {add(3, 4)}")  # 7

print("Immediately invoked lambda (rare) example:", end=" ")
print((lambda x: x + 1)(10))  # 11
#----------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -------------------------------------------------------------------------------
    # 2. Lambda vs Regular Functions
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Lambda vs Regular Functions")
    display_note("Lambda functions can't have statements (like assignments or loops) or docstrings, but regular functions can, Use def for more complex logic.", "warning")
    code2 = """
def add_def(x, y):
    return x + y

add_lambda = lambda x, y: x + y

print(f"Sum of 2 and 3 by regular function: {add_def(2, 3)}")      # 5
print(f"Sum of 2 and 3 by lambda function: {add_lambda(2, 3)}")    # 5
#--------------------------------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -------------------------------------------------------------------------------
    # 3. Lambda with map(), filter(), reduce(): Real Use Cases
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Lambda Expressions With map(), filter(), reduce()")
    display_note("The classic use: pass a lambda (as a short 'throwaway' function) into a higher-order function— no need to define a separate function.", "example")
    code3 = """
nums = [1, 2, 3, 4, 5]
print(f"Original list: {nums}")

# map: apply function to each
doubles = list(map(lambda x: x * 2, nums))
print(f"doubles of list by lambda and map: {doubles}") 

# filter: keep only if function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"filtering evens from list by lambda and filter: {evens}")

# reduce: accumulate result, needs functools
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(f"product of numbers of list by lambda and reduce: {product}") 
#-------------------------------------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------
    # 4. Lambda in Sorting, Key Functions (sorted, min, max)
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Lambda for Custom Sorting and Key-Functions")
    display_note("You can use a lambda as the `key` argument in functions like `sorted`, `min`, `max` for custom sorting/extracting.", "info")
    code4 = """
words = ['pear', 'apple', 'banana', 'kiwi']
print(f"Original list: {words}")
by_len = sorted(words, key=lambda w: len(w))
print(f"Sorting list by length with help of lambda: {by_len}") 

points = [(2, 3), (1, 5), (5, 1)]
print(f"\\nOriginal list: {points}")
by_y = sorted(points, key=lambda t: t[1])
print(f"Sorting list by decending order of first number: {by_y}")
#----------------------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -------------------------------------------------------------------------------
    # 5. Lambda as Return Value ("Function Factory")
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Lambda Returning Functions (Function Factories)")
    display_note("You can return a lambda (or any function) from a function to create specialized behaviors on demand.", "tip")
    code5 = """
def power_factory(n):
    return lambda x: x ** n

# passing value of n to function
square = power_factory(2)
cube = power_factory(3)

# using lambda present in regular function
print(f"Square and cube of 4: {square(4)}, {cube(4)}")
#-----------------------------------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -------------------------------------------------------------------------------
    # 6. Lambda, Closures, and "Late Binding" Gotcha
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Lambda Closures & The 'Late Binding' Trap")
    display_note("Be careful: lambdas (like all closures in Python) capture variables by reference, not value!", "warning")
    code6 = """
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
#--------------------------------------------------------------#"""
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    # -------------------------------------------------------------------------------
    # 7. Related/Advanced: Lambda with sorted, zip, GUI, and functools
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Advanced/Related Use Cases")
    display_note("Lambda can be handy in GUIs (event callbacks), dataframes (pandas DataFrame.apply), and custom iterators, or as a generator expression's key.","info")
    code7 = """
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_by_name = sorted(pairs, key=lambda x: x[1])
print(sorted_by_name)  # [(1, 'one'), (3, 'three'), (2, 'two')]

# In Pandas, you'd use df['col'].apply(lambda x: some_transform(x))
"""
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)


if __name__ == "__main__":
    main(1)
