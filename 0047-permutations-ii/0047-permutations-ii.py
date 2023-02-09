class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permu(comb, counter, res):
            if len(comb) == len(nums):
                res.append(comb[:])
                return res
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    permu(comb + [num], counter, res)
                    counter[num] += 1
            return res

        return permu([], Counter(nums), [])
