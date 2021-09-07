class Solution:
    def isValid(self, s: str) -> bool:
        closing_braces = {")", "}", "]"}
        opening_braces = {")": "(", "}":"{", "]":"["}
        stack = []
        
        for i in s:
            if i in closing_braces:
                if len(stack) <= 0 or stack.pop() != opening_braces[i]:
                    return False
            else:
                stack.append(i)
        
        return True if len(stack) == 0 else False
