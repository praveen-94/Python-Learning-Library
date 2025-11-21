from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Control statements", topic_number)
    imp_note_points("""
- Control statements are used to control the flow of execution in a program based on certain conditions or iterations in Python. 
- They allow you to make decisions, repeat actions, and manage the flow of your program effectively.
- Python uses indentation to define blocks of code, so there are no curly braces like in other languages.""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Selection Control statements
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Selection Control statements")
    print_small_sub_heading("1) if statement")
    code1 = '''# Example of if statement
user_input = 10
print(f"Enter Number is: {user_input}")
if(user_input == 10):
    print("User input is equal to 10")
#-------------------------------------#'''

    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)
    
    #-----------------------------------------------------------------
    print_small_sub_heading("2) if-else statement", True)
    code2 = '''# Example of if-else statement
user_input = 1234
print(f"Enter Number is: {user_input}")
if(user_input % 2 == 0):
    print("User input is even")
else:
    print("User input is odd")
#-------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)
    
    #------------------------------------------------------------------
    print_small_sub_heading("3) if-elif-else statement", True)
    code3 = '''# Example of if-elif-else statement
user_input = -20
print(f"Enter Number is: {user_input}")
if(user_input > 0):
    print("User input is positive")
elif(user_input < 0):
    print("User input is negative")
else:
    print("User input is zero")
#--------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #--------------------------------------------------------------------
    print_small_sub_heading("4) Dictionaries as Switch-Like Mappings", True)
    display_note("""Python does not have a traditional switch-case statement, but you can use dictionaries to achieve similar functionality.
This approach allows you to define functions for each command and retrieve them using the input command as a key.""")
    display_note("If you want to handle unknown commands gracefully, provide a default function that returns a message for unknown commands.", "tip")
    display_note("""This way, you can avoid using multiple if-elif statements and keep your code clean and efficient.
You can also use a lambda function to define the default or main behavior for unknown commands.""", "example") 
    code4 = '''# Example of dictionary as switch-like mapping
commands = {
    "start": lambda: "Starting the process...",
    "stop": lambda: "Stopping the process...",
    "pause": lambda: "Pausing the process...",
    "resume": lambda: "Resuming the process...",
    "unknown": lambda: "Unknown command!"
}
user_input1 = "resume"
user_input2 = "play"
print(f"Enter Command is: {user_input1}")
print(commands.get(user_input1, commands["unknown"])())
print(f"Enter Command is: {user_input2}")
print(commands.get(user_input2, commands["unknown"])())
#--------------------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)
    
    #------------------------------------------------------------------
    print_small_sub_heading("5) Ternary Operator", True)
    display_note("The ternary operator is a shorthand way to write an if-else statement in a single line.")
    display_note("It is useful for simple conditions where you want to assign a value based on a condition.", "tip")
    code5 ='''# Example of ternary operator
user_input = 33
print(f"Enter Number is: {user_input}")
result = "Even" if user_input % 2 == 0 else "Odd"
print(f"User input is {result}")
#-------------------------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)
    
    #------------------------------------------------------------------
    print_small_sub_heading("6) Match Case Statement", True)
    display_note("The match case statement is a powerful way to handle multiple conditions based on the value of a variable.")
    display_note("It is similar to switch-case statements in other languages.", "tip")
    display_note("It allows you to match patterns and execute code based on the matched pattern.", "example")
    display_note("The match case statement is available in Python 3.10 and later.", "warning")
    code6 = '''# Example of match case statement
user_input = "thursday"
print(f"Enter day of week is: {user_input}")
match user_input:
    case "monday":
        print("Start of the work week!")
    case "tuesday":
        print("It's Tuesday!")
    case "wednesday":
        print("Midweek already!")
    case "thursday":
        print("Almost the weekend!")
    case "friday":
        print("Last day of the work week!")
    case "saturday" | "sunday":
        print("It's the weekend!")
    case _:
        print("That's not a valid day of the week.")
#----------------------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Iteration Control statements
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Iteration Control statements")
    print_sub_heading("1) for loop")
    print_small_sub_heading("Example of simple for loop")
    code7 = '''# Example of for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
#--------------------------------------#'''
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)
 
    #--------------------------------------------------------------
    print_small_sub_heading("Using for loop with range:", True)
    code8 = '''# Example of for loop with range
# range(start, stop, step): generate from start to stop-1 with step 
for i in range(5):  
    print(f"Number: {i}")
#--------------------------------------#'''
    output8 = run_code_snippet(code8)
    show_code_with_output(code8, output8)

    #------------------------------------------------------------------
    print_small_sub_heading("Using for loop with else statement:", True)
    display_note("The else block in a for loop executes when the loop completes normally (i.e., not terminated by a break statement)")
    code9 = '''# Example of for loop with else statement
user_input = "Disco"
print(f"Enter string is: {user_input}")
print(f"Checking string for 'o': ", end="")
for char in user_input:
    if char == 'o':
        print(f"Present at index {user_input.index(char)}")
        break
else:
    print("Not present")

print(f"Checking string for 'a': ", end="")
for char in user_input:
    if char == 'a':
        print(f"Present at index {user_input.index(char)}")
        break
else:
    print("Not present")
#-------------------------------------------#'''
    output9 = run_code_snippet(code9)
    show_code_with_output(code9, output9)

    #----------------------------------------------------------------------------------
    print_small_sub_heading("Use of break and continue statements in for loop:", True)
    display_note("The break statement is used to exit the loop prematurely, and the continue statement is used to skip the current iteration.")
    code10 = '''# Demonstrating break and continue in a for loop
end_limit = 45
print(f"Enter end limit for range is: {end_limit}")
for i in range(end_limit):  # showing use of break statement and continue statement
    if(i % 2 == 0):
        continue  # Skip printing even numbers
    elif(i > 20):
        break  # Stop the loop when i is greater than 20
    else:
        print(i, end=", ")
print()
#---------------------------------------------------------------------------------------#'''
    output10 = run_code_snippet(code10)
    show_code_with_output(code10, output10)

    # 2) while loop............................................................
    print_sub_heading("2) while loop")
    print_small_sub_heading("Using while loop to print numbers from 1 to 5:")
    code11 = '''# while loop
i = 1
while(i <= 5):
    print(f"Number: {i}")
    i += 1
#---------------------------#'''
    output11 = run_code_snippet(code11)
    show_code_with_output(code11, output11)
    
    #---------------------------------------------------------------------------
    print_small_sub_heading("Using while loop with else statement:")
    display_note("The else block in a while loop executes only when the condition becomes false and the loop ends naturally (not via break).")
    code12 = '''# while with else
i = 1
while(i <= 5):
    print(f"Number: {i}")
    i += 1
else:
    print("Loop completed without break.")
#------------------------------------------#'''
    output12 = run_code_snippet(code12)
    show_code_with_output(code12, output12)

    #-------------------------------------------------------------------------
    print_small_sub_heading("Using pass statement in while loop:", True)
    display_note("""The pass statement is a null operation — it acts as a placeholder when no action is required.
You might use 'pass' when the loop body is required syntactically, but you don’t want it to do anything yet.""")
    code13 = '''# use of pass
i = 1
while(i <= 5):
    if(i == 3):
        pass  # Do nothing for i = 3
    else:
        print(f"Number: {i}")
    i += 1
#--------------------------------------#'''
    output13 = run_code_snippet(code13)
    show_code_with_output(code13, output13)

    #------------------------------------------------------------------------------------
    print_small_sub_heading("Using loop control statements in nested loops:", True)
    display_note("""Loop control statements like 'break' and 'continue' affect only the loop they are placed in— not the outer loops.
The outer loop continues even after inner loop is broken. This helps in fine-grained control over nested iterations.""")
    code14 = ''' # Nested loop example
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        if j == 2:
            continue  # Skip when j is 2
        elif j == 3:
            break  # Break the inner loop when j is 3
        print(f"i: {i}, j: {j}", end=" | ")
    print()  # New line after inner loop completes
#------------------------------------------------------#'''
    output14 = run_code_snippet(code14)
    show_code_with_output(code14, output14)
