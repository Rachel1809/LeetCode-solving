class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        q = len(range(0, dividend-divisor+1, divisor))
        
        return max(-q, -2**31) if sign else min(q, 2**31 - 1) 
            
            