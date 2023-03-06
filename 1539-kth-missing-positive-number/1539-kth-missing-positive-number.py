class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 1
        i, j = 0, 1
        res = 0
        
        while prev < arr[-1]:
            if j <= k:
                if prev != arr[i]:
                    j += 1
                    res = prev
                else:
                    i += 1
                prev += 1
            else:
                break            

                
        return res if j > k else arr[-1] + (k - j + 1)