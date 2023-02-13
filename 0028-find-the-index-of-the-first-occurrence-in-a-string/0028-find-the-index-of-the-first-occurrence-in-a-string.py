class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        check = False
        for i in range(n):
            j = 0
            init = i
            tmp = init
            while tmp < n and haystack[tmp] == needle[j]:
                if j == len(needle) - 1:
                    return init
                tmp += 1
                j += 1
        return -1