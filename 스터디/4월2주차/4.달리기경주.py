# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 시간초과
def solution(players, callings):
    for c in callings:
        p=players.index(c)
        players[p-1],players[p]=players[p],players[p-1]
    return players

def solution(players, callings):
    dic_players = {p:i for i,p in enumerate(players)}
    dic_rank = {i:p for i,p in enumerate(players)}
    
    for call in callings :
        call_rank = dic_players[call] 
        call_front = dic_rank[call_rank - 1] 
        
        
        dic_players[call], dic_players[call_front] = dic_players[call_front], dic_players[call]
        dic_rank[call_rank], dic_rank[call_rank - 1] = dic_rank[call_rank - 1], dic_rank[call_rank]
    
    return list(dic_rank.values())