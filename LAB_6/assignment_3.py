# Создание множества
my_set = {1, 2, 3}
print("Исходное множество:", my_set)

# Добавление элемента
my_set.add(4)
print("После добавления 4:", my_set)

# Удаление элемента
my_set.remove(2)
print("После удаления 2:", my_set)

# Проверка принадлежности
element = 3
if element in my_set:
    print(f"{element} есть в множестве")
else:
    print(f"{element} нет в множестве")