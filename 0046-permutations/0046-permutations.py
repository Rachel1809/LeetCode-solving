class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        res = []

        def permu(remain, idx, tmp, res):
            if idx == n:
                res.append(tmp[:])
                return
            for i in range(len(remain)):
                cur = remain.pop(i)
                tmp.append(cur)
                permu(remain, idx+1, tmp, res)
                tmp.pop(-1)
                remain.insert(i, cur)
            return

        permu(nums, 0, [], res)
        return res