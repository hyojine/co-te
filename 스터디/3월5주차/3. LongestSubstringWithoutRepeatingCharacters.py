# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        ans=0
        for ss in s:
            if ss not in stack:
                stack.append(ss)
                if len(stack)>ans:    
                    ans=len(stack)
            else:
                idx=stack.index(ss)
                stack=stack[idx+1:]
                stack.append(ss)
        return ans
                    