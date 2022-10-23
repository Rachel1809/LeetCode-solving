class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        store = {}
        
        def dfs(i,j):
            if (i,j) in store:
                return store[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            match = i < len(s) and ((s[i] == p[j]) or (p[j] == '.'))
            
            if j + 1 < len(p) and p[j+1] == '*':
                store[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))
                return store[(i,j)]
            
            if match:
                store[(i,j)] = dfs(i+1,j+1) 
                return store[(i,j)]
            
            return False
        
        return dfs(0,0)
                      
                