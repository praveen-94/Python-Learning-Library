# File: topics/OOPS/Basic_oops_concept.py
from helpers.display_utils import *

def main(topic_number: int):
    """Display basic OOP concepts in Python using Rich library.
    """
    print_heading("Object-Oriented Programming (OOP) in Python", topic_number)
    imp_note_points("""
- _Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure software._
- _It allows for encapsulation, inheritance, and polymorphism, making code more modular and reusable._""")

    print_sub_heading("1) Public, Protected, Private Members")
    imp_note_points("""- *Encapsulation hides internal data and exposes it via methods or properties.*
- *Achieved using private **(__var)** or protected **(_var)** members, getters/setters.*
- *Public members are accessible from anywhere. Default in Python—no special prefix needed.*
- *Protected members use single underscore **(_)** and signal: 'Internal use only' Accessible, but discouraged outside subclasses.*
- *Private members use double underscores **(__)**. Python hides them via name mangling—not true privacy.*
- *Accessing private members is discouraged but possible using name mangling: **_ClassName__member**.*""")
    code1 = '''
class BaseDemoClass:
    def __init__(self):
        self.name = "I am Public Member"
        self._data = "I am Protected Member"
        self.__secret = "I am Private Member"
    def reveal(self):
        return f"{self.__secret}, inside reveal method"
    def __secret_method(self):
        return "I am Private Method"
                    
class ChildDemoClass(BaseDemoClass):
    def show(self):
        return f"{self._data}, inside ChildDemoClass"
                    
BaseObj = BaseDemoClass()
print(BaseObj.name)  # ✅ Accessible from outside
print(BaseObj._data)  # ⚠️ Accessible, but discouraged
# print(BaseObj.__secret)  # ❌ AttributeError: 'BaseDemoClass' has no attribute '__secret'
print(BaseObj._BaseDemoClass__secret)  # 😏 Still accessible via name mangling
print(BaseObj.reveal())  # ✅ Access via method
# print(BaseObj.__secret_method())  # ❌ AttributeError: 'BaseDemoClass' has no attribute '__secret_method'
print(BaseObj._BaseDemoClass__secret_method())  # 😏 Access private method via name mangling
BaseObj.not_a_member = "I am not a member only for BaseObj instance"  # ✅ Can add new attributes dynamically
print(BaseObj.not_a_member)  # ✅ Access new attribute

print("Accessing members of base class from child class:")                  
ChildObj = ChildDemoClass()
print(ChildObj.name)     # ✅ OK
print(ChildObj.show())     # ✅ OK
print(ChildObj._data)      # ⚠️ Still accessible, but discouraged
# print(ChildObj.__secret)  # ❌ AttributeError: 'ChildDemoClass' has no attribute '__secret'
print(ChildObj.reveal())  # ✅ Access via method
#---------------------------------------------------------------------------------------------------------------#'''
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    print_sub_heading("2) @property Decorator– Getter, Setter, Deleter")
    imp_note_points("""- *The @property decorator in Python allows methods to be accessed like attributes.*
- *You can define custom behavior when getting, setting, or deleting an attribute.*
- *This is useful for encapsulation — internal data is protected while allowing controlled access.*""")
    code2 = '''
class Product:
    def __init__(self, price):
        self._price = price  # protected attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

item = Product(100)
print(item.price)       # ✅ Uses @property getter

item.price = 150        # ✅ Uses @property setter
# item.price = -50      # ❌ ValueError: Price cannot be negative
print(item.price)

del item.price          # ✅ Uses @property deleter
# print(item.price)     # ❌ AttributeError: 'Product' object has no attribute '_price'
#--------------------------------------------------------------------------------------------#'''
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)


    print_sub_heading("3) Class Variables, Instance Variables, and Methods")
    imp_note_points("""- ***Instance Variables:**  Unique to each object, Defined using 'self.var' inside __init__ or methods, Accessed via 'self.var'.*
- ***Class Variables:** Shared among all instances, Defined directly in the class body, Accessed via **ClassName.var** or **self.__class__.var**.*
- ***Class Methods:**  Defined with @classmethod decorator, Takes **cls** as first argument. Can access and modify class variables dynamically, and supports alternate constructors and subclass-aware behavior.*
- ***Static Methods:**  Defined with @staticmethod decorator, Takes no **self/cls**, Access class variables(**ClassName.var**) but not instance attributes, not class-aware or dynamic, Behaves like a normal function within class context.*""")
    display_note("Changing a class variable via instance creates a new instance variable—doesn’t affect others.", "warning")
    code3 = '''
class User:
    domain = "example.com"      # Class variable
    __name_email_dict = {}      # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable
        self.email = self.assign_email(name) # Instance variable

    @property
    def user_details(self):
        return f"'{self.email}' assign to user: '{self.name}'"

    @classmethod
    def assign_email(cls, name):
        email = f"{name.lower().replace(' ', '_')}@{cls.domain}"
        cls.__name_email_dict.update({name: email})
        return cls.__name_email_dict.get(name)
        
    @classmethod
    def get_all_user_details(cls):
        return f"Users List: {cls.__name_email_dict}"

    @staticmethod
    def Check_mail_availability(name):
        if name in User.__name_email_dict:
            return f"User '{name}' already exist"
        return f"Email '{name}' is available for assignment."

print("Domain name:", User.domain) # Accessing class variable
user1 = User("Alice Smith")
user2 = User("Bob Johnson")
user3 = User("Alice Smith") # Not create a new user, Return existing mail
print(user1.user_details)
print(user2.user_details)
print(user3.user_details)  # Should return the same email as user1

# Accessing class method to get all user details
print(User.get_all_user_details()) 

# Accessing static method to check email availability
print(User.Check_mail_availability("Alice Smith"))
print(User.Check_mail_availability("Charlie Brown"))

user1.notExist=404   # Creating instance variable dynamically for user1
print("User1 notExist:", user1.notExist)  # Accessing instance variable
try:
    print("User2 notExist:", user2.notExist)  # Accessing instance variable
except AttributeError:
    print("User2 notExist: Attribute not found") # Accessing instance variable
#--------------------------------------------------------------------------------------------#'''
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)


if __name__ == "__main__":
        main(1)
