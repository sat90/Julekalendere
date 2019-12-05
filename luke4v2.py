import time
slime = {}
tid = 0
X = 0
Y = 0

start = time.time()

with open("coords.csv") as file:
    for i, line in enumerate(file):
        if i != 0:
            xx, yy = line.split(",")
            x = int(xx)
            y = int(yy)

            while x != X:
                if x > X:
                    X += 1
                elif x < X:
                    X -= 1
                if (X, Y) not in slime:
                    slime[(X, Y)] = 0
                slime[(X, Y)] += 1
                tid += slime[(X, Y)]

            while y != Y:
                if y > Y:
                    Y += 1
                elif y < Y:
                    Y -= 1
                if (X, Y) not in slime:
                    slime[(X, Y)] = 0
                slime[(X, Y)] += 1
                tid += slime[(X, Y)]
print(f'Tok: {(time.time() - start)*1000} ms')
print(tid)
