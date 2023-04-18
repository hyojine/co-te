# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 시간초과
def solution(players, callings):
    for c in callings:
        p=players.index(c)
        players[p-1],players[p]=players[p],players[p-1]
    return players