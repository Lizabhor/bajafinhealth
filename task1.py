
import requests

url = 'https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON'

data = {"name": "Liza Bhor","regNo": "0827ci221083" ,"email":"lizabhor220387@acropolis.in"}


response = requests.post(url, json = data) 

print(response.text)