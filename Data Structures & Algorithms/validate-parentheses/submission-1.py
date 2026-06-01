class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #we are able to store all of our open brackets
        correctBrackets = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in correctBrackets:
                if stack and stack[-1] == correctBrackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        

        if len(stack) == 0:
            return True
        else:
            return False
        