# File: topics/OOPS/Basic_oops_concept.py
from helpers.display_utils import *

def main():
    """Display basic OOP concepts in Python using Rich library.
    """
    print_heading("Object-Oriented Programming (OOP) in Python")
    imp_points = """
- _Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure software._
- _It allows for encapsulation, inheritance, and polymorphism, making code more modular and reusable.__
"""
    imp_note_points(imp_points)

    print_sub_heading("1) Public, Protected, Private Members")
    display_note("Encapsulation hides internal data and exposes it via methods or properties.","note", "🔒")
    display_note("Achieved using private (`__var`) or protected (`_var`) members, getters/setters.", "note", "✅")
    display_note("Public members are accessible from anywhere. Default in Python—no special prefix needed.")
    display_note("Protected members use single underscore (_) and signal: 'Internal use only' Accessible, but discouraged outside subclasses.")
    display_note("Private members use double underscores (__). Python hides them via name mangling—not true privacy.")
    display_note("Accessing private members is discouraged but possible using name mangling: _ClassName__member.")
    show_code_with_output('''
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
    Baseobj.not_a_member = "I am not a member only for BaseObj instance"  # ✅ Can add new attributes dynamically
    print(BaseObj.not_a_member)  # ✅ Access new attribute

    print("Accessing members of base class from child class:")                  
    ChildObj = ChildDemoClass()
    print(ChildObj.name)     # ✅ OK
    print(ChildObj.show())     # ✅ OK
    print(ChildObj._data)      # ⚠️ Still accessible, but discouraged
    # print(ChildObj.__secret)  # ❌ AttributeError: 'ChildDemoClass' has no attribute '__secret'
    print(ChildObj.reveal())  # ✅ Access via method
    ''',
    "I am Public Member\n" + "I am Protected Member\n" + "I am Private Member\n" + "I am Private Member, inside reveal method\n" + "I am Private Method\n" + "I am not a member only for BaseObj instance\n" +
    "Accessing members of base class from child class:\n" + "I am Public Member\n" + "I am Protected Member, inside ChildDemoClass\n" + "I am Protected Member\n" + "I am Private Member, inside reveal method\n"
    )

    print_sub_heading("2) @property Decorator– Getter, Setter, Deleter")
    display_note("The @property decorator in Python allows methods to be accessed like attributes.")
    display_note("You can define custom behavior when getting, setting, or deleting an attribute.")
    display_note("This is useful for encapsulation — internal data is protected while allowing controlled access.")
    show_code_with_output('''
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
    ''',
    "100\n150\nDeleting price...\n"
    )

    print_sub_heading("3) Class Variables, Instance Variables, and Methods")
    display_note("Instance Variables:  Unique to each object, Defined using 'self.var' inside __init__ or methods, Accessed via 'self.var'.")
    display_note("Class Variables: Shared among all instances, Defined directly in the class body, ")
    display_note("Accessed via 'ClassName.var' or 'self.__class__.var'.", message_continue=True)
    display_note("Changing a class variable via instance creates a new instance variable—doesn’t affect others.", "warning")
    display_note("@classmethod: Takes `cls` as first argument. ")
    display_note("Can access and modify class variables dynamically, and supports alternate constructors and subclass-aware behavior.", message_continue=True)
    display_note("@staticmethod: Takes no `self/cls`, Access class variables(`ClassName.var`) ")
    display_note("but not instance attributes, not class-aware or dynamic, Behaves like a normal function within class context.", message_continue=True)
    show_code_with_output('''
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

    # Accessing class variable
    print("Domain name:", User.domain)

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

    user1.notExist=404

    print("User1 notExist:", user1.notExist)  # Accessing instance variable
    print("User2 notExist:", user2.notExist)  # Accessing instance variable
''',
    "Domain name: example.com\n" +
    "'alice_smith@example.com' assign to user: 'Alice Smith'\n" + "'bob_johnson@example.com' assign to user: 'Bob Johnson'\n" + "'alice_smith@example.com' assign to user: 'Alice Smith'\n" + 
    "Users List: {'Alice Smith': 'alice_smith@example.com', 'Bob Johnson': 'bob_johnson@example.com'}\n" + 
    "User 'Alice Smith' already exist\n" + "Email 'Charlie Brown' is available for assignment.")


if __name__ == "__main__":
        main()
