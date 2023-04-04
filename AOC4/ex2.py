file = open('input.txt', 'r')
lines = file.readlines()

tsum = 0

for line in lines:
    elve1, elve2 = line.split(",")
    elve1s, elve1e = elve1.split("-")
    elve2s, elve2e = elve2.split("-")
    set1 = set(range(int(elve1s), int(elve1e) + 1))
    set2 = set(range(int(elve2s), int(elve2e) + 1))
    if set1.intersection(set2):
        tsum += 1

print(tsum)