arr = [3,5,1,2]
print(arr)

#compare each element in the list one by one and swap it.
for i in range(len(arr)):
	for j in range(i+1, len(arr)):
		if arr[i] > arr[j]:
			arr[i], arr[j] = arr[j], arr[i]

print(arr)
