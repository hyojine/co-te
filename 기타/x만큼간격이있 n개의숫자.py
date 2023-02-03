def solution(x, n):
    ans=[]
    y=x
    while len(ans) != n:
        ans.append(y)
        y+=x
    return ans

def solution(x, n):
    return [x+(i)*x for i in range(n)]
    # return [(i+1)*x for i in range(n)]
    # i = 0~ n-1

def solution(x, n):
    return [x*i for i in range(1,n+1)]
    # i = 1~ n

def solution(x, n):
    if x==0:
        return [0]*n
    return list(range(x, x*(n+1), x))
    # range(start, end, gap)