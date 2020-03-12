import json
import random


def shuffle(in_str):
    elements = list(in_str)
    out = ""
    while len(elements) > 0:
        rand_int = random.randint(0, len(elements)-1)
        out += (elements[rand_int])
        elements.remove(elements[rand_int])
    return out


def test_shuffle():
    input_string = "abcde"
    result = {}

    for i in range(1000):
        shuffled = shuffle(input_string)
        for j, c in enumerate(shuffled):
            if c not in result:
                result[c] = {}
            if j not in result[c]:
                result[c][j] = 0
            result[c][j] += 1
    print(json.dumps(result, indent=4))


myString="test"
myString=shuffle()
print("test")

test_shuffle()
