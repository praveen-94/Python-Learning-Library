# os_module_essentials.py

from helpers.display_utils import *
import os

def main():
    print_heading("The `os` Module: System & Process Management")
    imp_note_points("""
- The `os` module is Python's interface for core operating system services.
- While the `pathlib` module is now preferred for path manipulation, `os` remains essential for system-level tasks.
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
    show_code_with_output('''# Get the name of the OS
import os
print(f"OS Name: {os.name}")'''
,
f"OS Name: {os.name}")

    print_small_sub_heading("b) os.getcwd()",True)
    display_note("Returns a string representing the Current Working Directory (CWD).")
    current_dir = os.getcwd()
    show_code_with_output('''# Get the current working directory
import os
print(f"Current Directory: {os.getcwd()}") '''
,
f"Current Directory: {current_dir}")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Directory Management (The Traditional Way)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Directory Management (The Traditional Way)")
    display_note("These functions create, rename, and delete directories. Operations are simulated for safety.", "warning")
    display_note("While these work, the `pathlib` module offers more convenient, object-oriented alternatives.", "tip")

    print_small_sub_heading("a) os.mkdir('path') and os.makedirs('path/to/dir')",True)
    display_note("`mkdir` creates a single directory. `makedirs` creates all intermediate directories (recursive).")
    show_code_with_output('''# Create a single and a nested directory
import os
# os.mkdir('new_folder')
print("Directory 'new_folder' created.") 
# os.makedirs('parent/child')
print("Directory 'parent/child' created.")'''
,
'''Directory 'new_folder' created.
Directory 'parent/child' created.''')

    print_small_sub_heading("b) os.listdir(path='.')",True)
    display_note("Returns a list containing the names of the entries in a directory.")
    show_code_with_output('''# List directory contents (simulated output)
import os
entries = os.listdir('.') 
print(entries)'''
,
"['docs', 'main.py', 'assets']")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Environment Variables
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Environment Variables")
    display_note("This is a key use case for the `os` module: securely accessing system configuration.")
    display_note("`os.environ` is a dictionary-like object of all environment variables.")
    display_note("`os.getenv('VAR')` is a safer way to get one variable, as it returns `None` if the key doesn't exist, preventing an error.", "tip")
    # Simulating output for privacy and consistency
    show_code_with_output('''# Get environment variables safely
import os

# Get the value of the 'PATH' variable (output is truncated) 
path_var = os.getenv('PATH', 'Not Found')
print(f"PATH (truncated): {path_var[:30]}...")

# Get a variable that likely doesn't exist
api_key = os.getenv('MY_API_KEY', 'No API Key was found')
print(f"My API Key: {api_key}")'''
,
f'''PATH (truncated): {os.getenv('PATH', '')[:30]}...
My API Key: No API Key was found''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Running System Commands
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Running System Commands")
    display_note("Allows you to execute shell commands. Use this with caution, as it can be a security risk if used with untrusted input.", "warning")
    display_note("The `subprocess` module is a more powerful and safer alternative for complex cases.", "tip")
    show_code_with_output('''# Execute a simple shell command (e.g., 'echo')
import os
# The return value is the exit code of the command (0 usually means success) 
# os.system('echo Hello from the OS!')
print("Command 'echo Hello from the OS!' executed.")
print("Output would appear directly in the console: Hello from the OS!")''' 
,
'''Command 'echo Hello from the OS!' executed.
Output would appear directly in the console: Hello from the OS!''')


if __name__ == "__main__":
    main()
