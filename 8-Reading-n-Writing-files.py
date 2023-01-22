#!/bin/python3

f= open('7-loops.py')
print(f)
#default mode is r, which is read mode
#other modes are appending, write, create mode.

f= open('dummy.txt', 'rt')
print(f)

print("\n-----------------------------------------------\n")

#print(f.read())
print(f.readlines()) #prints all lines as strings in an array format

print("\n-----------------------------------------------\n")
f.seek(0)
for line in f:
	print(line.strip())	#reads all lines in the file and strips extra characters

print("\n-----------------------------------------------\n")

print("Closing the file.........")
f.close()	#closing the file after use

print("\n-----------------------------------------------\n")

f= open("dummy2.txt", "w")	#opening a file in write mode
f.write("Test Line!\n")
f.close

f= open("dummy2.txt", "a")	#opening a file in append mode to edit
f.write("Test Line 2!\n")
f.close



print(f.name)	#specifies the name of the file in f
print(f.closed)	#specifies if the file has been closed or not? Good practice
print(f.mode)	#specifies the mode in which the file was last opened in

print("\n-----------------------------------------------\n")

########## ROCKYOU.TXT ############

with open('/usr/share/wordlists/rockyou.txt', encoding='latin-1') as f:
#it is important to mention encoding as some passwords might be encoded
	for line in f:
		pass	#iterating every password in the rockyou.txt file
