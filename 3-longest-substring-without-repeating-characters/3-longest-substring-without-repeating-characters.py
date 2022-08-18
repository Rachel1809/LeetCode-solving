class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        already = []
        maxCount = 0
        for i in range(len(s)):
            if (s[i] not in already):
                already.append(s[i])
                maxCount = max(len(already), maxCount)

            else:
                j = already.index(s[i])
                already = already[j+1:]
                already.append(s[i])

        return maxCount