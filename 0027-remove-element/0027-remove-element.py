class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        s = nums.count(val)
        
        for i in range(s):
            nums.remove(val)
        
        return len(nums)