def fibonacci(n):
    """Возвращает n-е число Фибоначчи (рекурсивно)."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Запрашиваем количество чисел у пользователя
n = int(input("Введите количество чисел Фибоначчи для вывода: "))
print(f"Первые {n} чисел Фибоначчи:")
for i in range(n):
    print(f"F({i}) = {fibonacci(i)}")