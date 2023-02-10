from itertools import combinations

def solution(numbers):
    ans=[]
    all=list(combinations(numbers,2))
    for a in all:
        ans.append(sum(a))
    return sorted(list(set(ans)))

from itertools import combinations

def solution(numbers):
    return sorted(list(set([sum(x) for x in list(combinations(numbers,2))])))