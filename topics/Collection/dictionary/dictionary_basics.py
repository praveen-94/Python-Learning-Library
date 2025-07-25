from helpers.display_utils import *

# --------------------------------------------------------
# 📘 Python Dictionaries: Basic Concepts
# --------------------------------------------------------
def main():
    print_heading("Python Dictionaries Basic Concepts")
    imp_note_points("""IMP Points
- Dictionaries are implemented using hash tables internally.
- Because of hashing, search, insert, and delete operations are typically done in constant time O(1).
- Unordered (before Python 3.7) → From 3.7+, they preserve insertion order.
- Keys must be unique and hashable (i.e. immutable types like str, int, tuple)
- But values can be duplicated or of any data type, including lists, dicts, etc.
- Cannot use lists or dicts as keys (they are unhashable).
- Dictionaries are mutable (can be changed).
- Python raises a KeyError if you access a missing key directly with [].
- Dictionary keys are case-sensitive (e.g., 'Name' and 'name' are different).
- Keys are used for fast lookup, not index-based like lists.
- Supports nesting, making it useful for structured or hierarchical data.""")
    
# --------------------------------------------------
    print_sub_heading("1) Creating Dictionaries")
    display_note("Dictionaries can be created using curly braces, dict() constructor, fromkeys(), zip() and by copying existing dict.")
    show_code_with_output("""# Creating Dictionaries
# Using literal
dict1 = {'a': 1, 'b': 2}
                          
# Using dict constructor
dict2 = dict(name='Alice', age=30)
                          
# From keys (with default value)
dict3 = dict.fromkeys(['x', 'y'], 0)
                          
# From zip
dict4 = dict(zip(['k1', 'k2'], [100, 200]))
                          
# Copying a dictionary
original = {'id': 1, 'lang': 'Python'}
copied = original.copy()

print(f"Showing dictionary created by Literal: {dict1}")
print(f"Showing dictionary created by Constructor: {dict2}")
print(f"Showing dictionary created From keys: {dict3}")
print(f"Showing dictionary created From zip: {dict4}")
print(f"Showing dictionary created by Copied: {copied}")"""
,
"""Showing dictionary created by Literal: {'a': 1, 'b': 2}
Showing dictionary created by Constructor: {'name': 'Alice', 'age': 30}
Showing dictionary created From keys: {'x': 0, 'y': 0}
Showing dictionary created From zip: {'k1': 100, 'k2': 200}
Showing dictionary created Copied: {'id': 1, 'lang': 'Python'}""")

# --------------------------------------------------
    print_sub_heading("2) Accessing Dictionary Values")
    display_note("Access values using square brackets, get(), and setdefault(). The get() and setdefault() are safer.")
    show_code_with_output("""# Accessing Dictionary Values
info = {'name': 'Bob', 'age': 25}
print(f"Fetching value of key 'name' Using []: {info['name']}") # give error if key not exist 
print(f"Fetching value of key 'age' Using get(): {info.get('age')}") # give none if key not exist
print(f"Fetching value of key 'height' Using get(): {info.get('height')}")
                          
# To get 'Not specified' if key not exist 
print(f"Fetching value of key 'name' Using get() with default: {info.get('name', 'Not specified')}")
print(f"Fetching value of key 'height' Using get() with default: {info.get('height', 'Not specified')}")
                          
# setdefault() set value if enter keys value not exist
print(f"Fetching value of key 'name' Using setdefault() for non-existing key: {info.setdefault('name', 'Unknown')}")
print(f"Fetching value of key 'name' Using setdefault() for non-existing key: {info.setdefault('city', 'Unknown')}")
print(f"After setdefault(): {info}")"""
,
"""Fetching value of key 'name' Using []: Bob
Fetching value of key 'age' Using get(): 25
Fetching value of key 'height' Using get(): None
Fetching value of key 'name' Using get() with default: Bob
Fetching value of key 'height' Using get() with default: Not specified
Fetching value of key 'name' Using setdefault() for non-existing key: Bob
Fetching value of key 'name' Using setdefault() for non-existing key: Unknown
After setdefault(): {'name': 'Bob', 'age': 25, 'city': 'Unknown'}""")

