FirstWire = set()
SecondWire = []
CrossingPts = []

with open("puz5.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            x = 0
            y = 0
            data = str.split(line, ",")
            for action in data:
                dir = action[0]
                amnt = int(action[1:len(action)])
                for i in range(amnt):
                    if dir == "R":
                        x += 1
                    elif dir == "L":
                        x -= 1
                    elif dir == "U":
                        y += 1
                    elif dir == "D":
                        y -= 1
                    FirstWire.add((x, y))
        elif i == 1:
            x = 0
            y = 0
            data = str.split(line, ",")
            for action in data:
                dir = action[0]
                amnt = int(action[1:len(action)])
                for i in range(amnt):
                    if dir == "R":
                        x += 1
                    elif dir == "L":
                        x -= 1
                    elif dir == "U":
                        y += 1
                    elif dir == "D":
                        y -= 1
                    if (x, y) in FirstWire:
                        print("found one")
                        CrossingPts.append((x, y))

min = 99999

for i in CrossingPts:
    if abs(i[0])+abs(i[1]) < min:
        min = abs(i[0])+abs(i[1])


print(min)
