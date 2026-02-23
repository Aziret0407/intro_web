"""
Lab 9: Error Handling and Debugging
Author: Student
"""

# 1. Common Built-in Exceptions

def builtin_exceptions_demo():
    print("=== Built-in Exceptions Demo ===")

    # ZeroDivisionError
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    # ValueError
    try:
        number = int("abc")
    except ValueError:
        print("Error: Invalid integer value.")

    # IndexError
    try:
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError:
        print("Error: List index out of range.")

    # KeyError
    try:
        d = {"name": "John"}
        print(d["age"])
    except KeyError:
        print("Error: Key not found in dictionary.")

    # TypeError
    try:
        result = "5" + 5
    except TypeError:
        print("Error: Incompatible types.")

    # FileNotFoundError
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: File not found.")

# 2. try-except with else and finally

def division_program():
    print("\n=== Division Program ===")

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError:
        print("Error: Please enter valid integers.")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.\n")

# 3. Handling Multiple Exceptions Together

def multiple_exceptions():
    print("=== Multiple Exceptions Together ===")

    try:
        number = int(input("Enter a number: "))
        result = 10 / number
    except (ValueError, ZeroDivisionError) as e:
        print("Error occurred:", e)

# 4. Raising Exceptions

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount

# 5. NotImplementedError Example

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# 6. Custom Exceptions

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot compute square root of a negative number.")
    return number ** 0.5

# 7. Assertion Example

def check_age(age):
    assert age >= 0, "Age cannot be negative!"
    print("Valid age:", age)

# 8. Simple Debugging Example

def debugging_example():
    print("\n=== Debugging Example ===")

    numbers = [1, 2, 3, 4, 5]
    total = 0

    for num in numbers:
        print("Adding:", num)  # Debug print
        total += num

    print("Total:", total)

# 9. Main Function

def main():
    builtin_exceptions_demo()

    division_program()

    multiple_exceptions()

    print("\n=== Raising Exception Example ===")
    try:
        print("New balance:", withdraw(100, 150))
    except ValueError as e:
        print("Error:", e)

    print("\n=== Custom Exception Example ===")
    try:
        print("Square root:", calculate_square_root(-9))
    except NegativeNumberError as e:
        print("Error:", e)

    print("\n=== Assertion Example ===")
    try:
        check_age(-5)
    except AssertionError as e:
        print("Assertion Error:", e)

    debugging_example()

    print("\nLab 9 Completed Successfully!")

if __name__ == "__main__":
    main()