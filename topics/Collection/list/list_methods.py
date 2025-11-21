from helpers.display_utils import *

# ------------------------------------------------------------------------------------------------------
# 📘 Python List Methods (Grouped & Ordered by Usage)
# ------------------------------------------------------------------------------------------------------
def main(topic_number: int):
    print_heading("Python List Methods", topic_number)

    #---------------------------------------------------------------------------
    # 1) Adding/Appending Elements
    #---------------------------------------------------------------------------
    print_sub_heading("1) Adding/Appending Elements")
    display_note("""These methods are used to add items to a list.
We can pass any iterable in `extend(collection)` method like list, tuple, set, dictionary, range etc""")
    code1 = """# Adding/Appending Elements
fruits = ["apple", "banana"]
fruits.append("cherry")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "orange")  # Insert at index 1
print(f"After insert at index 1: {fruits}")

more_fruits = ["kiwi", "melon"]
fruits.extend(more_fruits)  # Append multiple items
print(f"After extend: {fruits}")
#---------------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    #---------------------------------------------------------------------------
    # 2) Removing Elements
    #---------------------------------------------------------------------------
    print_sub_heading("2) Removing Elements")
    display_note("These methods remove items from a list by value, index, or clear all.")
    code2 = """# Removing Elements
items = ["pen", "pencil", "eraser", "pencil"]
items.remove("pencil")  # Removes first occurrence
print(f"After remove 'pencil': {items}")

last_item = items.pop()  # Removes last element
print(f"After pop: {items}, Popped item: {last_item}")

second_item = items.pop(1)  # Removes by index
print(f"After pop(1): {items}, Removed: {second_item}")

items.clear()  # Removes all
print(f"After clear: {items}")
#-------------------------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    #---------------------------------------------------------------------------
    # 3) Searching & Counting
    #---------------------------------------------------------------------------
    print_sub_heading("3) Searching & Counting")
    display_note("These methods find the position or count of items.")
    code3 = """# Searching & Counting
numbers = [1, 2, 3, 2, 4, 2]
print(f"Index of 2: {numbers.index(2)}")  # First occurrence
print(f"Count of 2: {numbers.count(2)}")  # Frequency
#------------------------------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #---------------------------------------------------------------------------
    # 4) Sorting & Reversing
    #---------------------------------------------------------------------------
    print_sub_heading("4) Sorting & Reversing")
    display_note("""These methods change the order of elements.
sort(): In-place (modifies original list), Returns None, Works with homogeneous types, Stable sort (equal elements retain their original order)
Use to sort numbers, strings, or objects by custom rules like length or case-insensitive comparison.
reverse(): In-place, Returns None, Stable, List-only (Not work in tuples, sets, or strings)""")
    display_note("""Use `sorted()` instead of sort() when you need to keep the original list unchanged.
Use reversed() with list() if want a reversed copy without modifying original, or reverse any iterable(strings, tuples, etc.)""","tip")
    code4 = """# sort(key=None, reverse=False)) & Reversing
nums = [4, 1, 5, 2]
nums.sort()  # Sort ascending
print(f"Sorted list: {nums}")

nums.sort(reverse=True)  # Descending sort
print(f"Sorted in reverse: {nums}")

#Using key with Custom Sorting
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)  # Sort by length of each word
print("Sorted by length of string:", words)
                          
nums.reverse()  # Just reverse
print(f"Reversed list: {nums}")
#--------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    #---------------------------------------------------------------------------
    # 5) Copying
    #---------------------------------------------------------------------------
    print_sub_heading("5) Copying Lists")
    display_note("Use `copy()` to clone a list without linking it to the original.")
    code5 = """# Copying Lists
original = [10, 20, 30]
copied = original.copy()
original.append(40)
print(f"Original: {original}")
print(f"Copied: {copied}")
#-----------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)
