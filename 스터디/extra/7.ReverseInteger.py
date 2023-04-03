# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            x*=(-1)
            flag=True
        rev=0    
        while x:
            rev=rev*10+x%10
            x//=10
        if flag:
            rev*=(-1)
        return rev if (rev <2**31 and rev>=-2**31) else 0