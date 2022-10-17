class Solution:
    def isValid(self, s: str) -> bool:
        tmpDict = {
            "}": "{",
            ")": "(",
            "]": "["
        } 
        stack = []
        for i in s:
            if i in tmpDict:
                if stack != [] and tmpDict[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)
        
        return stack == []
            