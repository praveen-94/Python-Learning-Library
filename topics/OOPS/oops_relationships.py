from helpers.display_utils import *

def main():
    print_heading("OOP Relationship- Composition, Aggregation, and Association Demo")
    print_sub_heading("1) Association (Uses-a Relationship, Weaker relationship)")
    display_note("Association is a relationship where one class uses another class without ownership. It can be one-to-one, one-to-many, or many-to-many, both can exist independently.")
    display_note("Ex: A customer can use a payment method, but the payment method does not own the customer.", "example", "👤")
    show_code_with_output('''
    class Customer:
        def __init__(self, name):
            self.name = name    
        def use_payment(self, payment):
            print(f"{self.name} is using {payment.method} for payment.")
                        
    class PaymentMethod:
        def __init__(self, method):
            self.method = method
                        
    customer = Customer("Alice")
    payment = PaymentMethod("Credit Card")
    customer.use_payment(payment)  # Alice is using Credit Card for payment.
    ''',
    "Alice is using Credit Card for payment.\n")

    print_sub_heading("2) Aggregation (Has-a Relationship)")
    display_note("Aggregation is a special form of association where one class contains references to another class, but the contained class can exist independently.")
    display_note("Ex: Example: Department has professors", "example", "📚")
    show_code_with_output('''
    class Professor:
        def __init__(self, name):
            self.name = name

    class Department:
        def __init__(self, dept_name):
            self.dept_name = dept_name
            self.professors = []  # Aggregates multiple Professor objects

        def add_professor(self, prof):
            self.professors.append(prof)

        def show_professors(self):
            return [prof.name for prof in self.professors]

    d = Department("Computer Science")
    p1 = Professor("Dr. Smith")
    p2 = Professor("Dr. Jane")

    d.add_professor(p1)
    d.add_professor(p2)

    print(d.show_professors())
    ''',
    "['Dr. Smith', 'Dr. Jane']\n")

    print_sub_heading("3) Composition (Part-of Relationship, Stronger relationship)")
    display_note("A strong form of aggregation where the contained class cannot exist independently of the containing class.")
    display_note("If the containing class is destroyed, the contained class is also destroyed.")
    display_note("Ex: A car has an engine, if the car is destroyed, the engine is also destroyed.", "example", "🚗")
    show_code_with_output('''
    class Engine:
        def __init__(self, type):
            self.type = type
        def __str__(self):
            return f"{self.type} Engine"
                        
    class Car:
        def __init__(self, model):
            self.model = model
            self.engine = Engine("V8")  # Composition: Car has an Engine
        def __str__(self):
            return f"{self.model} with {self.engine}"
                        
    car = Car("Mustang")
    print(car)  # Mustang with V8 Engine
    car.engine = None  # Engine is now None, but car still exists
    ''',
    "Mustang with V8 Engine\n")