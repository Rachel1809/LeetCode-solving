class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        odd = 1
        i = len(digits) - 1
        while odd > 0:
            if i < 0:
                digits.insert(0, odd)
                break
            tmp = digits[i]
            digits[i] = (tmp + odd) % 10
            odd = (tmp + odd) // 10
            i -= 1

            
        return digits
                