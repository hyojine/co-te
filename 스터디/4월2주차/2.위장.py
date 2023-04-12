# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic={}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]].append(c[0])
        else:
            dic[c[1]]=[c[0]]
    for d in dic:
        dic[d]=len(dic[d])
    l=1
    for d in dic.values():
        l*=(d+1)
    return l-1

