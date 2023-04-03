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

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        ans=str(x)[::-1]
        if ans[0]=='0':
            ans=ans[1:]
        if ans[-1]=='-':
            ans='-'+ans[:-1]
        ans=int(ans)
        return ans if -2**31<=ans<2**31 else 0