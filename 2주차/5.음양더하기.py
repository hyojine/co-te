def solution(absolutes, signs):
    answer=0
    for abs,sign in zip(absolutes,signs):
        if sign == False:
            abs=abs*(-1)
        answer+=abs
    return answer