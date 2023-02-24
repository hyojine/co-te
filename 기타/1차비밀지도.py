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

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=list(a12)
        for x in range(n):
            if a12[x]=='1':
                a12[x]='#'
            else: 
                a12[x]=' '
        answer.append(''.join(a12))
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(a12)
    return answer

# 람다식
solution = lambda n, arr1, arr2 : [bin(arr1[r]|arr2[r])[2:].rjust(n,'0').replace('1','#').replace('0',' ') for r in range(n)]

# 정규식
import re

def solution(n, arr1, arr2):
    answer = ["#"]*n # 길이의 배열을 먼저 만들어두고
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer

