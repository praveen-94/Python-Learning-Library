from helpers.display_utils import *

# ----------------------------------------
# 📘 Tuple Methods in Python
# ----------------------------------------
def main():
    print_heading("Tuple Methods in Python")
    print_sub_heading("1) count()")
    display_note("Returns the number of times a specified value occurs in the tuple.")
    show_code_with_output("""# count()
items = (1, 2, 2, 3, 2, 4)
print(f"Count of 2 in items: {items.count(2)}")"""
,
"Count of 2 in items: 3")

# ----------------------------------------

    print_sub_heading("2) index()")
    display_note("Returns the index of the first occurrence of a specified value.")
    display_note("Raises ValueError if the value is not found.")
    show_code_with_output("""# index()
letters = ('a', 'b', 'c', 'd', 'b')
print(f"Index of 'b': {letters.index('b')}")"""
,
"Index of 'b': 1")

# ----------------------------------------

    print_sub_heading("⚠️ Tuples are Immutable")
    display_note("Tuples do not support item assignment, appending, or removal. Methods like append(), remove(), or pop() are not available.")
    show_code_with_output("""# Tuples are Immutable
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10  # Attempting to modify tuple
except TypeError as e:
    print(f"Error: {e}")"""
,
"Error: 'tuple' object does not support item assignment")
