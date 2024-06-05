class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charmap = { ")":"(", "]":"[", "}":"{" }

        for char in s:
            if char in charmap:
                if stack and stack[-1] == charmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
