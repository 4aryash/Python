# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the left bar.

# Enjoy your interview!

# QUESTION: 
# Given are 5 types of escaped/defanged IPv4 Address, write a function to make it live again. Return a valid IP.


def defang_and_validate(input_ip):
    
	#print("Hello, world!")
	#return None


	# My code below - Time Complexity : O(n)

	##### TEST CASE 1
		# Input - 3 different types of defanged IPs
		# Output - 3 different fanged/live IPs

	# To check if the string elements are digits or special chars
	# If special characters are present in the input string, we append only digits in defanged_list
	# Then we join the list elements to make it back to a string and store it as defanged_IP
	# defanged_IP data type - str

	defanged_list = []

	for i in input_ip:
		if i.isdigit() or i == ".":
			defanged_list.append(i)

	defanged_IP = ''.join(defanged_list)
	# print(defanged_IP)
	# print(defanged_list, "\n")


	##### TEST CASE 3
		# 1.2.3.4.5.6.7 → IPs containing more than 3 periods OR Invalid IPs should be returned False/None/nothing/exception

	count = 0

	for k in defanged_IP:
		if k == ".":
			count += 1
	print(count)

	if count > 3:
		print(f"\n{input_ip} - Invalid IP - More than 3 period characters detected.")


	##### TEST CASE 2
		# +999.03.101.123 → IPs are Out of Range OR Invalid IPs should be returned as False/None/nothing/exception

    # To create a new list to check if IP is valid or not
    # Then splitting each element of the defanged_IP into a new list valid_IP
    # Iterating over valid_IP's str elements by comparing their integer values
    # First check would be to see if the first octet (index 0) starts with 0. If yes, then it becomes invalid
    # Rest of the octets should just fall in the range(0,256), since rest of the octets can start from 0 and end at 255.
    # valid_IP data type - list
    # elements of valid_IP data type - str

	valid_IP = defanged_IP.split('.')
	# print("\n", defanged_IP)
	# print("\n", valid_IP)

	for j in range(len(valid_IP)):

		if j == 0 and valid_IP[j] == 0:
			print(f"{input_ip} - Invalid IP - First Octet in IP starts with 0.")

		elif int(j) > 0 and int(j) <= 255:
			print("Valid IP")
			break
		
		else:
			print(f"{input_ip} - Invalid IP - IP Octets range out of bounds.")
    #check if ip is even valid and not #1.2.3.4.5.6.7 or +999.03.101.123



#     #return defanged_IP


# # Test-Case 2: # +999.03.101.123 → False / None / nothing / exception

#     valid_IP = defanged_IP.split('.')
#     for j in range(len(valid_IP)):
#         if j == 0 and valid_IP[j] == 0:
#             print ("Invalid IP") 
#         elif valid_IP[j] >=0 and valid_IP[j] <= 255:
#         	continue
#         else:
#             print ("Invalid IP")
#     return valid_IP


# # Test-Case 3: # 1.2.3.4.5.6.7   → False / None / nothing / exception

#     test_str2 = output_str.split('') # [1, '.', 2]
#     counter = 0
#     for k in range(len(test_str2)):
#         if k.isdigit() == False:
#             if test_str2[k] =='.':
#                 counter += 1
    
#     if counter > 3:
#         return output_str
#     else:
#         return False

ip = "192/.168/.10/.20"
ip2 = "192.168[.]110.5"
ip3 = "192.168#.20.54"
ip4 = "+999.03.101.123"
ip5 = "1.2.3.4.5.6.7"

print (defang_and_validate (ip))
print (defang_and_validate (ip2))
print (defang_and_validate (ip3))
print (defang_and_validate (ip4))
print (defang_and_validate (ip5))
