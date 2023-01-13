#!/bin/python3

for i in range(0,5): #loops from 0 to 4
	print(i)

print("------------")	#delineator

a=4
while a<9:	#loop break condition
	a+=1	#increment
	print(a)

print("------------")

for i in range(3):	#loops from 0 to 2
	for j in range(3):	#loops from 0 to 2
		print(i,j)	#prints the i,j values respc

print("------------")

for i in range(5):
	if i==2:
		#continue #continues to run the loop
		break	#breaks the loop when i=2
	print(i)

print("------------")

for x in "Hello":	#looping along the characters of string
	print(x)

print("------------")

for key,value in {"a":1, "b":2, "c":3}.items():
	print(key,value)
#looping along the items in a dictionary
