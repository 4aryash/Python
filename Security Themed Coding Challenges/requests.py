import requests

response = requests.get('http://crabby-clicker.ctf.umasscybersec.org/click')
print(response.text)
print(response.headers)
print(response.status_code)

response = requests.post('http://crabby-clicker.ctf.umasscybersec.org/click', data = {'hello':'world'})
if response.status_code == 200:
	print('Message sent successfully!')
else:
	print('Message undelivered. Error code:', response.status_code)
	#print(r'66.249.67.197 - - [18/Jul/2011:03:35:52 -0500] "GET /robots.txt HTTP/1.1" 404 286 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
