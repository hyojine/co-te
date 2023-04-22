# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 시간초과
def solution(players, callings):
    for c in callings:
        p=players.index(c)
        players[p-1],players[p]=players[p],players[p-1]
    return players

# 딕셔너리 1개
def solution(players, callings):
    player_indexes = {player: index for index, player in enumerate(players)}

    for j in callings:
        current_index = player_indexes[j]
        desired_index = current_index - 1
        if current_index > 0 and players[desired_index] != j:
            players[current_index], players[desired_index] = players[desired_index], players[current_index]
            player_indexes[players[current_index]] = current_index
            player_indexes[players[desired_index]] = desired_index
    return players

# 딕셔너리 2개 - 제일 빠름
def solution(players, callings):
    dic_players = {p:i for i,p in enumerate(players)}
    dic_rank = {i:p for i,p in enumerate(players)}
    
    for call in callings :
        call_rank = dic_players[call] 
        call_front = dic_rank[call_rank - 1] 
        
        dic_players[call], dic_players[call_front] = dic_players[call_front], dic_players[call]
        dic_rank[call_rank], dic_rank[call_rank - 1] = dic_rank[call_rank - 1], dic_rank[call_rank]
    
    return list(dic_rank.values())
