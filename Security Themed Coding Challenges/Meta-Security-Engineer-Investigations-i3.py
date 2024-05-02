# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the left bar.

# Enjoy your interview!

# QUESTION - Given an escaped/defanged IPv4 Address, write a function to make it live again.

# Test-Case 1: 
  # Input - 3 different types of defanged IPs
  # Output - 3 different fanged/live IPs

def defang(input_ip):
    ip = "192/.168/.10/.20"
    ip2 = "192.168[.]0.5"
    ip3 = "192.168\.0.5"
    
    list1 = []

    for i in input_ip:
        if i.isdigit() or i == ".":
            list1.append(i)
    
    defanged_IP = ''.join(list1)
    return final


# Test-Case 2: 
  # +999.03.101.123 → IPs Out of range OR Invalid IPs should be returned as False / None / nothing / exception

    valid_IP = defanged_IP.split('.')
    for j in range(len(valid_IP)):
        if j == 0 and valid_IP[j] == 0:
            return False 
        elif valid_IP[j]>=0 and valid_IP[j] <= 255:
            continue
        else:
            return False


# Test-Case 3: 
  # 1.2.3.4.5.6.7 → IPs containing more than 3 periods OR Invalid IPs should be returned False / None / nothing / exception

    test_str2 = output_str.split('') # [1, '.', 2]
    counter = 0
    for k in range(len(test_str2)):
        if k.isdigit() == False:
            if test_str2[k] =='.':
                counter += 1
    
    if counter > 3:
        return output_str
    else:
        return False
