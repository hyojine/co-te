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

# ans의 마지막 값과 비교하는 조건문 추가
def solution(k, score):
    ans=[]
    for i in range(len(score)):
        if i>=k:
            if ans[-1]<score[i]:
                ans.append(sorted(score[:i+1],reverse=True)[k-1])
            else:
                ans.append(ans[-1])
        else:
            ans.append(sorted(score[:i+1],reverse=True)[i])
    return ans