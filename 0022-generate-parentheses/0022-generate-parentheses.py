class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        current_open, current_close = 0, 0
        
        ans = []
        
        cur_sol = []
        
        def choose(i):
            nonlocal current_open, current_close
            if i == 2*n:
                if current_open == current_close:
                    ans.append("".join(cur_sol))
                return
            
            # choose the closing parenthesis
            if current_open > current_close:
                cur_sol.append(")")
                current_close += 1
                choose(i+1)
                current_close -= 1
                cur_sol.pop()
                
            cur_sol.append("(")
            current_open += 1
            choose(i+1)
            current_open -= 1
            cur_sol.pop()
            
        choose(0)
        return ans