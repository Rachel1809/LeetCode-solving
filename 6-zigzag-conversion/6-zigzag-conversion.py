class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows >= len(s) or numRows == 1):
            return s
        res = ""
        target = 2 * (numRows - 1)
        for i in range(numRows):
            res += s[i]
            j = i

            if (i == 0 or i == numRows-1):
                j += target
                while(j < len(s)):
                    res += s[j]
                    j += target
            else:
                for k in range(j+2, len(s)):
                    if (j + k) % target == 0:
                        res += s[k]
                        j = k
        return res
        