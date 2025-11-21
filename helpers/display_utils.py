# helpers/display_utils.py

from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich import box
from pathlib import Path
from playwright.sync_api import sync_playwright
from .custom_terminal_themes import get_terminal_theme
from rich.table import Table
from typing import List
from pathlib import Path
import re
import io
import sys
import traceback
#from rich.columns import Columns
#import rich.terminal_theme as themes

console = Console(record=True)

# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Print Heading
# ─────────────────────────────────────────────────────────────────────────────────────────────
def print_heading(title: str, topic_number: int)-> None:
    """
    Prints a stylish heading along with its use
    Args:
        title (str): Heading of any topic
        topic_number (int): Topic number for reference
    """
    panel = Panel(
    renderable=title,
    title="Chapter " + str(topic_number),
    title_align="left",
    padding=(0,0,0,2),
    safe_box=True,
    width=122,
    style="#870000") #Other arguments: subtitle="Demo", subtitle_align="left", width=30, height=10, expand=False, box=box.DOUBLE
    console.print(panel)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Print Sub Heading
# ─────────────────────────────────────────────────────────────────────────────────────────────
def print_sub_heading(title: str)-> None:
    """
    Prints a numbered section sub-heading like: '8) Formatting Methods'
    Args:
        title (str): SubHeading of any topic
    """
    print()
    panel = Panel(title="Topic", title_align="left", renderable=title, safe_box=True, width=120, style="#000087")
    console.print(panel)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Print Small Sub Heading
# ─────────────────────────────────────────────────────────────────────────────────────────────
def print_small_sub_heading(title: str, from_new_line: bool = False)-> None:
    """
    Prints a numbered section sub-heading inside Sub-heading'
    Args:
        title (str): SubHeading of any topic
        from_new_line (bool): want heading to start from newline
    """
    if(from_new_line):
         print()
    panel = Panel(renderable=title, safe_box=True, width=115, style="#0000d7")
    console.print(panel)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Print Note
# ─────────────────────────────────────────────────────────────────────────────────────────────
def display_note(message: str, type: str="note", icon: Optional[str]=None, color: Optional[str]=None)-> None:
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
        "info": "ℹ️",
        "warning": "⚠️",
        "tip": "💡",
        "error": "❌",
        "example": "📘",
    }

    colors = {
        "note": "#8700af",
        "info": "bold #00afaf",
        "warning": "bold #d75f00",
        "tip": "bold #008700",
        "error": "#d70000",
        "example": "#00005f",
    }

    icon = icon if icon else icons.get(type.lower())
    style = str(color if color else colors.get(type.lower()))
    title_name = f"{icon}{type.capitalize()}" if icon else type.capitalize()
    panel = Panel(renderable=message, title=title_name, title_align="left", safe_box=True, width=115, style=style, box=box.ASCII2)
    console.print(panel)

    
# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Print Important Note Points
# ─────────────────────────────────────────────────────────────────────────────────────────────
def imp_note_points(points: str, topic: str="Important Points")-> None:
    """
    Prints a stylish important points.
    Args:
       points (str): multiline string containing important notes
    """
    markdown = Markdown(points,)
    panel = Panel.fit(
    renderable=markdown,
    title=topic,
    title_align="left",
    safe_box=True,
    width=120,
    style="#000000",
    highlight=True
    ) #Other arguments: subtitle="Demo", subtitle_align="left", width=30, height=10, expand=False, box=box.DOUBLE
    console.print(panel)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Render 2D Table
# ─────────────────────────────────────────────────────────────────────────────────────────────
def render_2d_table(data: List[List], title: str="📋 Data Table", inner_border: bool=False):
    if not data or not all(isinstance(row, list) for row in data):
        console.print("[bold red]Invalid or empty data provided.[/bold red]")
        return

    headers = data[0]
    rows = data[1:]
    table = Table(title=title, show_lines=inner_border, title_justify="left", width=120, header_style="#875f00", border_style="#000000")

    for header in headers: # Adding headers
        table.add_column(str(header))

    for row in rows: # Adding rows
        # Ensure all rows have the same number of columns
        padded_row = row + [""] * (len(headers) - len(row))
        table.add_row(*[str(cell) for cell in padded_row], style="#000000")

    console.print(table)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Show Code with Output
