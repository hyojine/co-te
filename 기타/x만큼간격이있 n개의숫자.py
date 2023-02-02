def solution(x, n):
    ans=[]
    y=x
    while len(ans) != n:
        ans.append(y)
        y+=x
    return ans