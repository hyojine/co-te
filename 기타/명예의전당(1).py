def solution(k, score):
    ans=[]
    if len(score)>=k:
        for i in range(len(score)):
            if i>=k:
                ans.append(sorted(score[:i+1],reverse=True)[k-1])
            else:
                ans.append(sorted(score[:i+1],reverse=True)[i])
    else:
        for i in range(len(score)):
            ans.append(sorted(score[:i+1],reverse=True)[i])
    return ans