import string

file = open('input.txt', 'r')
lines = file.readlines()

tsum = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase

for line in lines:
    flag = False
    line = line.rstrip()
    first_half = line[:len(line) // 2]
    second_half = line[len(line) // 2:]
    for i in first_half:
        for j in second_half:
            if i == j:
                flag = True
                tsum += alphabet.index(i) + 1
                break
        if flag:
            break

print(tsum)