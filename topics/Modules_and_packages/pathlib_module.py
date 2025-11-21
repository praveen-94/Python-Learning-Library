# pathlib_module_deep_dive.py

from helpers.display_utils import *
from pathlib import Path
import os # Imported for the final summary example

def main(topic_number: int):
    print_heading("The `pathlib` Module: Modern Path Handling", topic_number)
    imp_note_points("""
- The ___pathlib___ module (introduced in Python 3.4) offers a modern, object-oriented way to represent and manipulate filesystem paths.
- It is now the recommended approach for path manipulation, replacing the procedural functions in ___os.path___.
- Its key advantages are improved readability, cross-platform consistency, and an intuitive API.
- A ___Path___ object represents a path, not just a string, making code cleaner and less error-prone.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Creating Paths and Joining Them
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Creating Paths and Joining Them")
    display_note("The most elegant feature of `pathlib` is using the `/` operator to join paths.")

    print_small_sub_heading("a) Creating a Path Object",True)
    code1 = '''# Create a Path object from a string
from pathlib import Path
p = Path('documents/reports')
print(f"Created Path object: {p}") 
print(f"Object type: {type(p)}")
#---------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("b) Joining with the '/' Operator",True)
    display_note("This is much more readable than `os.path.join()`.")
    code2 = '''# The intuitive way to build paths
from pathlib import Path
root = Path('/home/user')
config_path = root / 'app' / 'config.ini' 
print(config_path)
#-----------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Accessing Path Components
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Accessing Path Components")
    display_note("`pathlib` provides simple attributes to get parts of a path, replacing complex `os.path` functions.")
    code3 = '''# Extracting parts from a path
from pathlib import Path
p = Path('/home/user/data/archive.zip')

print(f"Parent directory: {p.parent}")
print(f"File name: {p.name}")
print(f"File stem (name without extension): {p.stem}") 
print(f"File extension (suffix): {p.suffix}")
#-----------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Checking Path Properties and File Operations
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Checking Properties and File Operations")

    print_small_sub_heading("a) Checking if a Path Exists",True)
    display_note("The path object has methods to check its own state.")
    code4 = '''# Check path properties
from pathlib import Path
file_path = Path('topics/Modules_and_packages/pathlib_module.py')
dir_path = Path('topics/Modules_and_packages')

print(f"Does {file_path} exist? {file_path.exists()}")  
print(f"Is {file_path} a file? {file_path.is_file()}")  
print(f"Is {dir_path} a directory? {dir_path.is_dir()}")
#-------------------------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)   


    print_small_sub_heading("b) Reading and Writing Files", True)
    display_note("`pathlib` simplifies basic file I/O, removing the need for `with open(...)` in simple cases.", "tip")
    code5 = '''# Simple file reading and writing
from pathlib import Path
p = Path('tests/output_dump/greeting.txt')

p.write_text('Hello, pathlib!')
print("Wrote 'Hello, pathlib!' to greeting.txt")

content = p.read_text()
print(f"Read from file: {content}")
#------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. The Best of Both Worlds
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Summary: The Best of Both Worlds")
    display_note("Rule of thumb: Use `pathlib` for all filesystem path manipulation. Use `os` for everything else.", "example")
    display_note("Here is a realistic example combining both modules for their intended strengths.")
    code6 = '''# A practical example using both modules
from pathlib import Path
import os

# 1. Use os to get a secret from environment variables
api_key = os.getenv('API_KEY', 'not-set')
print(f"Retrieved API key using 'os.getenv()': {api_key}")

# 2. Use pathlib to define a clean, cross-platform path to a log file 
# Path.cwd() returns a Path object representing the current working directory.
log_dir = Path.cwd() / 'tests' / 'output_dump'
log_file = log_dir / 'activity.log'

# 3. Create the directory using pathlib's mkdir
log_dir.mkdir(parents=True, exist_ok=True)
print(f"Ensured log directory exists: {log_dir.exists()}")

# 4. Write to the log file
log_file.write_text(f"API Key Used: {api_key}\\n")
print(f"Writing log to log_file......")

# 5. Read the log file
content = log_file.read_text()
print(f"Reading logs from file: {content}")
#-----------------------------------------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)


if __name__ == "__main__":
    main(1)
