from helpers.display_utils import *

def main(topic_number: int):
    print_heading("List Comprehension in Python", topic_number)
    
    imp_note_points("""
**List Comprehension:**  
- *A concise way to create new lists by transforming or filtering an existing iterable on a single line.*
- *Much shorter and more readable than traditional for loops for building lists.*
- *Syntax comes from mathematical set builder notation.*

**General Syntax:**  
- *[expression for item in iterable if condition (optional)]*
    
**Best Practices:**
- *List comprehensions are best for simple transformations or filters on a single line.*
- *For complex logic (multiple statements), use regular loops for readability.*
- *They can be nested, but avoid too much nesting, keep it readable!*""")

    # -------------------------------------------------------------------------------
    # 1. Basic List Comprehension Example
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Basic List Comprehension")
    display_note("Transform every item in a list or range with a single expression.", "info")
    code1 = """
nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print(f"Original list: {nums}")
print(f"Square list of list created by comprehension: {squares}")
#----------------------------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -------------------------------------------------------------------------------
    # 2. With Filtering Condition (If Clause)
    # -------------------------------------------------------------------------------
    print_sub_heading("2. List Comprehension With Condition (Filtering)")
    display_note("Add an `if` at the end to filter items. Only items meeting the condition appear in the output.", "tip")
    code2 = """
nums = range(1, 11)
even = [n for n in nums if n%2==0]
print(f"Original list: {nums}")
print(f"Even list of list created by comprehension: {even}")
#--------------------------------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -------------------------------------------------------------------------------
    # 3. If-Else Expression (Ternary)
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Using If-Else in a List Comprehension")
    display_note("You can use `if...else` to choose different output for each element.", "example")
    code3 = """
labels = ['Even' if x%2==0 else 'Odd' for x in range(1, 6)]
print(labels)
#-----------------------------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------
    # 4. Nested List Comprehension (for flattening, matrix, grid)
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Nested List Comprehension")
    display_note("Combine multiple for-loops for matrices, grids, or flattening a list of lists.", "info")
    code4 = """# Nested list comprehension
print("Creating a matrix of 3*3 using nested list comprehension")
coordinates=[(x,y) for x in range(3) for y in range(3)]
print(coordinates)
                          
print("\\nflattening this matrix using nested list comprehension")
flat_coordinates=[x for row in coordinates for x in row]
print(flat_coordinates)
#----------------------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -------------------------------------------------------------------------------
    # 5. List Comprehension With Functions
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Using Functions Inside List Comprehension")
    display_note("Call any function in the expression; very powerful for transformations.", "tip")
    code5 = """
def double(x):
    return x * 2

result = [double(n) for n in range(1, 6)]
print(result)
#-----------------------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -------------------------------------------------------------------------------
    # 6. List Comprehension with Strings and Formatting
    # -------------------------------------------------------------------------------
    print_sub_heading("6. List Comprehension for String Operations")
    display_note("You can apply string methods or formatting to each item.", "example")
    code6 = """
words = ['Python', 'List', 'Comprehension']
lowercase = [w.lower() for w in words]
print(f"Original list: {words}")
print(f"lowercase list of list created by comprehension: {lowercase}")

lengths = [len(w) for w in words]
print(f"list of length of words present in list by comprehension: {lengths}")
#----------------------------------------------------------------------------#"""
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    # -------------------------------------------------------------------------------
    # 7. Real World: Filtering Based on Substring
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Filtering Words by Substring")
    code7 = """
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
has_a = [x for x in fruits if 'a' in x]
print(f"Original list: {fruits}")
print(f"list of words contains 'a' from original list by comprehension: {has_a}")
#-------------------------------------------------------------------------------#"""
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)

    # -------------------------------------------------------------------------------
    # 8. Advanced: Nested Ifs and If-Else Chains
    # -------------------------------------------------------------------------------
    print_sub_heading("8. Nested Ifs and Categorization")
    display_note("You can use complex expressions (even chained if-else) to categorize items.", "info")
    code8= """
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
#---------------------------------------------------------#"""
    output8 = run_code_snippet(code8)
    show_code_with_output(code8, output8)

if __name__ == "__main__":
    main(1)
