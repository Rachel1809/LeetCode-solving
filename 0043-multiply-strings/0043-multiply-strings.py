class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = -1
        for i in num1, num2:
            tmp = 0
            for j in range(len(i)):
                tmp = (ord(i[j]) - 48) + tmp * 10
                
            if res == -1:
                res = tmp
            else:
                res *= tmp
            
        return str(res)
                
                
                