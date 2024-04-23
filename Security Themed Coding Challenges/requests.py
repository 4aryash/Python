import requests

response = requests.get('http://crabby-clicker.ctf.umasscybersec.org/click')
print(response.text)
print(response.status_code)

response = requests.post('http://crabby-clicker.ctf.umasscybersec.org/click', data = {'hello':'world'})
if response.status_code == 200:
	print('Message sent successfully!')
else:
	print('Message undelivered. Error code:', response.status_code)
