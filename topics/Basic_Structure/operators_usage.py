from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Python Operators and their use", topic_number)
    
    #---------------------------------------------------------------------------------------------------------------------
    # 1) Arithmetic Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) Arithmetic Operators")
    display_note("Arithmetic operators perform mathematical operations like +, -, *, /, %, etc.")
    code1 ='''# Arithmetic Operators
a = 10
b = 3
print(f"Sum of '{a}' and '{b}' using '+' operator is: {a + b}")
print(f"Difference of '{a}' and '{b}' using '-' operator is: {a - b}")
print(f"Product of '{a}' and '{b}' using '*' operator is: {a * b}")
print(f"Division of '{a}' by '{b}' using '/' operator is: {a / b}")
print(f"Remainder of '{a}' divided by '{b}' using '%' operator is: {a % b}")
print(f"'{a}' raised to the power of '{b}' using '**' operator is: {a ** b}")
print(f"Floor division of '{a}' by '{b}' using '//' operator is: {a // b}")
#-----------------------------------------------------------------------------'''

    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    #---------------------------------------------------------------------------------------------------------------------
    # 2) Assignment Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Assignment Operators")
    display_note("Assignment operators assign values using =, +=, -=, *=, etc.")
    code2 = '''# Assignment Operators
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
print(f"After 'x %= 3', x becomes: {x}")
#----------------------------------------'''

    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    #---------------------------------------------------------------------------------------------------------------------
    # 3) Comparison Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) Comparison Operators")
    display_note("Used to compare two values: ==, !=, >, <, >=, <=")
    code3 = '''# Comparison Operators
a = 5
b = 3
print(f"IS '{a} == {b}': {a == b}")
print(f"IS '{a} != {b}': {a != b}")
print(f"IS '{a} > {b}': {a > b}")
print(f"IS '{a} < {b}': {a < b}")
print(f"IS '{a} >= {b}': {a >= b}")
print(f"IS '{a} <= {b}': {a <= b}")
#-----------------------------------'''

    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #---------------------------------------------------------------------------------------------------------------------
    # 4) Logical Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3) Logical Operators")
    display_note("Used to combine conditional statements: and, or, not")
    code4 = ''' # Logical Operators
x = True
y = False
print(f"Result of '{x} and {y}' = {x and y}")
print(f"Result of '{x} or {y}' = {x or y}")
print(f"Result of 'not {x}' = {not x}")
#---------------------------------------------'''
    
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    #---------------------------------------------------------------------------------------------------------------------
    # 5) Identity Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4) Identity Operators")
    display_note("Used to compare object identities: is, is not")
    code5 = ''' # Identity Operators
a = [1, 2]
b = a
c = [1, 2]
print(f"'a' is 'b': {a is b}")
print(f"'a' is 'c': {a is c}")
print(f"'a' is not 'c': {a is not c}")
#--------------------------------------'''

    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)
    
    #---------------------------------------------------------------------------------------------------------------------
    # 6) Membership Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5) Membership Operators")
    display_note("Used to check if a value is in a sequence: in, not in")
    code6 = '''# Membership Operators
nums = [1, 2, 3, 4]
print(f"2 in 'nums': {2 in nums}")
print(f"5 not in 'nums': {5 not in nums}")
#------------------------------------------'''

    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    #---------------------------------------------------------------------------------------------------------------------
    # 7) Bitwise Operators
    #---------------------------------------------------------------------------------------------------------------------
    print_sub_heading("6) Bitwise Operators")
    display_note("Used to perform bit-level operations: &, |, ^, ~, <<, >>")
    code7 = '''# Bitwise Operators
a = 5  # 0101
b = 3  # 0011
print(f"'{a}' & '{b}' = {a & b} (Bitwise AND)")
print(f"'{a}' | '{b}' = {a | b} (Bitwise OR)")
print(f"'{a}' ^ '{b}' = {a ^ b} (Bitwise XOR)")
print(f"'~{a}' = {~a} (Bitwise NOT)")
print(f"'{a}' << 1 = {a << 1} (Left shift by 1)")
print(f"'{a}' >> 1 = {a >> 1} (Right shift by 1)")
#--------------------------------------------------'''

    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)