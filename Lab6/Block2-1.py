#Вариант 7
import random

print("Введите последовательность с концом 0:")

A =[]
while True:
    num = int(input())
    A.append(num)
    if num == 0:
        break
    

sumn = 0
num = 0

for n in A:
    sumn += n 
    num +=1

print("Последовательность: ", A)
print("Сумма: ", sumn)
print("Кол-во чисел: ", num)
