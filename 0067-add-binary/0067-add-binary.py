class Solution:
    def addBinary(self, a: str, b: str) -> str:        
        tmp = int(a) + int(b)
        
        if tmp == 0:
            return "0"
        
        odd, res = 0, ""

        while (tmp > 0):
            res += str(((tmp % 10) + odd) % 2)
            odd = ((tmp % 10) + odd) // 2
            tmp //= 10
            
        if odd > 0:
            res += str(odd)
            
        return res[::-1]
            
        
            
                
            
                
            
            