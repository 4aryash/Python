import requests

url = 'https://media.licdn.com/dms/image/v2/D4E22AQF2ys6he0WjjA/feedshare-shrink_1280/B4EZRY_xQZG0Ak-/0/1736659904777?e=1739404800&v=beta&t=X0KsXwM94tFydbqJGLsBxpJvMWqKDozMVh27ptq5R78'
response = requests.get(url)

with open ('shmoocon.jpg', 'wb') as f:
    f.write(response.content)