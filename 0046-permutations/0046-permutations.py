class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        def permu(remain, tmp, res):
            if not remain:
                res.append(tmp[:])
            else:
                for i in range(len(remain)):
                    permu(remain[:i] + remain[i+1:], tmp + [remain[i]], res)
            return res

        return permu(nums, [], [])
