# 스테이지의 번호가 담길 배열 stages
# 전체 스테이지의 갯수 N
# N-s
# 실패율=스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수/스테이지에 도달한 플레이어의 수
# -> 분자: 스테이지 번호에 있는 플레이어의 수
# -> 분모: 전체플레이어의수 - 스테이지 번호보다 작은 플레이어의 수
#          ==해당 스테이지 번호보다 큰 번호의 스테이지에 있는 플레이어의 수의 합
#          ==sum([스테이지+1:스테이지 지나서 배열 끝])까지의 count를 슬라이스해서 sum (스테이지 넘버 이상인 값)
# 실패율이 높은 스테이지부터 내림차순sort(reverse=True)으로 스테이지 번호를 담아서 리턴

# 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저(오름차순-> 어차피 같은 값이 있으면 작은거 먼저 발견해서 먼저 찾아주니까 상관 없을듯함)
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 -> n+1이 있으면 실패율이 어떻게됨?
# 스테이지 별 플레이어를 카운트한 배열이 N보다 짧으면 모자란만큼 0을 추가해줌 
# -> len 차만큼 0이담긴 배열을 만들어서 extend하거나
# -> len 차만큼 0을 append하면 되는데 어차피 for문 쓸듯


### stage_count=[] 에 stages 안에 있는 스테이지의 수를 세서 순서대로 담고 없으면 0을 담음 인덱스+1이 스테이지 번호가됨

def solution(N, stages):
    # 스테이지당 플레이어의 수
    # len= N이어야함
    no_of_player_on_stage=[]
    for i in range(N):
        # 인덱스+1 = 스테이지 넘버
        if i+1 in stages:
            stage_player=stages.count(i+1)
        elif i+1 not in stages: #else로 바꿔도 상관 없을듯
            stage_player=0
        no_of_player_on_stage.append(stage_player)
    # print('no_of_player_on_stage:',no_of_player_on_stage)
    
    # 같지 않을 동안 돌면서 0을 붙이라고 하는 건데 계속 도는 이유가? 해봤자 500갠데?
    # 헐 더 길어서 그랬던 거였음 도대체 왜 더 길쥐 len(stages)만큼 반복해서 그랬던 것->N으로 수정함
    # while len(no_of_player_on_stage)!=N:
    #     no_of_player_on_stage.append(0)
    # print(len(no_of_player_on_stage))
    
    failure=[]
    # no+1이 스테이지 넘버임
    all_players=sum(no_of_player_on_stage)
    fin_players=stages.count(N+1)
    for no,no_of_player in enumerate(no_of_player_on_stage):
        # 분모가 0이 아니어야하므로
        if (all_players-sum(no_of_player_on_stage[:no])+fin_players) !=0:
            fin_players=stages.count(N+1)
            failure.append(no_of_player/(all_players-sum(no_of_player_on_stage[:no])+fin_players))
        # if sum(no_of_player_on_stage[no:]) !=0:    
        #     if N+1 in stages:
        #         fin_players=stages.count(N+1)
        #         failure.append(no_of_player/(sum(no_of_player_on_stage[no:])+fin_players))
        #         print('분자:',no_of_player)
        #         print('sum:',sum(no_of_player_on_stage[no:])+fin_players)
        #     else:
        #         failure.append(no_of_player/sum(no_of_player_on_stage[no:]))
        else:
            failure.append(0)
    print('failure:',failure)
    # max 다음 값을 어떻게 찾음?
    # failure 길이만큼의 배열을 만들어서
    # 해당 인덱스 값에 len부터 -1 한 값을 넣어줌

    # 딕셔너리로 만들어서 밸류로 정렬하고 키값을 리스트로 출력하면 되는데
    stage_no = [x+1 for x in range(N)] #stage_no
    failure_dict=dict(zip(stage_no,failure))
    print('failure_dict:',failure_dict) # {1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0}
    
    # return_list=[]
    # for pair in zip(idx,failure):
    #     return_list.append(pair)
    # print('return_list:',dict(return_list)) # {1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0}
    # TypeError: cannot convert dictionary update sequence element #0 to a sequence -> append(dict(pair))했을 때 남
    # 딕셔너리로 바꿔야되는데 튜플은 딕셔너리로 저렇게 못바꾸나?
    
    failure_dict_sorted=sorted(failure_dict, key=lambda x: failure_dict[x], reverse=True)
    # print('----',return_list.keys())
    # TypeError: 'int' object is not subscriptable
    return failure_dict_sorted
# print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4,[4,4,4,4,4]))

# 수정 + 분모 구하는 방법 전체에서 빼는 방법으로
def solution2(N, stages):
    # 스테이지당 플레이어의 수
    no_of_player_on_stage=[]
    for i in range(N):
        if i+1 in stages:
            stage_player=stages.count(i+1)
        elif i+1 not in stages:
            stage_player=0
        no_of_player_on_stage.append(stage_player)
    
    # 실패율
    failure=[]
    all_players=sum(no_of_player_on_stage)
    fin_players=stages.count(N+1)
    for no,no_of_player in enumerate(no_of_player_on_stage):
        if (all_players-sum(no_of_player_on_stage[:no])+fin_players) !=0:
            failure.append(no_of_player/(all_players-sum(no_of_player_on_stage[:no])+fin_players))
        else:
            failure.append(0)
    
    # 실패율로 스테이지 넘버 정렬
    stage_no = [x+1 for x in range(N)]
    failure_dict=dict(zip(stage_no,failure))
    failure_sorted=sorted(failure_dict, key=lambda x: failure_dict[x], reverse=True)
    
    return failure_sorted

# 처음부터 클리어한 플레이어 수를 리스트에 포함시키기
def solution3(N, stages):
    # 스테이지당 플레이어의 수
    no_of_player_on_stage=[]
    for i in range(N):
        if i+1 in stages:
            stage_player=stages.count(i+1)
        elif i+1 not in stages:
            stage_player=0
        no_of_player_on_stage.append(stage_player)
    if N+1 in stages:
        no_of_player_on_stage.append(stages.count(N+1))
    
    # 실패율
    failure=[]
    for no,no_of_player in enumerate(no_of_player_on_stage):
        if sum(no_of_player_on_stage[no:]) !=0:
            failure.append(no_of_player/sum(no_of_player_on_stage[no:]))
        else:
            failure.append(0)
    
    # 실패율로 스테이지 넘버 정렬
    stage_no = [x+1 for x in range(N)]
    failure_dict=dict(zip(stage_no,failure))
    failure_sorted=sorted(failure_dict, key=lambda x: failure_dict[x], reverse=True)
    
    return failure_sorted

print(solution3(5,[2, 1, 2, 6, 2, 4, 3, 3]))