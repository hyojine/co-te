# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    distance=0
    left_d=0
    left_p=0
    for i in range(1,n+1):
        left_d+=deliveries[-i]
        left_p+=pickups[-i]
        while left_d>0 or left_p>0:
            left_d-=cap
            left_p-=cap
            distance+=(n+1-i)*2
    return distance