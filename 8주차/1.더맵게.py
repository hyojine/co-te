# 정렬
# 새로운 음식 스코빌지수 = 배열의 크기가 하나 줄어든다는 건가
# 삭제 후 append해서 재정렬
# 리스트 자체 정렬이 sort였나 sorted였나
# 1.정렬해서 k보다 작은 값이 있는지 확인하고
# 2.앞에꺼 두개 슬라이스해서 식에 넣고 재정렬해서 1반복
# 3.k보다 작은 값이 없으면 횟수 리턴하고
# 4.있으면 재정렬해서 1번 반복
# 길이가 2일때까지만 가능 -> 1일때도 k보다 작으면 -1리턴

# def solution(scoville, K):
#     count =0
#     for i in scoville:
#         scov=[v for idx,v in enumerate(scoville) if v<K]
#         if scov != []:
#             scoville.sort(reverse=True)
#             nscov=scoville[-1]+scoville[-2:][1]*2
#             del scoville[-2:]
#             scoville.append(nscov)
#             count+=1
#         if len(scoville)==1 and scoville[0]<K:
#             return -1
#     return count

# 효율성 테스트 통과 못함
# def solution(scoville, K):
#     count =0
#     for _ in range(len(scoville)):
#         scov=[v for v in scoville if v<K]
#         if scov != []:
#             scoville.sort()
#             print('scoville:',scoville)
#             nscov=scoville[0]+scoville[1]*2
#             scoville.append(nscov)
#             del scoville[:2]
#             print('new scoville:',scoville)
#             count+=1
#         else:
#             return count
#         if len(scoville)==1 and scoville[0]<K:
#             return -1
#     return count

# a=[1,2,4,5,633,52,0,3]

# 슬라이싱
# 리스트, 튜플, 문자열은 슬라이싱 가능
# print(a[-1:]) # 맨 마지막거
# print(a[-2:]) # 맨 마지막에서 두개
# print(a[0:])
# print(a[:2])

# 정렬
# a.sort()
# print(sorted(a)) a에 다시 저장 안됨
# print(a)

# heapq 모듈 사용
from heapq import heapify,heappop,heappush

def solution(scoville, K):
    count=0
    heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        min1=heappop(scoville)
        min2=heappop(scoville)
        new=min1+min2*2
        heappush(scoville,new)
        count+=1
        
    return count

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([1],7))