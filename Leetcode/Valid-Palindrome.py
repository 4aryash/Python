class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stack = []
        # result = ''
        # for i in s:
        #     if i.isalnum():
        #         stack.append(i.lower())

        # temp = stack
        # stack = stack[::-1]
        # result = ''.join(stack)
        # return (temp == stack)

        ### Using 2 pointers
        stack = []
        for i in s:
            if i.isalnum():
                stack.append(i.lower())
        left, right = 0, len(stack) - 1
        while left <= right:
            if stack[left] == stack[right]:
                left += 1
                right -= 1
                if left == right:
                    break
            else:
                return False
        return True
                
