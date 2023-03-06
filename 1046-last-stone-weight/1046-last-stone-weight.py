class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones[:] = [-s for s in stones]
        
        heapify(stones)
        
        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            heappush(stones, first - second)
            
        return -stones[0]