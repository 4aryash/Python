def defangIP(address):
	#logic

	#grab the IP
	#from IP, find '.' and replace with [.]

	defanged = address.replace(".", "[.]")
	print(address)
	print(defanged)

address = "8.8.8.8"
defangIP(address)
