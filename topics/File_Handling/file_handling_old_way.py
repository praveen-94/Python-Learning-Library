# file_handling_old_way.py

from helpers.display_utils import *
import os # Needed to clean up the sample file

def main():
    print_heading("File Handling: The Manual `open()` and `close()` Method")
    imp_note_points("""
- Before the `with` statement, files were managed by manually calling `open()` and then `close()`.
- This method is **no longer recommended** and is an anti-pattern in modern Python.
- **Why it's not recommended:**
    - **It's easy to forget `f.close()`:** Forgetting to close a file can leave it locked by the OS, consuming resources.
    - **It's not error-safe:** If an exception occurs after `open()` but before `close()`, the program crashes and the file is left open.
- The only safe way to use this method is with a `try...finally` block, which is much more verbose than the `with` statement.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. The Unsafe Method: Where an Error Occurs
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. The Unsafe Method: The Error Scenario")
    display_note("This example demonstrates the primary danger. An unexpected error will crash the program before the file can be closed.", "warning")
    show_code_with_output('''# An example where an error leaves the file open.
try:
    f = open('unsafe_file.txt', 'w')
    print("File 'unsafe_file.txt' is now open.")
    
    # This line will cause a ZeroDivisionError
    unsafe_operation = 10 / 0
    
    # This line is NEVER reached
    f.close()
    print("File was closed.")

except ZeroDivisionError as e:
    print(f"\\nAn error occurred: {e}")
    print("The f.close() line was never executed!")
''',
'''File 'unsafe_file.txt' is now open.

An error occurred: division by zero
The f.close() line was never executed!''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Exploring the File Object Attributes and Methods
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Exploring the File Object")
    display_note("When you `open()` a file, you get a file object.")
    display_note("This object has useful attributes and methods to interact with the file and its state.",message_continue=True)

    # Create a sample file for demonstration
    sample_filename = 'sample_data.txt'
    with open(sample_filename, 'w') as f:
        f.write('0123456789abcdefghijklmnopqrstuvwxyz')

    # --- Code to be displayed ---
    code_to_show = '''# Open a file to explore its methods
sample_filename = 'sample_data.txt'
f = open('{sample_filename}', 'r')

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
print(f"Is file closed now? (f.closed): {f.closed}")'''

    # --- Execute the code to generate the output ---
    f = open(sample_filename, 'r')
    output_str = f"--- File Object Attributes ---\n"
    output_str += f"File Name (f.name): {f.name}\n"
    output_str += f"File Mode (f.mode): {f.mode}\n"
    output_str += f"Is file closed? (f.closed): {f.closed}\n\n"
    output_str += f"--- Methods: tell() and read() ---\n"
    output_str += f"Current position (f.tell()): {f.tell()}\n"
    chunk1 = f.read(5)
    output_str += f"Read 5 chars: '{chunk1}'\n"
    output_str += f"New position (f.tell()): {f.tell()}\n\n"
    output_str += f"--- Methods: seek() ---\n"
    output_str += f"Moving cursor back to the beginning with f.seek(0)...\n"
    f.seek(0)
    output_str += f"Position after seek(0): {f.tell()}\n"
    chunk2 = f.read(5)
    output_str += f"Reading 5 chars again: '{chunk2}'\n\n"
    output_str += f"--- Methods: close() ---\n"
    f.close()
    output_str += f"f.close() has been called.\n"
    output_str += f"Is file closed now? (f.closed): {f.closed}"
    
    show_code_with_output(code_to_show, output_str)
    # Clean up the sample file
    os.remove(sample_filename)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. The 'Correct' Old Way: Using `try...finally`
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. The 'Correct' (but Verbose) Old Way: `try...finally`")
    display_note("To make the manual method safe, developers had to wrap their logic in a `try...finally` block.")
    display_note("The `finally` block guarantees its code will run, no matter what.",message_continue=True)
    show_code_with_output('''# The safe but verbose way to manually manage files.
f = None
try:
    f = open('safer_file.txt', 'w')
    f.write('This was written successfully.')
finally:
    if f: # Check if file was opened before trying to close
        f.close()
        print("File has been safely closed via 'finally'.")''',
"File has been safely closed via 'finally'.")


if __name__ == "__main__":
    main()
