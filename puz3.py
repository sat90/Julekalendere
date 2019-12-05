
with open("puz3.txt") as file:
    for line in file:
        data = str.split(line, ",")
        ints = [int(i) for i in data]

ints[1] = 12
ints[2] = 2
for i in range(0, len(ints), 4):
    instr = ints[i]
    if instr == 99:
        break
    if instr == 1:
        ints[ints[i+3]] = ints[ints[i+1]]+ints[ints[i+2]]
    if instr == 2:
        ints[ints[i+3]] = ints[ints[i+1]]*ints[ints[i+2]]
print(ints)
