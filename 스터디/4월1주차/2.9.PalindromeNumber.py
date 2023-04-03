# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[::-1]:
            return True

# Follow up: Solve it without converting the integer to a string.     
class Solution:
    def isPalindrome(self, x: int) -> bool:        
        if x<0:
            return False
        ans=0
        org=x
        while x:
            ans=ans*10+x%10
            x=x//10
        return org==ans