# file_io_deep_dive.py

from helpers.display_utils import *

def main():
    print_heading("File Handling (I/O) in Python")
    imp_note_points("""
- File Handling (Input/Output) is the process of reading from and writing to files on your computer.
- The built-in `open()` function is the primary tool for this, creating a file object to work with.
- The most crucial best practice is to always ensure a file is closed after use to free up system resources.
- The `with` statement is the modern, recommended way to handle files as it guarantees they are closed automatically.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. The `with` Statement: The Correct Way to Open Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. The Correct Way to Open Files: The `with` Statement")
    display_note("Using a `with` block automatically handles closing the file, even if errors occur within the block. This is the standard and safest way to manage file objects.")
    show_code_with_output('''# Using 'with' to open a file for writing
# The file is automatically closed when the block is exited.
with open('my_file.txt', 'w') as f:
    f.write('Hello, World!')
    # No need to call f.close()

print("File operation complete. 'with' ensures the file is closed.")''',
"File operation complete. 'with' ensures the file is closed.")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Understanding File Modes
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Understanding File Modes")
    display_note("""The 'mode' argument in `open()` tells Python how you intend to interact with the file.""")
    display_note("""
- `'r'` - **Read (default):** Opens a file for reading. Raises an error if the file does not exist.
- `'w'` - **Write:** Opens a file for writing. **Creates a new file if it does not exist, or overwrites the entire contents if it does.**
- `'a'` - **Append:** Opens a file for appending. Creates a new file if it does not exist. New data is written to the end of the file.
- `'x'` - **Create:** Creates a new file. Raises an error if the file already exists.
- `'+'` - **Update:** Can be added to other modes (e.g., `'r+'`, `'w+'`) to allow both reading and writing.
- `'b'` - **Binary:** For handling non-text files like images or executables (e.g., `'rb'`, `'wb'`).
- `'t'` - **Text (default):** For handling text files.
    """, "example")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Writing to Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Writing to Files")

    print_small_sub_heading("a) Write Mode ('w') - Overwrites Existing Content")
    display_note("Be careful! Write mode will erase everything in the file before writing new content.", "warning")
    show_code_with_output('''# Writing content to a file in 'w' mode.
lines_to_write = ["First line.\\n", "Second line.\\n"]
with open('journal.txt', 'w') as f:
    f.write("Journal Entry\\n")
    f.writelines(lines_to_write) # writelines writes a list of strings

# SIMULATED CONTENT of journal.txt:''',
'''Journal Entry
First line.
Second line.
''')

    print_small_sub_heading("b) Append Mode ('a') - Adds to the End of the File")
    display_note("Append mode is safe for adding to logs or existing documents without losing data.", "tip")
    show_code_with_output('''# Appending a new line to the same file.
with open('journal.txt', 'a') as f:
    f.write("Third line, appended later.\\n")

# SIMULATED CONTENT of journal.txt after appending:''',
'''Journal Entry
First line.
Second line.
Third line, appended later.
''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Reading from Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Reading from Files")
    display_note("For these examples, let's assume we have a file named `poem.txt` with the following content:\n\n*The road goes ever on and on,\nDown from the door where it began.*")

    print_small_sub_heading("a) `read()` - Read the Entire File into One String")
    show_code_with_output('''# Reading the whole file at once.
with open('poem.txt', 'r') as f:
    content = f.read()
    print(content)''',
'''The road goes ever on and on,
Down from the door where it began.
''')

    print_small_sub_heading("b) `readlines()` - Read All Lines into a List")
    display_note("This method keeps the newline characters (`\\n`) at the end of each string in the list.", "info")
    show_code_with_output('''# Reading all lines into a list of strings.
with open('poem.txt', 'r') as f:
    lines = f.readlines()
    print(lines)''',
"['The road goes ever on and on,\\n', 'Down from the door where it began.\\n']")

    print_small_sub_heading("c) The Best Way: Iterating Over the File Object")
    display_note("This is the most common and memory-efficient way to read a file, as it reads one line at a time into memory.", "example")
    show_code_with_output('''# The most efficient way to read a file line by line.
with open('poem.txt', 'r') as f:
    for line in f:
        # .strip() removes leading/trailing whitespace, including the newline character
        print(line.strip())''',
'''The road goes ever on and on,
Down from the door where it began.''')


if __name__ == "__main__":
    main()