# --------------------------------------------------
    print_sub_heading("3) Adding or Updating Values")
    display_note("Assigning to a key adds it if it doesn't exist, or updates it if it does. You can also use update().")
    show_code_with_output("""# Adding or Updating Values
student = {'name': 'Alice'}
print("Before update:", {student})
student['age'] = 22  # Add
student['name'] = 'Eve'  # Update
student.update({'city': 'Delhi', 'grade': 'A'})  # Merge
print(f"Updated student: {student}")"""
,
"Before update: {'name': 'Alice'}\nUpdated student: {'name': 'Eve', 'age': 22, 'city': 'Delhi', 'grade': 'A'}")

# --------------------------------------------------
    print_sub_heading("4) Removing Items from Dictionary")
    display_note("You can remove items using del, pop(), popitem(), or clear().")
    show_code_with_output("""# Removing Items from Dictionary
data = {'name': 'John', 'age': 28, 'country': 'India'}
del data['country']  # Remove specific key, give keyError if key not exist

# Pop() remove specific, and return its value, if not exist return none (default)
removed1 = data.pop('age')
print(f"Removed 'age': {removed1}, Now dictionary content is: {data}")   
removed2 = data.pop('height')
print(f"Removed 'height': {removed2}, Now dictionary content is: {data}")
removed3 = data.pop('city',"NA")
print(f"Removed 'city': {removed3}, Now dictionary content is: {data}")

# Popitem() remove and return last inserted key-value as tuple, give keyError if empty
last = data.popitem()  # Pop last item
print(f"Last popped item: {last}, Now dictionary content is: {data}")
                          
data.clear()  # Clear all
print(f"After clear(): {data}")"""
,
"""Removed 'age': 28, Now dictionary content is: {'name': 'John'}
Removed 'city': NA, Now dictionary content is: {'name': 'John'}
Last popped item: ('name', 'John'), Now dictionary content is: {}
After clear(): {}""")
    
# ----------------------------------------
    print_sub_heading("5) fetching keys(), values(), items()")
    display_note("Returns view objects: keys(), values(), and items() can be converted to lists for easy viewing.")
    show_code_with_output("""# keys(), values(), items()
d = {'name': 'Alice', 'age': 30}
print(f"Keys: {list(d.keys())}")
print(f"Values: {list(d.values())}")
print(f"Items: {list(d.items())}")"""
,
"Keys: ['name', 'age']\nValues: ['Alice', 30]\nItems: [('name', 'Alice'), ('age', 30)]")
    
# ----------------------------------------

    print_sub_heading("6) Iterating Through Dictionary")
    display_note("You can iterate through dictionary keys, values, or key-value pairs using a for loop.")
    show_code_with_output("""# Iterating Through Dictionary
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

print("Iterating through keys")
for key in student:
    print(f"Key: {key}", end=" | ")
print()

print("Iterating through values")
for value in student.values():
    print(f"Value: {value}", end=" | ")
print()

print("Iterating through key-value pairs")
for key, value in student.items():
    print(f"{key} -> {value}", end=" | ")"""
,
"Iterating through keys\nKey: name | Key: age | Key: grade | \nIterating through values\nValue: Alice | Value: 22 | Value: A | \nIterating through key-value pairs\nname -> Alice | age -> 22 | grade -> A | ")

# ----------------------------------------

    print_sub_heading("7) Dictionary Comprehension")
    display_note("Dictionary comprehension provides a concise way to create dictionaries from iterables.")
    show_code_with_output("""# Creating a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filtering dictionary to keep only even values
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v % 2 == 0}
print(f"Filtered (even values): {filtered}")"""
,
"Squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\nFiltered (even values): {'b': 2, 'd': 4}")
