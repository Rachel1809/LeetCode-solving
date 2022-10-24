class Solution:
    def isNumber(self, s: str) -> bool:
        num, sign, exp, dec = False, False, False, False

        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                num = True

            elif s[i] in '+-':
                if num or sign or dec:
                    return False
                else:
                    sign = True

            elif s[i] in 'eE':
                if not num or exp:
                    return False
                else:
                    exp = True
                    sign, num, dec = False, False , False

            elif s[i] == '.':
                if dec or exp:
                    return False
                else:
                    dec = True

            else:
                return False

        return num