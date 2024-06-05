# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

### Above code is O(n^2) time complexity.

### Below code is O(n) time complexity.
class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {}

        # for i in range(0, len(nums)):
        #     x = target - i
        #     hashmap[nums[i]] = i
            
        #     if x in hashmap:
        #         index1 = hashmap.get(i)
        #         index2 = hashmap.get(x)
                
        #         index_final = []
        #         index_final.append(index1)
        #         index_final.append(index2)
                
        #         return index_final
        for i, n in enumerate(nums):
	        x = target - n
	
	        if x in hashmap:
		    return [hashmap[x], i]
	
	        hashmap[n] = i
        return
