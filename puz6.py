FirstWire = {}
CrossingPts = {}

with open("puz5.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            x = 0
            y = 0
            steps = 0
            data = str.split(line, ",")
            for action in data:
                dir = action[0]
                amnt = int(action[1:len(action)])
                for i in range(amnt):
                    steps += 1
                    if dir == "R":
                        x += 1
                    elif dir == "L":
                        x -= 1
                    elif dir == "U":
                        y += 1
                    elif dir == "D":
                        y -= 1
                    FirstWire[(x, y)] = steps
        elif i == 1:
            x = 0
            y = 0
            steps = 0
            data = str.split(line, ",")
            for action in data:
                dir = action[0]
                amnt = int(action[1:len(action)])
                for i in range(amnt):
                    steps += 1
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
                        CrossingPts[(x, y)] = FirstWire[(x, y)]+steps

least = 9999999
for i in CrossingPts.values():
    if i < least:
        least = i

print(least)
