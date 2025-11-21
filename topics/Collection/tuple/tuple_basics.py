from helpers.display_utils import *

# ----------------------------------------
# 📘 Python Tuples: Basic Concepts
# ----------------------------------------

def main(topic_number: int):
    print_heading("Tuples Basic Concepts", topic_number)
    imp_note_point = '''- Tuple itself is immutable, it annot be modified after it's created, You can't add, remove, or reorder elements.
- Tuple elements may or may not be immutable, it can be mutable if you put a mutable object (like a list or dictionary) inside the tuple.'''
    imp_note_points(imp_note_point)

    #------------------------------------------------------------------------------------------------------------------
    # 1) Creating Tuples
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Creating Tuples")
    display_note("Tuples are ordered, immutable collections and store homo or heterogenous elements.")
    code1 = """# Creating Tuples
t1 = (1, 2, 3)
t2 = "apple", "banana", "cherry"  # No parentheses, still a tuple

single_element = (5,)  # Single-element tuple requires a trailing comma
empty_tuple = ()
print(f"Tuple t1: {t1}")
print(f"Tuple t2: {t2}")
print(f"Single-element tuple: {single_element}")
print(f"Empty element tuple: {empty_tuple}")

t = ([1, 2], [3, 4])  # Tuple of lists (mutable elements)
t[0].append(999)      # This is allowed— modifying the list inside
print(t)            # Output: ([1, 2, 999], [3, 4])
#------------------------------------------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    #------------------------------------------------------------------------------------------------------------------
    # 2) Accessing Tuple Elements
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Accessing Tuple Elements")
    display_note("You can access elements using indexing, just like lists.")
    code2 = """# Accessing Tuple Elements
fruits = ("apple", "banana", "cherry")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
#--------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    #------------------------------------------------------------------------------------------------------------------
    # 3) Tuple Unpacking
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3) Tuple Unpacking")
    display_note("Unpacking allows you to assign tuple values to multiple variables in one line.")
    code3 = """# Tuple Unpacking
data = ("John", 28, "Developer")
name, age, job = data
print(f"Name: {name}, Age: {age}, Job: {job}")
#----------------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


    #------------------------------------------------------------------------------------------------------------------
    # 4) Tuple Concatenation
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4) Tuple Concatenation")
    display_note("You can concatenate two tuples using the '+' operator to form a new tuple.")
    code4 = """# Tuple Concatenation
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2
print(f"Concatenated tuple: {result}")
#--------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)


    #------------------------------------------------------------------------------------------------------------------
    # 5) Tuple Repetition
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5) Tuple Repetition")
    display_note("You can repeat a tuple multiple times using the '*' operator.")
    code5 = """# Tuple Repetition
t = ('a', 'b')
result = t * 3
print(f"Repeated tuple: {result}")
#---------------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)


    #------------------------------------------------------------------------------------------------------------------
    # 6) Tuple Slicing
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("6) Tuple Slicing")
    display_note("You can extract a subpart of a tuple using slicing just like lists.")
    code6 = """# Tuple Slicing
t = (10, 20, 30, 40, 50)
result = t[1:4]
print(f"Sliced tuple: {result}")
#--------------------------------#"""
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)


    #------------------------------------------------------------------------------------------------------------------
    # 7) Tuples in Sets
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("7) Tuples in Sets")
    display_note("Since tuples are immutable and hashable, they can be added to sets unlike lists.")
    code7 = """# Tuples in Sets
s = set()
s.add((1, 2))
s.add((3, 4))
print(f"Set with tuples: {s}")
#------------------------------#"""
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)


    #------------------------------------------------------------------------------------------------------------------
    # 8) Tuples as Dictionary Keys
    #------------------------------------------------------------------------------------------------------------------
    print_sub_heading("8) Tuples as Dictionary Keys")
    display_note("Tuples can be used as dictionary keys because they are immutable and hashable.")
    code8 = """# Tuples as Dictionary Keys
location_data = {
    ('New York', 'USA'): 8419000,
    ('Tokyo', 'Japan'): 13960000
}
print(f"Population of Tokyo: {location_data[('Tokyo', 'Japan')]}")
#------------------------------------------------------------------#"""
    output8 = run_code_snippet(code8)
    show_code_with_output(code8, output8)   
