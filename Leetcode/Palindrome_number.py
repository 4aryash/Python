class Solution(object):
    def isPalindrome(self, x):

        strin = str(x)
        rev_strin = strin[::-1]

        if strin == rev_strin:
            answer = True
        else:
            answer = False
        
        return answer
#runtime 50ms

#Optmized solution
if x<0:
  return False
return str(x) == str(x)[::-1]
#runtime 45ms
