class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-s for s in stones]
        heapify(st)
        while len(st) > 1:
            first = heappop(st)
            second = heappop(st)
            heappush(st, first - second)
            
        return -st[0]