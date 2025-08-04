from helpers.display_utils import *

def main():
    print_heading("`map`, `filter` and Functional Programming Concepts in Python")

    imp_note_points("""
**Functional Programming Essentials:**
- *First-Class Functions:* Functions can be passed as arguments, returned, or assigned to variables.
- *Higher-Order Functions:* Functions that take other functions as parameters (`map`, `filter`, and `reduce`).
- *Pure Functions:* Output always depends only on input, with no side effects.
- *Anonymous Functions:* e.g., lambda expressions.
- *Immutability, Recursion, and Lazy Evaluation* are also key ideas.

**map, filter, reduce — What and Why?**
- `map(func, iterable, ...)`: Transform each element of an iterable using a function.
- `filter(func, iterable)`: Keep only those elements where func returns True.
- `reduce(func, iterable)`: Combine items into a single value, e.g., sum, product (from functools).
- All these return iterators (lazy evaluation).""")

    # -------------------------------------------------------------------------------
    # 1. map(): Apply Function to All Elements
    # -------------------------------------------------------------------------------
    print_sub_heading("1. map()— Transforming Iterables")
    display_note("it takes a function and one or more iterables, applies the function to each item, and returns an iterator with the results.", "info")
    imp_note_points("""**Syntax and Arguments:**
- `map(function, iterable, ...)`
    - *function*: Required; a callable (usually a function or lambda) to apply to each item.
    - *iterable(s)*: Required; one or more iterables (lists, tuples, etc.). The function is called with one argument from each iterable.
    - *Returns*: Map object (an iterator/generator), which yields transformed output.""")
    show_code_with_output("""
nums = [1, 2, 3, 4]
def sqr(x):
    return x * x

squares = list(map(sqr, nums))
print(squares)  # [1, 4, 9, 16]

# With lambda and two iterables:
nums2 = [10, 20, 30, 40]
added = list(map(lambda x, y: x + y, nums, nums2))
print(added)    # [11, 22, 33, 44]
""",
"""
[1, 4, 9, 16]
[11, 22, 33, 44]
""")

    # -------------------------------------------------------------------------------
    # 2. filter(): Filter Elements by a Condition
    # -------------------------------------------------------------------------------
    print_sub_heading("2. filter()— Selective Filtering")
    display_note("it takes a function that returns True/False and an iterable, returning only elements for which the function returns True.", "tip")
    imp_note_points("""**Syntax and Arguments:**
- `filter(function, iterable)`
    - *function*: Required; a callable that takes an element and returns True (keep) or False (skip). If None, keeps all truthy values.
    - *iterable*: Required; the sequence to filter.
    - *Returns*: Filter object (an iterator), yielding elements where function(item)==True.""")
    show_code_with_output("""
def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, nums))
print(evens)  # [2, 4, 6]

# With lambda:
odds = list(filter(lambda x: x % 2, nums))
print(odds)   # [1, 3, 5]
""",
"""
[2, 4, 6]
[1, 3, 5]
""")

    # -------------------------------------------------------------------------------
    # 3. functools.reduce(): Cumulative Reduction
    # -------------------------------------------------------------------------------
    print_sub_heading("3. reduce()— Accumulate Values (from functools)")
    imp_note_points("""**Syntax and Arguments:**
- `reduce(function, iterable, initializer=None)`
        - *function*: Required; a function of two arguments to apply cumulatively to items.
        - *iterable*: Required; items to combine.
        - *initializer*: Optional; value placed before the items, as a starting point.
        - *Returns*: Single, accumulated value (e.g., sum, product).""")
    display_note("reduce() repeatedly applies a function to accumulate a single result from an iterable (must import from functools module).", "info")
    show_code_with_output("""
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

# With a named function:
def add(x, y):
    return x + y

summed = reduce(add, nums)
print(summed)   # 10
""",
"""
24
10
""")

    # -------------------------------------------------------------------------------
    # 4. Composing map/filter/reduce (Functional Pipelines)
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Chaining `map` and `filter`")
    display_note("Both `map` and `filter` return iterators. You can combine them for data pipelines without intermediate lists.", "example")
    show_code_with_output("""
nums = range(10)
# Squares of all even numbers from 0 to 9:
result = map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums))
print(list(result))  # [0, 4, 16, 36, 64]
""",
"""
[0, 4, 16, 36, 64]
""")

    # -------------------------------------------------------------------------------
    # 5. Comparison with Comprehensions (Readability & Pythonic Style)
    # -------------------------------------------------------------------------------
    print_sub_heading("5. map/filter vs List Comprehension")
    display_note("List comprehensions are often clearer/more Pythonic. ", "warning")
    display_note("Use map/filter for functional pipelines or when passing functions explicitly.", "warning", message_continue=True)
    show_code_with_output("""
nums = [1, 2, 3, 4, 5, 6]

# Even numbers squared: list comprehension
evens_squared = [x*x for x in nums if x % 2 == 0]
print(evens_squared)  # [4, 16, 36]

# Same using map + filter
evens_squared_2 = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))
print(evens_squared_2)
""",
"""
[4, 16, 36]
[4, 16, 36]
""")

    # -------------------------------------------------------------------------------
    # 6. Working with Strings and Other Types
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Use with Strings and Multiple Iterables")
    show_code_with_output("""
words = ['apple', 'banana', 'Kiwi']

# Uppercase all words using map and str.upper
upper_words = list(map(str.upper, words))
print(upper_words)  # ['APPLE', 'BANANA', 'KIWI']

# Filter words that contain 'a'
words_with_a = list(filter(lambda w: 'a' in w, words))
print(words_with_a)  # ['apple', 'banana']
""",
"""
['APPLE', 'BANANA', 'KIWI']
['apple', 'banana']
""")

    # -------------------------------------------------------------------------------
    # 7. Lazy Evaluation and Memory Efficiency
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Lazy Evaluation, Performance, and Gotchas")
    imp_note_points("""
- map/filter/reduce are *lazy*: no results are generated until you iterate (e.g., via list(), for loop, etc.).
- This is great for large datasets—process one item at a time!
- If you want results as a list, wrap the call: list(map(...)), list(filter(...))
- List comprehensions often yield more readable code for simple cases.""")

    # -------------------------------------------------------------------------------
    # 8. Related: all(), any(), zip(), enumerate(), functors
    # -------------------------------------------------------------------------------
    print_sub_heading("8. Related Useful Built-ins and Patterns")
    display_note("You can also combine map/filter with `all`, `any`, `zip`, and `enumerate` to build powerful pipelines. Example:","tip")
    show_code_with_output("""
nums = [0, 1, 2, 3, 4, 5]
# Check if all numbers are positive
print(all(map(lambda x: x > 0, nums)))   # False
# Check if any number is negative
print(any(map(lambda x: x < 0, nums)))   # False

# zip two lists and filter pairs with same parity
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
parity_pairs = list(filter(lambda pair: pair[0] % 2 == pair[1] % 2, zip(x, y)))
print(parity_pairs)  # [(1, 5), (2, 6), (3, 7), (4, 8)]

# Enumerate with lambda, get indices for even values
even_indices = [i for i, val in enumerate(nums) if val % 2 == 0]
print(even_indices)  # [0, 2, 4]
""",
"""
False
False
[(1, 5), (2, 6), (3, 7), (4, 8)]
[0, 2, 4]
""")

    imp_note_points("""**Summary/Best Practices:**
- Use `map` for applying functions to every item.
- Use `filter` for selecting a subset matching a single criterion.
- Use `reduce` for cumulative aggregation (import from functools).
- Prefer comprehensions for most use-cases where possible—they are usually more readable.
- Great for data pipelines, memory efficiency, real-time transformations, and when needing to compose functions flexibly.""")

if __name__ == "__main__":
    main()
