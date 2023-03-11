# https://school.programmers.co.kr/learn/courses/30/lessons/72411

# 단품메뉴들을 코스요리 메뉴로 구성하기
# 최소 2가지 이상의 단품메뉴 **조합**
# 단품메뉴는 2명 이상 주문해야 코스메뉴 후보

# 각 손님은 단품메뉴를 2개 이상 주문
# 단품메뉴는 A ~ Z의 알파벳 대문자

# 코스마다 따로 저장하는 게 좋을듯

from itertools import combinations
from collections import Counter

def solution(orders, course):
    course_combi={}
    for c in course:
        temp=[]
        for order in orders:
            if len(order)>=c:
                order=''.join(sorted(order))
                temp.extend(list(combinations(order, c)))
        course_combi[c]=temp

    combi_freq=[]
    for k in course_combi.keys():
        combi_freq.append(dict(Counter(course_combi[k])))
     
    answer=[]
    for k in combi_freq:
        for kk in k.keys():
            if k[kk]==max(list(k.values())) and k[kk]>=2:
                answer.append(''.join(kk))
    answer.sort()
    return answer