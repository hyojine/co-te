from itertools import combinations

def solution(numbers):
    ans=[]
    all=list(combinations(numbers,2))
    for a in all:
        ans.append(sum(a))
    return sorted(list(set(ans)))