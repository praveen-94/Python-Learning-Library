# csv_file_handling.py

from helpers.display_utils import *
import csv
import os

def main(topic_number: int):
    print_heading("Handling CSV Files", topic_number)
    imp_note_points("""
- CSV (Comma-Separated Values) is a common plain text format for storing tabular data, like from a spreadsheet or database.
- Python's built-in ___csv___ module provides tools to easily read from and write to CSV files.
- The module correctly handles the complexities of CSV formatting, such as quoting fields that contain commas.
- Best practice is to always open CSV files with the ___newline=''___ argument to prevent blank rows from appearing.""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Writing to a CSV File with `csv.writer`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Writing to a CSV File with `csv.writer`")
    display_note("The `csv.writer` object converts your data into delimited strings and writes them to a file object.")
    code1 = '''# Sample code 
import csv

csv_filename = 'tests/output_dump/students.csv'

# Sample data for the writer
header = ['Name', 'Subject', 'Grade']
rows = [
    ['Tony Stark', 'Math', 95],
    ['Peter Parker', 'Science', 88],
    ['Black Widow', 'History', 92]
]

# Open the file with newline='' to prevent extra blank rows
with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"'{csv_filename}' created successfully.")
#-----------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Reading from a CSV File with `csv.reader`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Reading from a CSV File with `csv.reader`")
    display_note("The `csv.reader` object iterates over lines in the given CSV file, returning each row as a list of strings.")
    code2 = '''# Execute the read operation
import csv

csv_filename = 'tests/output_dump/students.csv'

with open(csv_filename, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader) # The first row is usually the header
    print(f"Header: {header}")
    for row in reader:
        # Each row is a list of strings
        print(f"Data Row: {row}")
#------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Working with Dictionaries: `DictWriter` and `DictReader`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. A Better Way: Using Dictionaries")
    display_note("Working with dictionaries is often more readable and robust, as you access data by column name instead of index.", "tip")

    print_small_sub_heading("a) Writing with `csv.DictWriter`")
    display_note("Requires you to specify the `fieldnames` (headers). You must explicitly write the header with `writeheader()`.")
    code3 = '''# sample code for writing with DictWriter
import csv

dict_csv_filename = 'tests/output_dump/employees.csv'
dict_rows = [
    {'ID': 'E101', 'Name': 'Diana Prince', 'Role': 'Developer'},
    {'ID': 'E102', 'Name': 'Clark Kent', 'Role': 'Analyst'},
    {'ID': 'E103', 'Name': 'Bruce Wayne', 'Role': 'Manager'}
]
fieldnames = ['ID', 'Name', 'Role']

with open(dict_csv_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_rows)

print(f"'{dict_csv_filename}' created successfully.")
#---------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    print_small_sub_heading("b) Reading with `csv.DictReader`",from_new_line=True)
    display_note("`csv.DictReader` automatically uses the first row as field names and yields each subsequent row as a dictionary.", "example")
    code4 = '''# Reading with DictReader
import csv

dict_csv_filename = 'tests/output_dump/employees.csv'
with open(dict_csv_filename, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Now you can access data by column name!
        print(f"Read data for {row['Name']} (ID: {row['ID']}, Role: {row['Role']})")
#------------------------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)


if __name__ == "__main__":
    main(1)
