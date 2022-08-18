class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        new_arr = Counter(arr)
        freq = sorted(new_arr.values(), reverse=True)
        res = 0
        half_len = len(arr) // 2
        while (half_len > 0):
            half_len -= freq[res]
            res += 1
        return res