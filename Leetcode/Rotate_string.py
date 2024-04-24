# s = "abcde"
# goal = "cdeab"

# list1 = list(s)
# list2 = list(goal)

# for i in range(1, len(list1)-1):
# 	test_list = list1[i:] + list1[:i]
#   print(test_list)
# 	if test_list == list2:
# 		print(True)
# 	else:
# 		print(False)


# print(list1)
# print(list2)
# print(test_list)

#leetcode answer
#This defines a class named Solution with a method called rotateString. This method takes two arguments, s and goal, which are both strings.
class Solution(object):
    def rotateString(self, s, goal):

      #list1 and list2 convert the input strings s and goal into lists of characters. This conversion is done to facilitate operations that will manipulate the order of elements (characters) more conveniently.
      #answer is initialized to False. This variable will be used to store the final result indicating whether s can be rotated to become goal.
        list1 = list(s)
        list2 = list(goal)
        answer = False

      #This loop iterates through all possible starting indices for shifts, effectively testing all possible rotations of string s. The index i represents the number of places the string s will be rotated.
        for i in range(0, len(list1)):
          #This line generates a new list temp_list which is a rotated version of list1. The list is sliced in two parts: 
          # list1[i:]: This slice takes the portion of list1 from index i to the end.
          # list1[:i]: This slice takes the portion of list1 from the start up to index i (not including i).

            temp_list = list1[i:] + list1[:i]
          #iteration 0 (i=0) - list[0:] = [a,b,c,d,e] + list[:0] = [] => [a,b,c,d,e]
          #iteration 1 (i=1) - list[1:] = [b,c,d,e] + list[:1] = [a] => [b,c,d,e] + [a] =>> [b,c,d,e,a]
          #iteration 2 (i=2) - list[2:] = [c,d,e] + list[:2] = [a,b] => [c,d,e] + [a,b] =>> [c,d,e,a,b] ---------- s == goal, here so loop breaks
            if temp_list == list2:
                answer = True
                break
            else:
                answer = False
                continue

        return answer
