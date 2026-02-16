def sum_list(numbers):
    """Возвращает сумму элементов списка."""
    total = 0
    for n in numbers:
        total += n
    return total

# Запрашиваем у пользователя список чисел, разделённых пробелами
input_str = input("Введите числа через пробел: ")
# Разбиваем строку на части, преобразуем каждую в число (с плавающей точкой)
numbers = [float(x) for x in input_str.split()]

print(f"Сумма введённых чисел = {sum_list(numbers)}")