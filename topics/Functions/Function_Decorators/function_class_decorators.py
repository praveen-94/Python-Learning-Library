from helpers.display_utils import *

def main():
    print_heading("Class Decorators: Decorating Classes Themselves")

    imp_note_points("""
- it is a function that takes a class object as an argument, optionally modifies it, and returns it (or a new class).
- Unlike function decorators that wrap functions, these decorators operate at the class level.
- They are used to add or modify methods, automatically register classes, enforce rules, or apply enhancements.
- The syntax is the same `@decorator` above a class definition, but the decorator receives a class instead of a function.
    """)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 1. Simple Example: Adding a __repr__ Method Dynamically
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("1. Adding a __repr__ Method Dynamically")
    show_code_with_output('''# Simple Example
def add_repr(cls):
    # Adds a __repr__ method if not defined
    if '__repr__' not in cls.__dict__:
        def __repr__(self):
            attrs = ', '.join(f"{k}={{self.__dict__[k]!r}}" for k in self.__dict__)
            return f"<{cls.__name__}({attrs})>"
        cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(repr(p))'''
,
'''<Person(name='Alice', age=30)>''')

    display_note("""
        - The decorator `add_repr` receives the class `Person` as `cls`.
        - It checks if `__repr__` is already defined. If not, it adds a new `__repr__` method dynamically.
        - When printing `repr(p)`, the newly added method is used.
    """, type="Explaination", icon="📝", color="green")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Registering Classes via Decorator
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("2. Registering Classes: Auto-track Decorated Classes")
    show_code_with_output('''# Registering Classes via Decorator
registry = []

def register(cls):
    registry.append(cls)
    return cls

@register
class PluginA:
    pass

@register
class PluginB:
    pass

print(f"Registered classes: {[cls.__name__ for cls in registry]}")'''
,
'''Registered classes: ['PluginA', 'PluginB']''')

    display_note("""
    - The `register` decorator appends the decorated class to a global `registry` list.
    - This pattern is used in plugin systems or when dynamic discovery of classes is needed.
    """, type="Explaination", icon="📝", color="green")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Enforcing Constraints Using Class Decorators
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("3. Enforcing Class Constraints")
    show_code_with_output('''# Enforcing Constraints 
def require_method(method_name):
    def decorator(cls):
        if not hasattr(cls, method_name):
            raise TypeError(f"Class {cls.__name__} must implement method '{method_name}'")
        return cls
    return decorator

@require_method('execute')
class Task:
    def execute(self):
        print("Running task")

try:
    @require_method('start')
    class Job:
        pass
except TypeError as e:
    print(f"Caught error: {e}")'''
,
'''Running task
Caught error: Class Job must implement method 'start' ''')

    display_note("""
    - Higher-order decorator that takes the name of a required method.
    - When decorating a class, it checks whether the class has that method.
    - If missing, it raises an error, enforcing design contracts dynamically.
    """, type="Explaination", icon="📝", color="green")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 4. Class Decorator with Extra Arguments (Stateful Factory)
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("4. Class Decorator with Parameters")
    show_code_with_output('''# Stateful Factory
def add_prefix(prefix):
    def decorator(cls):
        original_init = cls.__init__
        def __init__(self, name, *args, **kwargs):
            self.name = f"{prefix}_{name}"
            original_init(self, name, *args, **kwargs)
        cls.__init__ = __init__
        return cls

@add_prefix("PRE")
class User:
    def __init__(self, name):
        # Note: original init replaced, so this won't be called fully unless forwarded
        pass

u = User("Alice")
print(u.name)'''
,
'''PRE_Alice''')

    display_note("""
    - This decorator factory `add_prefix` accepts parameters.
    - It returns a decorator that modifies the `__init__` method to add a prefix to the `name` attribute.
    """, type="Explaination", icon="📝", color="green")

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 5. Difference Between Function and Class Decorators
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("5. Function vs Class Decorators (Summary)")
    display_note("""
    - Function decorators take a function and return a function (usually a wrapper).
    - Class decorators receive a class and return a class (modified or new).
    - Both use the `@` syntax but serve different purposes.
    - Class decorators are powerful for metaprogramming tasks like registration, protocol enforcement, or adding methods.
    """)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # 6. Bonus: Built-in `@dataclass` as a Class Decorator Example
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print_sub_heading("6. Built-in Class Decorator: @dataclass")
    show_code_with_output('''from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(3.5, 4.2)
print(p)  # __repr__ auto-generated
print(f"x={p.x}, y={p.y}")''',
'''Point(x=3.5, y=4.2)
x=3.5, y=4.2''')

    display_note("""
    - `@dataclass` automatically generates init, repr, eq, and other methods.
    - It is a classic real-world example of a class decorator that inspects and modifies the class.
    """, type="Explaination", icon="📝", color="green")

if __name__ == "__main__":
    main()
