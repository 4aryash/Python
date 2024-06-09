# To find the common elements between two sorted arrays with distinct numbers.
# Brute Force: O(n^2)
# Optimal: O(n)



a = [1,12,15,19,20,21]
b = [2,15,17,19,21,25,27]
c = []

######## O(n^2) using Two for loops
# for i in a:
#     for j in b:
#         if i == j and j not in c:
#             c.append(i)
#             print(c)
#             break
# print(c)


######## O(n) using Two pointers
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        c.append(a[i])
        i += 1
        j += 1
    
    elif a[i] < b[j]:
        i += 1
    
    else:
        j += 1
print(c)
