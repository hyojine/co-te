# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        sign=1
        # sign=-1 if s and s[0]=='-' else 1
        if s and s[0] in '-+':
            if s[0]=='-':
                sign=-1
            s=s[1:]
        for i in range(len(s)):
            if not s[i].isdigit():
                s=s[:i]
                break
        if s:
            s=int(s)*sign
            if -2**31<=s<2**31:
                return s
            elif -2**31>s:
                return -2**31
            else: return 2**31-1
        else:
            return 0
