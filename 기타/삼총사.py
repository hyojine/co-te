from itertools import combinations

def solution(number):
    count=0
    for a,b,c in combinations(number,3):
    # for combination in combinations(number,3):
        if a+b+c ==0:
        # if sum(combination)==0:
            count+=1
    return count