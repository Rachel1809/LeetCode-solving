class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        count = 1
        for i in range(1, n):
            if nums[i-1] != nums[i]:
                nums[count] = nums[i]
                count += 1
                
        nums = nums[:count+1]
        return count