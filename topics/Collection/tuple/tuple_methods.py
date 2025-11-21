from helpers.display_utils import *

# ----------------------------------------
# 📘 Tuple Methods in Python
# ----------------------------------------
def main(topic_number: int):
    print_heading("Tuple Methods in Python", topic_number)

    # --------------------------------------------------------------------------
    # 1) count()
    # --------------------------------------------------------------------------
    print_sub_heading("1) count()")
    display_note("Returns the number of times a specified value occurs in the tuple.")
    code1 = """# count()
items = (1, 2, 2, 3, 2, 4)
print(f"Count of 2 in items: {items.count(2)}")
#-----------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    # --------------------------------------------------------------------------
    # 2) index()
    # --------------------------------------------------------------------------
    print_sub_heading("2) index()")
    display_note("Returns the index of the first occurrence of a specified value.")
    display_note("Raises ValueError if the value is not found.")
    code2 = """# index()
letters = ('a', 'b', 'c', 'd', 'b')
print(f"Index of 'b': {letters.index('b')}")
#-------------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # --------------------------------------------------------------------------
    # 3) Modification
    # --------------------------------------------------------------------------
    print_sub_heading("⚠️ Tuples are Immutable")
    display_note("Tuples do not support item assignment, appending, or removal. Methods like append(), remove(), or pop() are not available.")
    code1 = """# Tuples are Immutable
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10  # Attempting to modify tuple
except TypeError as e:
    print(f"Error: {e}")
#--------------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)