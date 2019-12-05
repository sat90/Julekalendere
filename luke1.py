
import requests

url = "https://knowit-julekalender.s3.eu-central-1.amazonaws.com/sau.txt"
res = requests.get(url)
text = res.text

data = str.split(text, ", ")
ints = [int(i) for i in data]

dragon_size = 50
hangry = 0
rem_sheep = 0

for i, sheep in enumerate(ints):
    rem_sheep += sheep
    if rem_sheep >= dragon_size:
        rem_sheep -= dragon_size
        hangry = 0
        dragon_size += 1
    else:
        rem_sheep = 0
        hangry += 1
        dragon_size -= 1
    if hangry == 5:
        print(i)
        break
