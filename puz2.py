import math

sum = 0
with open("puz1.txt") as file:

    for line in file:
        nr = int(line)
        nr = nr/3
        nr = math.floor(nr)
        nr = nr-2
        sum += nr
        fuel = nr
        fuel = fuel/3
        fuel = math.floor(fuel)
        fuel = fuel-2
        while fuel > 0:
            sum += fuel
            fuel = fuel/3
            fuel = math.floor(fuel)
            fuel = fuel-2

print(sum)
