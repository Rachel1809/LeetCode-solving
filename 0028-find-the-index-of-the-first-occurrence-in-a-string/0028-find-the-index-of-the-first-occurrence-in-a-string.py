class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        for i in range(n):
            j = 0
            tmp = i
            while tmp < n and haystack[tmp] == needle[j]:
                if j == len(needle) - 1:
                    return i
                tmp += 1
                j += 1
        return -1