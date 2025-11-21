from helpers.display_utils import *

def main(topic_number: int):
    print_heading("`map`, `filter` and Functional Programming Concepts in Python", topic_number)

    imp_note_points("""
# **Functional Programming Essentials:**
- ***First-Class Functions:** Functions can be passed as arguments, returned, or assigned to variables.*
- ***Higher-Order Functions:** Functions that take other functions as parameters __(map, filter, and reduce)__.*
- ***Pure Functions:** Output always depends only on input, with no side effects.*
- ***Anonymous Functions:** e.g., lambda expressions.*
- *Immutability, Recursion, and Lazy Evaluation* are also key ideas.*

# **map, filter, reduce — What and Why?**
- ***map(func, iterable, ...):** Transform each element of an iterable using a function.*
- ***filter(func, iterable):** Keep only those elements where func returns True.*
- ***reduce(func, iterable):** Combine items into a single value, e.g., sum, product (from functools).*
- *All these return iterators (lazy evaluation).*
                    
# **Lazy Evaluation, Performance, and Gotchas**
- *map/filter/reduce are **lazy**: no results are generated until you iterate (e.g., via list(), for loop, etc.).*
- *This is great for large datasets—process one item at a time!*
- *If you want results as a list, wrap the call: list(map(...)), list(filter(...))*
- *List comprehensions often yield more readable code for simple cases.*

# **Summary/Best Practices:**
- *Use __map__ for applying functions to every item.*
- *Use __filter__ for selecting a subset matching a single criterion.*
- *Use __reduce__ for cumulative aggregation (import from functools).*
- *Prefer comprehensions for most use-cases where possible—they are usually more readable.*
- *Great for data pipelines, memory efficiency, real-time transformations, and when needing to compose functions flexibly.*""")         

    # -------------------------------------------------------------------------------
    # 1. map(): Apply Function to All Elements
    # -------------------------------------------------------------------------------
    print_sub_heading("1. map()— Transforming Iterables")
    display_note("it takes a function and one or more iterables, applies the function to each item, and returns an iterator with the results.", "info")
    imp_note_points("""- ___map(function, iterable, ...)___
    - *function*: Required; a callable (usually a function or lambda) to apply to each item.
    - *iterable(s)*: Required; one or more iterables (lists, tuples, etc.). The function is called with one argument from each iterable.
    - *Returns*: Map object (an iterator/generator), which yields transformed output.""", "Syntax and Arguments:")
    code1 = """
nums = [1, 2, 3, 4]
def sqr(x):
    return x * x

squares = list(map(sqr, nums))
print(squares) 

# With lambda and two iterables:
nums2 = [10, 20, 30, 40]
added = list(map(lambda x, y: x + y, nums, nums2))
print(added)
#--------------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -------------------------------------------------------------------------------
    # 2. filter(): Filter Elements by a Condition
    # -------------------------------------------------------------------------------
    print_sub_heading("2. filter()— Selective Filtering")
    display_note("it takes a function that returns True/False and an iterable, returning only elements for which the function returns True.", "tip")
    imp_note_points("""- ___filter(function, iterable)___
    - *function*: Required; a callable that takes an element and returns True (keep) or False (skip). If None, keeps all truthy values.
    - *iterable*: Required; the sequence to filter.
    - *Returns*: Filter object (an iterator), yielding elements where function(item)==True.""", "Syntax and Arguments:")
    code2 = """
def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, nums))
print(evens) 
# With lambda:
odds = list(filter(lambda x: x % 2, nums))
print(odds)  
#------------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -------------------------------------------------------------------------------
    # 3. functools.reduce(): Cumulative Reduction
    # -------------------------------------------------------------------------------
    print_sub_heading("3. reduce()— Accumulate Values (from functools)")
    imp_note_points("""- ___reduce(function, iterable, initializer=None)___
        - *function*: Required; a function of two arguments to apply cumulatively to items.
        - *iterable*: Required; items to combine.
        - *initializer*: Optional; value placed before the items, as a starting point.
        - *Returns*: Single, accumulated value (e.g., sum, product).""", "Syntax and Arguments:")
    display_note("reduce() repeatedly applies a function to accumulate a single result from an iterable (must import from functools module).", "info")
    code3 = """
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  

# With a named function:
def add(x, y):
    return x + y

summed = reduce(add, nums)
print(summed) 
#-------------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------
    # 4. Composing map/filter/reduce (Functional Pipelines)
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Chaining `map` and `filter`")
    display_note("Both `map` and `filter` return iterators. You can combine them for data pipelines without intermediate lists.", "example")
    code4 = """
nums = range(10)
# Squares of all even numbers from 0 to 9:
result = map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums))
print(list(result))  
#-----------------------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -------------------------------------------------------------------------------
    # 5. Comparison with Comprehensions (Readability & Pythonic Style)
    # -------------------------------------------------------------------------------
    print_sub_heading("5. map/filter vs List Comprehension")
    display_note("List comprehensions are often clearer/more Pythonic. Use map/filter for functional pipelines or when passing functions explicitly.", "warning")
    code5 = """
nums = [1, 2, 3, 4, 5, 6]

# Even numbers squared: list comprehension
evens_squared = [x*x for x in nums if x % 2 == 0]
print(evens_squared) 

# Same using map + filter
evens_squared_2 = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))
print(evens_squared_2)
#------------------------------------------------------------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -------------------------------------------------------------------------------
    # 6. Working with Strings and Other Types
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Use with Strings and Multiple Iterables")
    code6 = """
words = ['apple', 'banana', 'Kiwi']

# Uppercase all words using map and str.upper
upper_words = list(map(str.upper, words))
print(upper_words) 

# Filter words that contain 'a'
words_with_a = list(filter(lambda w: 'a' in w, words))
print(words_with_a) 
#-----------------------------------------------------#"""
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)



    # -------------------------------------------------------------------------------
    # 7. Related: all(), any(), zip(), enumerate(), functors
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Related Useful Built-ins and Patterns")
    display_note("You can also combine map/filter with `all`, `any`, `zip`, and `enumerate` to build powerful pipelines. Example:","tip")
    code7 = """
nums = [0, 1, 2, 3, 4, 5]
# Check if all numbers are positive
print(all(map(lambda x: x > 0, nums)))   
# Check if any number is negative
print(any(map(lambda x: x < 0, nums)))   

# zip two lists and filter pairs with same parity
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
parity_pairs = list(filter(lambda pair: pair[0] % 2 == pair[1] % 2, zip(x, y)))
print(parity_pairs)  # [(1, 5), (2, 6), (3, 7), (4, 8)]

# Enumerate with lambda, get indices for even values
even_indices = [i for i, val in enumerate(nums) if val % 2 == 0]
print(even_indices)  
#-------------------------------------------------------------------------------#"""
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)


if __name__ == "__main__":
    main(1)
