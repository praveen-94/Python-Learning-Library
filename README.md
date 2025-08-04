# Python Learning Journey
Welcome to my **Python Learning Journey**! This is a personal project where I implement and organize everything I’ve learned during my Python exploration from basic syntax to advanced concepts — through code examples, notes, and utilities.


## 📚 Project Purpose
This project is designed to:
- Reinforce my Python skills through practice
- Organize concepts topic-wise with example scripts
- Maintain notes for future reference
- Serve as a personal knowledge base and portfolio

Whether you're a beginner or revisiting Python, you may find the examples useful!


## 🗂️ Project Structure
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


## 🧪 How to Run
1. **Clone the repo or download manually**
2. **Navigate into the folder**
3. **Activate virtual environment** (optional but recommended):

```bash
python -m venv venv        # Create (only once)
venv\Scripts\activate      # Activate (Windows)
source venv/bin/activate   # Activate (macOS/Linux)
```
4. **Run main.py file**:
```bash
python main.py
```


## 📝 Topics Covered
| Topic                   | ⏳Status        | Description                                      |
|-------------------------|-----------------|--------------------------------------------------|
| Basic functionality     | ✅ Done         | Input and print function, Data Types             |
| Operators Usage         | ✅ Done         | All operators and their function                 |
| Control Statements      | ✅ Done         | Selection and iterative (loops) statements       |
| Variable                | ✅ Done         | Types of variable and their scope                |
| Strings                 | ✅ Done         | String methods, slicing, formatting, etc.        |
| Lists                   | ✅ Done         | Creation, methods, slicing, etc.                 |
| Tuples                  | ✅ Done         | Creation, methods, etc.                          |
| Sets                    | ✅ Done         | Creation, properties, methods, set based methods |
| Dictionaries            | ✅ Done         | Creation, Key/value pairs, methods               |
| Functions               | ✅ Done         | Parameters, annotations, docstrings, return      |
| OOP                     | ✅ Done         | Classes, objects, inheritance, decorators        |
| File I/O                | ✅ Done         | Reading and writing files                        |
| Exception Handling      | ✅ Done         | How to handle, raise and create exception        |
| Modules and Packages    | ✅ Done         | Create, import and use of built-in modules       |
------------------------------------------------------------------------------------------------
Track progress: [`progress.md`](progress.md)


## 🧰 Helpers
A reusable helper script is included to improve formatting and readability:

```python
from helpers.display_helpers import display_note, print_sub_heading
OR
from helpers.display_helpers import *
```


## 📦 Requirements
Add external packages (like `rich`, `pytest`), you can track them in:
```bash
requirements.txt
```
Install them using:
```bash
pip install -r requirements.txt
```


## 🚀 Future Plans
- Add markdown cheat sheets per topic
- Turn project into a minimal learning package or blog


## 🙋‍♂️ Contact / Feedback
If you’re a fellow learner, feel free to use this as a template for your own journey. Feedback or suggestions are always welcome!
📧 Email: praveenahirwar94@gmail.com  
📎 GitHub: [praveen-94](https://github.com/praveen-94)


## 📄 License
This project is for personal educational use. You're welcome to use, fork, or extend it.