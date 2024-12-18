#Вариант 14

strok = str(input("Введите строку: "))

words = strok.split()
result = [w for w in words if w.lower().startswith('а') or w.lower().endswith('я')]

print("Слова, начинающиеся на 'а' или заканчивающиеся на 'я':", result)