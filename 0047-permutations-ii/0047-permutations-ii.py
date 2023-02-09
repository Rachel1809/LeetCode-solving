class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def permu(remain, tmp, res):
            if not remain:
                res.add(tuple(tmp))
            else:
                for i in range(len(remain)):
                    permu(remain[:i] + remain[i+1:], tmp + [remain[i]], res)
            return list(res)
        return permu(nums, [], res)