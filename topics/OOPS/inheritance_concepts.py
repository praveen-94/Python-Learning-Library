from helpers.display_utils import *

def main(topic_number: int):
    """Display inheritance concepts in Python using Rich library.
    """
    
    print_heading("Object-Oriented Programming (OOP)- Inheritance (Is-A ) and its Types in Python", topic_number)
    important_points = """
_Inheritance is a mechanism where a new class (child) inherits attributes and methods from an existing class (parent)._

> ___Purpose and Advantages___
>> - *Helps build scalable and maintainable object-oriented systems.*
>> - *Promotes code reuse and establishes a hierarchical relationship between classes.*
>> - *Reduces redundancy in codebase.*
>> - *Easy to extend or override existing behavior.*
>> - *Enables polymorphism— same interface, different behavior.*

> ___Rules of Inheritance___
>> 1. ___Access Control:___
>>>   - *Parent’s methods and attributes are accessible in child class.*
>>>   - *Protected member inherited but by convention treated as internal.*
>>>   - *Private members are not directly inherited.*

>> 2. ___Method Overriding:___
>>>   - *Child can override any parent method by redefining it.*
>>>   - *Supports dynamic dispatch— runtime behavior decided by object type.*

>> 3. ___Super():___
>>>   - *Use to access parent methods or constructors.*
>>>   - *If child class has its own **'\_\_init\_\_'**, parent’s **'\_\_init\_\_'** won’t run automatically.*
>>>   - *Use **'super().\_\_init\_\_()'** to invoke it explicitly.*

>> 4. ___RO:___
>>> - *Python supports multiple inheritance— method lookup follows MRO (Method Resolution Order).*
>>> - *Use **'ClassName.\_\_mro\_\_'** or **'help(ClassName)'** to inspect inheritance path.*
"""
    imp_note_points(important_points)

    #---------------------------------------------------------------------------------------------------
    # Single Inheritance
    #---------------------------------------------------------------------------------------------------
    print_sub_heading("1) Single Inheritance")
    display_note("Single inheritance is when a class (child) inherits from one parent class.")
    code1 = '''
class Animal:
    def sound(self):
        return "Makes a sound"

class Dog(Animal):
    def bark(self):
        return "Barks"

d = Dog()
print(d.sound())  # Inherited
print(d.bark())   # Child's own method
#----------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)

    #---------------------------------------------------------------------------------------------------
    # Multilevel Inheritance
    #---------------------------------------------------------------------------------------------------
    print_sub_heading("2) Multilevel Inheritance")
    display_note("Multilevel inheritance is when a class inherits from another class, which in turn inherits from another class.")
    code2 = '''
class GrandParent:
    def home(self):
        return "Owns ancestral home"

class Parent(GrandParent):
    def car(self):
        return "Drives a car"

class Child(Parent):
    def bike(self):
        return "Rides a bike"

c = Child()
print(c.home())  # From GrandParent
print(c.car())   # From Parent
print(c.bike())  # Own method
#----------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    #---------------------------------------------------------------------------------------------------
    # Multiple Inheritance
    #---------------------------------------------------------------------------------------------------
    print_sub_heading("3) Multiple Inheritance")
    display_note("""When a class inherits from more than one parent class. It allows combining behaviors from multiple classes.
Python uses MRO to resolve conflicts when multiple parent classes have methods with the same name.""")
    code3 = '''
class Writer:
    def skill(self):
        return "Writes content"

class Speaker:
    def skill(self):
        return "Delivers speeches"

class Influencer(Writer, Speaker):
    pass

i = Influencer()
print(i.skill())  # ⚠️ MRO: Writer comes first
#------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    #---------------------------------------------------------------------------------------------------
    # Hierarchical Inheritance
    #---------------------------------------------------------------------------------------------------
    print_sub_heading("4) Hierarchical Inheritance")
    display_note("""Hierarchical inheritance is when multiple child classes inherit from a single parent class.
Each child gets the parent's features but remains separate.""")
    code4 = '''
class Parent:
    def rules(self):
        return "Follow the house rules"

class Child1(Parent):
    def play(self):
        return "Plays football"

class Child2(Parent):
    def sing(self):
        return "Sings song"

c1 = Child1()
c2 = Child2()
print(c1.rules(), c1.play())
print(c2.rules(), c2.sing())
#--------------------------------------------#'''
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    #---------------------------------------------------------------------------------------------------
    # Hybrid Inheritance
    #---------------------------------------------------------------------------------------------------
    print_sub_heading("5) Hybrid Inheritance")
    display_note("""Hybrid inheritance is a mix of two or more types of inheritance.
Often involves multiple + multilevel together.""")
    code5 = '''
class A:
    def msgA(self):
        return "Class A"

class B(A):
    def msgB(self):
        return "Class B"

class C(A):
    def msgC(self):
        return "Class C"

class D(B, C):  # Hybrid (Multilevel + Multiple)
    def msgD(self):
        return "Class D"

d = D()
print(d.msgA())
print(d.msgB())
print(d.msgC())
print(d.msgD())
'''
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)
