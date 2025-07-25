from helpers.display_utils import *

# ----------------------------------------
# 📘 Built-in Functions That Work on Iterables (Lists, Tuples, Sets)
# ----------------------------------------

def main():
    print_heading("Built-in Functions That Work on Iterables")
    display_note("These built-in functions work with all iterables like lists, tuples, sets.")

    print_sub_heading("1) Basic Aggregate Functions")
    display_note("`sum()` works only with numeric iterables and not with strings.", "warning")
    show_code_with_output("""# Basic Aggregate Functions
nums = [4, 2, 8, 6]
print(f"Length: {len(nums)}")
print(f"Sum: {sum(nums)}")
print(f"Minimum: {min(nums)}")
print(f"Maximum: {max(nums)}")"""
,
"Length: 4\nSum: 20\nMinimum: 2\nMaximum: 8")

# ----------------------------------------

    print_sub_heading("2) Boolean Test Functions")
    display_note("`any()` returns True if any item is true. `all()` returns True if all items are true.")
    display_note("Works well for truthy values like numbers, booleans, and non-empty strings.")
    show_code_with_output("""#  Boolean Test Functions
flags = [True, False, True]
print(f"any(flags): {any(flags)}")
print(f"all(flags): {all(flags)}")"""
,
"any(flags): True\nall(flags): False")

# ----------------------------------------

    print_sub_heading("3) enumerate()")
    display_note("`enumerate()` returns index-value pairs when looping through an iterable.")
    display_note("Useful when you need both index and item during iteration.","tip")
    show_code_with_output("""# enumerate
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")"""
,
"0: apple\n1: banana\n2: cherry")

# ----------------------------------------

    print_sub_heading("4) zip()")
    display_note("`zip()` combines multiple iterables element-wise into tuples.")
    display_note("If lengths are unequal, `zip()` stops at the shortest iterable.", "warning")
    display_note("Use `itertools.zip_longest()` to handle different lengths with a fill value.")
    show_code_with_output("""# Zip
names = ["Alice", "Bob", "Charlie", "Darth"]
ages = [25, 30, 22, 56]
height = [5.4, 5.8, 4.7]
combined = list(zip(names, ages, height))
print(f"Zipped result: {combined}")

from itertools import zip_longest
long_combined = list(zip(names, ages, height, fillvalue="N/A"))
print(f"long zipped result: {long_combined}")"""
,
"Zipped result: [('Alice', 25, 5.4), ('Bob', 30, 5.8), ('Charlie', 22, 4.7)]\n" +
"long zipped result: [('Alice', 25, 5.4), ('Bob', 30, 5.8), ('Charlie', 22, 4.7), ('Darth', 56, 'N/A')]")

# ----------------------------------------

    print_sub_heading("5) reversed()")
    display_note("`reversed()` returns a reverse iterator. Use `list()` to view the result.")
    display_note("Does not work directly on unordered types like sets.", "warning")
    show_code_with_output("""# reversed
numbers = [1, 2, 3, 4]
reversed_list = list(reversed(numbers))
print(f"Reversed list: {reversed_list}")"""
,
"Reversed list: [4, 3, 2, 1]")

