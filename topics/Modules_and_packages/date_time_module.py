# datetime_module_deep_dive.py

from helpers.display_utils import *
import datetime

def main():
    print_heading("The `datetime` Module: Handling Dates and Times")
    imp_note_points("""
- The `datetime` module supplies classes for manipulating dates and times in both simple and complex ways.
- It is a built-in module, so you only need to `import datetime` to use it.
- The primary objects are `date`, `time`, `datetime`, `timedelta`, and `tzinfo` (for timezones).
- "Naive" objects do not have timezone information, while "aware" objects do. By default, most objects are naive.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. The `date` Object
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. The `date` Object")
    display_note("A `date` object represents a date (year, month, and day). It is an idealized, naive date.")

    print_small_sub_heading("a) Getting Today's Date")
    today = datetime.date.today()
    show_code_with_output(f'''# Get the current local date
import datetime
today = datetime.date.today()
print(f"Today's date is: {{today}}")''',
f"Today's date is: {today}")

    print_small_sub_heading("b) Creating a Specific Date and Accessing Attributes")
    display_note("You can access parts of the date like `.year`, `.month`, and `.day`.")
    bday = datetime.date(1999, 8, 12)
    show_code_with_output(f'''# Create a specific date object
import datetime
birthday = datetime.date(1999, 8, 12)
print(f"Year: {{birthday.year}}")
print(f"Month: {{birthday.month}}")
print(f"Day: {{birthday.day}}")
# weekday() returns 0 for Monday and 6 for Sunday
print(f"Day of the week: {{birthday.weekday()}} (Thursday)")''',
f'''Year: {bday.year}
Month: {bday.month}
Day: {bday.day}
Day of the week: {bday.weekday()} (Thursday)''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. The `datetime` Object
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. The `datetime` Object")
    display_note("A `datetime` object contains all the information from a `date` object and a `time` object.")

    print_small_sub_heading("a) Getting the Current Date and Time")
    now = datetime.datetime.now()
    show_code_with_output(f'''# Get the current local date and time
import datetime
now = datetime.datetime.now()
print(f"Current date and time: {{now}}")''',
f"Current date and time: {now}")

    print_small_sub_heading("b) Getting UTC Date and Time")
    display_note("`utcnow()` is often preferred for server applications to avoid timezone ambiguities.", "tip")
    utcnow = datetime.datetime.utcnow()
    show_code_with_output(f'''# Get the current UTC date and time
import datetime
utcnow = datetime.datetime.utcnow()
print(f"Current UTC date and time: {{utcnow}}")''',
f"Current UTC date and time: {utcnow}")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. The `timedelta` Object and Date Arithmetic
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. The `timedelta` Object and Date Arithmetic")
    display_note("A `timedelta` object represents a duration, the difference between two dates or times.")

    print_small_sub_heading("a) Creating and Using a timedelta")
    display_note("You can perform arithmetic on `date` and `datetime` objects using `timedelta`.")
    today = datetime.date.today()
    ten_days = datetime.timedelta(days=10)
    future_date = today + ten_days
    show_code_with_output(f'''# Add 10 days to the current date
import datetime
today = datetime.date.today()
time_delta = datetime.timedelta(days=10)
future_date = today + time_delta
print(f"Today is: {{today}}")
print(f"10 days from now will be: {{future_date}}")''',
f'''Today is: {today}
10 days from now will be: {future_date}''')

    print_small_sub_heading("b) Calculating the Difference Between Two Dates")
    date1 = datetime.date(2025, 1, 1)
    date2 = datetime.date.today()
    difference = date1 - date2
    show_code_with_output(f'''# Calculate the time remaining until a future date
import datetime
new_year_2025 = datetime.date(2025, 1, 1)
today = datetime.date.today()
time_left = new_year_2025 - today
print(f"Days left until 2025: {{time_left.days}}")''',
f"Days left until 2025: {difference.days}")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Formatting and Parsing
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Formatting and Parsing with `strftime` and `strptime`")
    display_note("`strftime` converts a datetime object to a formatted string. `strptime` parses a string into a datetime object.")

    print_small_sub_heading("a) `strftime` (Object to String)")
    display_note("Common format codes: `%Y` (Year), `%m` (month), `%d` (day), `%H` (24hr), `%M` (min), `%S` (sec), `%A` (weekday).", "example")
    now_obj = datetime.datetime.now()
    formatted_str = now_obj.strftime("%A, %d %B %Y, %I:%M %p")
    show_code_with_output(f'''# Formatting a datetime object into a readable string
import datetime
now = datetime.datetime.now()
# Format: Weekday, dd Month YYYY, hh:mm AM/PM
formatted = now.strftime("%A, %d %B %Y, %I:%M %p")
print(formatted)''',
formatted_str)

    print_small_sub_heading("b) `strptime` (String to Object)")
    display_note("The format code in `strptime` must exactly match the format of the input string, or it will raise a `ValueError`.", "warning")
    date_string = "25 December, 2024"
    date_obj = datetime.datetime.strptime(date_string, "%d %B, %Y")
    show_code_with_output(f'''# Parsing a string into a datetime object
import datetime
date_str = "{date_string}"
date_object = datetime.datetime.strptime(date_str, "%d %B, %Y")
print(f"Parsed object: {{date_object}}")
print(f"Year from object: {{date_object.year}}")''',
f'''Parsed object: {date_obj}
Year from object: {date_obj.year}''')


if __name__ == "__main__":
    main()
