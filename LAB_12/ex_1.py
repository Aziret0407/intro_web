
# ============================================================
# PART 1: Basic Classes and Objects
# ============================================================

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.brand} {self.model} ({self.year})"


vehicle1 = Vehicle("Toyota", "Corolla", 2020)
vehicle2 = Vehicle("Honda", "Civic", 2019)

print("Example 1: Creating Objects")
print(vehicle1.get_description())
print(vehicle2.get_description())
print("-" * 50)


# ============================================================
# PART 2: Constructor and Methods
# ============================================================

class Individual:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_a = Individual("Alice", 25)
person_b = Individual("Bob", 30)

print("Example 2: __init__ Constructor")
print(f"{person_a.name}, age: {person_a.age}")
print(f"{person_b.name}, age: {person_b.age}")
print("-" * 50)


class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"


my_pet = Pet("Bobby", "Golden Retriever")
print("Example 3: Class Methods")
print(my_pet.speak())
print("-" * 50)


# ============================================================
# PART 3: Modifying Object Attributes
# ============================================================

class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


my_device = Device("Samsung", 500)
print("Example 4: Modifying Attributes")
print(f"Original price: {my_device.price}")

my_device.price = 450
print(f"New price: {my_device.price}")
print("-" * 50)


# ============================================================
# PART 4: Class Variables vs Instance Variables
# ============================================================

class Staff:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


staff1 = Staff("Alice", 50000)
staff2 = Staff("Bob", 60000)

print("Example 5: Class vs Instance Variables")
print(f"Staff 1: {staff1.name}, salary: {staff1.salary}, company: {staff1.company}")
print(f"Staff 2: {staff2.name}, salary: {staff2.salary}, company: {staff2.company}")

Staff.company = "NewTechCorp"
print(f"\nAfter changing class variable:")
print(f"Staff 1 company: {staff1.company}")
print(f"Staff 2 company: {staff2.company}")
print("-" * 50)


# ============================================================
# PART 5: The Role of self Keyword
# ============================================================

class Counter:
    def __init__(self, start_value):
        self.value = start_value

    def add(self, number):
        self.value += number

    def get_value(self):
        return self.value


calc = Counter(10)
calc.add(5)
print("Example 6: The Role of self")
print(f"Result: {calc.get_value()}")
print("-" * 50)


# ============================================================
# PART 6: Deleting Attributes and Objects
# ============================================================

class Profile:
    def __init__(self, username, email):
        self.username = username
        self.email = email


user_profile = Profile("Alice", "alice@gmail.com")
print("Example 7: Deleting Attributes and Objects")
print(f"User email: {user_profile.email}")

del user_profile.email
print("Email attribute deleted")

del user_profile
print("User profile object deleted")
print("-" * 50)


# ============================================================
# PART 7: Encapsulation (Data Protection)
# ============================================================

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 1000)
print("Example 8: Encapsulation")
print(f"Owner: {account.owner}")
print(f"Initial balance: {account.get_balance()}")

account.deposit(500)
account.withdraw(300)
print(f"Current balance: {account.get_balance()}")
print("-" * 50)


# ============================================================
# PART 8: Inheritance
# ============================================================

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


print("Example 9: Inheritance")
dog_obj = Dog("Buddy")
cat_obj = Cat("Whiskers")

print(f"{dog_obj.name} says: {dog_obj.make_sound()}")
print(f"{cat_obj.name} says: {cat_obj.make_sound()}")
print("-" * 50)


# ============================================================
# PART 9: Polymorphism
# ============================================================

class Bird:
    def fly(self):
        return "Flying high in the sky"


class Plane:
    def fly(self):
        return "Taking off into the sky"


class Fish:
    def fly(self):
        return "Can't fly!"


print("Example 10: Polymorphism")
objects = [Bird(), Plane(), Fish()]

for i, obj in enumerate(objects, 1):
    print(f"Object {i}: {obj.fly()}")
print("-" * 50)

# ============================================================
# PART 10: Abstraction (using ABC)
# ============================================================

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started!")


print("Example 11: Abstraction")
my_car = Car()
my_bike = Motorcycle()

my_car.start_engine()
my_bike.start_engine()
print("-" * 50)


# ============================================================
# PART 11: Method Overriding
# ============================================================

class Parent:
    def show(self):
        print("This is the parent class")


class Child(Parent):
    def show(self):
        print("This is the child class (overridden)")


print("Example 12: Method Overriding")
child_obj = Child()
child_obj.show()
print("-" * 50)


# ============================================================
# PART 12: Multiple Inheritance
# ============================================================

class A:
    def method_a(self):
        print("Method from parent A")


class B:
    def method_b(self):
        print("Method from parent B")


class C(A, B):
    pass


print("Example 13: Multiple Inheritance")
obj_c = C()
obj_c.method_a()
obj_c.method_b()
print("-" * 50)


# ============================================================
# PART 13: Real Example - Library Management System
# ============================================================

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author} ({self.year})"


book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("Library is empty")
        else:
            print("Books in library:")
            for i, book in enumerate(self.books, 1):
                print(f"  {i}. {book.get_info()}")


print("Example 14: Library System")
my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.show_books()
print("-" * 50)


# ============================================================
# PART 14: User Authentication System
# ============================================================

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, password):
        if password == self.__password:
            return f"Welcome, {self.username}!"
        else:
            return "Invalid password!"


print("Example 15: Authentication System")
admin_user = User("admin", "secure123")
print(admin_user.login("secure123"))
print(admin_user.login("wrongpass"))
print("-" * 50)