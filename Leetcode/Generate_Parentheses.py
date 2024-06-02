class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ### only add open if open < n
        ### only add close if close < open
        ### valid iff open == close == n

        temp_stack = []
        final_string = []

        def backtracking(openP, closeP):
            if openP == closeP == n:
                final_string.append("".join(temp_stack))
                return
            
            if openP < n:
                temp_stack.append("(")
                backtracking(openP + 1, closeP)
                temp_stack.pop()
            
            if closeP < openP:
                temp_stack.append(")")
                backtracking(openP, closeP + 1)
                temp_stack.pop()
            
        backtracking(0,0)
        return final_string
