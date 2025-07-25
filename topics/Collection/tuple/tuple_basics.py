from helpers.display_utils import *

# ----------------------------------------
# 📘 Python Tuples: Basic Concepts
# ----------------------------------------

def main():
    print_heading("Tuples Basic Concepts")
    imp_note_points = '''IMP Points
- Tuple itself is immutable, it annot be modified after it's created, You can't add, remove, or reorder elements.
- Tuple elements may or may not be immutable, it can be mutable if you put a mutable object (like a list or dictionary) inside the tuple.
> t = ([1, 2], [3, 4])  # Tuple of lists (mutable elements)
> t[0].append(999)      # ✅ This is allowed — modifying the list inside
> print(t)              # Output: ([1, 2, 999], [3, 4])
'''

    print_sub_heading("1) Creating Tuples")
    display_note("Tuples are ordered, immutable collections and store homo or heterogenous elements.")
    show_code_with_output("""# Creating Tuples
t1 = (1, 2, 3)
t2 = "apple", "banana", "cherry"  # No parentheses, still a tuple

single_element = (5,)  # Single-element tuple requires a trailing comma
empty_tuple = ()
print(f"Tuple t1: {t1}")
print(f"Tuple t2: {t2}")
print(f"Single-element tuple: {single_element}")
print(f"Empty element tuple: {empty_tuple}")"""
,
"Tuple t1: (1, 2, 3)\nTuple t2: ('apple', 'banana', 'cherry')\nSingle-element tuple: (5,)\nEmpty element tuple: ()")

# --------------------------------------------------------

    print_sub_heading("2) Accessing Tuple Elements")
    display_note("You can access elements using indexing, just like lists.")
    show_code_with_output("""# Accessing Tuple Elements
fruits = ("apple", "banana", "cherry")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")"""
,
"First fruit: apple\nLast fruit: cherry")

# --------------------------------------------------------

    print_sub_heading("3) Tuple Unpacking")
    display_note("Unpacking allows you to assign tuple values to multiple variables in one line.")
    show_code_with_output("""# Tuple Unpacking
data = ("John", 28, "Developer")
name, age, job = data
print(f"Name: {name}, Age: {age}, Job: {job}")"""
,
"Name: John, Age: 28, Job: Developer")
    
# --------------------------------------------------------

    print_sub_heading("4) Tuple Concatenation")
    display_note("You can concatenate two tuples using the '+' operator to form a new tuple.")
    show_code_with_output("""# Tuple Concatenation
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2
print(f"Concatenated tuple: {result}")"""
,
"Concatenated tuple: (1, 2, 3, 4)")

# ----------------------------------------

    print_sub_heading("5) Tuple Repetition")
    display_note("You can repeat a tuple multiple times using the '*' operator.")
    show_code_with_output("""# Tuple Repetition
t = ('a', 'b')
result = t * 3
print(f"Repeated tuple: {result}")"""
,
"Repeated tuple: ('a', 'b', 'a', 'b', 'a', 'b')")

# ----------------------------------------

    print_sub_heading("6) Tuple Slicing")
    display_note("You can extract a subpart of a tuple using slicing just like lists.")
    show_code_with_output("""# Tuple Slicing
t = (10, 20, 30, 40, 50)
result = t[1:4]
print(f"Sliced tuple: {result}")"""
,
"Sliced tuple: (20, 30, 40)")

# ----------------------------------------

    print_sub_heading("7) Tuples in Sets")
    display_note("Since tuples are immutable and hashable, they can be added to sets unlike lists.")
    show_code_with_output("""# Tuples in Sets
s = set()
s.add((1, 2))
s.add((3, 4))
print(f"Set with tuples: {s}")"""
,
"Set with tuples: {(1, 2), (3, 4)}")

# ----------------------------------------

print_sub_heading("8) Tuples as Dictionary Keys")
display_note("Tuples can be used as dictionary keys because they are immutable and hashable.")
show_code_with_output("""# Tuples as Dictionary Keys
location_data = {
    ('New York', 'USA'): 8419000,
    ('Tokyo', 'Japan'): 13960000
}
print(f"Population of Tokyo: {location_data[('Tokyo', 'Japan')]}")"""
,
"Population of Tokyo: 13960000")
