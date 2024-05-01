# Binary Search
nums = [-1,0,3,5,9,12]
target = 9

lp = 0
rp = len(nums) - 1
mid = len(nums)//2


while lp <= rp:
	mid = (lp + rp)//2

	# if target == mid then return mid
	if target == nums[mid]:
		print(mid)
		break

	# if target > mid then lp = mid, rp = rp, mid = (index of mid + rp)/2
	elif target > nums[mid]:
		lp = mid + 1

	# if target < mid then lp = lp, rp = mid, mid = (lp + index of mid)/2
	elif target < nums[mid]:
		rp = mid - 1
