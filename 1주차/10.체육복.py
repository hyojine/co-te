# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    res=list(set(reserve)-set(lost))
    los=list(set(lost)-set(reserve))
    for r in res:
        if r-1 in los:
            los.remove(r-1)
        elif r+1 in los:
            los.remove(r+1)
    return n-len(los)