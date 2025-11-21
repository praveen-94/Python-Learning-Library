# advanced_file_handling.py

from helpers.display_utils import *
import os

def main(topic_number: int):
    print_heading("Advanced File Handling: Encodings and Binary Files", topic_number)
    imp_note_points("""
- All files on a computer are ultimately stored as bytes. File handling can be split into two main categories:
    1. **Text Files:** Python decodes bytes into text characters. This requires an **encoding** rulebook.
    2. **Binary Files:** Python reads and writes the raw bytes directly, without any decoding.
- Understanding this distinction is key to avoiding errors and correctly handling any type of file.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Character Encoding for Text Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Character Encoding for Text Files")
    display_note("""Encoding is the rulebook for converting bytes to text.
If you use the wrong rulebook, the text can become corrupted or your program can crash.""")
    display_note("`UTF-8` is the modern, universal standard. ")
    display_note("Best Practice: Always specify `encoding='utf-8'` when opening text files.", "tip")

    print_small_sub_heading("a) The Correct Way: Specifying `encoding='utf-8'`", from_new_line=True)
    display_note("This ensures your code works reliably with text containing international characters, symbols, and emojis.") 
    code1 = '''# Writing and reading a file with special characters using UTF-8
text_filename = 'tests/output_dump/example_text.txt'
text_to_write = "Hello, World! ¡Hola, Mundo! 你好, 世界！"
with open(text_filename, 'w', encoding='utf-8') as f:
    f.write(text_to_write)

with open(text_filename, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
#----------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("b) The Error Scenario: `UnicodeDecodeError`", from_new_line=True)
    display_note("This error happens when Python tries to read a file using an encoding that doesn't match the file's actual content. This is a very common bug.", "warning")
    code2 = '''# sample code
text_filename = 'tests/output_dump/example_text.txt'
text_to_write = "it is a sample file | Es un archivo de muestra | これはサンプルファイルです。"
with open(text_filename, 'a', encoding='utf-8') as f:
    f.write(text_to_write)

try:
    with open(text_filename, 'r', encoding='ascii') as f:
        content = f.read()
    raise UnicodeDecodeError("'ascii' codec can't decode byte 0xc2 in position 14: ordinal not in range(128)")
except UnicodeDecodeError as e:
    print(f"Error caught: {e}")
    print("\\nThis is why explicitly using 'encoding=\\'utf-8\\'' is so important!")
#--------------------------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Handling Binary Files
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Handling Binary Files (`'rb'`, `'wb'`)")
    display_note("""Binary files are any files that are not plain text, such as images, audio, zip archives, or executables.
They must be opened in binary mode to avoid data corruption.""")
    display_note("Binary mode is activated by adding `'b'` to the mode string (e.g., `'rb'` for read-binary, `'wb'` for write-binary).", "example")

    print_small_sub_heading("a) Practical Example: Copying a File", from_new_line=True)
    display_note("The most common use case for binary mode is reading from one file and writing the raw bytes to another, such as when copying an image or downloading a file.")
    code3 = '''# A program to copy a file using binary mode
binary_source_filename = 'tests/output_dump/source_file.bin'
binary_dest_filename = 'tests/output_dump/destination_file.bin'

# Create a dummy binary file for the copy example
with open(binary_source_filename, 'wb') as f:
    f.write(b'\\xDE\\xAD\\xBE\\xEF\\xCA\\xFE\\xBA\\xBE') # Some arbitrary bytes

try:
    with open(binary_source_filename, 'rb') as source_file:
        with open(binary_dest_filename, 'wb') as dest_file:
            # Read the file in chunks to handle large files efficiently
            chunk = source_file.read(4096) # Read 4KB at a time
            while chunk:
                dest_file.write(chunk)
                chunk = source_file.read(4096)
    print(f"File '{binary_source_filename}' successfully copied to '{binary_dest_filename}'.")
except FileNotFoundError:
    print("Error: Source file not found.")

with open(binary_dest_filename, 'rb') as f:
    content = f.read()
    print("Binary content of source file: ", content)

with open(binary_dest_filename, 'rb') as f:
    content = f.read()
    print("Binary content of destination file: ", content)
#----------------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

if __name__ == "__main__":
    main(1)
