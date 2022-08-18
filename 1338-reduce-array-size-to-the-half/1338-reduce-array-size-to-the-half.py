class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = sorted(Counter(arr).values(), reverse=True)
        res = 0
        half_len = len(arr) // 2
        while (half_len > 0):
            half_len -= freq[res]
            res += 1
        return res
        