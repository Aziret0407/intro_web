#

try:
    import camelcase
except ImportError:
    print("Библиотека 'camelcase' не установлена. Установите: pip install camelcase")
    exit()

c = camelcase.CamelCase()
txt = "hello world"
result = c.hump(txt)
print(f"Исходная строка: '{txt}'")
print(f"После camelcase: '{result}'")