#Вариант 9
N = int(input("Введите количество элементов массива: "))

array = [float(input(f"Введите элемент {i + 1}: ")) for i in range(N)]

min_abs_element = min(abs(array))

print("Минимальный по модулю элемент:", min_abs_element)
print("Массив в обратном поряде:", array[::-1])