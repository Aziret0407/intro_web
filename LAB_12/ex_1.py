# PART 1: Classes and Objects
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        return f"{self.brand} {self.model} ({self.year})"


car1 = Vehicle("Toyota", "Corolla", 2020)
car2 = Vehicle("Honda", "Civic", 2019)
print("Vehicle objects:")
print(car1.display())
print(car2.display())
print("-" * 30)


# PART 2: Inheritance
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


dog = Dog("Buddy")
cat = Cat("Whiskers")
print("\nInheritance:")
print(f"{dog.name} says {dog.make_sound()}")
print(f"{cat.name} says {cat.make_sound()}")
print("-" * 30)


# PART 3: Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"\nEncapsulation:")
print(f"Owner: {account.owner}, Balance: {account.get_balance()}")
print("-" * 30)


# PART 4: Polymorphism
class Bird:
    def fly(self):
        return "Flying in the sky"


class Airplane:
    def fly(self):
        return "Flying at high altitude"


class Fish:
    def fly(self):
        return "I can't fly"


print("\nPolymorphism:")
objects = [Bird(), Airplane(), Fish()]
for obj in objects:
    print(f"  {obj.__class__.__name__}: {obj.fly()}")