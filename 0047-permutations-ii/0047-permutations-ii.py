class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permu(remain, tmp, res):
            if not remain and tmp not in res:
                res.append(tmp[:])
            else:
                for i in range(len(remain)):
                    permu(remain[:i] + remain[i+1:], tmp + [remain[i]], res)
            return res
        return permu(nums, [], res)