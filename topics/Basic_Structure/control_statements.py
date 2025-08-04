from helpers.display_utils import *

def main():
    print_heading("Control statements")
    imp_note_points("""
- Control statements are used to control the flow of execution in a program based on certain conditions or iterations in Python. 
- They allow you to make decisions, repeat actions, and manage the flow of your program effectively.
- Python uses indentation to define blocks of code, so there are no curly braces like in other languages.""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Selection Control statements
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Selection Control statements")
    print_small_sub_heading("1) if statement")
    user_input = 10
    show_code_with_output('''# Example of if statement
user_input = 10
print("Enter Number is: {user_input})
if(user_input == 10):
    print("User input is equal to 10")'''
,
"Enter Number is: " + str(user_input) + "\n" +
"User input is equal to 10" if user_input == 10 else "")

    print_small_sub_heading("2) if-else statement", True)
    user_input2 = 1234
    show_code_with_output('''# Example of if-else statement
user_input2 = 1234
print("Enter Number is: {user_input2})
if(user_input2 % 2 == 0):
    print("User input is even")
else:
    print("User input is odd")'''
,
"Enter Number is: " + str(user_input2) + "\n" +
"User input is even" if user_input2 % 2 == 0 else "User input is odd")

    print_small_sub_heading("3) if-elif-else statement", True)
    user_input3 = -20
    show_code_with_output('''# Example of if-elif-else statement
user_input3 = -20
print("Enter Number is: {user_input3})
if(user_input3 > 0):
    print("User input is positive")
elif(user_input3 < 0):
    print("User input is negative")
else:
    print("User input is zero")'''
,
"Enter Number is: " + str(user_input3) + "\n" +
"User input is positive" if user_input3 > 0 else "User input is negative" if user_input3 < 0 else "User input is zero")

    print_small_sub_heading("4) Dictionaries as Switch-Like Mappings", True)
    display_note("Python does not have a traditional switch-case statement, but you can use dictionaries to achieve similar functionality.")
    display_note("This approach allows you to define functions for each command and retrieve them using the input command as a key.")
    display_note("If you want to handle unknown commands gracefully, provide a default function that returns a message for unknown commands.", "tip")
    display_note("This way, you can avoid using multiple if-elif statements and keep your code clean and efficient.", "example")
    display_note("You can also use a lambda function to define the default or main behavior for unknown commands.", "example") 
    commands = {
        "start": lambda: "Starting the process...",
        "stop": lambda: "Stopping the process...",
        "pause": lambda: "Pausing the process...",
        "resume": lambda: "Resuming the process...",
        "unknown": lambda: "Unknown command!"
    }
    user_input4 = "resume"
    show_code_with_output('''# Example of dictionary as switch-like mapping
commands = {
    "start": lambda: "Starting the process...",
    "stop": lambda: "Stopping the process...",
    "pause": lambda: "Pausing the process...",
    "resume": lambda: "Resuming the process...",
    "unknown": lambda: "Unknown command!"
}
user_input4 = "resume"
print("Enter Command is: {user_input4})
print(commands.get(user_input4, commands["unknown"])())'''
,
"Enter Command is: " + str(user_input4) + "\n" +
commands.get(user_input4, commands["unknown"])())

    print_small_sub_heading("5) Ternary Operator", True)
    display_note("The ternary operator is a shorthand way to write an if-else statement in a single line.")
    display_note("It is useful for simple conditions where you want to assign a value based on a condition.", "tip")
    user_input5 = 33
    show_code_with_output('''# Example of ternary operator
user_input5 = 33
print("Enter Number is: {user_input5})
result = "Even" if user_input5 % 2 == 0 else "Odd"
print(f"User input is {result}")'''
,
"Enter Number is: " + str(user_input5) + "\n" +
f"User input is {'Even' if user_input5 % 2 == 0 else 'Odd'}")

    print_small_sub_heading("6) Match Case Statement", True)
    display_note("The match case statement is a powerful way to handle multiple conditions based on the value of a variable.")
    display_note("It is similar to switch-case statements in other languages.", "tip")
    display_note("It allows you to match patterns and execute code based on the matched pattern.", "example")
    display_note("The match case statement is available in Python 3.10 and later.", "warning")
    user_input6 = "thursday"
    show_code_with_output('''# Example of match case statement
user_input6 = "thursday"
print("Enter day of week is: {user_input6})
match user_input8:
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
        print("That's not a valid day of the week.")'''
,
"Enter day of week is: " + str(user_input6) + "\n" +
"That's not a valid day of the week." if user_input6 not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] else
"Start of the work week!" if user_input6 == "monday" else
"Last day of the work week!" if user_input6 == "friday" else    
"It's the weekend!" if user_input6 in ["saturday", "sunday"] else
"Midweek already!" if user_input6 == "wednesday" else       
"It's Tuesday!" if user_input6 == "tuesday" else
"Almost the weekend!" if user_input6 == "thursday" else "")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Iteration Control statements
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("Iteration Control statements")
    print_sub_heading("1) for loop")
    print_small_sub_heading("Example of simple for loop")
    show_code_with_output('''# Example of for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")'''
, "\n".join([f"I like {fruit}" for fruit in ["apple", "banana", "cherry"]]))

    print_small_sub_heading("Using for loop with range:", True)
    show_code_with_output('''# Example of for loop with range
for i in range(5):  # range(start, stop, step): generate from start to stop-1 with step
    print(f"Number: {i}")'''
, "\n".join([f"Number: {i}" for i in range(5)]))

    print_small_sub_heading("Using for loop with else statement:", True)
    display_note("The else block in a for loop executes when the loop completes normally (i.e., not terminated by a break statement")
    user_input7 = "Disco"
    output_lines = []
    for char in user_input7:
        if char == 'o':
            break
        output_lines.append(f"Character: {char}")
    else:
        output_lines.append("Loop completed without break.")
    show_code_with_output('''# Example of for loop with else statement
user_input7 = "Disco"
print("Enter string is: {user_input7})
for char in "hello":
    if char == 'o':
        break
    print(f"Character: {char}")
else:
    print("Loop completed without break.")'''
,
"Enter string is: " + user_input7 + "\n" +
"\n".join(output_lines))

    print_small_sub_heading("Use of break and continue statements in for loop:", True)
    display_note("The break statement is used to exit the loop prematurely, and the continue statement is used to skip the current iteration.")
    end_limit = 45
    show_code_with_output('''# Demonstrating break and continue in a for loop
end_limit = 45
print("Enter end limit for range is: {end_limit}")
for i in range({end_limit}):  # showing use of break statement and continue statement
    if(i % 2 == 0):
        continue  # Skip printing even numbers
    elif(i > 20):
        break  # Stop the loop when i is greater than 20
    else:
        print(i, end=", ")
print()'''
,
"Enter end limit for range is: " + str(end_limit) + "\n" +
", ".join([str(i) for i in range(1, 21, 2)]) + ", ")
    print()

    # 2) while loop............................................................
    print_sub_heading("2) while loop")
    print_small_sub_heading("Using while loop to print numbers from 1 to 5:")
    show_code_with_output('''i = 1
while(i <= 5):
    print(f"Number: {i}")
    i += 1''',
", ".join([f"Number: {i}" for i in range(1, 6)]))

    print_small_sub_heading("Using while loop with else statement:")
    display_note("The else block in a while loop executes only when the condition becomes false and the loop ends naturally (not via break).")
    show_code_with_output('''i = 1
while(i <= 5):
    print(f"Number: {i}")
    i += 1
else:
    print("Loop completed without break.")''',
", ".join([f"Number: {i}" for i in range(1, 6)]) + ", Loop completed without break.")

    print_small_sub_heading("Using pass statement in while loop:", True)
    display_note("The pass statement is a null operation — it acts as a placeholder when no action is required.")
    display_note("You might use 'pass' when the loop body is required syntactically, but you don’t want it to do anything yet.")
    show_code_with_output('''i = 1
while(i <= 5):
    if(i == 3):
        pass  # Do nothing for i = 3
    else:
        print(f"Number: {i}")
    i += 1''',
", ".join([f"Number: {i}" for i in range(1, 6) if i != 3]))

    print_small_sub_heading("Using loop control statements in nested loops:", True)
    display_note("Loop control statements like 'break' and 'continue' affect only the loop they are placed in — not the outer loops.")
    display_note("The outer loop continues even after inner loop is broken. This helps in fine-grained control over nested iterations.")
    show_code_with_output(''' #Nested loop example
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        if j == 2:
            continue  # Skip when j is 2
        elif j == 3:
            break  # Break the inner loop when j is 3
        print(f"i: {i}, j: {j}", end=" | ")
    print()  # New line after inner loop completes''',
"i: 1, j: 1 | \ni: 2, j: 1 | \ni: 3, j: 1 | ")
