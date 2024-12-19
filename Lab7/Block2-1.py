#Вариант 8
import csv

def minN(data, column):
    try:
        return min((row[column]) for row in data if row[column].strip())
    except: 
        print("Не удалось высчитать минимальное занчение")
   
def maxN(data, column):
    try:
        return max((row[column]) for row in data if row[column].strip())
    except:
        print("Не получилось определить максимальное значение ")

def calcSum(data, column):
    try:
        return sum((row[column]) for row in data if row[column].strip())
    except:
        print("Не получилось посчитать сумму")
   

def Avr(data, column):
    try:
        values = [(row[column]) for row in data if row[column].strip()]
        return sum(values) / len(values) if values else None
    except: 
        print("Невозможно рассчитать среднее значение")


file = '8.csv'

with open(file, 'r') as file:
        data = [row for row in csv.DictReader(file)]

for row in data:
    print(" | ".join([f"{key} -> {value}" for key, value in row.items()]))

if data != None:
    column = input("Введите название колонки: ")
    print("Min:", minN(data, column))
    print("Max:", maxN(data, column))
    print("Sum:", calcSum(data, column))
    print("Avg:", Avr(data, column))