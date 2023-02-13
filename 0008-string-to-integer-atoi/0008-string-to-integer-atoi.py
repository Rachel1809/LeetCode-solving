class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        y = ''
        s = s.lstrip()
        n = len(s)

        for i in range(n):
            if (s[i].isdigit() == False):
                if (i == 0):
                    if (s[i] == '-'):
                        sign = -1
                        continue
                    if (s[i] == '+'):
                        continue
                break
            else:
                y += s[i]
        
        if (y == ''):
            return 0
        
        y = int(y)*sign
        y = max(y, -2**31)
        y = min(y, 2**31-1)
        return y
        