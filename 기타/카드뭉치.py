# goal에서의 순서랑 뭉치에서의 순서가 같으면 됨
def solution(cards1, cards2, goal):
    idx_list=[]
    for card in cards1:
        if card in goal:
            idx_list.append(goal.index(card))
            goal.remove(card)
    for i in range(len(idx_list)-1):
        if idx_list[i]>idx_list[i+1]: # 인덱스가 2이상 차이나도 됨
            return "No"
    idx_list.clear()
    for card in cards2:
        if card in goal:
            idx_list.append(goal.index(card))
    for i in range(len(idx_list)-1):
        if idx_list[i]>idx_list[i+1]: # 인덱스가 2이상 차이나도 됨
            return "No"
    return "Yes"

def solution(cards1, cards2, goal):
    i,j=0,0
    for card in goal:
        if card in cards1[i:]: # 인덱스가 2이상 차이나도 됨
            i=cards1.index(card)+1
        elif card in cards2[j:]: # 인덱스가 2이상 차이나도 됨
            j=cards2.index(card)+1
        else:
            return "No"
    return "Yes"

# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다. == 무조건 인덱스가 1씩만 차이나야함
def solution(cards1, cards2, goal):
    i,j=0,0
    for card in goal:
        if card in cards1:
            if cards1.index(card)==i:
                i+=1
            else:
                return "No"
        elif card in cards2:
            if cards2.index(card)==j:
                j+=1
            else:
                return "No"    
        else:
            return "No"
    return "Yes"