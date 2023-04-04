# https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        ans=''
        roman={1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I',}
        for i,k in enumerate(roman.keys()):
            if num//k !=4:
                ans+=(num//k)*roman[k]
            else:
                if ans and ans[-1]==roman[list(roman.keys())[i-1]]:
                    ans=ans[:-1]
                    ans+=roman[k]+(roman[list(roman.keys())[i-2]])
                else:
                    ans+=roman[k]+(roman[list(roman.keys())[i-1]])
            num=num%k
        return ans