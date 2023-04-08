class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def F(n):
            if n <= 3:
                return n
            return F(n-1) + F(n-2)
        return F(n)