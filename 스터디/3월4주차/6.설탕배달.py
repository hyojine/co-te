# https://www.acmicpc.net/problem/2839
# N킬로그램을 배달시 배달해야하는 봉지의 최소 개수
# 3킬로그램 봉지와 5킬로그램 봉지
# N은 3kg 이상 5000kg 이하

def solution(n):
    if n%5 ==0:
        return n//5
    elif n%5 in (1,3):
        return n//5+1
    elif n%5 in (2,4):
        if n in (4,7):
            return -1
        return n//5+2

N=int(input())
print(solution(N))

#2
def solution(n):
    cnt = 0
    while n >= 0:
        if n % 5 == 0:
            cnt += n // 5
            return cnt
        n -= 3
        cnt += 1
    return -1

n=int(input())
print(solution(n))
