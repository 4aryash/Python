#!/bin/python3

temp= input("Enter something here: ")
print(temp)

while True:
	temp2= input("Give a one line feedback here: ")
	print("Thank you for saying {}".format(temp2),"We'll remember this. Now proceed below...")
	if temp2== "exit":
		break
		
while True:
	temp3= input("\nEnter your IP: ")
	if temp3 == "exit":
		break
	else:
		print("Exploiting the machine with IP {}...".format(temp3))
		print("$")
