# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 횟수를 최소화
# 길이가 n미터인 벽을 1미터 길이의 구역 n개
# 롤러의 길이는 m
# 롤러의 길이가 어느만큼 수용할 수 있는지 쳌
def solution(n, m, section):
    cnt=0
    s=section[0]
    for i in range(len(section)):
        if section[i]-(s+m-1)>0:
            s=section[i]
            cnt+=1
    if section.index(s)<=len(section)-1:
        cnt+=1
    return cnt