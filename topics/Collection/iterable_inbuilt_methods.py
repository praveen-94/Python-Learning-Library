from helpers.display_utils import *

# --------------------------------------------------------------------------------------------------------
# 📘 Built-in Functions That Work on Iterables (Lists, Tuples, Sets)
# ---------------------------------------------------------------------------------------------------------

def main(topic_number: int):
    print_heading("Built-in Functions That Work on Iterables", topic_number)
    display_note("These built-in functions work with all iterables like lists, tuples, sets.")

    # -----------------------------------------------------------------------------------------
    # 1) Basic Aggregate Functions
    # -----------------------------------------------------------------------------------------
    print_sub_heading("1) Basic Aggregate Functions")
    display_note("`sum()` works only with numeric iterables and not with strings.", "warning")
    code1 = """# Basic Aggregate Functions
nums = [4, 2, 8, 6]
print(f"Length: {len(nums)}")
print(f"Sum: {sum(nums)}")
print(f"Minimum: {min(nums)}")
print(f"Maximum: {max(nums)}")
#------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------
    # 2) Boolean Test Functions
    # -----------------------------------------------------------------------------------------
    print_sub_heading("2) Boolean Test Functions")
    display_note("""`any()` returns True if any item is true. `all()` returns True if all items are true.
Works well for truthy values like numbers, booleans, and non-empty strings.""")
    code2 = """#  Boolean Test Functions
flags = [True, False, True]
print(f"any(flags): {any(flags)}")
print(f"all(flags): {all(flags)}")
#----------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -----------------------------------------------------------------------------------------
    # 3) enumerate()
    # -----------------------------------------------------------------------------------------
    print_sub_heading("3) enumerate()")
    display_note("`enumerate()` returns index-value pairs when looping through an iterable.")
    display_note("Useful when you need both index and item during iteration.","tip")
    code3 = """# enumerate
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")
#--------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------------------
    # 4) zip()
    # -------------------------------------------------------------------------------------------
    print_sub_heading("4) zip()")
    display_note("`zip()` combines multiple iterables element-wise into tuples.")
    display_note("""If lengths are unequal, `zip()` stops at the shortest iterable.
itertools.zip_longest():
Use `itertools.zip_longest()` to handle different lengths with a fill value.
This function from the 'itertools' module does support a fillvalue argument, allowing you to pad shorter iterables.""", "warning")
    code4 = """# Zip
names = ["Alice", "Bob", "Charlie", "Darth"]
ages = [25, 30, 22, 56]
height = [5.4, 5.8, 4.7]
combined = list(zip(names, ages, height))
print(f"Zipped result: {combined}")

from itertools import zip_longest
long_combined = list(zip_longest(names, ages, height, fillvalue="N/A"))
print(f"long zipped result: {long_combined}")
#---------------------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)


    # --------------------------------------------------------------------------------------------
    # 5) reversed()
    # --------------------------------------------------------------------------------------------
    print_sub_heading("5) reversed()")
    display_note("`reversed()` returns a reverse iterator. Use `list()` to view the result.")
    display_note("Does not work directly on unordered types like sets.", "warning")
    code5 = """# reversed
numbers = [1, 2, 3, 4]
reversed_list = list(reversed(numbers))
print(f"Reversed list: {reversed_list}")
#----------------------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)