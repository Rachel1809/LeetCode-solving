class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        slow, fast = n, n
        
        while True:
            slow = self.sumSquared(slow)
            fast = self.sumSquared(self.sumSquared(fast))
            if slow == fast:
                break
        return fast == 1
        
    def sumSquared(self, x):
        total = 0
        while x > 0:
            digits = x%10
            total += digits**2
            x //= 10
        return total
            