# helpers/display_utils.py
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax
from pathlib import Path
from rich.table import Table
from typing import List
from playwright.async_api import async_playwright
#from rich.columns import Columns
#import rich.terminal_theme as themes

#console = Console()
console = Console(record=True)

def print_heading(title: str, description: str = "This Program is for showing working of ")-> None:
    """
    Prints a stylish heading along with its use
    Args:
        title (str): Heading of any topic
        description (str): Details of operation or task to perform on that topic
    """
    panel = Panel(
    renderable=description + title,
    title=title,
    title_align="left",
    padding=(0,0,0,2),
    safe_box=True,
    border_style="bold red",
    width=136,
    style="on black" ) #Other arguments: subtitle="Demo", subtitle_align="left", width=30, height=10, expand=False, box=box.DOUBLE
    console.print(panel)


def print_sub_heading(title: str)-> None:
    """
    Prints a numbered section sub-heading like: '8) Formatting Methods'
    Args:
        title (str): SubHeading of any topic
    """
    print()
    panel = Panel(renderable=title, safe_box=True, border_style="bold cyan", style="on black", width=134)
    console.print(panel)


def print_small_sub_heading(title: str, from_new_line: bool = False)-> None:
    """
    Prints a numbered section sub-heading inside Sub-heading'
    Args:
        title (str): SubHeading of any topic
        from_new_line (bool): want heading to start from newline
    """
    if(from_new_line):
         print()
    print(f" # {title}:")
    print("-" * (len(title) + 6))  # Print a line of dashes equal to the length of the title plus 2 for padding

def display_note(message: str, type: str="note", icon: Optional[str]=None, color: Optional[str]=None, message_continue: bool=False)-> None:
    """
    Display a styled note message.
    Supported types: 'note', 'info', 'warning', 'tip', 'error', 'example'
    Args:
        message (str): Message to print
        type (str): Types of message
        icon (str): imoji to print along with type
    """
    icons = {
        "note": "📝",
        "info": "ℹ️ ",
        "warning": "⚠️ ",
        "tip": "💡",
        "error": "❌",
        "example": "📘",
    }

    colors = {
        "note": "magenta",
        "info": "cyan",
        "warning": "yellow",
        "tip": "green",
        "error": "red",
        "example": "blue",
    }

    icon = icon if icon else icons.get(type.lower())
    style = color if color else colors.get(type.lower())
    if(message_continue):
        icon_style_str=f"{icon} {type.capitalize()}: "
        icon_style_len=len(icon_style_str)  # calculating combine length of icon, type and message
        empty_string=(icon_style_len-1)*" " if(type.lower()=="info" or type.lower()=="warning") else (icon_style_len+1)*" "# assigning empty string of length calculate above
        console.print(f"[{style}]{empty_string}{message}[/]") # space + only message
    else:
        console.print(f"[{style}]{icon} {type.capitalize()}: {message}[/]")


def imp_note_points(points: str, title: str="Important Points")-> None:
    """
    Prints a stylish important points.
    Args:
       points (str): multiline string containing important notes
    """
    markdown = Markdown(points)
    panel = Panel.fit(
    renderable=markdown,
    title=title,
    title_align="left",
    safe_box=True,
    border_style="bold magenta",
    width=134,
    style="on black" )
    console.print(panel)

def show_code_with_output(code_str: str, output_str: str)-> None:
    """
    Render code and its output side-by-side using Rich panels.
    Args:
        code_str (str): The Python code to display.
        output_str (str): The output/result of the code.
    """
    #themes: gruvbox-dark, ansi_dark, fruity, monokai, github-dark
    syntax_panel = Panel(Syntax(code_str, "python", line_numbers=True, theme="gruvbox-dark"), title="🐍 Code", title_align="left", expand=False)
    output_panel = Panel(output_str, title="🖨️ Output", title_align="left", highlight=True, expand=False)
    #console.print(Columns([syntax_panel, output_panel], column_first=True))
    console.print(syntax_panel)
    console.print(output_panel)

def render_2d_table(data: List[List], title: str="📋 Data Table", inner_border: bool=False):
    if not data or not all(isinstance(row, list) for row in data):
        console.print("[bold red]Invalid or empty data provided.[/bold red]")
        return

    headers = data[0]
    rows = data[1:]
    table = Table(title=title, show_lines=inner_border, header_style="bold bright_cyan", title_justify="left", row_styles=["white", "grey23"])

    for header in headers: # Adding headers
        table.add_column(str(header), style="bold cyan")

    for row in rows: # Adding rows
        # Ensure all rows have the same number of columns
        padded_row = row + [""] * (len(headers) - len(row))
        table.add_row(*[str(cell) for cell in padded_row])

    console.print(table)

imp_note_points("""A package is a way to structure Python’s module namespace by using 'dotted module names'.  
Let's imagine a more complex file structure:  
***`project/`***  
***`├── main.py`***  
***`└── my_app/`***  
***`    ├── __init__.py`***  
***`    ├── math_ops.py`***  
***`    └── text_ops/`***  
***`        ├── __init__.py`***  
***`        └── formatting.py`***  
    """, "Example")
