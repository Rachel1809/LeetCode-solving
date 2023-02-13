class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = -1
        d = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        for i in num1, num2:
            tmp = 0
            for j in i:
                tmp = d[j] + tmp * 10
                
            if res == -1:
                res = tmp
            else:
                res *= tmp
            
        return str(res)
                
                
                