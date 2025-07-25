# math_module_deep_dive.py

from helpers.display_utils import *
import math

def main():
    print_heading("The `math` Module: Mathematical Functions")
    imp_note_points("""
- The `math` module provides access to a wide range of mathematical functions and constants defined by the C standard.
- It operates on floating-point numbers. For complex number mathematics, you should use the `cmath` module.
- You do not need to install it; just `import math` to use its features.
- It is intended for more advanced math than basic arithmetic (`+`, `-`, `*`, `/`), which is already built into Python.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Constants
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Constants")
    display_note("The module provides access to fundamental mathematical constants.")
    display_note("`math.pi` is the mathematical constant π (pi). `math.e` is the mathematical constant e (Euler's number).")
    show_code_with_output('''# Accessing mathematical constants math.pi and math.e
import math
print(f"The value of Pi is: {math.pi}") 
print(f"The value of e is: {math.e}")'''
,
f"The value of Pi is: {math.pi}\nThe value of e is: {math.e}")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Number-Theoretic and Representation Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Number-Theoretic and Representation Functions")

    print_small_sub_heading("a) math.ceil() and math.floor()",True)
    display_note("`math.ceil(x)` returns the smallest integer greater than or equal to x (rounds up).")
    display_note("`math.floor(x)` returns the largest integer less than or equal to x (rounds down).")
    num_to_test = 9.2
    show_code_with_output(f'''# Rounding numbers up and down
import math
num = {num_to_test}
print(f"The ceiling of {{num}} is: {{math.ceil(num)}}") 
print(f"The floor of {{num}} is: {{math.floor(num)}}")'''
,
f"The ceiling of {num_to_test} is: {math.ceil(num_to_test)}\nThe floor of {num_to_test} is: {math.floor(num_to_test)}")

    print_small_sub_heading("b) math.fabs(x)",True)
    display_note("Returns the absolute value of x as a float. Similar to the built-in `abs()`, but always returns a float.")
    show_code_with_output('''# Get the absolute value
import math
print(f"Absolute value of -10 is: {math.fabs(-10)}") '''
,
f"Absolute value of -10 is: {math.fabs(-10)}")

    print_small_sub_heading("c) math.factorial(x)",True)
    display_note("Returns the factorial of x. Raises a `ValueError` if x is not an integer or is negative.")
    show_code_with_output('''# Calculate the factorial of a number
import math
print(f"Factorial of 5 is: {math.factorial(5)}") '''
,
f"Factorial of 5 is: {math.factorial(5)}")

    print_small_sub_heading("d) math.gcd(a, b)",True)
    display_note("Returns the Greatest Common Divisor of two integers `a` and `b`.")
    show_code_with_output('''# Find the greatest common divisor
import math
print(f"The GCD of 48 and 60 is: {math.gcd(48, 60)}") '''
,
f"The GCD of 48 and 60 is: {math.gcd(48, 60)}")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Power and Logarithmic Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Power and Logarithmic Functions")

    print_small_sub_heading("a) math.sqrt(x)",True)
    display_note("Returns the square root of x. Note that the result is always a float.")
    show_code_with_output('''# Calculate the square root
import math
print(f"Square root of 64 is: {math.sqrt(64)}") '''
,
f"Square root of 64 is: {math.sqrt(64)}")

    print_small_sub_heading("b) math.pow(x, y)",True)
    display_note("Returns x raised to the power of y (`x**y`). The result is always a float.")
    show_code_with_output('''# Calculate a number to the power of another
import math
print(f"3 to the power of 4 is: {math.pow(3, 4)}") '''
,
f"3 to the power of 4 is: {math.pow(3, 4)}")

    print_small_sub_heading("c) math.log(x, [base])",True)
    display_note("With one argument, returns the natural logarithm (base e) of x.")
    display_note("With two arguments, returns the logarithm of x to the given base.", "tip")
    show_code_with_output('''# Calculate logarithms
import math
# Natural logarithm (base e)
print(f"Natural log of 10 is: {math.log(10)}")
# Logarithm with a specific base
print(f"Log base 10 of 100 is: {math.log(100, 10)}") '''
,
f"Natural log of 10 is: {math.log(10)}\nLog base 10 of 100 is: {math.log(100, 10)}")


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Trigonometric Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Trigonometric Functions")
    display_note("These functions expect their arguments to be in radians, not degrees.", "warning")

    print_small_sub_heading("a) math.degrees() and math.radians()",True)
    display_note("Convenience functions to convert between degrees and radians.")
    angle_deg = 180.0
    show_code_with_output(f'''# Converting between degrees and radians
import math
degrees = {angle_deg}
radians = math.radians(degrees)
print(f"{{degrees}} degrees is {{radians}} radians.")

converted_degrees = math.degrees(radians)
print(f"{{radians}} radians is {{converted_degrees}} degrees.") '''
,
f"{angle_deg} degrees is {math.radians(angle_deg)} radians.\n{math.radians(angle_deg)} radians is {math.degrees(math.radians(angle_deg))} degrees.")

    print_small_sub_heading("b) math.sin(), math.cos(), math.tan()",True)
    display_note("Calculate the sine, cosine, and tangent of an angle given in radians.")
    angle_deg_for_trig = 90
    angle_rad_for_trig = math.radians(angle_deg_for_trig)
    show_code_with_output(f'''# Using trigonometric functions
import math
angle_degrees = {angle_deg_for_trig}
angle_radians = math.radians(angle_degrees)

print(f"Sine of {{angle_degrees}} degrees is: {{math.sin(angle_radians)}}")
print(f"Cosine of {{angle_degrees}} degrees is: {{math.cos(angle_radians)}}") '''
,
f'''Sine of {angle_deg_for_trig} degrees is: {math.sin(angle_rad_for_trig)}
Cosine of {angle_deg_for_trig} degrees is: {math.cos(angle_rad_for_trig)}''')
    display_note("Note: Due to floating-point inaccuracies, `math.cos(math.radians(90))` might be a very small number close to zero, not exactly 0.0.", "info")


if __name__ == "__main__":
    main()
