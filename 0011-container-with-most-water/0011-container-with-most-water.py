class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height) - 1
        while j >= i:
            maxArea = max(maxArea, (j-i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxArea