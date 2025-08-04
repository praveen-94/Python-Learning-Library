from helpers.display_utils import *

# -----------------------------------------------------------------------------------------------------------------------------------------------
# String Searching, Indexing and Replacing Methods Demo
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print_heading("String Searching, Indexing and Replacing Methods Demo")

    print_sub_heading("1) String Searching and Indexing Methods")
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    string1 = "Hello, world!"
    string2 = "Hello, World! Hello, Python!"
    print_small_sub_heading("'find/rfind(substring[, start[, end]])' and 'index/rindex(substring[, start[, end]])'method:")
    display_note("'find()' methods returns the index of the first/last occurrence of 'substring' in the string, if not found, it returns -1")
    display_note("'index()'method are similar to 'find()', but they raises a ValueError if the substring is not found.")
    display_note("The 'start' and 'end' arguments are optional and specify the range within which to search for the substring.")
    display_note("Use 'find()' if you're okay with not finding a match (non-breaking), ")
    display_note("Use index() if the match must exist, and you want to catch errors","TIP", message_continue=True)
    show_code_with_output('''string2 = "Hello, World! Hello, Python!"
print(f"Finding 'Hello' first occurance by 'find()' method in '{string2}' string: {string2.find('Hello')}")
print(f"Finding 'Hello' first occurance by 'find()' in '{string2}' string from index 1 to 10: {string2.find('Hello', 1, 10)}")
print(f"Finding 'Hello' last occurance by 'rfind()' method in '{string2}' string: {string2.rfind('Hello')}")
print(f"Finding 'Java' first occurance by 'find()' method in '{string2}' string: {string2.find('Java')}")
print(f"Finding 'Hello' first occurance by 'index()' method in '{string2}' string: {string2.index('Hello')}")
try:
    print(f"Finding 'Java' in '{string2}' string: {string2.index('Java')}")
except ValueError as e:
    print(f"Error: {e}")'''
,
"Finding 'Hello' first occurance by 'find()' method in '" + string2 + "' string: " + str(string2.find('Hello')) + "\n" +
"Finding 'Hello' first occurance by 'find()' in '" + string2 + "' string from index 1 to 10: " + str(string2.find('Hello', 1, 10)) + "\n" +
"Finding 'Hello' last occurance by 'rfind()' method in '" + string2 + "' string: " + str(string2.rfind('Hello')) + "\n" +
"Finding 'Java' first occurance by 'find()' method in '" + string2 + "' string: " + str(string2.find('Java')) + "\n" +
"Finding 'Hello' first occurance by 'index()' method in '" + string2 + "' string: " + str(string2.index('Hello')) + "\n" +
"Error: " + str(ValueError("substring not found")))

    print_small_sub_heading("count(substring[, start[, end]]) method:",True)
    display_note("The 'count(substring, start, end)' method returns the number of occurrences of 'substring' in the string")
    display_note("The 'start' and 'end' arguments are optional and specify the range within which to count the occurrences.")
    display_note("If not provided, the entire string is searched.", message_continue=True)
    display_note("it performs case-sensitive, non-overlapping ['aaa'.count(aa) → 1] counts, and returns 0 if the substring is not found.")
    show_code_with_output('''string2 = "Hello, World! Hello, Python!"
print(f"Counting occurrences of 'Hello' in '{string2}' string: {string2.count('Hello')}")
print(f"Counting occurrences of 'H' in '{string2}' string from index 2 to 10: {string2.count('H', 2, 10)}")
print(f"Counting occurrences of 'Java' in '{string2}' string: {string2.count('Java')}")'''
,
"Counting occurrences of 'Hello' in '" + string2 + "' string: " + str(string2.count('Hello')) + "\n" +
"Counting occurrences of 'H' in '" + string2 + "' string from index 2 to 10: " + str(string2.count('H', 2, 10)) + "\n" +
"Counting occurrences of 'Java' in '" + string2 + "' string: " + str(string2.count('Java')))

    print_small_sub_heading("startswith(prefix[, start[, end]]) and endswith(suffix[, start[, end]]) methods:",True)
    display_note("'startswith()/endswith()' method checks if string 'starts/ends' with the specified 'prefix'/'suffix', returning True/False.")
    display_note("start' and 'end' arguments are optional and specify the range within which to check for the prefix/suffix.")
    show_code_with_output(''''string1 = "Hello, World!"
print(f"Checking if '{string1}' starts with 'Hello': {string1.startswith('Hello')}")
print(f"Checking if '{string1}' ends with 'World!': {string1.endswith('World!')}")
print(f"Checking if '{string1}' starts with 'World' from index 7 to end: {string1.startswith('World', 7)}")
#these methods can also take a tuple of prefixes/suffixes to check against, returning True if any match is found."
print(f"Checking if '{string1}' starts with any of ('Hello', 'Hi'): {string1.startswith(('Hello', 'Hi'))}")'''  
,
"Checking if '" + string1 + "' starts with 'Hello': " + str(string1.startswith('Hello')) + "\n" +
"Checking if '" + string1 + "' ends with 'World!': " + str(string1.endswith('World!')) + "\n" +
"Checking if '" + string1 + "' starts with 'World' from index 7 to end: " + str(string1.startswith('World', 7)) + "\n" +
"Checking if '" + string1 + "' starts with any of ('Hello', 'Hi'): " + str(string1.startswith(('Hello', 'Hi'))))        

    print_sub_heading("2) String Replacement Methods")
    print_small_sub_heading("replace(old, new[, count]) method:")
    display_note("The 'replace(old, new, count)' method replaces all occurrences of 'old' substring with 'new' substring in the string.")
    display_note("The 'count' argument is optional and specifies the maximum number of replacements to make.")
    display_note("If not provided, all occurrences are replaced.", message_continue=True)
    display_note("replace() perform case-sensitive operation i.e","WARNING")
    display_note("'apples'≠'Apples', and it does not change the original string it returns a new string","WARNING", message_continue=True)
    show_code_with_output('''string2 = "Hello, World! Hello, Python!"
print(f"Replacing 'Hello' with 'Hi' in '{string2}' string: {string2.replace('Hello', 'Hi')}")
print(f"Replacing 'Hello' with 'Hi' in '{string2}' string with count=1: {string2.replace('Hello', 'Hi', 1)}")
print(f"Chain replacement in '2025-07-02' to change it to '02/07/25': {'2025-07-02'.replace('-', '/').replace('2025', '25')}")'''
,
"Replacing 'Hello' with 'Hi' in '" + string2 + "' string: " + string2.replace('Hello', 'Hi') + "\n" +
"Replacing 'Hello' with 'Hi' in '" + string2 + "' string with count=1: " + string2.replace('Hello', 'Hi', 1) + "\n" +
"Chain replacement in '2025-07-02' to change it to '02/07/25': " + '2025-07-02'.replace('-', '/').replace('2025', '25'))