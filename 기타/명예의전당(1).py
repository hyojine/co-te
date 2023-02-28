def solution(k, score):
    ans=[]
    for i in range(len(score)):
        if i>=k:
            ans.append(sorted(score[:i+1],reverse=True)[k-1])
        else:
            ans.append(sorted(score[:i+1],reverse=True)[i])
    return ans

def solution(k, score):
    return [sorted(score[:i+1],reverse=True)[k-1] if i>=k else sorted(score[:i+1],reverse=True)[i] for i in range(len(score)) ]