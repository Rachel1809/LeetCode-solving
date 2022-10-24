class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, c in enumerate(nums):
            if i > 0 and c == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while (l < r):
                total = c + nums[l] + nums[r]
                if total == 0:
                    res.append([c, nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                elif total > 0:
                    r = r - 1
                else:
                    l = l + 1
                    
        return res