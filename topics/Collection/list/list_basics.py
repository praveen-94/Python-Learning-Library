from helpers.display_utils import *

def main():
    print_heading("List Basic Concept")
    # 1) Creating Lists
    print_sub_heading("1) Creating Lists")
    display_note("Lists are ordered, mutable collections of items in Python. You can store elements of any type in a list.")
    display_note("Store both homo and heterogeneoud elements, in contiguous, dynamic")
    show_code_with_output('''# Creating different types of lists
print("Creating list by list literal.....")
empty_list1 = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
repeat_list1 = [None]*5   # empty list with known size
repeat_list2 = ["NO"]*5
print(f"Empty list1: {empty_list1}")
print(f"List of numbers: {numbers}")
print(f"Mixed type list: {mixed}")
# We can find length of list by 'len()' method
print(f"Repeat empty list with known size: {repeat_list1}, its length: {len(repeat_list1)}")
print(f"Repeat list with known size: {repeat_list2}, its length: {len(repeat_list2)}")

print("\nCreating list by 'list([iterable])' constructor.....")
empty_list2 = list()
# mixed = list(1, "hello", 3.14, True)   # give error

# From a string (each character becomes an element)
my_string = "hello"
new_list_from_string = list(my_string)
print("list created by passing a string:", new_list_from_string)

# From a range object
my_range = range(5)
new_list_from_range = list(my_range)
print("list created by passing range:", new_list_from_range)

# From another list (creates a shallow copy)
original_list = [5, 6, 7]
copied_list = list(original_list)
print("list created by passing a list:", copied_list)
print("they are distinct objects, Check by comparing 'original_list is copied_list':", original_list is copied_list) 

# From dictionary keys (by default)
my_dict = {'a': 1, 'b': 2, 'c': 3}
list_from_keys = list(my_dict)
print("list created by passing dictionary keys (by default):", list_from_keys)

# From dictionary values
list_from_values = list(my_dict.values())
print("list created by passing dictionary values:", list_from_values)'''
,
"Creating list by list literal....." + "\n" +
"Empty list1: []" + "\n" +
"List of numbers: [1, 2, 3, 4, 5]" + "\n" +
"Mixed type list: [1, 'hello', 3.14, True]" + "\n" +
"Repeat empty list with known size: [None, None, None, None, None], its length: 5" + "\n" +
"Repeat list with known size: ['NO', 'NO', 'NO', 'NO', 'NO'], its length: 5" + "\n" +
"\n\n" +
"Creating list by 'list([iterable])' constructor....." + "\n" +
"list created by passing a string: ['h', 'e', 'l', 'l', 'o']" + "\n" +
"list created by passing range: [0, 1, 2, 3, 4]" + "\n" +
"list created by passing a list: [5, 6, 7]" + "\n" +
"they are distinct objects, Check by comparing 'original_list is copied_list': False" + "\n" +
"list created by passing dictionary keys (by default): ['a', 'b', 'c']" + "\n" +
"list created by passing dictionary values: [1, 2, 3]" )
    display_note("Use [] (list literals) for creating lists when elements are known or for an empty list, as it's concise.", "tip")
    display_note("Use list() (constructor) primarily to convert other iterables (like tuples, strings, or sets) into a new list.","tip")

# --------------------------------------------------------------------

    # 2) Reading & Writing List Items (Indexing and Updating)
    print_sub_heading("2) Reading and Writing Items in a List")
    display_note("Lists support zero-based indexing. You can read or update elements using their index.")
    show_code_with_output('''# Indexing and Updating list
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")
print(f"First fruit (index 0): {fruits[0]}")
print(f"Last fruit (index -1): {fruits[-1]}")

# Updating an item
fruits[1] = "blueberry"
print(f"Updated list after changing index 1: {fruits}")'''
,
"""Original list: ['apple', 'banana', 'cherry']
First fruit (index 0): apple
Last fruit (index -1): cherry
Updated list after changing index 1: ['apple', 'blueberry', 'cherry']""")

