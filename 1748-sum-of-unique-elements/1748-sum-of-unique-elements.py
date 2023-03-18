class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict_num = Counter(nums)
        res = 0
        #for i in nums:
        #    if dict_num[i] == 1:
        #        res += i
        
        for i, j in dict_num.items():
            if j == 1:
                res += i
        
        return res