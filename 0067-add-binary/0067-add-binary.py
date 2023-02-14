class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        odd = 0
        while i >= 0 and j >= 0:
            res += str((odd + int(a[i]) + int(b[j])) % 2)
            odd = (odd + int(a[i]) + int(b[j])) // 2
            i -= 1
            j -= 1
        while i >= 0:
            res += str((odd + int(a[i])) % 2)
            odd = (odd + int(a[i])) // 2
            i -= 1
        while j >= 0:
            res += str((odd + int(b[j])) % 2)
            odd = (odd + int(b[j])) // 2
            j -= 1
        if odd > 0:
            res += "1"

        return res[::-1]
            
        
            
                
            
                
            
            