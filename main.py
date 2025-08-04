from helpers.display_utils import export_output_to_html, create_pdf_from_html
from rich.prompt import Confirm
from pathlib import Path
import importlib
import asyncio
import json

def clear_screen():
    print("\n" + "-" * 60 + "\n")

def pause():
    input("\nPress Enter to continue...")

def handle_menu(level_name, items):
    while True:
        clear_screen()
        print(f"📚 {level_name}:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item['title']}")
        print(f"{len(items)+1}. 🔙 Go Back")
        print(f"{len(items)+2}. ❌ Exit")

        choice = input("\nEnter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(items):
                selected = items[choice - 1]
                if "subtopics" in selected:
                    handle_menu(selected["title"], selected["subtopics"])
                elif "module" in selected:
                    try:
                        mod = importlib.import_module(selected["module"])
                        mod.main()

                        if Confirm.ask("\n[bold yellow]Do you want to export this output to an HTML file?[/]"):
                            if mod.__file__ is None:
                                print(f"❌ Module {selected['module']} does not have a __file__ attribute.")
                                pause()
                                continue
                            module_path = Path(mod.__file__)
                            notes_dir = module_path.parent / "Notes"
                            notes_dir.mkdir(parents=True, exist_ok=True)
                            html_dir = notes_dir / "HTMLs"
                            html_dir.mkdir(parents=True, exist_ok=True)
                            module_name = module_path.stem  # Gets the filename without the .py extension
                            html_filepath = html_dir / f"{module_name}.html"
                            export_output_to_html("fruity", str(html_filepath))

                            if Confirm.ask("\n[bold yellow]The HTML file was created. Do you want to convert it to a PDF?[/]"):
                                pdf_dir = notes_dir / "PDFs"
                                pdf_dir.mkdir(parents=True, exist_ok=True)
                                pdf_filepath = pdf_dir / f"{module_name}.pdf"
                                asyncio.run(create_pdf_from_html(str(html_filepath), str(pdf_filepath)))
                    except Exception as e:
                        print(f"❌ Failed to run {selected['module']}: {e}")
                        pause()
                else:
                    print("⚠️ No valid subtopic/module found.")
            elif choice == len(items)+1:
                return
            elif choice == len(items)+2:
                print("👋 Exiting... Bye!")
                exit()
        else:
            print("❗ Invalid input.")
            pause()

def main():
    with open("topics.json", "r") as f:
        menu = json.load(f)
    handle_menu("Python Topics....", menu)

if __name__ == "__main__":
    main()
