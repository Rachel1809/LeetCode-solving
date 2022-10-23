class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        store = {}
        m, n = len(s), len(p)
        
        def dfs(i,j):
            if (i,j) in store:
                return store[(i,j)]
            
            if j >= n:
                return i >= m
            
            match = i < m and (s[i] == p[j] or p[j] == '.')
            
            if j < n - 1 and p[j+1] == '*':
                store[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))
                return store[(i,j)]
            
            if match:
                store[(i,j)] = dfs(i+1,j+1) 
                return store[(i,j)]
            
            store[(i, j)] = False
            return False
        
        return dfs(0,0)
                      
                