from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Searching, Indexing and Replacing Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main(topic_number: int):
    print_heading("String Searching, Indexing and Replacing Methods Demo", topic_number)

    # -------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1) String Searching and Indexing Methods")
    # -------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("'find/rfind(substring[, start[, end]])' and 'index/rindex(substring[, start[, end]])'method:")
    display_note("""'find()': It returns index of the first/last occurrence of 'substring' in the string,, if not found, returns -1
'index()': It is similar to 'find()', but it raises a ValueError if the substring is not found.
The 'start' and 'end' arguments are optional and specify the range within which to search for the substring.""")
    display_note("Use 'find()' if you're okay with not finding a match (non-breaking), Use index() if the match must exist, and you want to catch errors","TIP")
    code1 = '''# sample code
string2 = "Hello, World! Hello, Python!"
print(f"Finding 'Hello' first occurance by 'find()' method in '{string2}' string: {string2.find('Hello')}")
print(f"Finding 'Hello' first occurance in '{string2}' from index 1 to 10: {string2.find('Hello', 1, 10)}")
print(f"Finding 'Hello' last occurance by 'rfind()' method in '{string2}' string: {string2.rfind('Hello')}")
print(f"Finding 'Java' first occurance by 'find()' method in '{string2}' string: {string2.find('Java')}")
print(f"Finding 'Hello' first occurance by 'index()' method in '{string2}' string: {string2.index('Hello')}")
try:
    print(f"Finding 'Java' in '{string2}' string: {string2.index('Java')}")
except ValueError as e:
    print(f"Error: {e}")
#-------------------------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("count(substring[, start[, end]]) method:",True)
    display_note("""The 'count(substring, start, end)' method returns the number of occurrences of 'substring' in the string.
The 'start' and 'end' arguments are optional and specify the range within which to count the occurrences, 
If not provided, the entire string is searched.
It performs case-sensitive, non-overlapping ['aaa'.count(aa) → 1] counts, and returns 0 if the substring is not found.""")
    code2 = '''# sample code
string2 = "Hello, World! Hello, Python!"
print(f"Counting occurrences of 'Hello' in '{string2}' string: {string2.count('Hello')}")
print(f"Counting occurrences of 'H' in '{string2}' string from index 2 to 10: {string2.count('H', 2, 10)}")
print(f"Counting occurrences of 'Java' in '{string2}' string: {string2.count('Java')}")
#----------------------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    print_small_sub_heading("startswith(prefix[, start[, end]]) and endswith(suffix[, start[, end]]) methods:",True)
    display_note("""Checks if string 'starts/ends' with the specified 'prefix'/'suffix', returning True/False.
'start' and 'end' arguments are optional and specify the range within which to check for the prefix/suffix.
These methods can also take a tuple of prefixes/suffixes to check against, returning True if any match is found.""")
    code3 = '''# sample code
string1 = "Hello, World!"
print(f"Checking if '{string1}' starts with 'Hello': {string1.startswith('Hello')}")
print(f"Checking if '{string1}' ends with 'World!': {string1.endswith('World!')}")
print(f"Checking if '{string1}' starts with 'World' from index 7 to end: {string1.startswith('World', 7)}")
# taking tuple of prefixes as arg
print(f"Checking if '{string1}' starts with any of ('Hello', 'Hi'): {string1.startswith(('Hello', 'Hi'))}")
#----------------------------------------------------------------------------------------------------------#'''          
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

   # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2) String Replacement Methods")
   # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_small_sub_heading("replace(old, new[, count]) method:")
    display_note("""'replace(old, new, count)': replaces all occurrences of 'old' substring with 'new' substring in the string.
The 'count' argument is optional and specifies the maximum number of replacements to make, if not provided, all occurrences are replaced.""")
    display_note("""replace() perform case-sensitive operation i.e 'apples'≠'Apples', and it does not change the original string it returns a new string""","WARNING")
    code4 = '''# sample code
string2 = "Hello, World! Hello, Python!"
print(f"Replacing 'Hello' with 'Hi' in '{string2}' string: {string2.replace('Hello', 'Hi')}")
print(f"Replacing 'Hello' with 'Hi' in '{string2}' string with count=1: {string2.replace('Hello', 'Hi', 1)}")
print(f"Chain replacement in '2025-07-02' to change it to '02/07/25': ", end="") 
print('2025-07-02'.replace('-', '/').replace('2025', '25'))
#------------------------------------------------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)