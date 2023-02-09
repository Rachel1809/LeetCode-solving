class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def permu(remain, idx, tmp, res):
          if idx == n:
            res.append(tmp[:])
            return res
          for i in range(len(remain)):
            cur = remain.pop(i)
            tmp.append(cur)
            res = permu(remain, idx+1, tmp, res)
            tmp.pop(-1)
            remain.insert(i, cur)
          return res

        res = permu(nums, 0, [], [])
        return res