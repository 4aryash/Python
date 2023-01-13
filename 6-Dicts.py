#!bin/python3



new_dict= {"Pratinav":1,"Preetham":3,"Sahil":2,"Aaryash":4}
print(new_dict)

print(type(new_dict))
print(len(new_dict))
print("----------")
print(new_dict["Aaryash"])	#prints the value of the "Aaryash" key element in the dict
print("----------")
print(new_dict.get("Pratinav"))	#printing the value of the "Pratinav" key using the get()
print("----------")
print(new_dict.keys())		#printing all the keys inside the dictionary using keys()
print("----------")
print(new_dict.values())	#printing all the values in the dict using values()
print("----------")
print(new_dict.items())		#printing each of the items or key-value-pairs in the dictionary using items()
print("----------")

new_dict["Krishna"]= 5		#adding a new key-value pair to the dictionary
print(new_dict) 
print("----------")

new_dict.update({"Preetham":2, "Sahil":3})	#appending the key-value pair
print(new_dict)
print("----------")

new_dict.pop("Krishna")		#popping a key-value pair from the dict
print(new_dict)
print("----------")

del new_dict["Preetham"]	#another way to pop a key-value pair from the dict
print(new_dict)
print("----------")

new_dict["Out"]= {"Preetham":2 ,"Krishna":5}	#creating a nested dict
print(new_dict)
print("----------")

ultraNewDict = {}		#method2 to define a dict
print(ultraNewDict)
print("----------")

ultraNewDict2= dict()		#method3 to define a dict
print(ultraNewDict2)
print("----------")
###These methods are useful when the type of data to be filled in the dict isn't known.
###Also empty dicts can be used while iterating something and using the dict as a dump.
