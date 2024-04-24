class Solution(object):
    def reverseWords(self, s):
        
        #trimming all the extra spaces from the input s
        trimmed_s = ' '.join(s.split())

        #storing the trimmed_s string into a new list and then reversing it
        x = trimmed_s.split(' ')[::-1]

        #converting the final list back to a string
        y = ' '.join(x)

        return y
