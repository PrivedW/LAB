#Вариант 8
import json

ifile = 'lab.json'


with open(ifile, 'r') as file:
    data = json.load(file)

version = float(input("Введите номер версии для фильтрации: "))
filtered_data = [user for user in data if user.get('version') == version]

with open('out.json', 'w') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)
