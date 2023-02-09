class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb[:])
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb + [num], counter)
                    # revert the choice for the next exploration
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results