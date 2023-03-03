def solution(lottos, win_nums):
    pos_nums=set(win_nums)-set(lottos)
    inter_nums=set(win_nums)&set(lottos)
    zero_cnt=lottos.count(0)
    if zero_cnt>=len(pos_nums):
        highest=len(inter_nums)+len(pos_nums)
        lowest=len(inter_nums)
    else:
        highest=len(inter_nums)+zero_cnt
        lowest=len(inter_nums)
    if highest==0:
        lowest,highest=1,1
    elif lowest==0:
        lowest=1
    return [6-highest+1,6-lowest+1]