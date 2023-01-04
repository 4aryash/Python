#!bin/python3

'''
if __name__ == "__main__":
	print("Hello World")	#prints Hello World
	print(__name__*5)	#prints the value of name 5 times
	print(type(__name__))	#prints the datatype of name variable
	print(len(__name__))	#prints the length of the value in name
	
	name_list = ["Hello", "World"]	#creating a list of objects
	print(name_list)	#printing the contents inside the list
	content1, content2= name_list	#variables are assigned the values of the list
	print(content1, content2)	#prints Hello World
	
	name_tuple = ("New","Tuple")	#assigning data in a tuple format
	print(name_tuple[1])
	
	name_dictionary = {"New":"3", "Dictionary":"10"}	#assigning data in a dict format
	print(name_dictionary['New'])
	
	name_boolean = "True"	#assigning data in a boolean format
	print(name_boolean)
	
	name_range = range(68)	#assigning data in a range format
	print(name_range)
	
	name_bytes = b"what is this?"	#assigning data in a bytes format
	print(name_bytes)
'''

#-------------------------------------------------------------------------------------


def test_function(a):
#A code block to demonstrate the working of a function in python.
	b = 10 + a
	return print(b)	#returns the value of the variable b, which is 30

test_function(20)	#sending 20 as an input to the test_function


#-------------------------------------------------------------------------------------

'''
def least_difference(a,b,c,d):
#A code block to find out the least difference between 4 numbers
	diff1= abs(a-b)	#finding the absolute value of the difference btwn a and b
	diff2= abs(a-c)
	diff3= abs(a-d)
	diff4= abs(b-c)
	diff5= abs(b-d)
	diff6= abs(c-d)
	
	ultimate= print(min(diff1, diff2, diff3, diff4, diff5, diff6))
	#storing the minimum of all differences in an ultimate variable
	
	return ultimate
	
least_difference(0,2,4,8)
'''
