
def calc(ints):
    for i in range(0, len(ints), 4):
        instr = ints[i]
        try:
            if instr == 99:
                break
            if instr == 1:
                ints[ints[i+3]] = ints[ints[i+1]]+ints[ints[i+2]]
            if instr == 2:
                ints[ints[i+3]] = ints[ints[i+1]]*ints[ints[i+2]]
        except:
            return 0
    return ints[0]


def findInstructions(ints):
    for i in range(100):
        for j in range(100):
            newList = [x for x in ints]
            newList[1] = i
            newList[2] = j
            result = calc(newList)
            if result == 19690720:
                return (i, j)
    print("didnt find")


with open("puz3.txt") as file:
    for line in file:
        data = str.split(line, ",")
        ints = [int(i) for i in data]


print(findInstructions(ints))
