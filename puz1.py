import math
with open("puz1.txt") as file:
    sum = 0
    for line in file:
        nr = int(line)
        nr = nr/3
        nr = math.floor(nr)
        nr = nr-2
        sum += nr
print(sum)
