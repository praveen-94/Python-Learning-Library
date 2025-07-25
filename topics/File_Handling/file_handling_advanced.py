# advanced_file_handling.py

from helpers.display_utils import *
import os

def main():
    print_heading("Advanced File Handling: Encodings and Binary Files")
    imp_note_points("""
- All files on a computer are ultimately stored as bytes. File handling can be split into two main categories:
    1. **Text Files:** Python decodes bytes into text characters. This requires an **encoding** rulebook.
    2. **Binary Files:** Python reads and writes the raw bytes directly, without any decoding.
- Understanding this distinction is key to avoiding errors and correctly handling any type of file.
""")

    # Setup for file examples
    text_filename = 'example_text.txt'
    binary_source_filename = 'source_file.bin'
    binary_dest_filename = 'destination_file.bin'

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Character Encoding for Text Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Character Encoding for Text Files")
    display_note("Encoding is the rulebook for converting bytes to text. ")
    display_note("If you use the wrong rulebook, the text can become corrupted or your program can crash.",message_continue=True)
    display_note("`UTF-8` is the modern, universal standard. **Best Practice:** Always specify `encoding='utf-8'` when opening text files.", "tip")

    print_small_sub_heading("a) The Correct Way: Specifying `encoding='utf-8'`", from_new_line=True)
    display_note("This ensures your code works reliably with text containing international characters, symbols, and emojis.")
    # Create the text file for the example
    with open(text_filename, 'w', encoding='utf-8') as f:
        f.write("Hello, World! ¡Hola, Mundo! 你好, 世界！")
    
    show_code_with_output('''# Writing and reading a file with special characters using UTF-8
text_filename = 'example_text.txt'
text_to_write = "Hello, World! ¡Hola, Mundo! 你好, 世界！"
with open('{text_filename}', 'w', encoding='utf-8') as f:
    f.write(text_to_write)

with open('{text_filename}', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)'''
,
"Hello, World! ¡Hola, Mundo! 你好, 世界！")

    print_small_sub_heading("b) The Error Scenario: `UnicodeDecodeError`", from_new_line=True)
    display_note("This error happens when Python tries to read a file using an encoding that doesn't match the file's actual content.","Warning")
    display_note("This is a very common bug.", "warning", message_continue=True)
    show_code_with_output('''# Simulating what happens when the wrong encoding is used
# Assume 'my_file.txt' was saved as UTF-8 but we try to read it as ASCII.
try:
    # with open('my_file.txt', 'r', encoding='ascii') as f:
    #     content = f.read()
    # This line below simulates the error that would occur.
    raise UnicodeDecodeError("'ascii' codec can't decode byte 0xc2 in position 14: ordinal not in range(128)")
except UnicodeDecodeError as e:
    print(f"Error caught: {e}")
    print("\\nThis is why explicitly using 'encoding=\\'utf-8\\'' is so important!")'''
,
'''Error caught: 'ascii' codec can't decode byte 0xc2 in position 14: ordinal not in range(128)

This is why explicitly using 'encoding='utf-8'' is so important!''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Handling Binary Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Handling Binary Files (`'rb'`, `'wb'`)")
    display_note("Binary files are any files that are not plain text, such as images, audio, zip archives, or executables.")
    display_note("They must be opened in binary mode to avoid data corruption.")
    display_note("Binary mode is activated by adding `'b'` to the mode string (e.g., `'rb'` for read-binary, `'wb'` for write-binary).", "example")

    print_small_sub_heading("a) Practical Example: Copying a File",from_new_line=True)
    display_note("The most common use case for binary mode is reading from one file and writing the raw bytes to another, ")
    display_note("such as when copying an image or downloading a file.")

    # Create a dummy binary file for the copy example
    with open(binary_source_filename, 'wb') as f:
        f.write(b'\xDE\xAD\xBE\xEF\xCA\xFE\xBA\xBE') # Some arbitrary bytes
    
    show_code_with_output('''# A program to copy a file using binary mode
binary_source_filename = 'source_file.bin'
binary_dest_filename = 'destination_file.bin'

try:
    with open(source, 'rb') as source_file:
        with open(destination, 'wb') as dest_file:
            # Read the file in chunks to handle large files efficiently
            chunk = source_file.read(4096) # Read 4KB at a time
            while chunk:
                dest_file.write(chunk)
                chunk = source_file.read(4096)
    print(f"File '{{source}}' successfully copied to '{{destination}}'.")
except FileNotFoundError:
    print("Error: Source file not found.")'''
,
f"File '{binary_source_filename}' successfully copied to '{binary_dest_filename}'.")


    # Final Cleanup ---
    # This block cleans up the files created during the demonstration
    try:
        if os.path.exists(text_filename):
            os.remove(text_filename)
        if os.path.exists(binary_source_filename):
            os.remove(binary_source_filename)
        if os.path.exists(binary_dest_filename):
            os.remove(binary_dest_filename)
    except Exception as e:
        print(f"Cleanup failed: {e}")


if __name__ == "__main__":
    main()
