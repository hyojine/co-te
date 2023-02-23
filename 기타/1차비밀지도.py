def solution(n, arr1, arr2):
    answer=[]
    for a in arr1:
        new=[]
        for i in range(n-1,-1,-1): 
            if a>=2**(i):
                a=a-2**(i)
                new.append('1')
            else:
                new.append('0')
        answer.append(''.join(new))
    answer2=[]
    for a in arr2:
        new=[]
        for i in range(n-1,-1,-1): 
            if a>=2**(i):
                a=a-2**(i)
                new.append('1')
            else:
                new.append('0')
        answer2.append(''.join(new))
    real=[]
    for i,j in zip(answer,answer2):
        final=[]
        for x in range(n):
            if '1' in i[x] or '1' in j[x]:
                final.append('#')
            else:
                final.append(' ')
        real.append(''.join(final))
    return real