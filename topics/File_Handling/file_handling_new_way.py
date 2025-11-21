# file_handling_new_way.py

from helpers.display_utils import *

def main(topic_number: int):
    print_heading("File Handling (I/O) in Python", topic_number)
    imp_note_points("""
- File Handling (Input/Output) is the process of reading from and writing to files on your computer.
- The built-in ___open()___ function is the primary tool for this, creating a file object to work with.
- The most crucial best practice is to always ensure a file is closed after use to free up system resources.
- The ___with___ statement is the modern, recommended way to handle files as it guarantees they are closed automatically.
- **Common File Modes:**
  - __'r'__ - **Read (default):** Opens for reading. Fails if the file does not exist.
  - __'w'__ - **Write:** Opens for writing. **Creates a new file or overwrites an existing one.**
  - __'a'__ - **Append:** Opens for appending. New data is written to the end of the file.
  - __'+'__ - Can be added to a mode (e.g., __'r+'__) to allow both reading and writing.
""")

    # -------------------------------------------------------------------------------
    # 1. Opening Files and Writing Content
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Opening Files and Writing Content")
    display_note("The `with open(...)` syntax is the standard, safe way to manage file objects. It automatically handles closing the file.")
    print_small_sub_heading("a) Writing and Appending to a File")
    code1 = '''# Write mode ('w') overwrites the file
with open('tests/output_dump/journal.txt', 'w') as f:
    f.write("Journal Entry\\n")
    f.writelines(["First line.\\n", "Second line.\\n"])

# Append mode ('a') adds to the end of the file
with open('tests/output_dump/journal.txt', 'a') as f:
    f.write("Third line, appended later.\\n")

# read mode ('r') reads the file
with open('tests/output_dump/journal.txt', 'r') as f:
    print(f.read())
#--------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -------------------------------------------------------------------------------
    # 2. Reading from Files
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Reading from Files")
    display_note("""For these examples, assume we have a file named `poem.txt` with the content:
The road goes ever on and on
Down from the door where it began.""")
    print_small_sub_heading("a) `read()`- Read the Entire File into One String")
    code2 = ''' # sample code for reading the entire file
with open('tests/output_dump/poem.txt', 'w') as f:
    f.write("The road goes ever on and on\\nDown from the door where it began.") 

# by `read()` method
with open('tests/output_dump/poem.txt', 'r') as f:
    content = f.read()
    print(content)
#---------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    print_small_sub_heading("b) The Best Way: Iterating Over the File Object", from_new_line=True)
    display_note("This is the most common and memory-efficient way to read a file, as it reads one line at a time.", "tip")
    code3 = '''# sample code for iterating over the file object
with open('tests/output_dump/poem.txt', 'r') as f:
    count=1
    for line in f:
        print(f"Line {count}: {line.strip()}") # .strip() removes leading/trailing whitespace
        count += 1
#---------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------
    # 3. Exploring the File Object (`seek`, `tell`, and attributes)
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Exploring the File Object (`seek`, `tell`, attributes)")
    display_note("The file object returned by `open()` has methods to control the file pointer (cursor) and attributes to check its state.")
    code4 = '''# Using file object methods within a 'with' block
sample_filename = 'tests/output_dump/sample_data.txt'
with open(sample_filename, 'w') as f:
    f.write('Hi there!, this is a sample text file.')

with open(tests/output_dump/sample_filename, 'r') as f:
    print("--- File Object Attributes ---")
    print(f"File Name (f.name): {f.name}")
    print(f"File Mode (f.mode): {f.mode}")
    print(f"Is file readable? (f.readable()): {f.readable()}")

    print("\\n--- Methods: tell() and read() ---")
    print(f"Cursor position at start (f.tell()): {f.tell()}")
    chunk1 = f.read(10) # Read the first 10 bytes
    print(f"Read 10 chars: {chunk1}")
    print(f"Cursor position now (f.tell()): {f.tell()}")

    print("\\n--- Methods: seek() ---")
    print("Moving cursor to byte 5 with f.seek(5)...")
    f.seek(5)
    print(f"Position after seek(5): {f.tell()}")
    chunk2 = f.read(5) # Read the next 5 bytes from the new position
    print(f"Reading 5 chars from new position: {chunk2}")

# After the 'with' block, the file is automatically closed
print(f"\\nIs file closed outside the 'with' block? {f.closed}")
#---------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)
    

if __name__ == "__main__":
    main(1)
