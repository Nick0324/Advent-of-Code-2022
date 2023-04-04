file = open('input.txt', 'r')
lines = file.readlines()

totalScore = 0

for line in lines:
    a, b = line.split()
    match a:
        case "A":
            match b:
                case "X":
                    totalScore += 3
                case "Y":
                    totalScore += 4
                case "Z":
                    totalScore += 8
        case "B":
            match b:
                case "X":
                    totalScore += 1
                case "Y":
                    totalScore += 5
                case "Z":
                    totalScore += 9
        case "C":
            match b:
                case "X":
                    totalScore += 2
                case "Y":
                    totalScore += 6
                case "Z":
                    totalScore += 7

print(totalScore)