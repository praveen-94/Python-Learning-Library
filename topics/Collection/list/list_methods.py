from helpers.display_utils import *

# ----------------------------------------
# 📘 Python List Methods (Grouped & Ordered by Usage)
# ----------------------------------------
def main():
    print_heading("Python List Methods")

    # 1) Adding/Appending Elements
    print_sub_heading("1) Adding/Appending Elements")
    display_note("These methods are used to add items to a list.")
    show_code_with_output("""# Adding/Appending Elements
fruits = ["apple", "banana"]
fruits.append("cherry")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "orange")  # Insert at index 1
print(f"After insert at index 1: {fruits}")

more_fruits = ["kiwi", "melon"]
fruits.extend(more_fruits)  # Append multiple items
print(f"After extend: {fruits}")"""
,
"After append: ['apple', 'banana', 'cherry']\nAfter insert at index 1: ['apple', 'orange', 'banana', 'cherry']\nAfter extend: ['apple', 'orange', 'banana', 'cherry', 'kiwi', 'melon']")
    display_note("We can pass any iterable in `extend(collection)` method like list, tuple, set, dictionary, range etc")

# ----------------------------------------

    # 2) Removing Elements
    print_sub_heading("2) Removing Elements")
    display_note("These methods remove items from a list by value, index, or clear all.")
    show_code_with_output("""# Removing Elements
items = ["pen", "pencil", "eraser", "pencil"]
items.remove("pencil")  # Removes first occurrence
print(f"After remove 'pencil': {items}")

last_item = items.pop()  # Removes last element
print(f"After pop: {items}, Popped item: {last_item}")

second_item = items.pop(1)  # Removes by index
print(f"After pop(1): {items}, Removed: {second_item}")

items.clear()  # Removes all
print(f"After clear: {items}")"""
,
"After remove 'pencil': ['pen', 'eraser', 'pencil']\nAfter pop: ['pen', 'eraser'], Popped item: pencil\nAfter pop(1): ['pen'], Removed: eraser\nAfter clear: []")

# ----------------------------------------

    # 3) Searching & Counting
    print_sub_heading("3) Searching & Counting")
    display_note("These methods find the position or count of items.")
    show_code_with_output("""# Searching & Counting
numbers = [1, 2, 3, 2, 4, 2]
print(f"Index of 2: {numbers.index(2)}")  # First occurrence
print(f"Count of 2: {numbers.count(2)}")  # Frequency"""
,
"Index of 2: 1\nCount of 2: 3")

# ----------------------------------------

    # 4) Sorting & Reversing
    print_sub_heading("4) Sorting & Reversing")
    display_note("These methods change the order of elements.")
    display_note("sort(): In-place (modifies original list), Returns None, Works with homogeneous types, ")
    display_note("Stable sort (equal elements retain their original order)", message_continue=True)
    display_note("Use to sort numbers, strings, or objects by custom rules like length or case-insensitive comparison.")
    display_note("Use `sorted()` instead of sort() when you need to keep the original list unchanged.","tip")
    display_note("'reverse()`: In-place, Returns None, Stable, List-only (Only works on lists, not work in tuples, sets, or strings)")
    display_note("Use reversed() with list() if want a reversed copy without modifying original, or reverse any iterable(strings, tuples, etc.)","tip")
    show_code_with_output("""# sort(key=None, reverse=False)) & Reversing
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
print(f"Reversed list: {nums}")"""
,
"Sorted list: [1, 2, 4, 5]\nSorted in reverse: [5, 4, 2, 1]\nSorted by length of string: ['date', 'apple', 'banana', 'cherry']\nReversed list: [1, 2, 4, 5]")

# ----------------------------------------

    # 5) Copying
    print_sub_heading("5) Copying Lists")
    display_note("Use `copy()` to clone a list without linking it to the original.")
    show_code_with_output("""# Copying Lists
original = [10, 20, 30]
copied = original.copy()
original.append(40)
print(f"Original: {original}")
print(f"Copied: {copied}")"""
,
"Original: [10, 20, 30, 40]\nCopied: [10, 20, 30]")
