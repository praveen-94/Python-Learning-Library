# re_module_deep_dive.py

from helpers.display_utils import *
import re

def main():
    print_heading("The `re` Module: Regular Expressions (Regex)")
    imp_note_points("""
- A regular expression, or regex, is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- The `re` module is Python's built-in package for working with regular expressions.
- It is extremely powerful for tasks like data validation (e.g., checking email formats), web scraping, and complex string parsing.
- Regex syntax can be complex, but mastering the basics is a valuable skill for any programmer.
- It's good practice to use raw strings (`r"..."`) for regex patterns to prevent backslashes from being interpreted as escape sequences by Python.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Core Matching Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Core Matching Functions")
    display_note("These are the primary functions you'll use to search for patterns in strings.")

    print_small_sub_heading("a) re.search(pattern, string)",True)
    display_note("Scans through a string, looking for the *first* location where the regex pattern produces a match. ")
    display_note("If found, it returns a 'match object'; otherwise, it returns `None`.", message_continue=True)
    text = "You can contact me at info@example.com for more details."
    match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    show_code_with_output(f'''# Find the first email address in a string
import re
text = "{text}"
# This pattern looks for an email-like structure
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{{2,}}' 
match = re.search(pattern, text)
print(match)''',
str(match))

    print_small_sub_heading("b) Understanding the Match Object",True)
    display_note("The match object returned by `re.search` and `re.match` contains information about the match.")
    display_note("`.group()` returns the actual matched string. `.start()` and `.end()` give the start/end indices.", "tip")
    show_code_with_output(f'''# Extracting info from the match object
text = "You can contact me at info@example.com for more details."
match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"Start Index: {match.start()}") 
    print(f"End Index: {match.end()}")
    print(f"Span: {match.span()}")
''',
f'''Full match: {match.group(0)}
Start Index: {match.start()}
End Index: {match.end()}
Span: {match.span()}''')

    print_small_sub_heading("c) re.match(pattern, string)", True)
    display_note("This function only attempts to match the pattern at the *beginning* of the string.")
    display_note("If the pattern doesn't start at index 0, it returns `None`.", message_continue=True)
    text_to_match = "Python is powerful"
    match1 = re.match(r'Python', text_to_match)
    match2 = re.match(r'powerful', text_to_match)
    show_code_with_output(f'''# Trying to match at the beginning of the string
import re
text = "{text_to_match}"
# This pattern will match because the string starts with 'Python' 
match1 = re.match(r'Python', text)
print(f"Match for 'Python': {match1}")

# This pattern will fail because 'powerful' is not at the start
match2 = re.match(r'powerful', text)
print(f"Match for 'powerful': {match2}")
''',
f'''Match for 'Python': {match1}
Match for 'powerful': {match2}''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Finding All Matches and Substituting
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Finding All Matches and Substituting")

    print_small_sub_heading("a) re.findall(pattern, string)",True)
    display_note("Finds all non-overlapping matches of the pattern in the string and returns them as a list of strings.")
    text_with_numbers = "Order numbers are 123-456, 789-012, and 345-678."
    all_numbers = re.findall(r'\d{3}-\d{3}', text_with_numbers)
    show_code_with_output(f'''# Find all order numbers in a string
import re
text = "{text_with_numbers}"
# \\d{{3}} matches exactly three digits
all_numbers = re.findall(r'\\d{{3}}-\\d{{3}}', text) 
print(all_numbers)
''',
str(all_numbers))

    print_small_sub_heading("b) re.sub(pattern, repl, string)",True)
    display_note("Finds all occurrences of the pattern and replaces them with the string `repl`.")
    text_to_censor = "Please contact agent Smith or agent Jones for help."
    censored_text = re.sub(r'agent \w+', '[REDACTED]', text_to_censor)
    show_code_with_output(f'''# Replace all agent names in a string
import re
text = "{text_to_censor}"
# \\w+ matches one or more word characters (letters, numbers, underscore) 
censored_text = re.sub(r'agent \\w+', '[REDACTED]', text)
print(censored_text)
''',
censored_text)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Compiling Patterns for Efficiency
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Compiling Patterns for Efficiency")
    display_note("If you are going to use same regex pattern multiple times, it is more efficient to compile it first using `re.compile()`.")
    display_note("The compiled pattern object has methods like .search(), .findall(), etc., so you don't have to pass the pattern each time.", "tip")
    
    # Logic for output
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    text1 = "Valid email: test@example.org"
    text2 = "Invalid email: not-an-email"
    match1 = email_pattern.search(text1)
    match2 = email_pattern.search(text2)
    output = f"Searching in '{text1}': {match1.group(0) if match1 else None}\nSearching in '{text2}': {match2.group(0) if match2 else None}"
    
    show_code_with_output(f'''# Compile a pattern for reuse
import re
email_pattern = re.compile(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{{2,}}\\b')

# Use the compiled pattern on multiple strings
text1 = "Valid email: test@example.org"
text2 = "Invalid email: not-an-email"

print(f"Searching in '{{text1}}': {{email_pattern.search(text1).group(0) if email_pattern.search(text1) else None}}")
print(f"Searching in '{{text2}}': {{email_pattern.search(text2).group(0) if email_pattern.search(text2) else None}}") 
''',
output)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Using Flags for Modified Behavior
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Using Flags for Modified Behavior")
    display_note("Flags can modify how a pattern is interpreted. One of the most common is `re.IGNORECASE`.")

    print_small_sub_heading("a) re.IGNORECASE or re.I")
    display_note("This flag makes the pattern matching case-insensitive.")
    case_text = "Python is a language. I love python."
    match_case_sensitive = re.search(r'python', case_text)
    match_case_insensitive = re.search(r'python', case_text, re.IGNORECASE)
    
    show_code_with_output(f'''# Demonstrating case-insensitive matching
import re
text = "{case_text}"

# Case-sensitive search (will only find the second 'python')
match1 = re.search(r'python', text)
print(f"Case-sensitive found: {{match1.group(0) if match1 else None}} at index {{match1.start() if match1 else 'N/A'}}")

# Case-insensitive search (will find the first 'Python')
match2 = re.search(r'python', text, re.IGNORECASE)
print(f"Case-insensitive found: {{match2.group(0) if match2 else None}} at index {{match2.start() if match2 else 'N/A'}}")  
''',
f'''Case-sensitive found: {match_case_sensitive.group(0) if match_case_sensitive else None} at index {match_case_sensitive.start() if match_case_sensitive else 'N/A'}
Case-insensitive found: {match_case_insensitive.group(0) if match_case_insensitive else None} at index {match_case_insensitive.start() if match_case_insensitive else 'N/A'}''')

if __name__ == "__main__":
    main()
