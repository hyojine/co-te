def solution(k, score):
    ans=[]
    if len(score)>=k:
        for i in range(len(score)):
            if len(score[:i+1])>=k:
                ans.append(sorted(score[:i+1],reverse=True)[k])
            else:
                ans.append(sorted(score[:i+1],reverse=True)[i])        
    return ans