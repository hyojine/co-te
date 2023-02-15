def solution(n):
    rev=[]
    x=n
    count=0
    ans=0
    while x>=3:
        x=x//3
        count+=1
    for c in range(count,-1,-1):
        if n>=(3**c)*2:
            n=n-(3**c)*2
            rev.append(2)
        elif n>=(3**c):
            n=n-(3**c)*1
            rev.append(1)
        else:
            rev.append(0)
    for idx,r in enumerate(reversed(rev)):
        ans+=(3**(count-idx))*r
    return ans
