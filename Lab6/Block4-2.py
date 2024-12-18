#Вариант 9

A = [float(input(f"Введите элемент массива A[{i + 1}]: ")) for i in range(10)]
B = [float(input(f"Введите элемент массива B[{i + 1}]: ")) for i in range(10)]

print("Исходный массив A:", A)
print("Исходный массив B:", B)

A, B = B, A

print("Преобразованный массив A:", A)
print("Преобразованный массив B:", B)