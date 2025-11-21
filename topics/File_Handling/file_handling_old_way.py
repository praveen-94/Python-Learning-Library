# file_handling_old_way.py

from helpers.display_utils import *
import os # Needed to clean up the sample file

def main(topic_number: int):
    print_heading("File Handling: The Manual `open()` and `close()` Method", topic_number)
    imp_note_points("""
- Before the ___with___ statement, files were managed by manually calling ___open()___ and then ___close()___.
- This method is **no longer recommended** and is an anti-pattern in modern Python.
- **Why it's not recommended:**
    - **It's easy to forget ___f.close()___:** Forgetting to close a file can leave it locked by the OS, consuming resources.
    - **It's not error-safe:** If an exception occurs after ___open()___ but before ___close()___, the program crashes and the file is left open.
- The only safe way to use this method is with a ___try...finally___ block, which is much more verbose than the ___with___ statement.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. The Unsafe Method: Where an Error Occurs
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. The Unsafe Method: The Error Scenario")
    display_note("This example demonstrates the primary danger. An unexpected error will crash the program before the file can be closed.", "warning")
    code1 = '''# An example where an error leaves the file open.
try:
    f = open('tests/output_dump/unsafe_file.txt', 'w')
    print("File 'unsafe_file.txt' is now open.")
    
    # This line will cause a ZeroDivisionError
    unsafe_operation = 10 / 0
    
    # This line is NEVER reached
    f.close()
    print("File was closed.")

except ZeroDivisionError as e:
    print(f"\\nAn error occurred: {e}")
    print("The f.close() line was never executed!")
    # Manually close the file if it was opened, due to the error
    if f:
        f.close()
#--------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. The 'Correct' Old Way: Using `try...finally`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. The 'Correct' (but Verbose) Old Way: `try...finally`")
    display_note("""To make the manual method safe, developers had to wrap their logic in a `try...finally` block."
The `finally` block guarantees its code will run, no matter what.""")
    code2 = '''# The safe but verbose way to manually manage files.
f = None
try:
    f = open('tests/output_dump/safer_file.txt', 'w')
    f.write('This was written successfully.')
finally:
    if f: # Check if file was opened before trying to close
        f.close()
        print("File has been safely closed via 'finally'.")
#-----------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Exploring the File Object Attributes and Methods
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Exploring the File Object")
    display_note("""When you `open()` a file, you get a file object.
This object has useful attributes and methods to interact with the file and its state.""")
    code3 = '''# Create and open a file to explore its methods
sample_filename = 'tests/output_dump/sample_data.txt'
with open(sample_filename, 'w') as f:
    f.write('Hi,this file is created for exploring file methods.')

f = open(sample_filename, 'r')

# --- Attributes ---
print("--- File Object Attributes ---")
print(f"File Name (f.name): {f.name}")
print(f"File Mode (f.mode): {f.mode}")
print(f"Is file closed? (f.closed): {f.closed}")

# --- Methods: tell() and read() ---
print("\\n--- Methods: tell() and read() ---")
print(f"Current position (f.tell()): {f.tell()}")
chunk1 = f.read(5)
print(f"Read 5 chars: '{{chunk1}}'")
print(f"New position (f.tell()): {f.tell()}")

# --- Methods: seek() ---
print("\\n--- Methods: seek() ---")
print("Moving cursor back to the beginning with f.seek(0)...")
f.seek(0)
print(f"Position after seek(0): {f.tell()}")
chunk2 = f.read(5)
print(f"Reading 5 chars again: '{{chunk2}}'")

# --- Methods: close() ---
print("\\n--- Methods: close() ---")
f.close()
print("f.close() has been called.")
print(f"Is file closed now? (f.closed): {f.closed}")
#-------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


if __name__ == "__main__":
    main(1)
