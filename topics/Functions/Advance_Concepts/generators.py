from helpers.display_utils import *

def main():
    print_heading("Generators in Python")

    imp_note_points("""
**Generators:**  
- *A way to create iterators in Python easily and efficiently—using either a function (with `yield`) or a generator expression.*
- *They allow you to produce sequence of values one-at-a-time, pausing and resuming execution as needed (saving memory!).*
- *Ideal for large data processing, streaming, pipelines, or anytime you want lazy evaluation instead of building a whole list in memory.*

**Core Topics:**
- Generator functions (`yield`)
- Generator expressions (like lazy list comprehensions)
- Real-world uses: infinite streams, file parsing, pipelines
    """)

    # -------------------------------------------------------------------------------
    # 1. Generator Function: The Basics (yield)
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Generator Function Basics (`yield`)")
    display_note("A generator function uses `yield` to return values one at a time. ", "info")
    display_note("Each time you call `next()`, execution resumes right after the last yield.", "info", message_continue=True)
    show_code_with_output("""
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

gen = count_up_to(3)
print(next(gen))    # 1
print(next(gen))    # 2
print(next(gen))    # 3
# next(gen)         # Raises StopIteration
"""
,
"""
1
2
3
""")

    display_note("`yield` temporarily suspends the function, saving its local state. When called again, it resumes right where it left off.", "tip")

    # -------------------------------------------------------------------------------
    # 2. Looping Over Generators
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Looping Over a Generator")
    show_code_with_output("""
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

values = count_up_to(10)                      
for val in values:
    if(val==5):
        print(val, end=' ')
        break
    else:
        print(val, end=' ')
print("\npause")

for i in range(5):
    print(next(values), end=' ')
"""
,
"""
1 2 3 4 5 
pause
6 7 8 9 10
"""
    )

    display_note("Generators are iterable! Use them directly in loops, comprehensions, or with tools like `sum()`, `list()`, etc.", "example")

    # -------------------------------------------------------------------------------
    # 3. Generator Expressions— Like Lazy List Comprehensions
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Generator Expressions (One-liners)")
    display_note("Generator expressions look like list comprehensions, but use parentheses. ", "info")
    display_note("They are *lazy*: items are computed one at a time, as needed.", "info", message_continue=True)
    show_code_with_output("""
squared = (x * x for x in range(4))
print(next(squared))   # 0
print(next(squared))   # 1
print(next(squared))   # 4
print(list(squared))   # [9]
""",
"""0
1
4
[9]
""")

    # -------------------------------------------------------------------------------
    # 4. Real-World: File Processing with Generators
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Real-World Example: Read Large File Line-By-Line")
    display_note("When reading large files, use generators to process one line at a time—never load all lines at once.", "tip")
    show_code_with_output("""
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

# Example usage:
example_lines = ["foo\n", "bar\n", "baz\n", "foobar\n"]
for line in grep("foo", example_lines):
    print(line.strip())
""",
"""
foo
foobar
""")

    # -------------------------------------------------------------------------------
    # 5. Infinite Generators
    # -------------------------------------------------------------------------------
    print_sub_heading("5. Infinite / Unbounded Generators")
    display_note("Generators can model infinite streams. Only compute as much as needed, so you don’t consume unbounded memory.", "warning")
    show_code_with_output("""
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

nat = natural_numbers()
for _ in range(5):
    print(next(nat), end=" ")
print()
""",
"""
1 2 3 4 5
""")

    # -------------------------------------------------------------------------------
    # 6. Sending Values, Generator Coroutines & `close()`
    # -------------------------------------------------------------------------------
    print_sub_heading("6. Advanced: Sending Values Into Generators")
    display_note("You can use `.send(value)` to send data back into a generator at each yield point. This is the base for Python coroutines.", "info")
    show_code_with_output("""
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
print(next(gen))    # Start, yields 0
print(gen.send(3))  # Yields 3
print(gen.send(5))  # Yields 8
gen.close()         # End
""",
"""
0
3
8""")

    # -------------------------------------------------------------------------------
    # 7. Generator vs List Comprehension: Memory Comparison
    # -------------------------------------------------------------------------------
    print_sub_heading("7. Generator Expressions vs List Comprehensions")
    imp_note_points("""
- List comprehensions build all elements at once and store them in memory: `[x*x for x in range(10**6)]`
- Generator expressions `(...)` compute values *one-at-a-time,* so memory is constant and very efficient for big data streams!
- Use generators when you only need to process one item at a time, especially for very large data.
    """)

    # -------------------------------------------------------------------------------
    # 8. Best Practices and Summary
    # -------------------------------------------------------------------------------
    print_sub_heading("8. Best Practices and Tips")
    imp_note_points("""
- Use generators for streaming, pipelines, and lazy evaluation.
- Either use `yield` (for custom generators) or `(expression for item in iter)` syntax (for generator expression).
- Don't turn a generator into a list unless you need all the results at once.
- Generators make code clean and efficient for big/unknown-sized input.
    """)

if __name__ == "__main__":
    main()
