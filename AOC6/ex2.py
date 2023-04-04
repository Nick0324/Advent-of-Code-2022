file = open('input.txt', 'r')
lines = file.readlines()

line = lines[0]



for i in range(len(line) - 14):
    l = line[i:i+14]
    if len(l) == len(set(l)):
        print(i + 14)
        break
