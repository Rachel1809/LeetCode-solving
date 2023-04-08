class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        current_solution = []
        ans = []
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def choose(i):
            if i == len(digits):
                ans.append("".join(current_solution))
                return
            
            for next_char in digits_map[digits[i]]:
                current_solution.append(next_char)
                choose(i+1)
                current_solution.pop()
                           
        choose(0)
        return ans