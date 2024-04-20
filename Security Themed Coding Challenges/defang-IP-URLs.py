def defangIP(address):
	#logic

	#grab the IP
	#from IP, find '.' and replace with [.]

	defanged = address.replace(".", "[.]")
	print(address)
	print(defanged)

def defangURL(url):

	defanged = url.replace(".", "[.]").replace("http", "hxxp")
	print(url)
	print(defanged)


address = "8.8.8.8"
url = "http://www.example.com"
defangIP(address)
defangURL(url)
