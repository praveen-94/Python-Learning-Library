# os_module_essentials.py

from helpers.display_utils import *
import os

def main(topic_number: int):
    print_heading("The `os` Module: System & Process Management", topic_number)
    imp_note_points("""
- The ___os___ module is Python's interface for core operating system services.
- While the ___pathlib___ module is now preferred for path manipulation, ___os___ remains essential for system-level tasks.
- Key responsibilities include managing directories, running system commands, and accessing environment variables.
- Its behavior can vary across operating systems (e.g., 'posix' for Linux/macOS, 'nt' for Windows).
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. System Information
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. System Information")
    display_note("These functions provide information about the operating system and the current process.")

    print_small_sub_heading("a) os.name", True)
    display_note("Returns the name of the operating system dependent module imported. ('posix', 'nt', 'java').")
    code1 = '''# Get the name of the OS
import os
print(f"OS Name: {os.name}")
#----------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    print_small_sub_heading("b) os.getcwd()",True)
    display_note("Returns a string representing the Current Working Directory (CWD).")
    code2 = '''# Get the current working directory
import os
#current_dir = os.getcwd()
print("Current Directory: {current_dir}")
#-----------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Directory Management (The Traditional Way)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Directory Management (The Traditional Way)")
    display_note("These functions create, rename, and delete directories. Operations are simulated for safety.", "warning")
    display_note("While these work, the `pathlib` module offers more convenient, object-oriented alternatives.", "tip")

    print_small_sub_heading("a) os.mkdir('path') and os.makedirs('path/to/dir')",True)
    display_note("`mkdir` creates a single directory. `makedirs` creates all intermediate directories (recursive).")
    code3 = '''# Create a single and a nested directory
import os
print("Checking directory exist or not before creating...")
print(f"Is directory 'tests/output_dump/new_folder' exist:", end=" ")
print(os.path.isdir('tests/output_dump/new_folder'))
print(f"Is directory 'tests/output_dump/new_folder/new_subfolder/child' exist:", end=" ")
print(os.path.isdir('tests/output_dump/new_folder/new_subfolder/child'))

print("\\nCreating directories...")
os.mkdir('tests/output_dump/new_folder')
print("Directory 'tests/output_dump/new_folder' created.") 
os.makedirs('tests/output_dump/new_folder/new_subfolder/child')
print("Directory 'tests/output_dump/new_folder/new_subfolder/child' created.")

print("\\nChecking directory existence after creation...")
print(f"Is directory 'tests/output_dump/new_folder' exist:", end=" ")
print(os.path.isdir('tests/output_dump/new_folder'))
print(f"Is directory 'tests/output_dump/new_folder/new_subfolder/child' exist:", end=" ")
print(os.path.isdir('tests/output_dump/new_folder/new_subfolder/child'))
#----------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    print_small_sub_heading("b) os.listdir(path='.')",True)
    display_note("Returns a list containing the names of the entries in a directory.")
    code4 = '''# List directory contents (simulated output)
import os
entries = os.listdir('.') 
for entry in entries:
    print(entry)
#------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Environment Variables
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Environment Variables")
    display_note("""This is a key use case for the `os` module: securely accessing system configuration.
`os.environ` is a dictionary-like object of all environment variables.""")
    display_note("`os.getenv('VAR')` is a safer way to get one variable, as it returns `None` if the key doesn't exist, preventing an error.", "tip")
    code5 = '''# Get environment variables safely
import os

# Get the value of the 'PATH' variable (output is truncated) 
#path_var = os.getenv('PATH', 'Not Found')
print("PATH (truncated): {path_var}")

# Get a variable that likely doesn't exist
#api_key = os.getenv('MY_API_KEY', 'No API Key was found')
print("My API Key: No API Key was found")
#-----------------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Running System Commands
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Running System Commands")
    display_note("""`os.system(command)` runs the command (a string) in the system shell (like Bash on Linux/macOS or CMD on Windows). Output appears directly in the console.
It behaves just like typing the command into your terminal manually.""")
    display_note("Allows you to execute shell commands. Use this with caution, as it can be a security risk if used with untrusted input.", "warning")
    display_note("The `subprocess` module is a more powerful and safer alternative for complex cases.", "tip")
    code6 = '''# Execute a simple shell command (e.g., 'echo')
import os
# The return value is the exit code of the command (0 usually means success) 
#os.system('ls')
print("Command 'ls' executed.")
#----------------------------------------------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)


if __name__ == "__main__":
    main(1)
