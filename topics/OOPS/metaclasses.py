from helpers.display_utils import *

def main():
    print_heading("Metaclasses in Python")

    imp_note_points("""
**What is a Metaclass?**  
- *A metaclass is the "class of a class": it defines how classes themselves are constructed and behaves like a blueprint for classes.*
- *Just as classes define the structure of objects, metaclasses define the structure and creation of classes.*
- *The most common metaclass is `type`, which is used by Python to create all classes by default.*

**Why Use Metaclasses?**  
- *Control class creation— customize class attributes, methods, or enforce contracts/patterns automatically.*
- *Implement automatic registration, singletons, validation or modify inherited behaviors for groups of classes.*""")

    # -------------------------------------------------------------------------------
    # 1. How Metaclasses Work
    # -------------------------------------------------------------------------------
    print_sub_heading("1. How Metaclasses Work")
    display_note("When you define a class, Python actually does: `MyClass = type('MyClass', (BaseClasses,), class_dict)`.", "info")
    show_code_with_output("""
# The normal way to declare a class:
class Foo:
    pass

# is equivalent to:
Foo = type('Foo', (), {})
print(type(Foo))     # <class 'type'>
print(isinstance(Foo, type))  # True
""",
"""
<class 'type'>
True
""" )

    display_note("You can control the creation of classes by passing ")
    display_note("a custom metaclass using the `metaclass` keyword argument in the class definition.", message_continue=True)

    # -------------------------------------------------------------------------------
    # 2. Defining and Using a Custom Metaclass
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Custom Metaclass Example")
    display_note("Define a metaclass by subclassing type and overriding __new__ (class creation) and/or __init__ (post-creation).", "tip")
    show_code_with_output("""
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f'Creating class {name}')
        namespace['created_by_metaclass'] = True
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.created_by_metaclass)  # True
""",
"""
Creating class MyClass
True
""")

    # -------------------------------------------------------------------------------
    # 3. Metaclass with __init__ or __call__ (advanced)
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Advanced: Metaclass __init__ and __call__")
    show_code_with_output("""
class VerboseMeta(type):
    def __init__(cls, name, bases, namespace):
        print(f'Init metaclass for {name}')
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(f'Creating instance of {cls.__name__}')
        return super().__call__(*args, **kwargs)

class Demo(metaclass=VerboseMeta):
    pass

d = Demo()
""",
"""
Init metaclass for Demo
Creating instance of Demo
""")

    # -------------------------------------------------------------------------------
    # 4. Practical Use Case: Enforcing Class Attributes
    # -------------------------------------------------------------------------------
    print_sub_heading("4. Use Case: Automatic Attribute Enforcement")
    display_note("You can use a metaclass to ensure every subclass defines certain attributes or methods, ", "warning")
    display_note("enforcing contracts at class creation.", "warning", message_continue=True)
    show_code_with_output("""
class RequireNameMeta(type):
    def __init__(cls, name, bases, namespace):
        if 'name' not in namespace:
            raise TypeError(f"Class '{name}' must define a 'name' attribute.")
        super().__init__(name, bases, namespace)

class Good(metaclass=RequireNameMeta):
    name = "I'm defined"

# class Bad(metaclass=RequireNameMeta):
#     pass  # Would raise TypeError!
"""
,
""""
(no output-- Good class works, Bad would error out at class creation)
""")

    # -------------------------------------------------------------------------------
    # 5. Best Practice and Alternatives
    # -------------------------------------------------------------------------------
    print_sub_heading("5. When to Use Metaclasses?")
    imp_note_points("""
- Use metaclasses only for advanced library design or frameworks, when class creation truly needs to be dynamically modified.
- Prefer class decorators or inheritance for most ordinary cases; they're easier to debug and read.
- If you find yourself needing metaclasses but can't explain why—likely you just need a class decorator or a factory function.""")

if __name__ == "__main__":
    main()
