# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 유저별로 처리 결과 메일을 받은 횟수

# 95.8
def solution(id_list, report, k):
    re_result = []
    ans=[]
    answer=[]
    cnt=dict([x for x in zip(id_list,[0]*len(id_list))]) # 유저별 신고당한 횟수
    er_ee=[x.split(' ') for x in set(report)] #(신고한 사람,신고 당한 사람)
    # 유저별 신고 당한 수를 cnt에 저장
    for e in er_ee:
        er,ee=e
        cnt[ee]+=1
        if cnt[ee]>=k:
            re_result.append(ee)
    for e in er_ee:
        if e[1] in re_result:
            answer.append(e[0])
    for id in id_list:
        if id in answer:
            ans.append(answer.count(id))
        else:
            ans.append(0) 
    return ans

# 통과
from collections import Counter

def solution(id_list, report, k):
    
    ans=dict([x for x in zip(id_list,[0]*len(id_list))]) 
    er_ee=[x.split(' ') for x in set(report)]
    re_list= [kk for kk,v in Counter([x[1] for x in er_ee]).items() if v>=k]
        
    for e in er_ee:
        er,ee=e
        if ee in re_list:
            ans[er]+=1
    return list(ans.values())