# helpers/display_utils.py

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax
from pathlib import Path
from playwright.async_api import async_playwright
from .custom_terminal_themes import get_terminal_theme
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


def display_note(message: str, type: str="note", icon: str=None, message_continue: str=False)-> None:
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
    style = colors.get(type.lower())
    if(message_continue):
        icon_style_str=f"{icon} {type.capitalize()}: "
        icon_style_len=len(icon_style_str)  # calculating combine length of icon, type and message
        empty_string=icon_style_len*" "+" " # assigning empty string of length calculate above
        console.print(f"[{style}]{empty_string}{message}[/]") # space + only message
    else:
        console.print(f"[{style}]{icon} {type.capitalize()}: {message}[/]")


def imp_note_points(points: str)-> None:
    """
    Prints a stylish important points.
    Args:
       points (str): multiline string containing important notes
    """
    markdown = Markdown(points)
    panel = Panel.fit(
    renderable=markdown,
    title="Important Points",
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


def export_output_to_html(theme_name: str, filepath: str)-> None:
    """
    Saves all previously recorded console output to an HTML file.
    Args:
        theme_name (str): name of theme in which you want to export you output to html file
        filepath (str): file path where this file will save
    """
    try:
        theme_object = get_terminal_theme(theme_name)
        console.save_html(filepath, theme=theme_object)
        console.print(f"[bold bright_green]Successfully exported output to '{filepath}'[/]")
    except Exception as e:
        console.print(f"[bold red]Error!!!: {e}[/bold red]")


async def create_pdf_from_html(html_filepath: str, pdf_filepath: str)-> None:
    """
    Converts a local HTML file to a PDF using a headless browser via Playwright.
    Args:
        html_filepath (str): html file path, require for conversion
        pdf_filepath (str): file path where pdf file will store
    """
    try:
        console.print(f"[yellow]Converting HTML to PDF using browser automation...[/]")
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            absolute_html_path = Path(html_filepath).resolve() # Resolving relative file path to an absolute path.
            html_uri = absolute_html_path.as_uri() # Convert that absolute path into a proper file:/// URI.
           
            await page.goto(html_uri)  # Go to the local HTML file using the full URI
            await page.pdf(path=pdf_filepath, print_background=True)  # Generate the PDF
            await browser.close()   
        console.print(f"[bold bright_green]Successfully exported PDF to '{pdf_filepath}'[/]")
    except Exception as e:
        console.print(f"[bold red]Error converting with Playwright: {e}[/bold red]")

