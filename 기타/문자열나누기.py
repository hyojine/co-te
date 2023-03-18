# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    cnt=0
    dif,same=0,1
    stack=[s[0]]
    while len(s)>1 and same<len(s):
        if stack[-1]!=s[same+dif]:
            dif+=1
        else:
            same+=1
        if dif==same:
            cnt+=1
            s=s[same*2:]
            if s:
                stack.append(s[0])
            # else:
            #     return cnt # break
            dif,same=0,1
    if len(s)>=1:
        cnt+=1
    return cnt
