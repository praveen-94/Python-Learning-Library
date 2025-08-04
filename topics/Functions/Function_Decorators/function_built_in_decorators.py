from helpers.display_utils import *

def main():
    print_heading("Python’s Built-in Decorators")
    imp_note_points("""
**Built-in Decorators in Python:**  
*Special decorators provided by Python to simplify common pattern implementation in classes and functions.*  
*They leverage internal mechanisms like the descriptor protocol to make code cleaner, safer, and more expressive.*  

**Main Built-in Decorators Covered Here:**  
- @property  
- @staticmethod  
- @classmethod  
- @functools.lru_cache  
- @dataclasses.dataclass  
- @functools.wraps  """)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. @property: Managed Attributes via Descriptors
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. @property- Managed Attributes (Getters/Setters)")
    display_note("@property lets you define methods that are accessed like attributes.", "info")
    display_note("Behind the scenes, it is implemented using the descriptor protocol, ", "info", message_continue=True)
    display_note("providing automatic handling of getting, setting, and deleting attributes.", "info", message_continue=True)
    show_code_with_output('''
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Name must be alphabetic")
        self._name = value

p = Person("Alice")
print(p.name)         # Alice
p.name = "Bob"
print(p.name)         # Bob
# p.name = "Bob123"   # Raises ValueError
'''
,
'''Alice
Bob''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. @staticmethod - Method Without Instance or Class Context
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. @staticmethod- Plain Utility Methods Inside Classes")
    display_note("@staticmethod defines a method that doesn't receive 'self' or 'cls', ", "tip")
    display_note("so it behaves like a regular function organized logically inside a class.", "tip", message_continue=True)
    show_code_with_output('''
class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.multiply(5, 4))  # 20
'''
,
'''20''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. @classmethod - Method With Class Context
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. @classmethod- Alternative Constructors and Class-aware Methods")
    display_note("@classmethod receives the class (cls) as the first argument instead of the instance. ")
    display_note("Great for factory methods or modifying class-wide state.", message_continue=True)
    show_code_with_output('''
class Circle:
    pi = 3.1416
    
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

c = Circle.from_diameter(10)
print(c.radius)  # 5.0
'''
,
'''5.0''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. @functools.lru_cache - Caching Decorator for Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. @functools.lru_cache- Memoization / Caching Results")
    display_note("Caches results of functions to avoid expensive recomputation for the same inputs. ")
    display_note("Very useful for recursive or heavy computations.", message_continue=True)
    show_code_with_output('''
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 55
'''
,
'''55''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 5. @dataclasses.dataclass - Boilerplate-Free Data Containers
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5. @dataclasses.dataclass- Auto-Generated Init and More")
    display_note("Automatically generates methods like __init__, __repr__, __eq__, ")
    display_note("based on class annotations. Great for classes storing data with minimal boilerplate.", message_continue=True)
    show_code_with_output('''
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

pt = Point(3, 4)
print(pt)
'''
,
'''Point(x=3, y=4)''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 6. @functools.wraps - Preserving Metadata in Custom Decorators
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("6. @functools.wraps- Keep Function Metadata in Decorators")
    display_note("When writing decorators, use @wraps to preserve the original function's name, docstring etc. ", "warning")
    display_note("Otherwise, decorated functions lose identity causing debugging and introspection issues.", "warning", message_continue=True)
    show_code_with_output('''
from functools import wraps

def log_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper

@log_decorator
def greet():
    """Say hello"""
    print("Hello!")

print(greet.__name__)
print(greet.__doc__)
greet()
'''
,
'''greet
Say hello
Calling greet
Hello!''')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 7. Descriptors: Low-level Attribute Access Control
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print("\n\n\n")
    print_heading("Descriptors Explained")

    imp_note_points("""
**What is a Descriptor?**  
An object that implements at least one of:  
- `__get__(self, instance, owner)`  
- `__set__(self, instance, value)`  
- `__delete__(self, instance)`  

When you access or set an attribute managed by a descriptor, Python calls these methods automatically.

**Why Use Descriptors?**  
They provide a low-level, reusable way to customize attribute access logic like validation, computed attributes, or delegation.

**Relationship Between Descriptors and Decorators:**  
- Built-in decorators like @property, @staticmethod, and @classmethod are implemented as descriptors under the hood.  
- Decorators act as syntax sugar assigning descriptor instances to class attributes.  
- You can create your own descriptors for complex attribute behaviors beyond simple methods.
""")

    show_code_with_output('''
class RevealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
    
    def __get__(self, instance, owner):
        print(f"__get__ called for {self.name}")
        return self.val
    
    def __set__(self, instance, value):
        print(f"__set__ called for {self.name}")
        self.val = value

class MyClass:
    x = RevealAccess(10, 'x')

obj = MyClass()
print(obj.x)        # triggers __get__()
obj.x = 20          # triggers __set__()
print(obj.x)
'''
,
'''__get__ called for x
10
__set__ called for x
__get__ called for x
20''')

if __name__ == "__main__":
    main()
