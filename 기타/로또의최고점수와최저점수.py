def solution(lottos, win_nums):
    inter_nums=set(win_nums)&set(lottos)
    zero_cnt=lottos.count(0)
    lowest=len(inter_nums)
    highest=lowest+zero_cnt
    if highest==0:
        lowest,highest=1,1
    elif lowest==0:
        lowest=1
    return [6-highest+1,6-lowest+1]
