# 오름차순으로 정렬해서
# 작은거부터 계속 더하고 버짓 안넘을때까지 더하기
def solution(d, budget):
    d.sort()
    print(d)
    total=0
    for idx,dd in enumerate(d):
        total+=dd
        if total>budget:
            return idx
    return idx+1

d=[1,3,2,5,4]
budget=9
print(solution(d, budget))