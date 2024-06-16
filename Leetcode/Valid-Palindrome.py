class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        result = ''
        for i in s:
            if i.isalnum():
                stack.append(i.lower())

        temp = stack
        stack = stack[::-1]
        result = ''.join(stack)
        return (temp == stack)
