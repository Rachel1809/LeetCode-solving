class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low + 1 if low%2 == 0 else low
        return len(range(low, high + 1, 2)) 
        