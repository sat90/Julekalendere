
slime = {}
time = 0
X = 0
Y = 0

with open("coords.csv") as file:
    for i, line in enumerate(file):
        if i != 0:
            xx, yy = line.split(",")
            x = int(xx)
            y = int(yy)

            while x > X:
                X += 1
                if (X, Y) not in slime:
                    slime[(X, Y)] = 0
                slime[(X, Y)] += 1
                time += slime[(X, Y)]
            while x < X:
                X -= 1
                if (X, Y) not in slime:
                    slime[(X, Y)] = 0
                slime[(X, Y)] += 1
                time += slime[(X, Y)]
            while y > Y:
                Y += 1
                if (X, Y) not in slime:
                    slime[(X, Y)] = 0
                slime[(X, Y)] += 1
                time += slime[(X, Y)]
            while y < Y:
                Y -= 1
                if (X, Y) not in slime:
                    slime[(X, Y)] = 0
                slime[(X, Y)] += 1
                time += slime[(X, Y)]

print(time)
