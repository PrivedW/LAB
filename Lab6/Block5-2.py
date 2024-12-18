#Вариант 3

def fibonacci(k):
    if k == 1 or k == 2:
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)


k = int(input("Введите номер k для вычисления числа Фибоначчи: "))

if k <= 0:
    print("Введите положительное число.")
else:
    result = fibonacci(k)
    print(f"{k}-е число Фибоначчи: {result}")