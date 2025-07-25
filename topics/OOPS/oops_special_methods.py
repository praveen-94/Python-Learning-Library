# oop_special_methods.py

from helpers.display_utils import *

def main():
    print_heading("Special (Magic/Dunder) Methods in OOP")
    imp_note_points("""
- Special methods, also called "magic" or "dunder" (double underscore) methods, allow you to give your custom objects the behaviors of built-in Python types.
- Their names always start and end with double underscores (e.g., `__init__`, `__str__`).
- You don't call these methods directly. Python calls them for you in response to specific operations like addition (`+`), printing (`print()`), or attribute access.
- By implementing these methods, you can control how your objects are created, represented as strings, compared with others, and how they interact with operators.
- If you don't define a special method in your class, it will either use the default behavior from Python's base `object` class or raise a `TypeError`.
""")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Object Initialization and Construction
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Initialization and Construction")
    display_note("These methods control how your objects are created and destroyed.")

    print_small_sub_heading("a) __new__(cls, ...)",True)
    display_note("This is the first method called during object creation. Its job is to create and return a new instance of the class. You rarely need to override it.", "tip")
    display_note("Default Behavior: `object.__new__()` handles creating a blank instance of the class.", "example")
    show_code_with_output('''#  __new__(cls, ...)
class MyClass:
    def __new__(cls):  
        print("Creating a new instance by Customizing `__new__` methods...")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("Initializing the instance...")

obj = MyClass()'''
,
'''Creating a new instance by Customizing `__new__` methods...
Initializing the instance...''')

    print_small_sub_heading("b) __init__(self, ...)",True)
    display_note("Called right after `__new__`, this method initializes the newly created instance, often by assigning values to its attributes. It does not return anything.")
    display_note("Default Behavior: The base `object` class's `__init__` method does nothing.", "example")
    show_code_with_output('''#  __init__(self, ...)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Book '{self.title}' initialized.")

book = Book("The Hobbit", "J.R.R. Tolkien")'''
,
'''Book 'The Hobbit' initialized.''')

    print_small_sub_heading("c) __del__(self)",True)
    display_note("This is the 'destructor'. It's called when an object's reference count drops to zero and it is about to be garbage collected.")
    display_note("Default Behavior: The base `object` class's `__del__` method does nothing.", "example")
    display_note("Its execution is not guaranteed and can be unpredictable. Use it for cleanup tasks, but avoid relying on it for critical operations.", "warning")
    show_code_with_output('''#  __del__(self)
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print(f"FileHandler for {filename} created.")

    def __del__(self):
        print(f"FileHandler for {self.filename} is being destroyed.")

handler = FileHandler("report.txt")
del handler # Force deletion for demonstration'''
,
'''FileHandler for report.txt created.
FileHandler for report.txt is being destroyed.''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # String Representation
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. String Representation")
    display_note("These methods define how your object is converted to a string.")
    display_note("`__str__` is for creating a user-friendly, readable output for end-users (used by `print()` and `str()`).")
    display_note("`__repr__` is for creating an unambiguous, developer-focused representation of the object, which should ideally be valid Python code to recreate the object (used by `repr()`).")
    display_note("Default Behavior `__str__`: If not defined, Python falls back to using `__repr__`.", "tip")
    display_note("Default Behavior `__repr__`: If neither is defined, it shows the class name and memory address (e.g., `<Book object at 0x...a50>`).", "example")
    show_code_with_output('''#  __str__(self) vs. __repr__(self)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("1984", "George Orwell")

print(str(book))  # Calls __str__
print(repr(book)) # Calls __repr__'''
,
'''1984 by George Orwell
Book(title='1984', author='George Orwell')''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Comparison Methods
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Comparison Methods")
    display_note("These methods allow you to use comparison operators like `==`, `!=`, `<`, `>` on your objects.")
    display_note("`__eq__` implements the equality operator (`==`). `__ne__` implements the inequality operator (`!=`).")
    display_note("Default Behavior: If not defined, `__eq__` checks if two references point to the exact same object in memory (identity check, like the `is` operator). `__ne__` is the logical opposite.", "example")
    show_code_with_output('''#  __eq__(self, other) and __ne__(self, other)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")'''
,
'''p1 == p2: True
p1 == p3: False''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Arithmetic Operators")
    display_note("These methods let you use arithmetic operators like `+`, `-`, `*` with your objects.")
    display_note("Default Behavior: If not defined, using an arithmetic operator on your object will raise a `TypeError`.", "warning")
    show_code_with_output('''# Arithmetic Operators
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(3, 1)
v3 = v1 + v2

print(f"{v1} + {v2} = {v3}")'''
,
'''Vector(2, 4) + Vector(3, 1) = Vector(5, 5)''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Attribute Access
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5. Attribute Access")
    display_note("These methods customize what happens when you get, set, or delete an object's attributes.")

    print_small_sub_heading("a) __getattr__(self, name)",True)
    display_note("This method is called ONLY when an attribute lookup fails (i.e., the attribute doesn't exist). It's a great way to provide a default value or custom behavior for missing attributes.")
    display_note("Default Behavior: If not defined, accessing a non-existent attribute raises an `AttributeError`.", "example")
    show_code_with_output('''# __getattr__(self, name)
class DynamicAttributes:
    def __getattr__(self, name):
        return f"Attribute '{name}' does not exist!"

d = DynamicAttributes()
print(d.some_attribute)
print(d.another_one)'''
,
'''Attribute 'some_attribute' does not exist!
Attribute 'another_one' does not exist!''')


    print_small_sub_heading("b) __setattr__(self, name, value)",True)
    display_note("This method is called every time you assign a value to an attribute. Be careful when overriding it to avoid infinite recursion.")
    display_note("Default Behavior: The default implementation sets the attribute's value in the object's internal dictionary (`__dict__`).", "example")
    show_code_with_output('''# __setattr__(self, name, value)
class Logger:
    def __setattr__(self, name, value):
        print(f"Setting attribute '{name}' to '{value}'")
        super().__setattr__(name, value) # Avoids recursion

log = Logger()
log.status = "active"
log.user = "admin"'''
,
'''Setting attribute 'status' to 'active'
Setting attribute 'user' to 'admin' ''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Emulating Container Types
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("6. Emulating Container Types")
    display_note("Implementing these methods makes your object behave like a list, dictionary, or other container.")
    display_note("`__len__` is called by `len()` and should return the object's length.")
    display_note("`__getitem__` is used for accessing items via a key or index, like `my_object[5]` or `my_object['name']`.")
    display_note("Default Behavior: If not defined, `len(obj)` or `obj[key]` will raise a `TypeError`.", "example")
    show_code_with_output('''# __len__(self) and __getitem__(self, key)
class MyList:
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

my_list = MyList([10, 20, 30, 40])
print(f"Length: {len(my_list)}")
print(f"Element at index 2: {my_list[2]}")'''
,
'''Length: 4
Element at index 2: 30''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Callable Objects
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("7. Callable Objects")
    display_note("Implementing `__call__` allows you to treat an instance of your class as if it were a function.")
    display_note("Default Behavior: If not defined, trying to 'call' an instance (`my_instance()`) will raise a `TypeError`.", "example")
    show_code_with_output('''# __call__(self, ...)
class Adder:
    def __call__(self, x, y):
        return x + y

add = Adder()
result = add(5, 10) # Calls the __call__ method
print(f"The result is: {result}")'''
,
'''The result is: 15''')


    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Context Managers
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("8. Context Managers (with statement)")
    display_note("These methods allow your object to be used with the `with` statement, which is great for managing resources like files or network connections.")
    display_note("`__enter__` is called when entering the `with` block. It should return the resource to be managed.")
    display_note("`__exit__` is called when exiting the `with` block, even if an error occurred. It's used for cleanup.")
    display_note("Default Behavior: If not defined, the object cannot be used in a `with` statement and will raise an `AttributeError`.", "example")
    show_code_with_output('''# __enter__(self) and __exit__(self, ...)
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f"Opening {self.filename}...")
        return f"Content of {self.filename}"

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.filename}...")

with ManagedFile("document.txt") as f:
    print(f"Working with: {f}")
print("Finished with block.")''',
'''Opening document.txt...
Working with: Content of document.txt
Closing document.txt...
Finished with block.''')

