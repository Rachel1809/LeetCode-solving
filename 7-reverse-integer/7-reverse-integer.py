class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        y = 0
        x = abs(x)
        
        while (x > 0):
            y = y*10 + x%10
            x //= 10
        if y >= 0x7fffffff:
            return 0  
        return y*sign