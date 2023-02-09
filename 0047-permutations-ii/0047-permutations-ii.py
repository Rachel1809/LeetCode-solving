class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb, counter, res):
            if len(comb) == len(nums):
                res.append(comb[:])
            else:
                for num in counter:
                    if counter[num] > 0:
                        # add this number into the current combination
                        counter[num] -= 1
                        # continue the exploration
                        backtrack(comb + [num], counter, res)
                        # revert the choice for the next exploration
                        counter[num] += 1
            return res

        return backtrack([], Counter(nums), [])
