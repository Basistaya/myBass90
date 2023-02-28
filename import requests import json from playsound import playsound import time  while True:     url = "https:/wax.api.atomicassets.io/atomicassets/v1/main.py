import requests
import json
from playsound import playsound
import time

while True:
    url = "https://wax.api.atomicassets.io/atomicassets/v1/collections"
    response = requests.get(url)
    otvetik = response.json()['data'][0]['data']['socials']


    #with open('love.txt', 'rt+') as f:
         #file = f.read()
    file = open('love.txt', 'rt')
    if otvetik != "{}":
        disc = json.loads(otvetik)
        if file.read() != disc['discord'] and disc['discord'] != "":
