"""
Различные способы импорта и использования модулей.
Для работы требуется файл mymodule.py в той же папке.
"""

# 1. Импорт всего модуля
import mymodule
mymodule.greeting("Jonathan")          # Hello, Jonathan

# 2. Доступ к атрибуту модуля
age = mymodule.person1["age"]
print(f"Возраст (через mymodule): {age}")

# 3. Импорт с псевдонимом
import mymodule as mx
print(f"Возраст (через псевдоним mx): {mx.person1['age']}")

# 4. Импорт стандартного модуля platform
import platform
system_name = platform.system()
print(f"Операционная система: {system_name}")

# 5. Использование dir() для получения списка атрибутов модуля
print("\nАтрибуты модуля platform (первые 10):")
attributes = dir(platform)
print(attributes[:10])   # покажем только первые 10 для краткости

# 6. Импорт конкретного объекта из модуля
from mymodule import person1
print(f"Возраст (после from ... import): {person1['age']}")