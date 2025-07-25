# Python Learning Journey

Welcome to my **Python Learning Journey**! This is a personal project where I implement and organize everything I’ve learned during my Python exploration from basic syntax to advanced concepts — through code examples, notes, and utilities.

---------------------------------------------------------------------------------------------------------------------------------------
## 📚 Project Purpose
---------------------------------------------------------------------------------------------------------------------------------------
This project is designed to:
- Reinforce my Python skills through practice
- Organize concepts topic-wise with example scripts
- Maintain notes for future reference
- Serve as a personal knowledge base and portfolio

Whether you're a beginner or revisiting Python, you may find the examples useful!

---------------------------------------------------------------------------------------------------------------------------------------
## 🗂️ Project Structure
---------------------------------------------------------------------------------------------------------------------------------------
```
pyCodeNotes/
├── .venv/             # Virtual environment (excluded from Git)
├── helpers/           # Reusable helper functions
├── tests/             # Manual test scripts (optional)
├── topics/            # Topic-wise Python scripts
│   ├── strings/
│   ├── functions/
│   |── loops/
│   └── ...
├── main.py            # entry point of project
├── progress.md/       # Markdown progress tracking
├── requirements.txt   # Installed dependencies (if any)
├── .gitignore         # Files/folders to ignore in version control
|── README.md          # Project overview and instructions
└── topics.json        # Contains name of topic, subtopic.. and their modules
```
---------------------------------------------------------------------------------------------------------------------------------------
## 🧪 How to Run
---------------------------------------------------------------------------------------------------------------------------------------
1. **Clone the repo or download manually**
2. **Navigate into the folder**
3. **Activate virtual environment** (optional but recommended):

```bash
python -m venv venv        # Create (only once)
venv\Scripts\activate      # Activate (Windows)
source venv/bin/activate   # Activate (macOS/Linux)
```
---------------------------------------------------------------------------------------------------------------------------------------
4. **Run main.py file**:
---------------------------------------------------------------------------------------------------------------------------------------
```bash
python main.py
```
---------------------------------------------------------------------------------------------------------------------------------------
## 📝 Topics Covered
---------------------------------------------------------------------------------------------------------------------------------------
| Topic       | Status          | Description                                  |
|-------------|-----------------|----------------------------------------------|
| Strings     | ✅ Done         | String methods, slicing, formatting, etc.    |
| Functions   | ✅ Done         | Parameters, annotations, docstrings, return  |
| Loops       | 🔄 In Progress  | `for`, `while`, nested, break/continue       |
| Lists       | ⏳ Upcoming     | List methods, slicing, list comps            |
| Dictionaries| ⏳ Upcoming     | Key/value pairs, methods, nesting            |
| File I/O    | ⏳ Upcoming     | Reading and writing files                    |
| OOP         | ⏳ Upcoming     | Classes, objects, inheritance, decorators    |
--------------------------------------------------------------------------------
Track progress: [`progress.md`](progress.md)

---------------------------------------------------------------------------------------------------------------------------------------
## 🧰 Helpers
---------------------------------------------------------------------------------------------------------------------------------------
A reusable helper script is included to improve formatting and readability:

```python
from helpers.display_helpers import display_note, print_sub_heading
OR
from helpers.display_helpers import *
```
---------------------------------------------------------------------------------------------------------------------------------------
## 📦 Requirements
---------------------------------------------------------------------------------------------------------------------------------------
Add external packages (like `rich`, `pytest`), you can track them in:
```bash
requirements.txt
```
Install them using:
```bash
pip install -r requirements.txt
```
---------------------------------------------------------------------------------------------------------------------------------------
## 🚀 Future Plans
---------------------------------------------------------------------------------------------------------------------------------------
- Add markdown cheat sheets per topic
- Turn project into a minimal learning package or blog

---------------------------------------------------------------------------------------------------------------------------------------
## 🙋‍♂️ Contact / Feedback
---------------------------------------------------------------------------------------------------------------------------------------
If you’re a fellow learner, feel free to use this as a template for your own journey. Feedback or suggestions are always welcome!
📧 Email: praveenahirwar94@gmail.com  
📎 GitHub: [your-username-here](https://github.com/your-username-here)

---------------------------------------------------------------------------------------------------------------------------------------
## 📄 License
---------------------------------------------------------------------------------------------------------------------------------------
This project is for personal educational use. You're welcome to use, fork, or extend it.