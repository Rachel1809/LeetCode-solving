class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        sign = 0
        sign += dividend < 0
        sign += divisor < 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        q = len(range(0, dividend-divisor+1, divisor))
        
        if sign == 2 or sign == 0:
            return min(q, 2**31 - 1)
        return max(-q, -2**31)
            
            