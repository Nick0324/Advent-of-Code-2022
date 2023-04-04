import string

file = open('input.txt', 'r')
lines = file.readlines()

tsum = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase

for i in range(2, len(lines), 3):
    line1, line2, line3 = lines[i - 2], lines[i - 1], lines[i]
    line1, line2, line3 = line1.rstrip(), line2.rstrip(), line3.rstrip()
    for c in line1:
        if c in line2 and c in line3:
            tsum += alphabet.index(c) + 1
            break

print(tsum)
