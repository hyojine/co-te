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

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        print('인덱스i:',i) #i=4일때 아래 for문이 실행이 안되고 에러도 안남
        for j in range(i+1, len(numbers)):
            print('인덱스: ',i,j)
            print('값: ',numbers[i], numbers[j])
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

numbers=[1,2,3,4,5]

for i in range(5,5):
    print(i) # 프린트 안됨

def solution2(numbers):
    answer = []
    for i in range(len(numbers)-1):
        print('인덱스i:',i) #i=3까지 전체 실행됨
        for j in range(i+1, len(numbers)):
            print('인덱스: ',i,j)
            print('값: ',numbers[i], numbers[j])
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
print(solution2(numbers))