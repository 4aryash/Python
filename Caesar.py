#!bin/python3

import sys

#GLOBAL VARIABLES
UID = 119222119
Last_Name = 'Sinha'
First_Name = 'Aaryash Raj'


#ENCRYPTION CODE SNIPPET
def caesar_str_enc(s, shift):
	s = s.upper()
	encrypted = ""
	for j in s:
		if j.isupper():
			encrypted += chr((ord(j) + shift - 65) % 26 + 65)
		else:
			encrypted += j
	return encrypted


#DECRYPTION CODE SNIPPET
def caesar_str_dec(s, shift):
	s = s.upper()
	decrypted = ""
	for j in s:
		if j.isupper():
			decrypted += chr((ord(j) - shift - 65) % 26 + 65)
		else:
			decrypted += j
	return decrypted


#MAIN FUNCTION
if __name__ == "__main__":
	
	#BANNER
	print("\n")
	print("	 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗ ██╗███████╗██████╗")
	print("	██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗")
	print("	██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝")
	print("	██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗")
	print("	╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║")
	print("	 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
	
	#working code
	selection = input("\n\tHi! Select an option below \n\t1. Encrypt a string\n\t2. Decrypt a string\n\n")
	if selection == "1":
		s = input("\tEnter the string to encrypt: ")
		shift = int(input("\tEnter the shift value: "))
		encstr = caesar_str_enc(s, shift)
		print("\tEncrypted String: ",encstr)
    	
	elif selection == "2":
    		s = input("\tEnter the string to decrypt: ")
    		shift = int(input("\tEnter the shift value: "))
    		decstr = caesar_str_dec(s, shift)
    		print("\tDecrypted String: ",decstr)
    		
	else: sys.exit()
