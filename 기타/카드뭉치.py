# goal에서의 순서랑 뭉치에서의 순서가 같으면 됨

def solution(cards1, cards2, goal):
    idx_list=[]
    for card in cards1:
        if card in goal:
            idx_list.append(goal.index(card))
            goal.remove(card)
    for i in range(len(idx_list)-1):
        if idx_list[i]>idx_list[i+1]:
            return "No"
    idx_list.clear()
    for card in cards2:
        if card in goal:
            idx_list.append(goal.index(card))
    for i in range(len(idx_list)-1):
        if idx_list[i]>idx_list[i+1]:
            return "No"
    return "Yes"