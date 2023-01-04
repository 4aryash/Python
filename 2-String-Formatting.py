#!/bin/python3

string1= "I am a string"
print(string1)

string2= "I'm a string"
print(string2)

string3= 'I\'m a string too but with an escape character.'
print(string3)

string4= 'XXX'
print(string4)

string5= 'X' * 3
print(string5)

print(len(string5))


#some other basic string functions
string6= '	Hello-World-of-Kali! \n\n'

#startswith()
print(string6.startswith('H'))	#boolean output if condition is met. Also, case-sensitive
#endswith()
print(string6.endswith('z'))

#strip()
print(string6)
temp_var = string6.strip()	#removes unintended blank spaces like tabspace before hello and \n\n
print(temp_var)

#replace()
print(temp_var.replace('!','!!?'))	#replaces ! with !!?

#split()
print(temp_var.split())	#splits strings into words by splitting at spaces by default, here no spaces between words so the list will only have one element
print(temp_var.split('-'))	#splitting the string at provided parameter, here hyphen

#rjust() and ljust()
print('Hello'.ljust(30,'>'))	#justifying text from left
print('World'.rjust(30,'<'))	#from right

#bin()
x= 13
print(bin(x))
print(bin(x)[2:].rjust(4,"0"))	#removing the 0b from the start and right justf so that the string is always 4 bits in length
