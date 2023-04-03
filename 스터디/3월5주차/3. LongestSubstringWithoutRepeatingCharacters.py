class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=[]
        ans=0
        if len(s)==1:
            return 1
        for ss in s:
            if ss not in answer:
                answer.append(ss)
                if len(answer)>ans:    
                    ans=len(answer)
            else:
                if answer and answer[0]==ss:
                    if len(answer)>ans:
                        ans=len(answer)
                    answer.pop(0)
                else:
                    idx=answer.index(ss)
                    answer=answer[idx+1:]
                answer.append(ss)
        return ans
                    