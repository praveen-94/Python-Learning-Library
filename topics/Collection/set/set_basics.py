from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Sets", topic_number)
    imp_note_points("""IMP Points
- Sets are unordered collections of unique items.
- Implemented using hash tables → average time complexity of O(1) for add, remove, and lookup.
- Mutable → can add or remove elements, but elements themselves must be immutable (e.g., int, str, tuple).
- Unordered → no index, so no slicing or indexing like lists.
- No duplicate items allowed → repeated elements are automatically removed.
- Can be used for membership testing and eliminating duplicate entries.
- Supports mathematical operations like union, intersection, difference.
- Sets cannot contain other sets or mutable items like lists as elements.
- Efficient for tasks involving uniqueness and set-based logic.
- A set can be created using literals, constructor, from iterable, or comprehension.
- Frozenset is the immutable version of a set (cannot be modified).""")

    #--------------------------------------------------------------------------------------------------
    # 1) Creating Sets
    #--------------------------------------------------------------------------------------------------
    print_sub_heading("1) Creating Sets")
    display_note("An empty set must be created using set(), Not by {} because {} creates an empty dictionary.", "warning")
    code1 = """# Creating a set from a list
set1 = {1, 2, 3, 4, 5}
print(f"Set1 (by Literal): {set1}")

# Creating a set using set() constructor
set2 = set([3, 4, 5, 6])
print(f"Set2 (by Constructor): {set2}")

# Creating an empty set 
empty_set = set()
print(f"Empty Set (by set()): {empty_set}")

# Creating empty set from empty list/tuple/string
empty_from_list = set([])
empty_from_tuple = set(())
empty_from_string = set("")
print(f"Empty Set from list: {empty_from_list}")
print(f"Empty Set from tuple: {empty_from_tuple}")
print(f"Empty Set from string: {empty_from_string}")

# Creating set from a string
char_set = set("hello")
print(f"Character Set: {char_set}")

# Creating set using comprehension
squared_set = {x * x for x in range(1, 6)}
print(f"Squared Set by comprehension: {squared_set}")

# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(f"Frozen Set: {frozen}")
#-------------------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    #--------------------------------------------------------------------------------------------------
    # 2) Accessing Elements
    #--------------------------------------------------------------------------------------------------
    print_sub_heading("2) Accessing Elements")
    display_note("You cannot access elements by index since sets are unordered.")
    code2 = """# Using for loop to access all elements
set1 = {1, 2, 3, 4, 5}
for item in set1:
    print(item, end=", ")
#-------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    #--------------------------------------------------------------------------------------------------
    # 3) Adding Elements
    #--------------------------------------------------------------------------------------------------
    print_sub_heading("3) Adding Elements")
    display_note("You can use add() for a single element and update() for multiple.")
    code3 = """# Adding an element
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(f"After add: {set1}")

# Adding multiple elements
set1.update([7, 8, 9])
print(f"After update: {set1}")
#------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


    #--------------------------------------------------------------------------------------------------
    # 4) Removing Elements
    #--------------------------------------------------------------------------------------------------
    print_sub_heading("4) Removing Elements")
    display_note("Use remove() if you're sure the item exists, discard() if not sure. pop() removes an arbitrary element.")
    code4 = """# Remove an element
set1 = {1, 2, 3, 4, 5}
set1.remove(4)
print(f"After remove(4): {set1}")

# Discard an element (no error if element not found)
set1.discard(100)
print(f"After discard(100): {set1}")

# Pop an arbitrary element
popped = set1.pop()
print(f"Popped element: {popped}")
print(f"After pop: {set1}")

# Clear all elements
set1.clear()
print(f"After clear: {set1}")
#------------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)