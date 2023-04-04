file = open('input.txt', 'r')
lines = file.readlines()

tsum = 0

for line in lines:
    elve1, elve2 = line.split(",")
    elve1s, elve1e = elve1.split("-")
    elve2s, elve2e = elve2.split("-")
    if int(elve2s) <= int(elve1s) <= int(elve2e) and int(elve2s) <= int(elve1e) <= int(elve2e) or int(elve1s) <= int(elve2s) <= int(elve1e) and int(elve1s) <= int(elve2e) <= int(elve1e):
        tsum += 1

print(tsum)