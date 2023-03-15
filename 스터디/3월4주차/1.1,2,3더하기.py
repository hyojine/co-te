# https://www.acmicpc.net/problem/9095
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수

# 1을 만드는 방법 - 1가지
# 1

# 2를 만드는 방법 - 2가지
# 1+1, 2

# 3을 만드는 방법 - 4가지
# 1+1+1, 1+2, 2+1, 3

# 4를 만드는 방법 - 7가지
# 1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2, 3+1, 1+3

# 5를 만드는 방법 - 13가지
# 1+1+1+1+1, 1+1+1+2(4자리니까 4가지), 1+1+3(3가지), 2+2+1(3가지), 3+2(2가지)

import sys

T=int(input())
for t in range(T):
    n=int(sys.stdin.readline())
    dp = [0]*(n+1) 
    for i in range(1,len(dp)):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
        if i<4: 
            print(i)
            dp[i]+=1 
    print(dp[n])

# 재귀로
def solution(x):
    answer=0
    if x==1:
       return answer+1
    elif x==2:
        return answer+2
    elif x==3:
        return answer+4
    return solution(x-3)+solution(x-2)+solution(x-1)

T=int(input())
for _ in range(T):
    n=int(input())
    print(solution(n))

# 다른 재귀로
def solution(sum,n):
    if sum>n:
        return 0
    elif sum == n: # 성공
        return 1
    curr =0
    for i in range(1,4):
        curr+=solution(sum+i,n)
    return curr

T=int(input())
for _ in range(T):
    n=int(input())
    print(solution(0,n))