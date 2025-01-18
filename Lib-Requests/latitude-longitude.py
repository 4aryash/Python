import requests

response = requests.get("http://ip-api.com/json/24.48.0.1")#.json()

# print(response.get('lat'), response.get('lon'))
# OR
#print(response.json().get('lat'), response.json().get('lon'))
# OR
# deets = response.json()
# print(deets['city'], deets['lat'], deets['lon'])
# OR
print(response.json()['city'], response.json()['lat'], response.json()['lon'])