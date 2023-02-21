class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid % 2 == 0 and nums[mid] == nums[mid-1]) or (mid%2 != 0 and nums[mid] == nums[mid+1]):
                high = mid - 1 
                
            else:
                low = mid + 1
                
        return nums[low-1]