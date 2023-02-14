class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea, i, j = 0, 0, len(height) - 1
        while j > i:
            maxArea = max(maxArea, (j-i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxArea