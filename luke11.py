import requests

url = "https://julekalender.knowit.no/resources/2019-luke11/terreng.txt"
res = requests.get(url)
text = res.text

speed = 10703437
fjell = False
ice = 0
distance = 0

for c in text:
    distance += 1

    if c != "I":
        ice = 0

    if c == "G":
        speed -= 27
    elif c == "I":
        ice += 1
        speed += 12*ice
    elif c == "A":
        speed -= 59
    elif c == "S":
        speed -= 212
    elif c == "F":
        if fjell:
            speed += 35
            fjell = False
        else:
            speed -= 70
            fjell = True

    if speed <= 0:
        break
print(distance)
