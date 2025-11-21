from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Python’s Built-in Decorators", topic_number)
    imp_note_points("""
***Built-in Decorators in Python:***  
*Special decorators provided by Python to simplify common pattern implementation in classes and functions.*  
*They leverage internal mechanisms like the descriptor protocol to make code cleaner, safer, and more expressive.*  

***Main Built-in Decorators Covered Here:***  
- ***@property***  
- ***@staticmethod***  
- ***@classmethod***  
- ***@functools.lru_cache***  
- ***@dataclasses.dataclass***  
- ***@functools.wraps***  """)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. @property: Managed Attributes via Descriptors
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. @property- Managed Attributes (Getters/Setters)")
    display_note("@property lets you define methods that are accessed like attributes. Behind the scenes, it is implemented using the descriptor protocol, providing automatic handling of getting, setting, and deleting attributes.", "info")
    code1 = '''
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Error: Name must be alphabetic")
        self._name = value

p = Person("Alice")
print(p.name)         # Alice
p.name = "Bob"
print(p.name)         # Bob
try:
    p.name = "Bob123"   # Raises ValueError
except ValueError as e:
    print(e)
#-------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. @staticmethod - Method Without Instance or Class Context
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. @staticmethod- Plain Utility Methods Inside Classes")
    display_note("@staticmethod defines a method that doesn't receive 'self' or 'cls', so it behaves like a regular function organized logically inside a class.", "tip")
    code2 = '''
class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.multiply(5, 4))  # 20
#-------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. @classmethod - Method With Class Context
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. @classmethod- Alternative Constructors and Class-aware Methods")
    display_note("@classmethod receives the class (cls) as the first argument instead of the instance. Great for factory methods or modifying class-wide state.")
    code3 = '''
class Circle:
    pi = 3.1416
    
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

c = Circle.from_diameter(10)
print(c.radius)  # 5.0
#---------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. @functools.lru_cache - Caching Decorator for Functions
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. @functools.lru_cache- Memoization / Caching Results")
    display_note("Caches results of functions to avoid expensive recomputation for the same inputs. Very useful for recursive or heavy computations.")
    code4 = '''
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 55
#-------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 5. @dataclasses.dataclass - Boilerplate-Free Data Containers
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5. @dataclasses.dataclass- Auto-Generated Init and More")
    display_note("Automatically generates methods like __init__, __repr__, __eq__, based on class annotations. Great for classes storing data with minimal boilerplate.")
    code5 = '''
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

pt = Point(3, 4)
print(pt)
#-----------------------------------#'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 6. @functools.wraps - Preserving Metadata in Custom Decorators
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("6. @functools.wraps- Keep Function Metadata in Decorators")
    display_note("When writing decorators, use @wraps to preserve the original function's name, docstring etc. Otherwise, decorated functions lose identity causing debugging and introspection issues.", "warning")
    code6 = '''
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
#-----------------------------------------#'''
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 7. Descriptors: Low-level Attribute Access Control
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print("\\n\\n\\n")
    print_sub_heading("Descriptors Explained")

    imp_note_points("""
***What is a Descriptor?***  
*An object that implements at least one of:*  
- ***__get__(self, instance, owner)***  
- ***__set__(self, instance, value)***  
- ***__delete__(self, instance)***  

*When you access or set an attribute managed by a descriptor, Python calls these methods automatically.*

***Why Use Descriptors?***  
*They provide a low-level, reusable way to customize attribute access logic like validation, computed attributes, or delegation.*

***Relationship Between Descriptors and Decorators:***  
- *Built-in decorators like @property, @staticmethod, and @classmethod are implemented as descriptors under the hood.*  
- *Decorators act as syntax sugar assigning descriptor instances to class attributes.*  
- *You can create your own descriptors for complex attribute behaviors beyond simple methods.*""")

    code7 = '''
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
#---------------------------------------------------#'''
    output7 = run_code_snippet(code7)
    show_code_with_output(code7, output7)

    print("\n\n")
    display_note("In summary, Python's built-in decorators leverage the descriptor protocol to provide powerful, reusable patterns for managing attributes and methods in classes. Understanding descriptors helps you grasp how these decorators work under the hood and enables you to create your own advanced attribute behaviors when needed.")

if __name__ == "__main__":
    main(1)
