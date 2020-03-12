amnt = 0


def arrToNum(input):
    nr = 0
    for tens, i in enumerate(input):
        nr += (10**(len(input)-tens-1))*i
    return nr


def iterate(input):
    numbers = [int(d) for d in str(input)]
    while len(numbers) < 4:
        numbers.insert(0, 0)
    numbers.sort()
    smallnumber = arrToNum(numbers)
    numbers.sort(reverse=True)
    bignumber = arrToNum(numbers)
    return bignumber-smallnumber


for i in range(1000, 9999):
    if i % 1111 == 0:
        continue
    number = i
    times = 0
    while number != 6174 and times < 7:
        number = iterate(number)
        times += 1
    if times == 7:
        amnt += 1

print(amnt)
