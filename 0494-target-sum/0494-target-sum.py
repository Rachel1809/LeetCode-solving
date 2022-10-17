class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = {}
        def dp(index, current):
            if index == n:
                return int(current == target)
            
            if (index, current) in mem:
                return mem[(index, current)]
            
            mem[(index, current)] = dp(index+1, current + nums[index]) + dp(index + 1, current - nums[index])
            
            return mem[(index, current)]
                    
        return dp(0, 0)