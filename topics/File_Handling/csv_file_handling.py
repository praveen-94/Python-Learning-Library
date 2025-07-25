# csv_file_handling.py

from helpers.display_utils import *
import csv
import os

def main():
    print_heading("Handling CSV Files")
    imp_note_points("""
- CSV (Comma-Separated Values) is a common plain text format for storing tabular data, like from a spreadsheet or database.
- Python's built-in `csv` module provides tools to easily read from and write to CSV files.
- The module correctly handles the complexities of CSV formatting, such as quoting fields that contain commas.
- Best practice is to always open CSV files with the `newline=''` argument to prevent blank rows from appearing.
""")
    
    # Define the filenames for our examples
    csv_filename = 'grades.csv'
    dict_csv_filename = 'employees.csv'

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Writing to a CSV File with `csv.writer`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Writing to a CSV File with `csv.writer`")
    display_note("The `csv.writer` object converts your data into delimited strings and writes them to a file object.")

    # Sample data for the writer
    header = ['Name', 'Subject', 'Grade']
    rows = [
        ['Alice', 'Math', 95],
        ['Bob', 'Science', 88],
        ['Charlie', 'History', 92]
    ] 

    # Execute the code to be shown
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header) # writerow writes a single list
        writer.writerows(rows)  # writerows writes a list of lists

    # Read the file to display its actual content
    read_output1 = ""
    with open(csv_filename, 'r', encoding='utf-8') as f:
        file_content = csv.reader(f)
        for row in file_content:
            read_output1 += f"{row}\n"

    # Show the code and simulated file content
    show_code_with_output(f'''import csv

header = {header}
rows = {rows} 

# Open the file with newline='' to prevent extra blank rows
with open('{csv_filename}', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("'{csv_filename}' created successfully.")
''', 
f"'{csv_filename}' created successfully.\n"+
f"The content of `{csv_filename}` would now be:\n{read_output1.strip()}")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Reading from a CSV File with `csv.reader`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Reading from a CSV File with `csv.reader`")
    display_note("The `csv.reader` object iterates over lines in the given CSV file, returning each row as a list of strings.")

    # Execute the read operation
    read_output = ""
    with open(csv_filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header_read = next(reader) # Read the header row
        read_output += f"Header: {header_read}\n"
        for row in reader:
            read_output += f"Data Row: {row}\n"
            
    show_code_with_output(f'''import csv

with open('{csv_filename}', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader) # The first row is usually the header
    print(f"Header: {{header}}")
    for row in reader:
        # Each row is a list of strings
        print(f"Data Row: {{row}}")
''',
read_output.strip())


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Working with Dictionaries: `DictWriter` and `DictReader`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. A Better Way: Using Dictionaries")
    display_note("Working with dictionaries is often more readable and robust, as you access data by column name instead of index.", "tip")

    print_small_sub_heading("a) Writing with `csv.DictWriter`")
    display_note("Requires you to specify the `fieldnames` (headers). You must explicitly write the header with `writeheader()`.")
    
    # Sample data for DictWriter
    dict_rows = [
        {'ID': 'E101', 'Name': 'Diana Prince', 'Role': 'Developer'},
        {'ID': 'E102', 'Name': 'Clark Kent', 'Role': 'Analyst'},
        {'ID': 'E103', 'Name': 'Bruce Wayne', 'Role': 'Manager'}
    ]
    fieldnames = ['ID', 'Name', 'Role']
    
    # Execute and show DictWriter code
    with open(dict_csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dict_rows)
        
    show_code_with_output('''import csv
dict_rows = [
    {'ID': 'E101', 'Name': 'Diana Prince', 'Role': 'Developer'},
    {'ID': 'E102', 'Name': 'Clark Kent', 'Role': 'Analyst'},
    {'ID': 'E103', 'Name': 'Bruce Wayne', 'Role': 'Manager'}
]
fieldnames = ['ID', 'Name', 'Role']
                          
data = {dict_rows}
fieldnames = {fieldnames}

with open('{dict_csv_filename}', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    
print("'{dict_csv_filename}' created successfully.")'''
, 
f"'{dict_csv_filename}' created successfully.")
    
    print_small_sub_heading("b) Reading with `csv.DictReader`",from_new_line=True)
    display_note("`csv.DictReader` automatically uses the first row as field names and yields each subsequent row as a dictionary.", "example")
    
    dict_read_output = ""
    with open(dict_csv_filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dict_read_output += f"Read data for {row['Name']} (ID: {row['ID']}, Role: {row['Role']})\n"
            
    show_code_with_output('''import csv

with open('{dict_csv_filename}', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Now you can access data by column name!
        print(f"Read data for {{row['Name']}} (ID: {{row['ID']}}, Role: {{row['Role']}})")'''
,
dict_read_output.strip())


    # Clean up the created files
    if os.path.exists(csv_filename):
        os.remove(csv_filename)
    if os.path.exists(dict_csv_filename):
        os.remove(dict_csv_filename)


if __name__ == "__main__":
    main()
