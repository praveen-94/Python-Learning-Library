from rich.terminal_theme import TerminalTheme
from rich.console import Console
import rich.terminal_theme as TerminalThemes
console = Console()

FRUITY = TerminalTheme(
    (30, 30, 30),           # Background (very dark gray)
    (255, 255, 255),        # Foreground (white)

    [  # Normal ANSI (0–7)
        (0, 0, 0),          # Black
        (255, 85, 85),      # Red
        (102, 217, 0),      # Green
        (255, 221, 0),      # Yellow
        (102, 153, 255),    # Blue
        (255, 102, 255),    # Magenta
        (0, 255, 255),      # Cyan
        (192, 192, 192),    # White
    ],
    [  # Bright ANSI (8–15)
        (128, 128, 128),    # Bright Black
        (255, 0, 0),        # Bright Red
        (0, 255, 0),        # Bright Green
        (255, 255, 0),      # Bright Yellow
        (0, 128, 255),      # Bright Blue
        (255, 0, 255),      # Bright Magenta
        (0, 255, 255),      # Bright Cyan
        (255, 255, 255),    # Bright White
    ]
)

GITHUB_DARK = TerminalTheme(
    (13, 17, 23),           # Background (GitHub Dark #0d1117)
    (201, 209, 217),        # Foreground (Soft white text #c9d1d9)

    [  # Normal ANSI (0–7)
        (22, 27, 34),       # Black
        (248, 81, 73),      # Red
        (166, 226, 46),     # Green
        (255, 204, 0),      # Yellow
        (97, 175, 239),     # Blue
        (174, 129, 255),    # Magenta
        (56, 139, 253),     # Cyan
        (197, 200, 198),    # White
    ],
    [  # Bright ANSI (8–15)
        (76, 86, 106),      # Bright Black (gray)
        (255, 88, 116),     # Bright Red
        (173, 255, 47),     # Bright Green
        (255, 234, 90),     # Bright Yellow
        (120, 180, 255),    # Bright Blue
        (205, 135, 255),    # Bright Magenta
        (102, 217, 239),    # Bright Cyan
        (255, 255, 255),    # Bright White
    ]
)


def get_terminal_theme(name: str) -> TerminalTheme:
    name = name.lower()
    if name == "fruity":
        return FRUITY
    elif name == "githubdark":
        return GITHUB_DARK
    else:
        theme_object = getattr(TerminalThemes,name.upper(),TerminalThemes.MONOKAI)
        console.print(f"[bold red]'{name}' theme is not defined, Checking if it is match to any predefined theme, if not using MONOKOI theme[/bold red]")
        return theme_object