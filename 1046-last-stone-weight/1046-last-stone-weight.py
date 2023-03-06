class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-s for s in stones]
        
        heapify(st)
        
        while len(st) > 1:
            heappush(st, heappop(st) - heappop(st))
            
        return -st[0]