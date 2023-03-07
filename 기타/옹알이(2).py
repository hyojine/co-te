def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:# 연속해서 같은 발음을 할 수는 없음
                i=i.replace(j,'')
                print('i=',i)
        if len(i)==0:
            answer +=1
    return answer

# break하는 게 더 느림
def solution_break(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 in i:
                break
            else:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer



# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
