from helpers.display_utils import *

def main():
    print_heading("List Comprehension in Python")
    
    imp_note_points("""
**List Comprehension:**  
- *A concise way to create new lists by transforming or filtering an existing iterable on a single line.*
- *Much shorter and more readable than traditional for-loops for building lists.*
- *Syntax comes from mathematical set builder notation.*

**General Syntax:**  
`[expression for item in iterable if condition (optional)]`
    """)

    # -------------------------------------------------------------------------------
    # 1. Basic List Comprehension Example
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Basic List Comprehension")
    display_note("Transform every item in a list or range with a single expression.", "info")
    show_code_with_output("""
nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print(squares)
"""
,
"""
[1, 4, 9, 16, 25]
""")

    # -------------------------------------------------------------------------------
    # 2. With Filtering Condition (If Clause)
    # -------------------------------------------------------------------------------
    print_sub_heading("2. List Comprehension With Condition (Filtering)")
    display_note("Add an `if` at the end to filter items. Only items meeting the condition appear in the output.", "tip")
    show_code_with_output("""
nums = range(1, 11)
even = [n for n in nums if n%2==0]
print(even)
"""
,
"""
[2, 4, 6, 8, 10]
""")

    # -------------------------------------------------------------------------------
    # 3. If-Else Expression (Ternary)
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Using If-Else in a List Comprehension")
    display_note("You can use `if...else` to choose different output for each element.", "example")
    show_code_with_output("""
labels = ['Even' if x%2==0 else 'Odd' for x in range(1, 6)]
print(labels)
"""
,
"""
['Odd', 'Even', 'Odd', 'Even', 'Odd']
""")

    # -------------------------------------------------------------------------------
    # 4. Nested List Comprehension (for flattening, matrix, grid)
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Nested List Comprehension")
    display_note("Combine multiple for-loops for matrices, grids, or flattening a list of lists.", "info")
    show_code_with_output("""# Nested list comprehension
print("Creating a matrix of 3*3 using nested list comprehension")
coordinates=[(x,y) for x in range(3) for y in range(3)]
print(coordinates)
                          
print("\nflattening this matrix using nested list comprehension")
flat_coordinates=[x for row in coordinates for x in row]
print(flat_coordinates)
"""
,
"""
Creating a matrix of 3*3 using nested list comprehension
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

flattening this matrix using nested list comprehension
[0, 0, 0, 1, 0, 2, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 2, 2]
""")

    # -------------------------------------------------------------------------------
    # 5. List Comprehension With Functions
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Using Functions Inside List Comprehension")
    display_note("Call any function in the expression; very powerful for transformations.", "tip")
    show_code_with_output("""
def double(x):
    return x * 2

result = [double(n) for n in range(1, 6)]
print(result)
"""
,
"""
[2, 4, 6, 8, 10]
""")

    # -------------------------------------------------------------------------------
    # 6. List Comprehension with Strings and Formatting
    # -------------------------------------------------------------------------------
    print_sub_heading("6. List Comprehension for String Operations")
    display_note("You can apply string methods or formatting to each item.", "example")
    show_code_with_output("""
words = ['Python', 'List', 'Comprehension']
lowercase = [w.lower() for w in words]
print(lowercase)

lengths = [len(w) for w in words]
print(lengths)
"""
,
"""
['python', 'list', 'comprehension']
[6, 4, 13]
""")

    # -------------------------------------------------------------------------------
    # 7. Real World: Filtering Based on Substring
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Filtering Words by Substring")
    show_code_with_output("""
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
has_a = [x for x in fruits if 'a' in x]
print(has_a)
"""
,
"""
['apple', 'banana', 'mango']
""")

    # -------------------------------------------------------------------------------
    # 8. Advanced: Nested Ifs and If-Else Chains
    # -------------------------------------------------------------------------------
    print_sub_heading("8. Nested Ifs and Categorization")
    display_note("You can use complex expressions (even chained if-else) to categorize items.", "info")
    show_code_with_output("""
nums = range(1, 11)
categories = [
    f'{n} is Divisible by 2 and 3' if n%2==0 and n%3==0
    else f'{n} is Divisible by 2' if n%2==0
    else f'{n} is Divisible by 3' if n%3==0
    else f'{n} is Not Divisible by 2 or 3'
    for n in nums
]

for category in categories:
    print(category)
"""
,
"""
1 is Not Divisible by 2 or 3
2 is Divisible by 2
3 is Divisible by 3
4 is Divisible by 2
5 is Not Divisible by 2 or 3
6 is Divisible by 2 and 3
7 is Not Divisible by 2 or 3
8 is Divisible by 2
9 is Divisible by 3
10 is Divisible by 2
""")

    imp_note_points("""
**Best Practices:**
- List comprehensions are best for simple transformations or filters on a single line.
- For complex logic (multiple statements), use regular loops for readability.
- They can be nested, but avoid too much nesting, keep it readable!""")

if __name__ == "__main__":
    main()
