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
                if stack != [] and tmpDict[i] == stack[0]:
                    stack.pop(0)
                else:
                    return False
            else:
                stack.insert(0, i)
        
        return stack == []
            