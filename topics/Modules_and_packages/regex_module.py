# re_module_deep_dive.py

from helpers.display_utils import *
import re

def main(topic_number: int):
    print_heading("The `re` Module: Regular Expressions (Regex)", topic_number)
    imp_note_points("""
- A regular expression, or regex, is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- The ___re___ module is Python's built-in package for working with regular expressions.
- It is extremely powerful for tasks like data validation (e.g., checking email formats), web scraping, and complex string parsing.
- Regex syntax can be complex, but mastering the basics is a valuable skill for any programmer.
- It's good practice to use raw strings ___(r"...")___ for regex patterns to prevent backslashes from being interpreted as escape sequences by Python.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Core Matching Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Core Matching Functions")
    display_note("These are the primary functions you'll use to search for patterns in strings.")

    print_small_sub_heading("a) re.search(pattern, string)", True)
    display_note("Scans through a string, looking for the 'first' location where the regex pattern produces a match.If found, it returns a 'match object'; otherwise, it returns `None`.")
    code1 = '''# Find the first email address in a string
import re
text = "You can contact me at info@example.com for more details."
# This pattern looks for an email-like structure
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}' 
match = re.search(pattern, text)
print("Checking if any email matches:", match)
#---------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("b) Understanding the Match Object", True)
    display_note("The match object returned by `re.search` and `re.match` contains information about the match.")
    display_note("`.group()` returns the actual matched string. `.start()` and `.end()` give the start/end indices.", "tip")
    code2 = '''# Extracting info from the match object
import re
text = "You can contact me at info@example.com for more details."
match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}', text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"Start Index: {match.start()}") 
    print(f"End Index: {match.end()}")
    print(f"Span: {match.span()}")
#--------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    print_small_sub_heading("c) re.match(pattern, string)", True)
    display_note("This function only attempts to match the pattern at the *beginning* of the string. If the pattern doesn't start at index 0, it returns `None`.")
    code3 = '''# Trying to match at the beginning of the string
import re
text = "Python is powerful"
# This pattern will match because the string starts with 'Python' 
match1 = re.match(r'Python', text)
print(f"Match for 'Python': {match1}")

# This pattern will fail because 'powerful' is not at the start
match2 = re.match(r'powerful', text)
print(f"Match for 'powerful': {match2}")
#-----------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Finding All Matches and Substituting
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Finding All Matches and Substituting")

    print_small_sub_heading("a) re.findall(pattern, string)", True)
    display_note("Finds all non-overlapping matches of the pattern in the string and returns them as a list of strings.")
    code4 = '''# Find all order numbers in a string
import re
text = "Order numbers are 123-456, 789-012, and 345-678."
# \\d{{3}} matches exactly three digits
all_numbers = re.findall(r'\\d{3}-\\d{3}', text) 
print(f"All order numbers found: {all_numbers}")
#----------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    print_small_sub_heading("b) re.sub(pattern, repl, string)", True)
    display_note("Finds all occurrences of the pattern and replaces them with the string `repl`.")
    code5 = '''# Replace all agent names in a string
import re
text = "Please contact agent Smith or agent Jones for help."
# \\w+ matches one or more word characters (letters, numbers, underscore) 
censored_text = re.sub(r'agent \\w+', '[REDACTED]', text)
print(f"Censored text: {censored_text}")
#-------------------------------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Compiling Patterns for Efficiency
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Compiling Patterns for Efficiency")
    display_note("If you are going to use same regex pattern multiple times, it is more efficient to compile it first using `re.compile()`.")
    display_note("The compiled pattern object has methods like .search(), .findall(), etc., so you don't have to pass the pattern each time.", "tip")
    code6 = '''# Compile a pattern for reuse
import re
email_pattern = re.compile(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b')

# Use the compiled pattern on multiple strings
text1 = "Valid email: test@example.org"
text2 = "Invalid email: not-an-email"

print("Searching in valid mail in '{text1}':", end=" ")
print(f"{email_pattern.search(text1).group(0) if email_pattern.search(text1) else None}")
print("Searching in valid mail in '{text2}':", end=" ")
print(f"{email_pattern.search(text2).group(0) if email_pattern.search(text2) else None}")
#----------------------------------------------------------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Using Flags for Modified Behavior
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Using Flags for Modified Behavior")
    display_note("Flags can modify how a pattern is interpreted. One of the most common is `re.IGNORECASE`.")

    print_small_sub_heading("a) re.IGNORECASE or re.I")
    display_note("This flag makes the pattern matching case-insensitive.")    
    code7 = '''# Demonstrating case-insensitive matching
import re
text = "Python is a language. I love python."

# Case-sensitive search (will only find the second 'python')
print("Checking 'python' in a case-sensitive manner:")
match1 = re.search(r'python', text)
print("Case-sensitive found:", end=" ")
print(f"{match1.group(0) if match1 else None} at index {match1.start() if match1 else 'N/A'}")

# Case-insensitive search (will find the first 'Python')
print("Checking 'python' in a case-insensitive manner:")
match2 = re.search(r'python', text, re.IGNORECASE)
print("Case-insensitive found:")
print(f"{match2.group(0) if match2 else None} at index {match2.start() if match2 else 'N/A'}")
#------------------------------------------------------------------------------------------------#'''
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)
    

if __name__ == "__main__":
    main(1)