# ─────────────────────────────────────────────────────────────────────────────────────────────
def show_code_with_output(code_str: str, output_str: str)-> None:
    """
    Render code and its output side-by-side using Rich panels.
    Args:
        code_str (str): The Python code to display.
        output_str (str): The output/result of the code.
    """
    #themes: gruvbox-dark, ansi_dark, fruity, monokai, github-dark
    syntax_panel = Panel(Syntax(code_str, "python", line_numbers=True, theme="gruvbox-dark"), title="CODE", title_align="left", expand=False, border_style="#000000")
    output_panel = Panel(output_str, title="OUTPUT", title_align="left", expand=False, style="#000000", box=box.SQUARE)
    #console.print(Columns([syntax_panel, output_panel], column_first=True))
    console.print(syntax_panel)
    console.print(output_panel)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Run Code Snippet
# ─────────────────────────────────────────────────────────────────────────────────────────────
def run_code_snippet(code_snippet: str):
    """
    Run a block of Python code safely and capture output.
    - Returns stdout if successful.
    - Appends warnings (stderr) at the end if present.
    - Returns traceback if an error occurs.
    """
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()

    try:
        # Redirect stdout/stderr
        sys.stdout = stdout_buffer
        sys.stderr = stderr_buffer

        # Execute the code
        exec(code_snippet, {})

        # Restore
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        # Collect outputs
        stdout = stdout_buffer.getvalue()
        stderr = stderr_buffer.getvalue()

        if stderr.strip():  # warnings present
            return stdout.strip() + "\nWarnings:\n" + stderr.strip()
        else:
            return stdout.strip()  # no warnings, return only stdout

    except Exception:
        # Restore before returning error
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        return traceback.format_exc()


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: wrap_sections_in_html
# ─────────────────────────────────────────────────────────────────────────────────────────────
def wrap_sections_in_html(html_content: str) -> str:
    """
    Wrap blocks between:
      ╭ ... ╮   (start)
      └ ... ┘   (end)
    into <div class="section"> ... </div> without altering inline styles.
    """
    # Match from ╭ ... ╮ until └ ... ┘
    pattern = re.compile(r"(╭[^\n]*╮[\s\S]*?└[^\n]*┘)", re.MULTILINE)

    def replacer(match):
        block = match.group(1)
        # Only wrap, no style change
        return f'<div class="section">{block}</div>'

    return pattern.sub(replacer, html_content)


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Export Output to HTML
# ─────────────────────────────────────────────────────────────────────────────────────────────
def export_output_to_html(theme_name: str, filepath: str, smart_page_breaks: bool = True) -> None:
    try:
        theme_object = get_terminal_theme(theme_name)
        html_content = console.export_html(theme=theme_object, inline_styles=True)  
        # 👆 ensures Rich preserves color as inline CSS

        if smart_page_breaks:
            css = """
            <style>
                .section {
                    page-break-inside: avoid;
                    break-inside: avoid;
                }
                body {
                    margin: 0;
                    padding: 0;
                }
            </style>
            """
            html_content = css + wrap_sections_in_html(html_content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        console.print(f"[bold bright_green]✅ Exported HTML to '{filepath}'[/]")

    except Exception as e:
        console.print(f"[bold red]❌ Error exporting HTML: {e}[/bold red]")


# ─────────────────────────────────────────────────────────────────────────────────────────────
#  Function: Create PDF from HTML
# ─────────────────────────────────────────────────────────────────────────────────────────────
def create_pdf_from_html(html_filepath: str, pdf_filepath: str)-> None:
    try:
        console.print(f"[yellow]Converting HTML to PDF using browser automation...[/]")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            absolute_html_path = Path(html_filepath).resolve() # Resolving relative file path to an absolute path.
            html_uri = absolute_html_path.as_uri() # Convert that absolute path into a proper file:/// URI.

            # Load HTML
            page.goto(html_uri)

            # Export PDF
            page.pdf(
                path=pdf_filepath,
                print_background=True,
                format="A4",
                margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"},
            )

            browser.close()

        console.print(f"[bold bright_green]✅ Exported PDF to '{pdf_filepath}'[/]")

    except Exception as e:
        console.print(f"[bold red]❌ Error exporting PDF: {e}[/bold red]")

