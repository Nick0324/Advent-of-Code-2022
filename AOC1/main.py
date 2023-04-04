file = open('input.txt', 'r')
lines = file.readlines()


csum = 0

arr = []

for line in lines:
    if line != '\n':
        csum += int(line)
    else:
        arr.append(csum)
        csum = 0

arr.sort(reverse=True)

csum = 0
for i in range(3):
    csum += arr[i]

print(csum)