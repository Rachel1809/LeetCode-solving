class Solution:
    def isNumber(self, s: str) -> bool:
        num, sign, exp, dec = False, False, False, False

        for c in s:
            if '0' <= c <= '9':
                num = True

            elif c in '+-':
                if num or sign or dec:
                    return False
                else:
                    sign = True
                
            elif c in 'eE':
                if not num or exp:
                    return False
                else:
                    exp = True
                    sign = False
                    num = False
                    dec = False
            
            elif c == '.':
                if dec or exp:
                    return False
                else:
                    dec = True
                    
            else:
                return False
            
            
    
        return num