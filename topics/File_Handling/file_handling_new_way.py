# file_io_deep_dive.py

from helpers.display_utils import *
import os # Needed to clean up the sample file

def main():
    print_heading("File Handling (I/O) in Python")
    imp_note_points("""
- File Handling (Input/Output) is the process of reading from and writing to files on your computer.
- The built-in `open()` function is the primary tool for this, creating a file object to work with.
- The most crucial best practice is to always ensure a file is closed after use to free up system resources.
- The `with` statement is the modern, recommended way to handle files as it guarantees they are closed automatically.
- **Common File Modes:**
  - `'r'` - **Read (default):** Opens for reading. Fails if the file does not exist.
  - `'w'` - **Write:** Opens for writing. **Creates a new file or overwrites an existing one.**
  - `'a'` - **Append:** Opens for appending. New data is written to the end of the file.
  - `'+'` - Can be added to a mode (e.g., `'r+'`) to allow both reading and writing.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Opening Files and Writing Content
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Opening Files and Writing Content")
    display_note("The `with open(...)` syntax is the standard, safe way to manage file objects. It automatically handles closing the file.")
    print_small_sub_heading("a) Writing and Appending to a File")
    show_code_with_output('''# Write mode ('w') overwrites the file
with open('journal.txt', 'w') as f:
    f.write("Journal Entry\\n")
    f.writelines(["First line.\\n", "Second line.\\n"])

# Append mode ('a') adds to the end of the file
with open('journal.txt', 'a') as f:
    f.write("Third line, appended later.\\n")'''
,
'''Journal Entry
First line.
Second line.
Third line, appended later.
''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Reading from Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Reading from Files")
    display_note("For these examples, assume we have a file named `poem.txt` with the content:")
    display_note("The road goes ever on and on",message_continue=True)
    display_note("Down from the door where it began.",message_continue=True)
    print_small_sub_heading("a) `read()` - Read the Entire File into One String")
    show_code_with_output('''# by `read()` method
with open('poem.txt', 'r') as f:
    content = f.read()
    print(content)'''
,
'''The road goes ever on and on,
Down from the door where it began.
''')

    print_small_sub_heading("b) The Best Way: Iterating Over the File Object",from_new_line=True)
    display_note("This is the most common and memory-efficient way to read a file, as it reads one line at a time.", "tip")
    show_code_with_output('''# by for loop
with open('poem.txt', 'r') as f:
    for line in f:
        print(line.strip()) # .strip() removes leading/trailing whitespace'''
,
'''The road goes ever on and on,
Down from the door where it began.''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Exploring the File Object (`seek`, `tell`, and attributes)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Exploring the File Object (`seek`, `tell`, attributes)")
    display_note("The file object returned by `open()` has methods to control the file pointer (cursor) and attributes to check its state.")
    # Create a sample file for demonstration
    sample_filename = 'sample_data.txt'
    with open(sample_filename, 'w') as f:
        f.write('0123456789abcdefghijklmnopqrstuvwxyz')

    # Code to be displayed
    code_to_show = '''# Using file object methods within a 'with' block
sample_filename = 'sample_data.txt'
with open('{sample_filename}', 'r') as f:
    # --- Attributes ---
    print("--- File Object Attributes ---")
    print(f"File Name (f.name): {f.name}")
    print(f"File Mode (f.mode): {f.mode}")
    print(f"Is file readable? (f.readable()): {f.readable()}")

    # --- Methods: tell() and read() ---
    print("\\n--- Methods: tell() and read() ---")
    print(f"Cursor position at start (f.tell()): {f.tell()}")
    chunk1 = f.read(10) # Read the first 10 bytes
    print(f"Read 10 chars: '{{chunk1}}'")
    print(f"Cursor position now (f.tell()): {f.tell()}")

    # --- Methods: seek() ---
    print("\\n--- Methods: seek() ---")
    print("Moving cursor to byte 5 with f.seek(5)...")
    f.seek(5)
    print(f"Position after seek(5): {f.tell()}")
    chunk2 = f.read(5) # Read the next 5 bytes from the new position
    print(f"Reading 5 chars from new position: '{{chunk2}}'")

# After the 'with' block, the file is automatically closed
print(f"\\nIs file closed outside the 'with' block? {f.closed}")'''

    # Execute the code to generate the output ---
    with open(sample_filename, 'r') as f:
        output_str = f"--- File Object Attributes ---\n"
        output_str += f"File Name (f.name): {f.name}\n"
        output_str += f"File Mode (f.mode): {f.mode}\n"
        output_str += f"Is file readable? (f.readable()): {f.readable()}\n\n"
        output_str += f"--- Methods: tell() and read() ---\n"
        output_str += f"Cursor position at start (f.tell()): {f.tell()}\n"
        chunk1 = f.read(10)
        output_str += f"Read 10 chars: '{chunk1}'\n"
        output_str += f"Cursor position now (f.tell()): {f.tell()}\n\n"
        output_str += f"--- Methods: seek() ---\n"
        output_str += f"Moving cursor to byte 5 with f.seek(5)...\n"
        f.seek(5)
        output_str += f"Position after seek(5): {f.tell()}\n"
        chunk2 = f.read(5)
        output_str += f"Reading 5 chars from new position: '{chunk2}'\n"
    output_str += f"\nIs file closed outside the 'with' block? {f.closed}"
    
    try:
        show_code_with_output(code_to_show, output_str)
    except:
        print()
    # Clean up the sample file
    os.remove(sample_filename)


if __name__ == "__main__":
    main()
