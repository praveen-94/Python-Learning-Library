# pathlib_module_deep_dive.py

from helpers.display_utils import *
from pathlib import Path
import os # Imported for the final summary example

def main():
    print_heading("The `pathlib` Module: Modern Path Handling")
    imp_note_points("""
- The `pathlib` module (introduced in Python 3.4) offers a modern, object-oriented way to represent and manipulate filesystem paths.
- It is now the recommended approach for path manipulation, replacing the procedural functions in `os.path`.
- Its key advantages are improved readability, cross-platform consistency, and an intuitive API.
- A `Path` object represents a path, not just a string, making code cleaner and less error-prone.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Creating Paths and Joining Them
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Creating Paths and Joining Them")
    display_note("The most elegant feature of `pathlib` is using the `/` operator to join paths.")

    print_small_sub_heading("a) Creating a Path Object",True)
    show_code_with_output('''# Create a Path object from a string
from pathlib import Path
p = Path('documents/reports')
print(f"Created Path object: {p}") 
print(f"Object type: {type(p)}")'''
,
'''Created Path object: documents/reports
Object type: <class 'pathlib.PosixPath'> (or WindowsPath on Windows)''')

    print_small_sub_heading("b) Joining with the '/' Operator",True)
    display_note("This is much more readable than `os.path.join()`.")
    show_code_with_output('''# The intuitive way to build paths
from pathlib import Path
root = Path('/home/user')
config_path = root / 'app' / 'config.ini' 
print(config_path)'''
,
"/home/user/app/config.ini")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Accessing Path Components
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Accessing Path Components")
    display_note("`pathlib` provides simple attributes to get parts of a path, replacing complex `os.path` functions.")
    show_code_with_output('''# Extracting parts from a path
from pathlib import Path
p = Path('/home/user/data/archive.zip')

print(f"Parent directory: {p.parent}")
print(f"File name: {p.name}")
print(f"File stem (name without extension): {p.stem}") 
print(f"File extension (suffix): {p.suffix}")'''
,
'''Parent directory: /home/user/data
File name: archive.zip
File stem (name without extension): archive
File extension (suffix): .zip''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Checking Path Properties and File Operations
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Checking Properties and File Operations")

    print_small_sub_heading("a) Checking if a Path Exists",True)
    display_note("The path object has methods to check its own state.")
    show_code_with_output('''# Check path properties (simulated)
from pathlib import Path
# Assuming 'my_app/main.py' exists as a file
file_path = Path('my_app/main.py')
dir_path = Path('my_app')

print(f"Does {file_path} exist? {True}")  # Simulating file_path.exists()
print(f"Is {file_path} a file? {True}")   # Simulating file_path.is_file() 
print(f"Is {dir_path} a directory? {True}")# Simulating dir_path.is_dir()
'''
,
'''Does my_app/main.py exist? True
Is my_app/main.py a file? True
Is my_app a directory? True''')

    print_small_sub_heading("b) Reading and Writing Files", True)
    display_note("`pathlib` simplifies basic file I/O, removing the need for `with open(...)` in simple cases.", "tip")
    show_code_with_output('''# Simple file reading and writing (simulated)
from pathlib import Path
p = Path('greeting.txt')

# p.write_text('Hello, pathlib!')
print("Wrote 'Hello, pathlib!' to greeting.txt")

# content = p.read_text()
# print(f"Read from file: {content}")
print("Read from file: Hello, pathlib!")
''',
'''Wrote 'Hello, pathlib!' to greeting.txt
Read from file: Hello, pathlib!''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. The Best of Both Worlds
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Summary: The Best of Both Worlds")
    display_note("Rule of thumb: Use `pathlib` for all filesystem path manipulation. Use `os` for everything else.", "example")
    display_note("Here is a realistic example combining both modules for their intended strengths.")
    show_code_with_output('''# A practical example using both modules
from pathlib import Path
import os

# 1. Use os to get a secret from environment variables
api_key = os.getenv('API_KEY', 'not-set')
print(f"Retrieved API key using 'os.getenv()'.")

# 2. Use pathlib to define a clean, cross-platform path to a log file 
# Path.home() gets the user's home directory
log_dir = Path.home() / '.my_app' / 'logs'
log_file = log_dir / 'activity.log'

# 3. Create the directory using pathlib's mkdir
# log_dir.mkdir(parents=True, exist_ok=True)
print(f"Ensured log directory exists: {log_dir}")

# 4. Write to the log file
# log_file.write_text(f"API Key Used: {api_key}\\n")
print(f"Wrote log to: {log_file}")
'''
,
f'''Retrieved API key using 'os.getenv()'.
Ensured log directory exists: {Path.home() / '.my_app' / 'logs'}
Wrote log to: {Path.home() / '.my_app' / 'logs' / 'activity.log'}''')


if __name__ == "__main__":
    main()
