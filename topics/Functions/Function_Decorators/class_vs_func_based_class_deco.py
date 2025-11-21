from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Class-based vs Function-based Class Decorators Explained", topic_number)

    imp_note_points("""
**Decorators can be implemented as functions or classes. Both modify classes/functions by wrapping or replacing them.**

**Key Differences:**
- Class-based decorators define a class with __init__ and __call__; they can hold internal state and have more structure.
- Function-based decorators are simple functions returning a wrapped or modified class/function, usually using closures.
- Class-decorated objects become instances of the decorator class which must implement __call__.
- Function-decorated objects are replaced by whatever the decorator function returns.
    """)

    # -------------------------------------------------------------------------------
    # 1. Function-based Class Decorator Example
    # -------------------------------------------------------------------------------
    print_sub_heading("1. Function-based Class Decorator")
    display_note("Simple decorator as a function; receives class and returns class(or modified version). Does not keep state beyond closures.", "info")
    code1 = '''
def simple_deco(cls):
    print(f"Decorating class {cls.__name__}")
    # Just return the original class unchanged
    return cls

@simple_deco
class ExampleA:
    pass

a = ExampleA()  # Normal instantiation, decorator prints message once
#---------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    # -------------------------------------------------------------------------------
    # 2. Class-based Class Decorator Example
    # -------------------------------------------------------------------------------
    print_sub_heading("2. Class-based Class Decorator")
    display_note("Decorator implemented as a class that stores the original class in 'self.cls' and implements __call__ to intercept instantiation calls.", "info")
    code2 = '''
class LogInstantiations:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        print(f"Creating instance of {self.cls.__name__} with args {args} and kwargs {kwargs}")
        return self.cls(*args, **kwargs)

@LogInstantiations
class ExampleB:
    def __init__(self, x, y):
        self.x = x
        self.y = y

b = ExampleB(10, 20)
#-----------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -------------------------------------------------------------------------------
    # 3. Summary Table
    # -------------------------------------------------------------------------------
    print_sub_heading("3. Summary: Differences at a Glance")
    decorator_comparison = [
        ["Feature", "Class-based Decorator", "Function-based Decorator"],
        ["Syntax", "Class with __init__ and __call__", "Plain function receiving and returning class"],
        ["Stateful", "Yes, can hold internal state in instance", "Normally stateless; state held via closures"],
        ["Wrapped object type", "Instance of decorator class", "The returned class/function from decorator function"],
        ["Use Cases", "Complex logic, maintaining state, config", "Simple wrapping, lightweight decoration"],
        ["Behavior at runtime", "__call__ intercepts invocation", "Decorated object replaced by return value"]
    ]
    render_2d_table(decorator_comparison, title="🆚 Class vs Function Decorators")

    imp_note_points("""
**When Python executes the decoration:**

- Function-based:  
    ___MyClass = simple_deco(MyClass)___ → replaces ___MyClass___ directly.

- Class-based:  
    ___MyClass = LogInstantiations(MyClass)___ creates an instance of ___LogInstantiations___.  
    Later, calling ___MyClass()___ triggers ___LogInstantiations.__call__()___.""")
