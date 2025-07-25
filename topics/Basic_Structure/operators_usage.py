from helpers.display_utils import *

def main():
    print_heading("Python Operators and their use")

    # 1) Arithmetic Operators
    print_sub_heading("1) Arithmetic Operators")
    display_note("Arithmetic operators perform mathematical operations like +, -, *, /, %, etc.")
    show_code_with_output('''# Arithmetic Operators
a = 10
b = 3
print(f"Sum of {a} and {b} using '+' operator is: {a + b}")
print(f"Difference of {a} and {b} using '-' operator is: {a - b}")
print(f"Product of {a} and {b} using '*' operator is: {a * b}")
print(f"Division of {a} by {b} using '/' operator is: {a / b}")
print(f"Remainder of {a} divided by {b} using '%' operator is: {a % b}")
print(f"{a} raised to the power of {b} using '**' operator is: {a ** b}")
print(f"Floor division of {a} by {b} using '//' operator is: {a // b}")'''
,
"""Sum of 10 and 3 using '+' operator is: 13
Difference of 10 and 3 using '-' operator is: 7
Product of 10 and 3 using '*' operator is: 30
Division of 10 by 3 using '/' operator is: 3.3333333333333335
Remainder of 10 divided by 3 using '%' operator is: 1
10 raised to the power of 3 using '**' operator is: 1000
Floor division of 10 by 3 using '//' operator is: 3""")

    # 2) Assignment Operators
    print_sub_heading("2) Assignment Operators")
    display_note("Assignment operators assign values using =, +=, -=, *=, etc.")
    show_code_with_output('''# Assignment Operators
x = 5
print(f"Initial value of x is: {x}")
x += 3
print(f"After 'x += 3', x becomes: {x}")
x -= 2
print(f"After 'x -= 2', x becomes: {x}")
x *= 4
print(f"After 'x *= 4', x becomes: {x}")
x /= 2
print(f"After 'x /= 2', x becomes: {x}")
x %= 3
print(f"After 'x %= 3', x becomes: {x}")'''
,
"""Initial value of x is: 5
After 'x += 3', x becomes: 8
After 'x -= 2', x becomes: 6
After 'x *= 4', x becomes: 24
After 'x /= 2', x becomes: 12.0
After 'x %= 3', x becomes: 0.0""")

    # 3) Comparison Operators
    print_sub_heading("2) Comparison Operators")
    display_note("Used to compare two values: ==, !=, >, <, >=, <=")
    show_code_with_output('''# Comparison Operators
a = 5
b = 3
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")'''
,
"""5 == 3: False
5 != 3: True
5 > 3: True
5 < 3: False
5 >= 3: True
5 <= 3: False""")

    # 4) Logical Operators
    print_sub_heading("3) Logical Operators")
    display_note("Used to combine conditional statements: and, or, not")
    show_code_with_output(''' # Logical Operators
x = True
y = False
print(f"{x} and {y} = {x and y}")
print(f"{x} or {y} = {x or y}")
print(f"not {x} = {not x}")'''
,
"""True and False = False
True or False = True
not True = False""")

    # 5) Identity Operators
    print_sub_heading("4) Identity Operators")
    display_note("Used to compare object identities: is, is not")
    show_code_with_output(''' # Identity Operators
a = [1, 2]
b = a
c = [1, 2]
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a is not c: {a is not c}")''',
"""a is b: True
a is c: False
a is not c: True""")

    # 6) Membership Operators
    print_sub_heading("5) Membership Operators")
    display_note("Used to check if a value is in a sequence: in, not in")
    show_code_with_output('''# Membership Operators
nums = [1, 2, 3, 4]
print(f"2 in nums: {2 in nums}")
print(f"5 not in nums: {5 not in nums}")'''
,
"""2 in nums: True
5 not in nums: True""")

    # 7) Bitwise Operators
    print_sub_heading("6) Bitwise Operators")
    display_note("Used to perform bit-level operations: &, |, ^, ~, <<, >>")
    show_code_with_output('''# Bitwise Operators
a = 5  # 0101
b = 3  # 0011
print(f"{a} & {b} = {a & b} (Bitwise AND)")
print(f"{a} | {b} = {a | b} (Bitwise OR)")
print(f"{a} ^ {b} = {a ^ b} (Bitwise XOR)")
print(f"~{a} = {~a} (Bitwise NOT)")
print(f"{a} << 1 = {a << 1} (Left shift by 1)")
print(f"{a} >> 1 = {a >> 1} (Right shift by 1)")'''
,
"""5 & 3 = 1 (Bitwise AND)
5 | 3 = 7 (Bitwise OR)
5 ^ 3 = 6 (Bitwise XOR)
~5 = -6 (Bitwise NOT)
5 << 1 = 10 (Left shift by 1)
5 >> 1 = 2 (Right shift by 1)""")