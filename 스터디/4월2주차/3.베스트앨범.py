# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    cnt=[(i,x) for i,x in enumerate(zip(genres,plays))]
    cnt=sorted(cnt,key=lambda x: x[1],reverse=True)
    for c in range(len(cnt)):
        answer.append(cnt[c][0])
    return answer