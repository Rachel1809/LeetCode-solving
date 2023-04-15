class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        iLeft = self.select_left(nums, target)
        iLeft = bisect_left(nums, target)
        # bisect_left is built-in function that helps to find the lowest index greater than or equal
        # to target
        
        if iLeft == len(nums) or nums[iLeft] != target:
            return [-1, -1]
                
        # iRight = max(0, self.select_right(nums, target) - 1)
        iRight = bisect_right(nums, target) - 1
        
        return [iLeft, iRight]

    def select_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
    
    def select_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans