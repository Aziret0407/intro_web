def square(num):
    """Возвращает квадрат числа."""
    return num ** 2

# Запрашиваем число у пользователя
number = float(input("Введите число: "))
print(f"Квадрат числа {number} = {square(number)}")