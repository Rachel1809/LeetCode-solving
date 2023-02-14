class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        odd = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                odd += int(a[i])
            if j >= 0:
                odd += int(b[j])
            res += str(odd % 2)
            odd //= 2
            i -= 1
            j -= 1
        if odd > 0:
            res += "1"

        return res[::-1]
            
        
            
                
            
                
            
            