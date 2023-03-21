# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer=[]
    if len(s)==1:
        return 1
    for i in range(1, (len(s)//2)+1):
        word = ''
        cnt = 1
        temp=s[:i]
        for j in range(i, len(s), i):
            if temp==s[j:i+j]:
                cnt+=1
            else:
                if cnt>1:
                    word += str(cnt)
                word+=temp
                temp=s[j:j+i]
                cnt = 1
        if cnt>1:
            word += str(cnt)
        word += temp
        answer.append(len(word))
    return min(answer)