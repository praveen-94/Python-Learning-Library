# datetime_module_deep_dive.py

from helpers.display_utils import *
import datetime

def main(topic_number: int):
    print_heading("The `datetime` Module: Handling Dates and Times", topic_number)
    imp_note_points("""
- The ___datetime___ module supplies classes for manipulating dates and times in both simple and complex ways.
- It is a built-in module, so you only need to ___import datetime___ to use it.
- The primary objects are ___date, time, datetime, timedelta, and tzinfo (for timezones)___.
- "Naive" objects do not have timezone information, while "aware" objects do. By default, most objects are naive.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. The `date` Object
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. The `date` Object")
    display_note("A `date` object represents a date (year, month, and day). It is an idealized, naive date.")
    code1 = '''# Get the current local date
import datetime
today = datetime.date.today()
print(f"Today's date is: {today}")
#---------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    #------------------------------------------------------------------------------------------
    print_small_sub_heading("b) Creating a Specific Date and Accessing Attributes")
    display_note("You can access parts of the date like `.year`, `.month`, and `.day`.")
    code2 = '''# Create a specific date object
import datetime
birthday = datetime.date(1999, 8, 12)
print(f"Year: {birthday.year}")
print(f"Month: {birthday.month}")
print(f"Day: {birthday.day}")
# weekday() returns 0 for Monday and 6 for Sunday
print(f"Day of the week: {birthday.weekday()} (Thursday)")
#-----------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. The `datetime` Object
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. The `datetime` Object")
    display_note("A `datetime` object contains all the information from a `date` object and a `time` object.")

    print_small_sub_heading("a) Getting the Current Date and Time")
    code3 = '''# Get the current local date and time
import datetime
now = datetime.datetime.now()
print(f"Current date and time: {now}")
#-------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #----------------------------------------------------------------------------------------------------------
    print_small_sub_heading("b) Getting UTC Date and Time")
    display_note("`utcnow()` is often preferred for server applications to avoid timezone ambiguities.", "tip")
    code4 = '''# Get the current UTC date and time
import datetime
utcnow = datetime.datetime.utcnow()
print(f"Current UTC date and time: {utcnow}")
#----------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. The `timedelta` Object and Date Arithmetic
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. The `timedelta` Object and Date Arithmetic")
    display_note("A `timedelta` object represents a duration, the difference between two dates or times.")

    print_small_sub_heading("a) Creating and Using a timedelta")
    display_note("You can perform arithmetic on `date` and `datetime` objects using `timedelta`.")
    code5 = '''# Add 10 days to the current date
import datetime
today = datetime.date.today()
time_delta = datetime.timedelta(days=10)
future_date = today + time_delta
print(f"Today is: {today}")
print(f"10 days from now will be: {future_date}")
#--------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    #---------------------------------------------------------------------------------
    print_small_sub_heading("b) Calculating the Difference Between Two Dates")
    code6 = '''# Calculate the time remaining until a future date
import datetime
new_year_2026 = datetime.date(2026, 1, 1)
today = datetime.date.today()
time_left = new_year_2026 - today
print(f"Days left until 2026: {time_left.days}")
#--------------------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Formatting and Parsing
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Formatting and Parsing with `strftime` and `strptime`")
    display_note("`strftime` converts a datetime object to a formatted string. `strptime` parses a string into a datetime object.")

    print_small_sub_heading("a) `strftime` (Object to String)")
    display_note("Common format codes: `%Y` (Year), `%m` (month), `%d` (day), `%H` (24hr), `%M` (min), `%S` (sec), `%A` (weekday).", "example")
    code7 = '''# Formatting a datetime object into a readable string
import datetime
now = datetime.datetime.now()
# Format: Weekday, dd Month YYYY, hh:mm AM/PM
formatted = now.strftime("%A, %d %B %Y, %I:%M %p")
print(formatted)
#--------------------------------------------------#'''
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)

    #----------------------------------------------------------------------
    print_small_sub_heading("b) `strptime` (String to Object)")
    display_note("The format code in `strptime` must exactly match the format of the input string, or it will raise a `ValueError`.", "warning")
    code8 = '''# Parsing a string into a datetime object
import datetime
date_str = "25 December, 2024"
date_object = datetime.datetime.strptime(date_str, "%d %B, %Y")
print(f"Parsed object: {date_object}")
print(f"Year from object: {date_object.year}")
#---------------------------------------------------------------#'''
    output8 = run_code_snippet(code8)
    show_code_with_output(code8, output8)
    

if __name__ == "__main__":
    main(1)