# --------------------------------------------------------------------

    # 3) Concatenating Lists
    print_sub_heading("3) Concatenating Lists")
    display_note("You can use the `+` operator to combine two or more lists into a single list.")
    show_code_with_output('''even_numbers = [2, 4, 6]
odd_numbers = [1, 3, 5]
combined = even_numbers + odd_numbers

print(f"Even numbers list: {even_numbers}")
print(f"Odd numbers list: {odd_numbers}")
print(f"Combined list using '+': {combined}")'''
,
"""Even numbers list: [2, 4, 6]
Odd numbers list: [1, 3, 5]
Combined list using '+': [2, 4, 6, 1, 3, 5]""")

# --------------------------------------------------------------------

    # 4) List Slicing
    print_sub_heading("4) List Slicing")
    display_note("Slicing allows you to extract a sublist using [start:stop:step].")
    show_code_with_output('''# List Slicing
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Original list: {colors}")
print(f"First three colors: {colors[0:3]}")
print(f"Every second color: {colors[::2]}")
print(f"Reversed list: {colors[::-1]}")'''
,
"""Original list: ['red', 'green', 'blue', 'yellow', 'purple']
First three colors: ['red', 'green', 'blue']
Every second color: ['red', 'blue', 'purple']
Reversed list: ['purple', 'yellow', 'blue', 'green', 'red']""")

# --------------------------------------------------------------------

    # 5) Membership Test (in, not in)
    print_sub_heading("6) Membership Test Using `in` and `not in`")
    display_note("Use the `in` operator to test if an element exists in the list, and `not in` to test if it does not.")
    show_code_with_output('''# Membership Test (in, not in)
nums = [10, 20, 30, 40]
print(f"Is 20 in the list? {'Yes' if 20 in nums else 'No'}")
print(f"Is 50 not in the list? {'Yes' if 50 not in nums else 'No'}")'''
,
"""Is 20 in the list? Yes
Is 50 not in the list? Yes""")
    
    # --------------------------------------------------------------------

    # 6) Nested Lists
    print_sub_heading("8) Nested Lists")
    display_note("A nested list is a list inside another list. You can access inner elements using multiple indices.")
    show_code_with_output('''# Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Complete matrix: {matrix}")
print(f"Element at row 2, column 3: {matrix[1][2]}")
print(f"First row: {matrix[0]}")
print(f"Last column of each row: {[row[-1] for row in matrix]}")'''
,
"""Complete matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Element at row 2, column 3: 6
First row: [1, 2, 3]
Last column of each row: [3, 6, 9]""")
    
    # --------------------------------------------------------------------

    # 7) List Unpacking
    print_sub_heading("9) List Unpacking")
    display_note("List unpacking allows assigning list elements to individual variables in a single line.")
    show_code_with_output('''# List Unpacking
person = ["Alice", 30, "Engineer"]
name, age, profession = person

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")'''
,
"""Name: Alice
Age: 30
Profession: Engineer""")
    
    # --------------------------------------------------------------------

    # 8) Copying Lists
    print_sub_heading("10) Copying Lists")
    display_note("Assigning a list to another variable creates a reference, not a copy.")
    display_note("Use `list.copy()` or `list[:]` to create a shallow copy that does not share memory.")
    show_code_with_output('''Copying Lists"
original = [1, 2, 3]
reference = original
copy1 = original.copy()
copy2 = original[:]
original[0] = 99

print(f"Original list after change: {original}")
print(f"Reference (same object): {reference}")
print(f"Copy using copy(): {copy1}")
print(f"Copy using slicing [:]: {copy2}")'''
,
"""Original list after change: [99, 2, 3]
Reference (same object): [99, 2, 3]
Copy using copy(): [1, 2, 3]
Copy using slicing [:]: [1, 2, 3]""")
