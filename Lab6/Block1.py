#Вариант 8
import math

a = int(input("Введите боковую сторону треугольника:" ))
Asin = int(input("Введите угол между боковыми сторонами: "))

S = 1/2*(a*a)*math.ceil(math.sin(math.radians(Asin))*10)/10

print("Площадь треугольника:", S)
if  S % 2 == 0:
    print(S/2)
else:
    print("Не могу делить на 2!")