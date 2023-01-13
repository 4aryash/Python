#!bin/python3

list1= ["A","B","C"]		#a list of ordered data
list2= ["A","100",[],["Nested","List"],("Tuple"),False]
#a list of unordered data containing a string, integer, an empty list, a nested list, a tuple, and a Boolean.

print("\n")
print(list1)		#prints list1
print(list2)		#prints list2

#INDEXING LISTS
print("________________\n")
print(list1[0])		#prints first element of list1
print(list1[:])		#prints all elements of list1

#INDEXING NESTED LISTS
print("________________\n")
print(list2[3])		#prints fourth element/3rd-index of list2
print(list2[3][0])	#prints first element/zeroth-index of nested list at 3rd index of list2

#APPENDING LIST ELEMENTS
print("________________\n")
list1[0]= "B"		#appending the value of first element ie. "A" to "B"
print(list1[:])		#printing the entire list1
list2[3][0]= "Editable"	#appending the value of first-element/zeroth-index of the nested list to "Editable"
print(list2[:])		#printing the entire list2

#DELETING LIST ELEMENTS
print("________________\n")
del list1[0]		#deleting the first-element "A" from the list
del list2[4:]		#deleting all the elements after the fifth-element/4th-index from list2
print(list1[:])
print(list2[:])

#INSERTING ELEMENTS IN LIST
print("________________\n")
list1.insert(0,"A")	#inserting the deleted element back as the first-element on zeroth-index
list2.insert(4,["New","List"])	#inserting a new nested list as the fifth-element on 4th-index
print(list1[:])
print(list2[:])

#APPENDING VALUES TO THE END OF A LIST
print("________________\n")
list1.append("D")	#appends a new element at the end of a list
print(list1)

#REVERSING ELEMENTS OF A LIST
print("________________\n")
list1.reverse()		#reversing using the reverse function
print(list1)
#or by another method
list1= list1[::-1]	#reversing using the slice method
print(list1)

#COUNTING THE OCCURANCE OF AN ELEMENT IN THE LIST
print("________________\n")
print(list1.count("A"))	#prints the total number of A's in the list

#POPPING ELEMENTS IN A LIST
print("________________\n")
list1.append("F")	#adding F into the list
print(list1)
list1.pop()		#removing the last element added to the list
print(list1)

#EXTENDING LISTS
print("________________\n")
list3= ["E","F","G"]	#creating a new list
list4= list1[:]+list3[:]	#combining list1 and list3 into list4
print(list4)
