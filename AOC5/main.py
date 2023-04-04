file = open('input.txt', 'r')
lines = file.readlines()

tab = {
    1: "BGSC",
    2: "TMWHJNVG",
    3: "MQS",
    4: "BSLTWNM",
    5: "JZFTVGWP",
    6: "CTBGQHS",
    7: "TJPBW",
    8: "GDCZFTQM",
    9: "NSHBPF"
}

for line in lines:
    instr = line.split()
    amount = int(instr[1])
    fr = int(instr[3])
    to = int(instr[5])
    tab[to] = tab[to] + tab[fr][-amount:][::-1]
    tab[fr] = tab[fr][:-amount]

for i in range(1, 10):
    print(tab[i])
