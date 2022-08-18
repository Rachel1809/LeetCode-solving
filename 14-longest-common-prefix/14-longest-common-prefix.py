class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        indexLetter = 0
        res = ""
        minLen = len(min(strs, key = len))
        while (indexLetter < minLen):
            tmp = strs[0][indexLetter]
            for stringIndex in range(1, len(strs)):
                if strs[stringIndex][indexLetter] != tmp:
                    return res
            res += tmp
            indexLetter += 1
        return res
            