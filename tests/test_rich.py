from rich.console import Console
import rich

print(rich.__spec__)


console = Console()
console.print("[bold red]Error:[/] File not found.")
console.print("Welcome to [italic cyan]Praveen's CLI Toolkit[/]")
console.print("[underline green]Success:[/] Operation completed.")

from rich.console import Console
from rich.markdown import Markdown

console = Console()

md_text = """
<!-- Headings -->
# Heading Level 1
## Heading Level 2
### Heading Level 3
#### Heading Level 4
##### Heading Level 5
###### Heading Level 6

---

<!-- Text styles -->
**This is bold text**  
*This is italic text*  
***This is bold and italic***  
~~This is strikethrough~~

---

<!-- Blockquote -->
> This is a blockquote  
>> This is a nested blockquote

---

<!-- Lists -->
- Bullet list item A
- Bullet list item B
  - Sub item B1
  - Sub item B2

1. Numbered item 1
2. Numbered item 2
   1. Sub item 2.1
   2. Sub item 2.2

---

<!-- Inline code -->
You can call `len()` to get the length of a list.

---

<!-- Code block -->
```python
def add(x, y):
    return x + y

print(add(5, 3))  # Output: 8

"""

markdown = Markdown(md_text)
console.print(markdown)
print()

from rich.console import Console
from rich.syntax import Syntax

console = Console()

code = """def greet(name):
    return f"Hello, {name}!"
"""

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
print()

md_text = """
 - Functions in Python are defined using the `def` keyword, and they can take parameters and return values.
 - we can pass argumnet to function by two ways, `pass by value` and `pass by reference`.
 - In Python, all arguments are passed by reference, but immutable types (like integers, strings, tuple) behave like pass by value.
"""

from rich.panel import Panel
from rich import box
def print_heading(title):
    """Prints a stylish important points."""
    panel = Panel.fit(
    renderable=title,
    safe_box=True,
    border_style="bold green",
    box=box.ASCII,
    style="on black" )
    console.print(panel)

print_heading("Welcome to sub-sub-heading")


from rich.columns import Columns

def show_code_with_output(code_str: str, output_str: str):
    """
    Render code and its output side-by-side using Rich panels.

    Args:
        code_str (str): The Python code to display.
        output_str (str): The output/result of the code.
    """
    console = Console()

    syntax_panel = Panel(
        Syntax(code_str, "python", line_numbers=False, theme="monokai"),
        title="🐍 Code",
        border_style="bright_cyan"
    )

    output_panel = Panel(
        output_str,
        title="🖨️ Output",
        border_style="bright_green"
    )

    console.print(Columns([syntax_panel, output_panel]))

# ✅ Example usage:
show_code_with_output(
    'print("Hello, Praveen!")',
    'Hello, Praveen!'
)


def display_code_n_output(code,output):
        console.print(f"[bold bright_white]{code}:[/]")
        #console.print(Syntax)
        console.print(f"\n[bold bright_green]Output:[/] {output}")

display_code_n_output('print("Hello, Praveen!")','Hello, Praveen!')
