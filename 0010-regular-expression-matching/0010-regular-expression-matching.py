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
                store[(i,j)] = (match and dfs(i+1,j)) or dfs(i,j+2)
                return store[(i,j)]
            
            if match:
                store[(i,j)] = dfs(i+1,j+1) 
            else:
                store[(i, j)] = False
                
            return store[(i,j)]

        
        return dfs(0,0)
                      
                