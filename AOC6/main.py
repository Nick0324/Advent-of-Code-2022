file = open('input.txt', 'r')
lines = file.readlines()

line = lines[0]


for i in range(len(line) - 3):
    l = [line[i], line[i + 1], line[i + 2], line[i + 3]]
    if len(l) == len(set(l)):
        print(i + 4)
        break
