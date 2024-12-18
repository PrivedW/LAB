#Вариант 7

with open("input.txt", "r") as file:
    lines = file.readlines()

sort_lines = sorted(lines, key=lambda line: len(line.split()))


with open("output.txt", "w") as outfile:
    outfile.writelines(sort_lines) 