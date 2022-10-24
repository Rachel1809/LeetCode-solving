class Solution:
    def isNumber(self, s: str) -> bool:
        num, sign, exp, dec = False, False, False, False

        for char in s:
            if '0' <= char <= '9':
                num = True

            elif char in '+-':
                if num or sign or dec:
                    return False
                else:
                    sign = True

            elif char in 'eE':
                if not num or exp:
                    return False
                else:
                    exp = True
                    sign, num, dec = False, False , False

            elif char == '.':
                if dec or exp:
                    return False
                else:
                    dec = True

            else:
                return False

        return num