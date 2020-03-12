
import requests

url = "https://julekalender.knowit.no/resources/2019-luke10/logg.txt"
res = requests.get(url)
text = res.text


tannkrem=0
tktube=125
sjampo=0
sjampotube=300
tp=0
tprull=25

for line in text:
    print(line)
