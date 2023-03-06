class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums
        heapify(self.pq)
        for _ in range(len(nums) - k):
            heappop(self.pq)

    def add(self, val):
        heappush(self.pq, val)
        if len(self.pq) > self.k: 
            heappop(self.pq)
        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)