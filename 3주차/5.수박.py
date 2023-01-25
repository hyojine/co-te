def solution(n):
    s=''
    for i in range(n):
        if i%2==0:
            s+='수'
        else:
            s+='박'
    return s
print(solution(3))