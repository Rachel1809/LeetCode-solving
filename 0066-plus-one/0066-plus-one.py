class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        odd = 1
        i = len(digits) - 1
        while i >= 0:
            tmp = digits[i]
            digits[i] = (tmp + odd) % 10
            odd = (tmp + odd) // 10
            if odd == 0:
                break
            i -= 1
            
        if odd > 0:
            digits.insert(0, odd)
        return digits
                